import logging
from tlx.apigateway import APIGException
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def add_key(table, key, item):
    """ If the item doesn't exist yet. Create the key.
        !! Does NOT support tables with Partition and Sort keys Yet.
    """

    key_names = [k for k in key]
    item_template = {**key, **item}
    logger.debug(f'submitting item: {item_template}')

    try:
        logger.info(f"Attempting to add new record for: {key} ")
        res = table.put_item(
            Item=item_template,
            ConditionExpression=f"attribute_not_exists({key_names[0]})",  # TODO fix for items with Partition and Sort key
        )
    except Exception as e:
        msg = f'Failed to add {item_template}: {e}'
        logger.error(msg)
        raise APIGException(msg, code=500)

    logger.info(f"Successfully added new record.")
    logger.debug(f"{item_template}")
    return res['ResponseMetadata']['HTTPStatusCode']


def append_to_list_field(table, key, field_to_update, expression_attribute_names, new_item, add_missing_key=False):
    """ Appends `new_item` to existing item `field_to_update` for a given `key`.

        N.B. If the field is not found, attempts are made to create the entire path of `field_to_update`.
        If the key is not found, attempt to create it.

        Args:
            table (boto3 Table):
            key (dict): Primary key for the table. e.g {'matchid': matchid}
            field_to_update (list): ['providers', '#dataproviderid'].  Variables for substitution should start with a hash and
                have values defined in `expression_attribute_names`.
            expression_attribute_names (dict): Expansion of variables names in the field to update. E.g {'#dataproviderid': "OPTA"}
            new_item (list): To be appended to a list the object must be a list.
            add_missing_key (bool): Default False. If True add the primary key for the table if it is not found.
                                    Otherwise returns dict of data to be added by user.

         Returns:
            int (200)                   - If successfully added item to Dynamodb
            dict {unadded data}         - If the primary key was not found. use `add_key` to add it.
    """
    try:
        str_path = '.'.join(field_to_update)
        # TODO: Consider adding a check for if key exists here rather than in the `_add_new_map_field` call stack
        res = table.update_item(
            Key=key,
            UpdateExpression=f"SET {str_path} = list_append(:new_item, {str_path})",
            ExpressionAttributeNames=expression_attribute_names,
            ExpressionAttributeValues={":new_item": new_item},
            ConditionExpression=f"attribute_exists({str_path})",
        )
        logger.info(f"Successfully added new odds to: {str_path}")
        logger.debug(f'{new_item}')
        return res['ResponseMetadata']['HTTPStatusCode']
    except table.meta.client.exceptions.ConditionalCheckFailedException as ccfe:
        # Table missing some amount of structure
        logger.info(f"field not found: {str_path}")

    return add_new_map_field(table, key, field_to_update[:-1], field_to_update[-1], expression_attribute_names, new_item, add_missing_key)


def add_new_map_field(table, key, path, field_to_add, expression_attribute_names, data, add_missing_key=False):
    """ Adds a new field (field_to_add) to an existing path in a map (path) for a given Primary key (key).

        N.B If the path doesn't exist attempts to create that path.  If the key doesn't exist, will attempt to
        create IFF add_missing_key=True.

        Args:
            table (boto3 Table):
            key (dict): Must match the schema for `table`,
            path (list): List of field name strings in the map path. Use # if the field should be substitued for a value.
                         Specify that value in `expression_attribute_names`. E.g ['root', '#firstkey', '2ndkey']
            field_to_add (string): The name of the new field to add at the end of existing map described by `path`.
            expression_attribute_names (dict): Substitutes for the #values in `path`. E.g {'#firstkey': 'TeamMembers'}
            data (any): Value to be saved under `path`+`field_to_add`.  Must be valid datatypes for Dynamodb.
            add_missing_key (bool): Default False. If True add the primary key for the table if it is not found.
                                    Otherwise returns dict of data to be added by user.
         Returns:
            int (200)                   - If successfully added item to Dynamodb
            dict {unadded data}         - If the primary key was not found. use `add_key` to add it.
    """

    if not path:  # Limit of recursion (Primary key was not found)
        return add_key(table, key, field_to_add, data) if add_missing_key else {field_to_add: data}

    str_path = '.'.join(path)

    try:
        res = table.update_item(
            Key=key,
            UpdateExpression=f"SET {str_path}.{field_to_add} = :new_item",  # want dots to expand
            ExpressionAttributeNames=expression_attribute_names,
            ExpressionAttributeValues={":new_item": data},
            ConditionExpression=f"attribute_not_exists({str_path}.{field_to_add}) AND attribute_exists({str_path})",
        )
        logger.info(f"Successfully added new data to: {str_path}.{field_to_add}")
        logger.debug(f'{data}')
        return res['ResponseMetadata']['HTTPStatusCode']
    except table.meta.client.exceptions.ConditionalCheckFailedException as ccfe:
        logger.info(f"Path ({str_path}) not found.")

    # Must remove otherwise boto complains 'unused in expressions' next time
    new_data = {expression_attribute_names.pop(field_to_add, field_to_add): data}

    # Recursively try to add until we empty the 'path' variable
    return add_new_map_field(table, key, path[:-1], path[-1], expression_attribute_names, new_data)


def get_item(table, key):
    """Get latest item for a given key otherwise returns an empty array"""

    return table.get_item(
        Key=key,
        ConsistentRead=True,
    ).get('Item', [])

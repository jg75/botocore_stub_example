"""Provide some usage examples in my_module."""
from my_package import dynamodb


def get(table, **kwargs):
    """Get an item from a dynamodb table using a boto3 resource."""
    table = dynamodb.Table(table)
    response = table.get_item(**kwargs)

    return response.get("Item", {})

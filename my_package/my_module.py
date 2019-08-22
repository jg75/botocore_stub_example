from my_package import dynamodb


def get(table, **kwargs):
    table = dynamodb.Table(table)
    response = table.get_item(**kwargs)

    return response.get("Item", {})

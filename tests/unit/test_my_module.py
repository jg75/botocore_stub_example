"""Test suite for my_module."""
import botocore
import pytest

from my_package.my_module import get


@pytest.mark.unit
def test_get(dynamodb_stub, params, partition_key, sort_key, item):
    """Assert that get returns an item dictionary with desired attributes."""
    dynamodb_stub.add_response(
        "get_item", {"Item": item["encoded"]}, expected_params=params
    )

    with dynamodb_stub:
        response = get("test-table", Key={partition_key: "1", sort_key: "2"})

    assert response == item["decoded"]


@pytest.mark.unit
def test_get_not_found(dynamodb_stub, params, partition_key, sort_key, item):
    """Assert that get returns an empty dictionary when no attributes are found."""
    dynamodb_stub.add_response("get_item", {}, expected_params=params)

    with dynamodb_stub:
        response = get("test-table", Key={partition_key: "1", sort_key: "2"})

    assert response == dict()


@pytest.mark.unit
def test_get_error(dynamodb_stub, params, partition_key, sort_key, item):
    """Assert that get raises a ClientError when something unexpected happens."""
    dynamodb_stub.add_client_error("get_item", expected_params=params)

    with dynamodb_stub, pytest.raises(botocore.exceptions.ClientError):
        get("test-table", Key={partition_key: "1", sort_key: "2"})

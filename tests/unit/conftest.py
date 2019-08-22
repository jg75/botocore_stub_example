"""Provide unit test fixture to the test suite for my_package."""
import botocore.stub
import pytest

from my_package import dynamodb


@pytest.fixture
def partition_key():
    """Provide the dynamodb table partition key name."""
    return "id"


@pytest.fixture
def sort_key():
    """Provide the dynamodb table sort key name."""
    return "sub_id"


@pytest.fixture
def item():
    """
    Provide a sample item.

    encoded The encoded item that is passed to the get_item client method.
    decoded: The item returned from the resource.
    """
    return {
        "encoded": {"field1": {"S": "stuff"}, "field2": {"S": "more stuff"}},
        "decoded": {"field1": "stuff", "field2": "more stuff"}
    }


@pytest.fixture
def params(partition_key, sort_key):
    """Provide expected parameters for get_item stubbed client method."""
    return {
        "TableName": botocore.stub.ANY,
        "Key": {
            partition_key: botocore.stub.ANY,
            sort_key: botocore.stub.ANY
        }
    }


@pytest.fixture
def dynamodb_stub(request):
    """
    Provide a dynamodb stub.

    Add a spy to the finalizer to check that the response queue is empty
    when the stub goes out of scope.
    """
    stub = botocore.stub.Stubber(dynamodb.meta.client)

    request.addfinalizer(stub.assert_no_pending_responses)

    return stub

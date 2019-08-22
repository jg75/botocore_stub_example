import botocore.stub
import pytest

from my_package import dynamodb


@pytest.fixture
def partition_key():
    return "id"


@pytest.fixture
def sort_key():
    return "sub_id"


@pytest.fixture
def item():
    return {
        "encoded": {"field1": {"S": "stuff"}, "field2": {"S": "more stuff"}},
        "decoded": {"field1": "stuff", "field2": "more stuff"}
    }


@pytest.fixture
def params(partition_key, sort_key):
    return {
        "TableName": botocore.stub.ANY,
        "Key": {
            partition_key: botocore.stub.ANY,
            sort_key: botocore.stub.ANY
        }
    }


@pytest.fixture
def dynamodb_stub(request):
    stub = botocore.stub.Stubber(dynamodb.meta.client)

    request.addfinalizer(stub.assert_no_pending_responses)

    return stub

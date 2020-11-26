import pytest
import string
import random
import json
import os
from core.tcg_secret import tcg_secret


def generate_unique_id(length):
    chars = string.ascii_letters + string.digits
    random.seed = (os.urandom(1024))
    return ''.join(random.choice(chars) for i in range(length))


description = """
This is a test secret autogenerated by the tcg_package during CI testing
"""
secret_name = 'test_tcg_secret_' + generate_unique_id(10)
secret_string = json.dumps({'test': 'test_secret_string'})
key_alias = 'alias/aws/secretsmanager'


@pytest.fixture
def secret():
    """Returns a tcg_secret() object"""
    return tcg_secret()


def test_create_string_body(secret):
    response = secret.create_secret(secret_name,
                                    description,
                                    secret_string,
                                    key_alias)
    assert list(response.keys()) == ['ARN', 'Name', 'VersionId', 'ResponseMetadata']
    assert response['Name'] == secret_name


def test_create_exists(secret):
    with pytest.raises(secret.client.exceptions.ResourceExistsException):
        secret.create_secret(secret_name,
                             description,
                             secret_string,
                             key_alias)


def test_get_exists(secret):
    response = secret.get_secret(secret_name)
    assert type(response) is dict


def test_get_not_exists(secret):
    with pytest.raises(secret.client.exceptions.ResourceNotFoundException):
        not_exists_name = 'does_not_exist_' + generate_unique_id(10)
        secret.get_secret(not_exists_name)


def test_delete(secret):
    response = secret.delete_secret(secret_name)
    assert list(response.keys()) == ['ARN', 'Name', 'DeletionDate', 'ResponseMetadata']
    assert response['Name'] == secret_name


def test_delete_not_exists(secret):
    with pytest.raises(secret.client.exceptions.ResourceNotFoundException):
        not_exists_name = 'does_not_exist_' + generate_unique_id(10)
        secret.delete_secret(not_exists_name)


"""
update
    update existing
    update missing
get_arn
    get existing
    get missing
"""

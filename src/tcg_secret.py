'''
    *** Configuration management package:
This package is a generic configuration management module.
1- It manages the configurations by serialising and deserialising
from config file formats
2- It get's the application secrets from preferred secret management
system.
NB- change the KMS encryption key when moving between accounts
Documentation:
https://iclp-dp.atlassian.net/wiki/spaces/IDLK/pages/409075713/IDLK+-+Configuration+Secret+Management+Solution+Design
10/05/2018 Emre Akarsu
Updated 4/6/2018 Lachlan Ratjens
2018-09-14 - PK - Added update_secret function
'''

import boto3
import json


class tcg_secret:

    def __init__(self):
        # init the aws parameters
        self.region_name = 'eu-west-1'
        self.endpoint_url = "https://secretsmanager.eu-west-1.amazonaws.com"
        self.session = boto3.session.Session()
        self.client = self.session.client(
            service_name='secretsmanager',
            region_name=self.region_name,
            endpoint_url=self.endpoint_url
        )
        print("This is the v1.0.1 version of the TCG Secret Package")

    def __del__(self):
        # terminate the class
        pass

    def get_secret(self, secret_name):
        """
        This function reads a secure parameter from AWS' Secrets Manager.
        Permissions inherited AWS configure / role
        Input: secret name as stored in AWS secrets manager.
        Output: object with secrets string and metadata
        """
        response = self.client.get_secret_value(
            SecretId=secret_name
        )
        credentials = json.loads(response['SecretString'])
        return credentials

    def create_secret(self, secret_name, description, secret_string, key_alias):
        """
        Creates a secret in AWS' secrets manager

        Parameters
        ----------
        secret_name: str
            Name of secret
        description: str
            Secret description
        secret_string: str
            Contents of the secret. Usually a stringified json
        key_alias: str
            KMS name to map to secret

        Returns
        -------
        response: dict
            Dict object returned by boto3 secrets manager
        """
        kms_client = self.session.client('kms')
        key_json = kms_client.describe_key(KeyId=key_alias)
        key_id = key_json['KeyMetadata']['Arn']

        response = self.client.create_secret(
            Name=secret_name,
            Description=description,
            KmsKeyId=key_id,
            SecretString=secret_string,
            Tags=[
                {
                    'Key': 'billing_id',
                    'Value': 'IFD'
                },
                {
                    'Key': 'created_by',
                    'Value': 'tcg_secret.py'
                },
            ]
        )
        return response

    def delete_secret(self, secret_name):
        response = self.client.delete_secret(
            SecretId=secret_name,
            RecoveryWindowInDays=9
        )
        return response

    def update_secret(self, secret_name, description, secret_string, key_alias):
        kms_client = self.session.client('kms')
        key_json = kms_client.describe_key(KeyId=key_alias)
        key_id = key_json['KeyMetadata']['Arn']

        response = self.client.update_secret(
            SecretId=secret_name,
            Description=description,
            KmsKeyId=key_id,
            SecretString=secret_string
        )
        return response

    def get_arn(self, secret_name):
        response = self.client.describe_secret(
            SecretId=secret_name
        )
        return response['ARN']

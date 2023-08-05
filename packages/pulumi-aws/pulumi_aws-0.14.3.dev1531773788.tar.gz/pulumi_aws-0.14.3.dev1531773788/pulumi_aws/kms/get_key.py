# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class GetKeyResult(object):
    """
    A collection of values returned by getKey.
    """
    def __init__(__self__, arn=None, aws_account_id=None, creation_date=None, deletion_date=None, description=None, enabled=None, expiration_model=None, key_manager=None, key_state=None, key_usage=None, origin=None, valid_to=None, id=None):
        if arn and not isinstance(arn, basestring):
            raise TypeError('Expected argument arn to be a basestring')
        __self__.arn = arn
        if aws_account_id and not isinstance(aws_account_id, basestring):
            raise TypeError('Expected argument aws_account_id to be a basestring')
        __self__.aws_account_id = aws_account_id
        if creation_date and not isinstance(creation_date, basestring):
            raise TypeError('Expected argument creation_date to be a basestring')
        __self__.creation_date = creation_date
        if deletion_date and not isinstance(deletion_date, basestring):
            raise TypeError('Expected argument deletion_date to be a basestring')
        __self__.deletion_date = deletion_date
        if description and not isinstance(description, basestring):
            raise TypeError('Expected argument description to be a basestring')
        __self__.description = description
        if enabled and not isinstance(enabled, bool):
            raise TypeError('Expected argument enabled to be a bool')
        __self__.enabled = enabled
        if expiration_model and not isinstance(expiration_model, basestring):
            raise TypeError('Expected argument expiration_model to be a basestring')
        __self__.expiration_model = expiration_model
        if key_manager and not isinstance(key_manager, basestring):
            raise TypeError('Expected argument key_manager to be a basestring')
        __self__.key_manager = key_manager
        if key_state and not isinstance(key_state, basestring):
            raise TypeError('Expected argument key_state to be a basestring')
        __self__.key_state = key_state
        if key_usage and not isinstance(key_usage, basestring):
            raise TypeError('Expected argument key_usage to be a basestring')
        __self__.key_usage = key_usage
        if origin and not isinstance(origin, basestring):
            raise TypeError('Expected argument origin to be a basestring')
        __self__.origin = origin
        if valid_to and not isinstance(valid_to, basestring):
            raise TypeError('Expected argument valid_to to be a basestring')
        __self__.valid_to = valid_to
        if id and not isinstance(id, basestring):
            raise TypeError('Expected argument id to be a basestring')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

def get_key(grant_tokens=None, key_id=None):
    """
    Use this data source to get detailed information about 
    the specified KMS Key with flexible key id input. 
    This can be useful to reference key alias 
    without having to hard code the ARN as input.
    """
    __args__ = dict()

    __args__['grantTokens'] = grant_tokens
    __args__['keyId'] = key_id
    __ret__ = pulumi.runtime.invoke('aws:kms/getKey:getKey', __args__)

    return GetKeyResult(
        arn=__ret__.get('arn'),
        aws_account_id=__ret__.get('awsAccountId'),
        creation_date=__ret__.get('creationDate'),
        deletion_date=__ret__.get('deletionDate'),
        description=__ret__.get('description'),
        enabled=__ret__.get('enabled'),
        expiration_model=__ret__.get('expirationModel'),
        key_manager=__ret__.get('keyManager'),
        key_state=__ret__.get('keyState'),
        key_usage=__ret__.get('keyUsage'),
        origin=__ret__.get('origin'),
        valid_to=__ret__.get('validTo'),
        id=__ret__.get('id'))

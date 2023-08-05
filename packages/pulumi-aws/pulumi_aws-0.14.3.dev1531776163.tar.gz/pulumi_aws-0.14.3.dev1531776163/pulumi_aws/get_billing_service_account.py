# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class GetBillingServiceAccountResult(object):
    """
    A collection of values returned by getBillingServiceAccount.
    """
    def __init__(__self__, arn=None, id=None):
        if arn and not isinstance(arn, basestring):
            raise TypeError('Expected argument arn to be a basestring')
        __self__.arn = arn
        """
        The ARN of the AWS billing service account.
        """
        if id and not isinstance(id, basestring):
            raise TypeError('Expected argument id to be a basestring')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

def get_billing_service_account():
    """
    Use this data source to get the Account ID of the [AWS Billing and Cost Management Service Account](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-getting-started.html#step-2) for the purpose of whitelisting in S3 bucket policy.
    """
    __args__ = dict()

    __ret__ = pulumi.runtime.invoke('aws:index/getBillingServiceAccount:getBillingServiceAccount', __args__)

    return GetBillingServiceAccountResult(
        arn=__ret__.get('arn'),
        id=__ret__.get('id'))

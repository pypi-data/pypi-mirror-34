# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class Database(pulumi.CustomResource):
    """
    Provides an Athena database.
    """
    def __init__(__self__, __name__, __opts__=None, bucket=None, force_destroy=None, name=None):
        """Create a Database resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not bucket:
            raise TypeError('Missing required property bucket')
        elif not isinstance(bucket, basestring):
            raise TypeError('Expected property bucket to be a basestring')
        __self__.bucket = bucket
        """
        Name of s3 bucket to save the results of the query execution.
        """
        __props__['bucket'] = bucket

        if force_destroy and not isinstance(force_destroy, bool):
            raise TypeError('Expected property force_destroy to be a bool')
        __self__.force_destroy = force_destroy
        """
        A boolean that indicates all tables should be deleted from the database so that the database can be destroyed without error. The tables are *not* recoverable.
        """
        __props__['forceDestroy'] = force_destroy

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        Name of the database to create.
        """
        __props__['name'] = name

        super(Database, __self__).__init__(
            'aws:athena/database:Database',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'bucket' in outs:
            self.bucket = outs['bucket']
        if 'forceDestroy' in outs:
            self.force_destroy = outs['forceDestroy']
        if 'name' in outs:
            self.name = outs['name']

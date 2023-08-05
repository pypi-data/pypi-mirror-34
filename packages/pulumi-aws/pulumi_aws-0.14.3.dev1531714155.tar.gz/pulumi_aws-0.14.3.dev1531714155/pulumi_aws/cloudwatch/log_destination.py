# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class LogDestination(pulumi.CustomResource):
    """
    Provides a CloudWatch Logs destination resource.
    """
    def __init__(__self__, __name__, __opts__=None, name=None, role_arn=None, target_arn=None):
        """Create a LogDestination resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        A name for the log destination
        """
        __props__['name'] = name

        if not role_arn:
            raise TypeError('Missing required property role_arn')
        elif not isinstance(role_arn, basestring):
            raise TypeError('Expected property role_arn to be a basestring')
        __self__.role_arn = role_arn
        """
        The ARN of an IAM role that grants Amazon CloudWatch Logs permissions to put data into the target
        """
        __props__['roleArn'] = role_arn

        if not target_arn:
            raise TypeError('Missing required property target_arn')
        elif not isinstance(target_arn, basestring):
            raise TypeError('Expected property target_arn to be a basestring')
        __self__.target_arn = target_arn
        """
        The ARN of the target Amazon Kinesis stream or Amazon Lambda resource for the destination
        """
        __props__['targetArn'] = target_arn

        __self__.arn = pulumi.runtime.UNKNOWN
        """
        The Amazon Resource Name (ARN) specifying the log destination.
        """

        super(LogDestination, __self__).__init__(
            'aws:cloudwatch/logDestination:LogDestination',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'arn' in outs:
            self.arn = outs['arn']
        if 'name' in outs:
            self.name = outs['name']
        if 'roleArn' in outs:
            self.role_arn = outs['roleArn']
        if 'targetArn' in outs:
            self.target_arn = outs['targetArn']

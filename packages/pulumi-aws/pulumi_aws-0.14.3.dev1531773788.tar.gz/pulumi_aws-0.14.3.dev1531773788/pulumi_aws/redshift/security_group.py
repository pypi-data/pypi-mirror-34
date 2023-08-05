# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class SecurityGroup(pulumi.CustomResource):
    """
    Creates a new Amazon Redshift security group. You use security groups to control access to non-VPC clusters
    """
    def __init__(__self__, __name__, __opts__=None, description=None, ingress=None, name=None):
        """Create a SecurityGroup resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if description and not isinstance(description, basestring):
            raise TypeError('Expected property description to be a basestring')
        __self__.description = description
        """
        The description of the Redshift security group. Defaults to "Managed by Terraform".
        """
        __props__['description'] = description

        if not ingress:
            raise TypeError('Missing required property ingress')
        elif not isinstance(ingress, list):
            raise TypeError('Expected property ingress to be a list')
        __self__.ingress = ingress
        """
        A list of ingress rules.
        """
        __props__['ingress'] = ingress

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the Redshift security group.
        """
        __props__['name'] = name

        super(SecurityGroup, __self__).__init__(
            'aws:redshift/securityGroup:SecurityGroup',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'description' in outs:
            self.description = outs['description']
        if 'ingress' in outs:
            self.ingress = outs['ingress']
        if 'name' in outs:
            self.name = outs['name']

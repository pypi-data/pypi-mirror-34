# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class Repository(pulumi.CustomResource):
    """
    Provides an EC2 Container Registry Repository.
    
    ~> **NOTE on ECR Availability**: The EC2 Container Registry is not yet rolled out
    in all regions - available regions are listed
    [the AWS Docs](https://docs.aws.amazon.com/general/latest/gr/rande.html#ecr_region).
    """
    def __init__(__self__, __name__, __opts__=None, name=None):
        """Create a Repository resource with the given unique name, props, and options."""
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
        Name of the repository.
        """
        __props__['name'] = name

        __self__.arn = pulumi.runtime.UNKNOWN
        """
        Full ARN of the repository.
        """
        __self__.registry_id = pulumi.runtime.UNKNOWN
        """
        The registry ID where the repository was created.
        """
        __self__.repository_url = pulumi.runtime.UNKNOWN
        """
        The URL of the repository (in the form `aws_account_id.dkr.ecr.region.amazonaws.com/repositoryName`
        """

        super(Repository, __self__).__init__(
            'aws:ecr/repository:Repository',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'arn' in outs:
            self.arn = outs['arn']
        if 'name' in outs:
            self.name = outs['name']
        if 'registryId' in outs:
            self.registry_id = outs['registryId']
        if 'repositoryUrl' in outs:
            self.repository_url = outs['repositoryUrl']

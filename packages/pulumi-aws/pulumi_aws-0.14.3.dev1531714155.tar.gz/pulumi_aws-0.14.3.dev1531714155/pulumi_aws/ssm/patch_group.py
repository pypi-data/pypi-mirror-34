# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class PatchGroup(pulumi.CustomResource):
    """
    Provides an SSM Patch Group resource
    """
    def __init__(__self__, __name__, __opts__=None, baseline_id=None, patch_group=None):
        """Create a PatchGroup resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not baseline_id:
            raise TypeError('Missing required property baseline_id')
        elif not isinstance(baseline_id, basestring):
            raise TypeError('Expected property baseline_id to be a basestring')
        __self__.baseline_id = baseline_id
        """
        The ID of the patch baseline to register the patch group with.
        """
        __props__['baselineId'] = baseline_id

        if not patch_group:
            raise TypeError('Missing required property patch_group')
        elif not isinstance(patch_group, basestring):
            raise TypeError('Expected property patch_group to be a basestring')
        __self__.patch_group = patch_group
        """
        The name of the patch group that should be registered with the patch baseline.
        """
        __props__['patchGroup'] = patch_group

        super(PatchGroup, __self__).__init__(
            'aws:ssm/patchGroup:PatchGroup',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'baselineId' in outs:
            self.baseline_id = outs['baselineId']
        if 'patchGroup' in outs:
            self.patch_group = outs['patchGroup']

# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class VolumeAttachment(pulumi.CustomResource):
    """
    Provides an AWS EBS Volume Attachment as a top level resource, to attach and
    detach volumes from AWS Instances.
    
    ~> **NOTE on EBS block devices:** If you use `ebs_block_device` on an `aws_instance`, Terraform will assume management over the full set of non-root EBS block devices for the instance, and treats additional block devices as drift. For this reason, `ebs_block_device` cannot be mixed with external `aws_ebs_volume` + `aws_ebs_volume_attachment` resources for a given instance.
    """
    def __init__(__self__, __name__, __opts__=None, device_name=None, force_detach=None, instance_id=None, skip_destroy=None, volume_id=None):
        """Create a VolumeAttachment resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not device_name:
            raise TypeError('Missing required property device_name')
        elif not isinstance(device_name, basestring):
            raise TypeError('Expected property device_name to be a basestring')
        __self__.device_name = device_name
        """
        The device name to expose to the instance (for
        example, `/dev/sdh` or `xvdh`)
        """
        __props__['deviceName'] = device_name

        if force_detach and not isinstance(force_detach, bool):
            raise TypeError('Expected property force_detach to be a bool')
        __self__.force_detach = force_detach
        """
        Set to `true` if you want to force the
        volume to detach. Useful if previous attempts failed, but use this option only
        as a last resort, as this can result in **data loss**. See
        [Detaching an Amazon EBS Volume from an Instance][1] for more information.
        """
        __props__['forceDetach'] = force_detach

        if not instance_id:
            raise TypeError('Missing required property instance_id')
        elif not isinstance(instance_id, basestring):
            raise TypeError('Expected property instance_id to be a basestring')
        __self__.instance_id = instance_id
        """
        ID of the Instance to attach to
        """
        __props__['instanceId'] = instance_id

        if skip_destroy and not isinstance(skip_destroy, bool):
            raise TypeError('Expected property skip_destroy to be a bool')
        __self__.skip_destroy = skip_destroy
        """
        Set this to true if you do not wish
        to detach the volume from the instance to which it is attached at destroy
        time, and instead just remove the attachment from Terraform state. This is
        useful when destroying an instance which has volumes created by some other
        means attached.
        """
        __props__['skipDestroy'] = skip_destroy

        if not volume_id:
            raise TypeError('Missing required property volume_id')
        elif not isinstance(volume_id, basestring):
            raise TypeError('Expected property volume_id to be a basestring')
        __self__.volume_id = volume_id
        """
        ID of the Volume to be attached
        """
        __props__['volumeId'] = volume_id

        super(VolumeAttachment, __self__).__init__(
            'aws:ec2/volumeAttachment:VolumeAttachment',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'deviceName' in outs:
            self.device_name = outs['deviceName']
        if 'forceDetach' in outs:
            self.force_detach = outs['forceDetach']
        if 'instanceId' in outs:
            self.instance_id = outs['instanceId']
        if 'skipDestroy' in outs:
            self.skip_destroy = outs['skipDestroy']
        if 'volumeId' in outs:
            self.volume_id = outs['volumeId']

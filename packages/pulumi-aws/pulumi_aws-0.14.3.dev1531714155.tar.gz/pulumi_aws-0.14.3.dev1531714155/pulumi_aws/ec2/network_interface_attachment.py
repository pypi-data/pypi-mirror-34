# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class NetworkInterfaceAttachment(pulumi.CustomResource):
    """
    Attach an Elastic network interface (ENI) resource with EC2 instance.
    """
    def __init__(__self__, __name__, __opts__=None, device_index=None, instance_id=None, network_interface_id=None):
        """Create a NetworkInterfaceAttachment resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not device_index:
            raise TypeError('Missing required property device_index')
        elif not isinstance(device_index, int):
            raise TypeError('Expected property device_index to be a int')
        __self__.device_index = device_index
        """
        Network interface index (int).
        """
        __props__['deviceIndex'] = device_index

        if not instance_id:
            raise TypeError('Missing required property instance_id')
        elif not isinstance(instance_id, basestring):
            raise TypeError('Expected property instance_id to be a basestring')
        __self__.instance_id = instance_id
        """
        Instance ID to attach.
        """
        __props__['instanceId'] = instance_id

        if not network_interface_id:
            raise TypeError('Missing required property network_interface_id')
        elif not isinstance(network_interface_id, basestring):
            raise TypeError('Expected property network_interface_id to be a basestring')
        __self__.network_interface_id = network_interface_id
        """
        ENI ID to attach.
        """
        __props__['networkInterfaceId'] = network_interface_id

        __self__.attachment_id = pulumi.runtime.UNKNOWN
        """
        The ENI Attachment ID.
        """
        __self__.status = pulumi.runtime.UNKNOWN
        """
        The status of the Network Interface Attachment.
        """

        super(NetworkInterfaceAttachment, __self__).__init__(
            'aws:ec2/networkInterfaceAttachment:NetworkInterfaceAttachment',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'attachmentId' in outs:
            self.attachment_id = outs['attachmentId']
        if 'deviceIndex' in outs:
            self.device_index = outs['deviceIndex']
        if 'instanceId' in outs:
            self.instance_id = outs['instanceId']
        if 'networkInterfaceId' in outs:
            self.network_interface_id = outs['networkInterfaceId']
        if 'status' in outs:
            self.status = outs['status']

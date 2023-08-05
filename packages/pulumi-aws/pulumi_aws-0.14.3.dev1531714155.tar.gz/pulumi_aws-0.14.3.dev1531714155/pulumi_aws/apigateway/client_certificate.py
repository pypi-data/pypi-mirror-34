# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class ClientCertificate(pulumi.CustomResource):
    """
    Provides an API Gateway Client Certificate.
    """
    def __init__(__self__, __name__, __opts__=None, description=None):
        """Create a ClientCertificate resource with the given unique name, props, and options."""
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
        The description of the client certificate.
        """
        __props__['description'] = description

        __self__.created_date = pulumi.runtime.UNKNOWN
        """
        The date when the client certificate was created.
        """
        __self__.expiration_date = pulumi.runtime.UNKNOWN
        """
        The date when the client certificate will expire.
        """
        __self__.pem_encoded_certificate = pulumi.runtime.UNKNOWN
        """
        The PEM-encoded public key of the client certificate.
        """

        super(ClientCertificate, __self__).__init__(
            'aws:apigateway/clientCertificate:ClientCertificate',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'createdDate' in outs:
            self.created_date = outs['createdDate']
        if 'description' in outs:
            self.description = outs['description']
        if 'expirationDate' in outs:
            self.expiration_date = outs['expirationDate']
        if 'pemEncodedCertificate' in outs:
            self.pem_encoded_certificate = outs['pemEncodedCertificate']

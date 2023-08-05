# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class XssMatchSet(pulumi.CustomResource):
    """
    Provides a WAF XSS Match Set Resource
    """
    def __init__(__self__, __name__, __opts__=None, name=None, xss_match_tuples=None):
        """Create a XssMatchSet resource with the given unique name, props, and options."""
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
        The name or description of the SizeConstraintSet.
        """
        __props__['name'] = name

        if xss_match_tuples and not isinstance(xss_match_tuples, list):
            raise TypeError('Expected property xss_match_tuples to be a list')
        __self__.xss_match_tuples = xss_match_tuples
        """
        The parts of web requests that you want to inspect for cross-site scripting attacks.
        """
        __props__['xssMatchTuples'] = xss_match_tuples

        super(XssMatchSet, __self__).__init__(
            'aws:waf/xssMatchSet:XssMatchSet',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'name' in outs:
            self.name = outs['name']
        if 'xssMatchTuples' in outs:
            self.xss_match_tuples = outs['xssMatchTuples']

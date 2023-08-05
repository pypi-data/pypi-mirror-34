# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class RegexPatternSet(pulumi.CustomResource):
    """
    Provides a WAF Regional Regex Pattern Set Resource
    """
    def __init__(__self__, __name__, __opts__=None, name=None, regex_pattern_strings=None):
        """Create a RegexPatternSet resource with the given unique name, props, and options."""
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
        The name or description of the Regex Pattern Set.
        """
        __props__['name'] = name

        if regex_pattern_strings and not isinstance(regex_pattern_strings, list):
            raise TypeError('Expected property regex_pattern_strings to be a list')
        __self__.regex_pattern_strings = regex_pattern_strings
        """
        A list of regular expression (regex) patterns that you want AWS WAF to search for, such as `B[a@]dB[o0]t`.
        """
        __props__['regexPatternStrings'] = regex_pattern_strings

        super(RegexPatternSet, __self__).__init__(
            'aws:wafregional/regexPatternSet:RegexPatternSet',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'name' in outs:
            self.name = outs['name']
        if 'regexPatternStrings' in outs:
            self.regex_pattern_strings = outs['regexPatternStrings']

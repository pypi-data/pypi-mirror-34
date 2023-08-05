# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class HealthCheck(pulumi.CustomResource):
    """
    Provides a Route53 health check.
    """
    def __init__(__self__, __name__, __opts__=None, child_health_threshold=None, child_healthchecks=None, cloudwatch_alarm_name=None, cloudwatch_alarm_region=None, enable_sni=None, failure_threshold=None, fqdn=None, insufficient_data_health_status=None, invert_healthcheck=None, ip_address=None, measure_latency=None, port=None, reference_name=None, regions=None, request_interval=None, resource_path=None, search_string=None, tags=None, type=None):
        """Create a HealthCheck resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if child_health_threshold and not isinstance(child_health_threshold, int):
            raise TypeError('Expected property child_health_threshold to be a int')
        __self__.child_health_threshold = child_health_threshold
        """
        The minimum number of child health checks that must be healthy for Route 53 to consider the parent health check to be healthy. Valid values are integers between 0 and 256, inclusive
        """
        __props__['childHealthThreshold'] = child_health_threshold

        if child_healthchecks and not isinstance(child_healthchecks, list):
            raise TypeError('Expected property child_healthchecks to be a list')
        __self__.child_healthchecks = child_healthchecks
        """
        For a specified parent health check, a list of HealthCheckId values for the associated child health checks.
        """
        __props__['childHealthchecks'] = child_healthchecks

        if cloudwatch_alarm_name and not isinstance(cloudwatch_alarm_name, basestring):
            raise TypeError('Expected property cloudwatch_alarm_name to be a basestring')
        __self__.cloudwatch_alarm_name = cloudwatch_alarm_name
        """
        The name of the CloudWatch alarm.
        """
        __props__['cloudwatchAlarmName'] = cloudwatch_alarm_name

        if cloudwatch_alarm_region and not isinstance(cloudwatch_alarm_region, basestring):
            raise TypeError('Expected property cloudwatch_alarm_region to be a basestring')
        __self__.cloudwatch_alarm_region = cloudwatch_alarm_region
        """
        The CloudWatchRegion that the CloudWatch alarm was created in.
        """
        __props__['cloudwatchAlarmRegion'] = cloudwatch_alarm_region

        if enable_sni and not isinstance(enable_sni, bool):
            raise TypeError('Expected property enable_sni to be a bool')
        __self__.enable_sni = enable_sni
        """
        A boolean value that indicates whether Route53 should send the `fqdn` to the endpoint when performing the health check. This defaults to AWS' defaults: when the `type` is "HTTPS" `enable_sni` defaults to `true`, when `type` is anything else `enable_sni` defaults to `false`.
        """
        __props__['enableSni'] = enable_sni

        if failure_threshold and not isinstance(failure_threshold, int):
            raise TypeError('Expected property failure_threshold to be a int')
        __self__.failure_threshold = failure_threshold
        """
        The number of consecutive health checks that an endpoint must pass or fail.
        """
        __props__['failureThreshold'] = failure_threshold

        if fqdn and not isinstance(fqdn, basestring):
            raise TypeError('Expected property fqdn to be a basestring')
        __self__.fqdn = fqdn
        """
        The fully qualified domain name of the endpoint to be checked.
        """
        __props__['fqdn'] = fqdn

        if insufficient_data_health_status and not isinstance(insufficient_data_health_status, basestring):
            raise TypeError('Expected property insufficient_data_health_status to be a basestring')
        __self__.insufficient_data_health_status = insufficient_data_health_status
        """
        The status of the health check when CloudWatch has insufficient data about the state of associated alarm. Valid values are `Healthy` , `Unhealthy` and `LastKnownStatus`.
        """
        __props__['insufficientDataHealthStatus'] = insufficient_data_health_status

        if invert_healthcheck and not isinstance(invert_healthcheck, bool):
            raise TypeError('Expected property invert_healthcheck to be a bool')
        __self__.invert_healthcheck = invert_healthcheck
        """
        A boolean value that indicates whether the status of health check should be inverted. For example, if a health check is healthy but Inverted is True , then Route 53 considers the health check to be unhealthy.
        """
        __props__['invertHealthcheck'] = invert_healthcheck

        if ip_address and not isinstance(ip_address, basestring):
            raise TypeError('Expected property ip_address to be a basestring')
        __self__.ip_address = ip_address
        """
        The IP address of the endpoint to be checked.
        """
        __props__['ipAddress'] = ip_address

        if measure_latency and not isinstance(measure_latency, bool):
            raise TypeError('Expected property measure_latency to be a bool')
        __self__.measure_latency = measure_latency
        """
        A Boolean value that indicates whether you want Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint and to display CloudWatch latency graphs in the Route 53 console.
        """
        __props__['measureLatency'] = measure_latency

        if port and not isinstance(port, int):
            raise TypeError('Expected property port to be a int')
        __self__.port = port
        """
        The port of the endpoint to be checked.
        """
        __props__['port'] = port

        if reference_name and not isinstance(reference_name, basestring):
            raise TypeError('Expected property reference_name to be a basestring')
        __self__.reference_name = reference_name
        """
        This is a reference name used in Caller Reference
        (helpful for identifying single health_check set amongst others)
        """
        __props__['referenceName'] = reference_name

        if regions and not isinstance(regions, list):
            raise TypeError('Expected property regions to be a list')
        __self__.regions = regions
        """
        A list of AWS regions that you want Amazon Route 53 health checkers to check the specified endpoint from.
        """
        __props__['regions'] = regions

        if request_interval and not isinstance(request_interval, int):
            raise TypeError('Expected property request_interval to be a int')
        __self__.request_interval = request_interval
        """
        The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health-check request.
        """
        __props__['requestInterval'] = request_interval

        if resource_path and not isinstance(resource_path, basestring):
            raise TypeError('Expected property resource_path to be a basestring')
        __self__.resource_path = resource_path
        """
        The path that you want Amazon Route 53 to request when performing health checks.
        """
        __props__['resourcePath'] = resource_path

        if search_string and not isinstance(search_string, basestring):
            raise TypeError('Expected property search_string to be a basestring')
        __self__.search_string = search_string
        """
        String searched in the first 5120 bytes of the response body for check to be considered healthy.
        """
        __props__['searchString'] = search_string

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags to assign to the health check.
        """
        __props__['tags'] = tags

        if not type:
            raise TypeError('Missing required property type')
        elif not isinstance(type, basestring):
            raise TypeError('Expected property type to be a basestring')
        __self__.type = type
        """
        The protocol to use when performing health checks. Valid values are `HTTP`, `HTTPS`, `HTTP_STR_MATCH`, `HTTPS_STR_MATCH`, `TCP`, `CALCULATED` and `CLOUDWATCH_METRIC`.
        """
        __props__['type'] = type

        super(HealthCheck, __self__).__init__(
            'aws:route53/healthCheck:HealthCheck',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'childHealthThreshold' in outs:
            self.child_health_threshold = outs['childHealthThreshold']
        if 'childHealthchecks' in outs:
            self.child_healthchecks = outs['childHealthchecks']
        if 'cloudwatchAlarmName' in outs:
            self.cloudwatch_alarm_name = outs['cloudwatchAlarmName']
        if 'cloudwatchAlarmRegion' in outs:
            self.cloudwatch_alarm_region = outs['cloudwatchAlarmRegion']
        if 'enableSni' in outs:
            self.enable_sni = outs['enableSni']
        if 'failureThreshold' in outs:
            self.failure_threshold = outs['failureThreshold']
        if 'fqdn' in outs:
            self.fqdn = outs['fqdn']
        if 'insufficientDataHealthStatus' in outs:
            self.insufficient_data_health_status = outs['insufficientDataHealthStatus']
        if 'invertHealthcheck' in outs:
            self.invert_healthcheck = outs['invertHealthcheck']
        if 'ipAddress' in outs:
            self.ip_address = outs['ipAddress']
        if 'measureLatency' in outs:
            self.measure_latency = outs['measureLatency']
        if 'port' in outs:
            self.port = outs['port']
        if 'referenceName' in outs:
            self.reference_name = outs['referenceName']
        if 'regions' in outs:
            self.regions = outs['regions']
        if 'requestInterval' in outs:
            self.request_interval = outs['requestInterval']
        if 'resourcePath' in outs:
            self.resource_path = outs['resourcePath']
        if 'searchString' in outs:
            self.search_string = outs['searchString']
        if 'tags' in outs:
            self.tags = outs['tags']
        if 'type' in outs:
            self.type = outs['type']

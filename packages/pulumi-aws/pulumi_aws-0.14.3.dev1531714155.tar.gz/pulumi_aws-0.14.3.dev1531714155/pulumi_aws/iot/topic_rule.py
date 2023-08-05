# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class TopicRule(pulumi.CustomResource):
    def __init__(__self__, __name__, __opts__=None, cloudwatch_alarm=None, cloudwatch_metric=None, description=None, dynamodb=None, elasticsearch=None, enabled=None, firehose=None, kinesis=None, lambda=None, name=None, republish=None, s3=None, sns=None, sql=None, sql_version=None, sqs=None):
        """Create a TopicRule resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if cloudwatch_alarm and not isinstance(cloudwatch_alarm, dict):
            raise TypeError('Expected property cloudwatch_alarm to be a dict')
        __self__.cloudwatch_alarm = cloudwatch_alarm
        __props__['cloudwatchAlarm'] = cloudwatch_alarm

        if cloudwatch_metric and not isinstance(cloudwatch_metric, dict):
            raise TypeError('Expected property cloudwatch_metric to be a dict')
        __self__.cloudwatch_metric = cloudwatch_metric
        __props__['cloudwatchMetric'] = cloudwatch_metric

        if description and not isinstance(description, basestring):
            raise TypeError('Expected property description to be a basestring')
        __self__.description = description
        """
        The description of the rule.
        """
        __props__['description'] = description

        if dynamodb and not isinstance(dynamodb, dict):
            raise TypeError('Expected property dynamodb to be a dict')
        __self__.dynamodb = dynamodb
        __props__['dynamodb'] = dynamodb

        if elasticsearch and not isinstance(elasticsearch, dict):
            raise TypeError('Expected property elasticsearch to be a dict')
        __self__.elasticsearch = elasticsearch
        __props__['elasticsearch'] = elasticsearch

        if not enabled:
            raise TypeError('Missing required property enabled')
        elif not isinstance(enabled, bool):
            raise TypeError('Expected property enabled to be a bool')
        __self__.enabled = enabled
        """
        Specifies whether the rule is enabled.
        """
        __props__['enabled'] = enabled

        if firehose and not isinstance(firehose, dict):
            raise TypeError('Expected property firehose to be a dict')
        __self__.firehose = firehose
        __props__['firehose'] = firehose

        if kinesis and not isinstance(kinesis, dict):
            raise TypeError('Expected property kinesis to be a dict')
        __self__.kinesis = kinesis
        __props__['kinesis'] = kinesis

        if lambda and not isinstance(lambda, dict):
            raise TypeError('Expected property lambda to be a dict')
        __self__.lambda = lambda
        __props__['lambda'] = lambda

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the rule.
        """
        __props__['name'] = name

        if republish and not isinstance(republish, dict):
            raise TypeError('Expected property republish to be a dict')
        __self__.republish = republish
        __props__['republish'] = republish

        if s3 and not isinstance(s3, dict):
            raise TypeError('Expected property s3 to be a dict')
        __self__.s3 = s3
        __props__['s3'] = s3

        if sns and not isinstance(sns, dict):
            raise TypeError('Expected property sns to be a dict')
        __self__.sns = sns
        __props__['sns'] = sns

        if not sql:
            raise TypeError('Missing required property sql')
        elif not isinstance(sql, basestring):
            raise TypeError('Expected property sql to be a basestring')
        __self__.sql = sql
        """
        The SQL statement used to query the topic. For more information, see AWS IoT SQL Reference (http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference) in the AWS IoT Developer Guide.
        """
        __props__['sql'] = sql

        if not sql_version:
            raise TypeError('Missing required property sql_version')
        elif not isinstance(sql_version, basestring):
            raise TypeError('Expected property sql_version to be a basestring')
        __self__.sql_version = sql_version
        """
        The version of the SQL rules engine to use when evaluating the rule.
        """
        __props__['sqlVersion'] = sql_version

        if sqs and not isinstance(sqs, dict):
            raise TypeError('Expected property sqs to be a dict')
        __self__.sqs = sqs
        __props__['sqs'] = sqs

        __self__.arn = pulumi.runtime.UNKNOWN
        """
        The ARN of the topic rule
        """

        super(TopicRule, __self__).__init__(
            'aws:iot/topicRule:TopicRule',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'arn' in outs:
            self.arn = outs['arn']
        if 'cloudwatchAlarm' in outs:
            self.cloudwatch_alarm = outs['cloudwatchAlarm']
        if 'cloudwatchMetric' in outs:
            self.cloudwatch_metric = outs['cloudwatchMetric']
        if 'description' in outs:
            self.description = outs['description']
        if 'dynamodb' in outs:
            self.dynamodb = outs['dynamodb']
        if 'elasticsearch' in outs:
            self.elasticsearch = outs['elasticsearch']
        if 'enabled' in outs:
            self.enabled = outs['enabled']
        if 'firehose' in outs:
            self.firehose = outs['firehose']
        if 'kinesis' in outs:
            self.kinesis = outs['kinesis']
        if 'lambda' in outs:
            self.lambda = outs['lambda']
        if 'name' in outs:
            self.name = outs['name']
        if 'republish' in outs:
            self.republish = outs['republish']
        if 's3' in outs:
            self.s3 = outs['s3']
        if 'sns' in outs:
            self.sns = outs['sns']
        if 'sql' in outs:
            self.sql = outs['sql']
        if 'sqlVersion' in outs:
            self.sql_version = outs['sqlVersion']
        if 'sqs' in outs:
            self.sqs = outs['sqs']

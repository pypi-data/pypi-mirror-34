# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class Job(pulumi.CustomResource):
    """
    Provides a Glue Job resource.
    """
    def __init__(__self__, __name__, __opts__=None, allocated_capacity=None, command=None, connections=None, default_arguments=None, description=None, execution_property=None, max_retries=None, name=None, role_arn=None, timeout=None):
        """Create a Job resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if allocated_capacity and not isinstance(allocated_capacity, int):
            raise TypeError('Expected property allocated_capacity to be a int')
        __self__.allocated_capacity = allocated_capacity
        """
        The number of AWS Glue data processing units (DPUs) to allocate to this Job. At least 2 DPUs need to be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory.
        """
        __props__['allocatedCapacity'] = allocated_capacity

        if not command:
            raise TypeError('Missing required property command')
        elif not isinstance(command, dict):
            raise TypeError('Expected property command to be a dict')
        __self__.command = command
        """
        The command of the job. Defined below.
        """
        __props__['command'] = command

        if connections and not isinstance(connections, list):
            raise TypeError('Expected property connections to be a list')
        __self__.connections = connections
        """
        The list of connections used for this job.
        """
        __props__['connections'] = connections

        if default_arguments and not isinstance(default_arguments, dict):
            raise TypeError('Expected property default_arguments to be a dict')
        __self__.default_arguments = default_arguments
        """
        The map of default arguments for this job. You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes. For information about how to specify and consume your own Job arguments, see the [Calling AWS Glue APIs in Python](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html) topic in the developer guide. For information about the key-value pairs that AWS Glue consumes to set up your job, see the [Special Parameters Used by AWS Glue](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-glue-arguments.html) topic in the developer guide.
        """
        __props__['defaultArguments'] = default_arguments

        if description and not isinstance(description, basestring):
            raise TypeError('Expected property description to be a basestring')
        __self__.description = description
        """
        Description of the job.
        """
        __props__['description'] = description

        if execution_property and not isinstance(execution_property, dict):
            raise TypeError('Expected property execution_property to be a dict')
        __self__.execution_property = execution_property
        """
        Execution property of the job. Defined below.
        """
        __props__['executionProperty'] = execution_property

        if max_retries and not isinstance(max_retries, int):
            raise TypeError('Expected property max_retries to be a int')
        __self__.max_retries = max_retries
        """
        The maximum number of times to retry this job if it fails.
        """
        __props__['maxRetries'] = max_retries

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the job command. Defaults to `glueetl`
        """
        __props__['name'] = name

        if not role_arn:
            raise TypeError('Missing required property role_arn')
        elif not isinstance(role_arn, basestring):
            raise TypeError('Expected property role_arn to be a basestring')
        __self__.role_arn = role_arn
        """
        The ARN of the IAM role associated with this job.
        """
        __props__['roleArn'] = role_arn

        if timeout and not isinstance(timeout, int):
            raise TypeError('Expected property timeout to be a int')
        __self__.timeout = timeout
        """
        The job timeout in minutes. The default is 2880 minutes (48 hours).
        """
        __props__['timeout'] = timeout

        super(Job, __self__).__init__(
            'aws:glue/job:Job',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'allocatedCapacity' in outs:
            self.allocated_capacity = outs['allocatedCapacity']
        if 'command' in outs:
            self.command = outs['command']
        if 'connections' in outs:
            self.connections = outs['connections']
        if 'defaultArguments' in outs:
            self.default_arguments = outs['defaultArguments']
        if 'description' in outs:
            self.description = outs['description']
        if 'executionProperty' in outs:
            self.execution_property = outs['executionProperty']
        if 'maxRetries' in outs:
            self.max_retries = outs['maxRetries']
        if 'name' in outs:
            self.name = outs['name']
        if 'roleArn' in outs:
            self.role_arn = outs['roleArn']
        if 'timeout' in outs:
            self.timeout = outs['timeout']

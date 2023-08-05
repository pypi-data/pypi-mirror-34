# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class Cluster(pulumi.CustomResource):
    """
    Provides an Elastic MapReduce Cluster, a web service that makes it easy to
    process large amounts of data efficiently. See [Amazon Elastic MapReduce Documentation](https://aws.amazon.com/documentation/elastic-mapreduce/)
    for more information.
    """
    def __init__(__self__, __name__, __opts__=None, additional_info=None, applications=None, autoscaling_role=None, bootstrap_actions=None, configurations=None, core_instance_count=None, core_instance_type=None, custom_ami_id=None, ebs_root_volume_size=None, ec2_attributes=None, instance_groups=None, keep_job_flow_alive_when_no_steps=None, kerberos_attributes=None, log_uri=None, master_instance_type=None, name=None, release_label=None, scale_down_behavior=None, security_configuration=None, service_role=None, steps=None, tags=None, termination_protection=None, visible_to_all_users=None):
        """Create a Cluster resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if additional_info and not isinstance(additional_info, basestring):
            raise TypeError('Expected property additional_info to be a basestring')
        __self__.additional_info = additional_info
        """
        A JSON string for selecting additional features such as adding proxy information. Note: Currently there is no API to retrieve the value of this argument after EMR cluster creation from provider, therefore Terraform cannot detect drift from the actual EMR cluster if its value is changed outside Terraform.
        """
        __props__['additionalInfo'] = additional_info

        if applications and not isinstance(applications, list):
            raise TypeError('Expected property applications to be a list')
        __self__.applications = applications
        """
        A list of applications for the cluster. Valid values are: `Flink`, `Hadoop`, `Hive`, `Mahout`, `Pig`, and `Spark`. Case insensitive
        """
        __props__['applications'] = applications

        if autoscaling_role and not isinstance(autoscaling_role, basestring):
            raise TypeError('Expected property autoscaling_role to be a basestring')
        __self__.autoscaling_role = autoscaling_role
        """
        An IAM role for automatic scaling policies. The IAM role provides permissions that the automatic scaling feature requires to launch and terminate EC2 instances in an instance group.
        """
        __props__['autoscalingRole'] = autoscaling_role

        if bootstrap_actions and not isinstance(bootstrap_actions, list):
            raise TypeError('Expected property bootstrap_actions to be a list')
        __self__.bootstrap_actions = bootstrap_actions
        """
        List of bootstrap actions that will be run before Hadoop is started on
        the cluster nodes. Defined below
        """
        __props__['bootstrapActions'] = bootstrap_actions

        if configurations and not isinstance(configurations, basestring):
            raise TypeError('Expected property configurations to be a basestring')
        __self__.configurations = configurations
        """
        List of configurations supplied for the EMR cluster you are creating
        """
        __props__['configurations'] = configurations

        if core_instance_count and not isinstance(core_instance_count, int):
            raise TypeError('Expected property core_instance_count to be a int')
        __self__.core_instance_count = core_instance_count
        """
        Number of Amazon EC2 instances used to execute the job flow. EMR will use one node as the cluster's master node and use the remainder of the nodes (`core_instance_count`-1) as core nodes. Cannot be specified if `instance_groups` is set. Default `1`
        """
        __props__['coreInstanceCount'] = core_instance_count

        if core_instance_type and not isinstance(core_instance_type, basestring):
            raise TypeError('Expected property core_instance_type to be a basestring')
        __self__.core_instance_type = core_instance_type
        """
        The EC2 instance type of the slave nodes. Cannot be specified if `instance_groups` is set
        """
        __props__['coreInstanceType'] = core_instance_type

        if custom_ami_id and not isinstance(custom_ami_id, basestring):
            raise TypeError('Expected property custom_ami_id to be a basestring')
        __self__.custom_ami_id = custom_ami_id
        """
        A custom Amazon Linux AMI for the cluster (instead of an EMR-owned AMI). Available in Amazon EMR version 5.7.0 and later.
        """
        __props__['customAmiId'] = custom_ami_id

        if ebs_root_volume_size and not isinstance(ebs_root_volume_size, int):
            raise TypeError('Expected property ebs_root_volume_size to be a int')
        __self__.ebs_root_volume_size = ebs_root_volume_size
        """
        Size in GiB of the EBS root device volume of the Linux AMI that is used for each EC2 instance. Available in Amazon EMR version 4.x and later.
        """
        __props__['ebsRootVolumeSize'] = ebs_root_volume_size

        if ec2_attributes and not isinstance(ec2_attributes, dict):
            raise TypeError('Expected property ec2_attributes to be a dict')
        __self__.ec2_attributes = ec2_attributes
        """
        Attributes for the EC2 instances running the job
        flow. Defined below
        """
        __props__['ec2Attributes'] = ec2_attributes

        if instance_groups and not isinstance(instance_groups, list):
            raise TypeError('Expected property instance_groups to be a list')
        __self__.instance_groups = instance_groups
        """
        A list of `instance_group` objects for each instance group in the cluster. Exactly one of `master_instance_type` and `instance_group` must be specified. If `instance_group` is set, then it must contain a configuration block for at least the `MASTER` instance group type (as well as any additional instance groups). Defined below
        """
        __props__['instanceGroups'] = instance_groups

        if keep_job_flow_alive_when_no_steps and not isinstance(keep_job_flow_alive_when_no_steps, bool):
            raise TypeError('Expected property keep_job_flow_alive_when_no_steps to be a bool')
        __self__.keep_job_flow_alive_when_no_steps = keep_job_flow_alive_when_no_steps
        """
        Switch on/off run cluster with no steps or when all steps are complete (default is on)
        """
        __props__['keepJobFlowAliveWhenNoSteps'] = keep_job_flow_alive_when_no_steps

        if kerberos_attributes and not isinstance(kerberos_attributes, dict):
            raise TypeError('Expected property kerberos_attributes to be a dict')
        __self__.kerberos_attributes = kerberos_attributes
        """
        Kerberos configuration for the cluster. Defined below
        """
        __props__['kerberosAttributes'] = kerberos_attributes

        if log_uri and not isinstance(log_uri, basestring):
            raise TypeError('Expected property log_uri to be a basestring')
        __self__.log_uri = log_uri
        """
        S3 bucket to write the log files of the job flow. If a value
        is not provided, logs are not created
        """
        __props__['logUri'] = log_uri

        if master_instance_type and not isinstance(master_instance_type, basestring):
            raise TypeError('Expected property master_instance_type to be a basestring')
        __self__.master_instance_type = master_instance_type
        """
        The EC2 instance type of the master node. Exactly one of `master_instance_type` and `instance_group` must be specified.
        """
        __props__['masterInstanceType'] = master_instance_type

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the job flow
        """
        __props__['name'] = name

        if not release_label:
            raise TypeError('Missing required property release_label')
        elif not isinstance(release_label, basestring):
            raise TypeError('Expected property release_label to be a basestring')
        __self__.release_label = release_label
        """
        The release label for the Amazon EMR release
        """
        __props__['releaseLabel'] = release_label

        if scale_down_behavior and not isinstance(scale_down_behavior, basestring):
            raise TypeError('Expected property scale_down_behavior to be a basestring')
        __self__.scale_down_behavior = scale_down_behavior
        """
        The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an `instance group` is resized. 
        """
        __props__['scaleDownBehavior'] = scale_down_behavior

        if security_configuration and not isinstance(security_configuration, basestring):
            raise TypeError('Expected property security_configuration to be a basestring')
        __self__.security_configuration = security_configuration
        """
        The security configuration name to attach to the EMR cluster. Only valid for EMR clusters with `release_label` 4.8.0 or greater
        """
        __props__['securityConfiguration'] = security_configuration

        if not service_role:
            raise TypeError('Missing required property service_role')
        elif not isinstance(service_role, basestring):
            raise TypeError('Expected property service_role to be a basestring')
        __self__.service_role = service_role
        """
        IAM role that will be assumed by the Amazon EMR service to access AWS resources
        """
        __props__['serviceRole'] = service_role

        if steps and not isinstance(steps, list):
            raise TypeError('Expected property steps to be a list')
        __self__.steps = steps
        """
        List of steps to run when creating the cluster. Defined below. It is highly recommended to utilize the [lifecycle configuration block](/docs/configuration/resources.html) with `ignore_changes` if other steps are being managed outside of Terraform.
        """
        __props__['steps'] = steps

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        """
        list of tags to apply to the EMR Cluster
        """
        __props__['tags'] = tags

        if termination_protection and not isinstance(termination_protection, bool):
            raise TypeError('Expected property termination_protection to be a bool')
        __self__.termination_protection = termination_protection
        """
        Switch on/off termination protection (default is off)
        """
        __props__['terminationProtection'] = termination_protection

        if visible_to_all_users and not isinstance(visible_to_all_users, bool):
            raise TypeError('Expected property visible_to_all_users to be a bool')
        __self__.visible_to_all_users = visible_to_all_users
        """
        Whether the job flow is visible to all IAM users of the AWS account associated with the job flow. Default `true`
        """
        __props__['visibleToAllUsers'] = visible_to_all_users

        __self__.cluster_state = pulumi.runtime.UNKNOWN
        __self__.master_public_dns = pulumi.runtime.UNKNOWN
        """
        The public DNS name of the master EC2 instance.
        """

        super(Cluster, __self__).__init__(
            'aws:emr/cluster:Cluster',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'additionalInfo' in outs:
            self.additional_info = outs['additionalInfo']
        if 'applications' in outs:
            self.applications = outs['applications']
        if 'autoscalingRole' in outs:
            self.autoscaling_role = outs['autoscalingRole']
        if 'bootstrapActions' in outs:
            self.bootstrap_actions = outs['bootstrapActions']
        if 'clusterState' in outs:
            self.cluster_state = outs['clusterState']
        if 'configurations' in outs:
            self.configurations = outs['configurations']
        if 'coreInstanceCount' in outs:
            self.core_instance_count = outs['coreInstanceCount']
        if 'coreInstanceType' in outs:
            self.core_instance_type = outs['coreInstanceType']
        if 'customAmiId' in outs:
            self.custom_ami_id = outs['customAmiId']
        if 'ebsRootVolumeSize' in outs:
            self.ebs_root_volume_size = outs['ebsRootVolumeSize']
        if 'ec2Attributes' in outs:
            self.ec2_attributes = outs['ec2Attributes']
        if 'instanceGroups' in outs:
            self.instance_groups = outs['instanceGroups']
        if 'keepJobFlowAliveWhenNoSteps' in outs:
            self.keep_job_flow_alive_when_no_steps = outs['keepJobFlowAliveWhenNoSteps']
        if 'kerberosAttributes' in outs:
            self.kerberos_attributes = outs['kerberosAttributes']
        if 'logUri' in outs:
            self.log_uri = outs['logUri']
        if 'masterInstanceType' in outs:
            self.master_instance_type = outs['masterInstanceType']
        if 'masterPublicDns' in outs:
            self.master_public_dns = outs['masterPublicDns']
        if 'name' in outs:
            self.name = outs['name']
        if 'releaseLabel' in outs:
            self.release_label = outs['releaseLabel']
        if 'scaleDownBehavior' in outs:
            self.scale_down_behavior = outs['scaleDownBehavior']
        if 'securityConfiguration' in outs:
            self.security_configuration = outs['securityConfiguration']
        if 'serviceRole' in outs:
            self.service_role = outs['serviceRole']
        if 'steps' in outs:
            self.steps = outs['steps']
        if 'tags' in outs:
            self.tags = outs['tags']
        if 'terminationProtection' in outs:
            self.termination_protection = outs['terminationProtection']
        if 'visibleToAllUsers' in outs:
            self.visible_to_all_users = outs['visibleToAllUsers']

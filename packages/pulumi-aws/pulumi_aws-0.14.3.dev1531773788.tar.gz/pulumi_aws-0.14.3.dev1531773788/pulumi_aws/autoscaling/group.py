# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class Group(pulumi.CustomResource):
    """
    Provides an AutoScaling Group resource.
    
    -> **Note:** You must specify either `launch_configuration` or `launch_template`.
    """
    def __init__(__self__, __name__, __opts__=None, availability_zones=None, default_cooldown=None, desired_capacity=None, enabled_metrics=None, force_delete=None, health_check_grace_period=None, health_check_type=None, initial_lifecycle_hooks=None, launch_configuration=None, launch_template=None, load_balancers=None, max_size=None, metrics_granularity=None, min_elb_capacity=None, min_size=None, name=None, name_prefix=None, placement_group=None, protect_from_scale_in=None, service_linked_role_arn=None, suspended_processes=None, tags=None, tags_collection=None, target_group_arns=None, termination_policies=None, vpc_zone_identifiers=None, wait_for_capacity_timeout=None, wait_for_elb_capacity=None):
        """Create a Group resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if availability_zones and not isinstance(availability_zones, list):
            raise TypeError('Expected property availability_zones to be a list')
        __self__.availability_zones = availability_zones
        """
        A list of one or more availability zones for the group. This parameter should not be specified when using `vpc_zone_identifier`.
        """
        __props__['availabilityZones'] = availability_zones

        if default_cooldown and not isinstance(default_cooldown, int):
            raise TypeError('Expected property default_cooldown to be a int')
        __self__.default_cooldown = default_cooldown
        """
        The amount of time, in seconds, after a scaling activity completes before another scaling activity can start.
        """
        __props__['defaultCooldown'] = default_cooldown

        if desired_capacity and not isinstance(desired_capacity, int):
            raise TypeError('Expected property desired_capacity to be a int')
        __self__.desired_capacity = desired_capacity
        """
        The number of Amazon EC2 instances that
        should be running in the group. (See also [Waiting for
        Capacity](#waiting-for-capacity) below.)
        """
        __props__['desiredCapacity'] = desired_capacity

        if enabled_metrics and not isinstance(enabled_metrics, list):
            raise TypeError('Expected property enabled_metrics to be a list')
        __self__.enabled_metrics = enabled_metrics
        """
        A list of metrics to collect. The allowed values are `GroupMinSize`, `GroupMaxSize`, `GroupDesiredCapacity`, `GroupInServiceInstances`, `GroupPendingInstances`, `GroupStandbyInstances`, `GroupTerminatingInstances`, `GroupTotalInstances`.
        * `wait_for_capacity_timeout` (Default: "10m") A maximum
        [duration](https://golang.org/pkg/time/#ParseDuration) that Terraform should
        wait for ASG instances to be healthy before timing out.  (See also [Waiting
        for Capacity](#waiting-for-capacity) below.) Setting this to "0" causes
        Terraform to skip all Capacity Waiting behavior.
        """
        __props__['enabledMetrics'] = enabled_metrics

        if force_delete and not isinstance(force_delete, bool):
            raise TypeError('Expected property force_delete to be a bool')
        __self__.force_delete = force_delete
        """
        Allows deleting the autoscaling group without waiting
        for all instances in the pool to terminate.  You can force an autoscaling group to delete
        even if it's in the process of scaling a resource. Normally, Terraform
        drains all the instances before deleting the group.  This bypasses that
        behavior and potentially leaves resources dangling.
        """
        __props__['forceDelete'] = force_delete

        if health_check_grace_period and not isinstance(health_check_grace_period, int):
            raise TypeError('Expected property health_check_grace_period to be a int')
        __self__.health_check_grace_period = health_check_grace_period
        """
        Time (in seconds) after instance comes into service before checking health.
        """
        __props__['healthCheckGracePeriod'] = health_check_grace_period

        if health_check_type and not isinstance(health_check_type, basestring):
            raise TypeError('Expected property health_check_type to be a basestring')
        __self__.health_check_type = health_check_type
        """
        "EC2" or "ELB". Controls how health checking is done.
        """
        __props__['healthCheckType'] = health_check_type

        if initial_lifecycle_hooks and not isinstance(initial_lifecycle_hooks, list):
            raise TypeError('Expected property initial_lifecycle_hooks to be a list')
        __self__.initial_lifecycle_hooks = initial_lifecycle_hooks
        """
        One or more
        [Lifecycle Hooks](http://docs.aws.amazon.com/autoscaling/latest/userguide/lifecycle-hooks.html)
        to attach to the autoscaling group **before** instances are launched. The
        syntax is exactly the same as the separate
        [`aws_autoscaling_lifecycle_hook`](/docs/providers/aws/r/autoscaling_lifecycle_hooks.html)
        resource, without the `autoscaling_group_name` attribute. Please note that this will only work when creating
        a new autoscaling group. For all other use-cases, please use `aws_autoscaling_lifecycle_hook` resource.
        """
        __props__['initialLifecycleHooks'] = initial_lifecycle_hooks

        if launch_configuration and not isinstance(launch_configuration, basestring):
            raise TypeError('Expected property launch_configuration to be a basestring')
        __self__.launch_configuration = launch_configuration
        """
        The name of the launch configuration to use.
        """
        __props__['launchConfiguration'] = launch_configuration

        if launch_template and not isinstance(launch_template, dict):
            raise TypeError('Expected property launch_template to be a dict')
        __self__.launch_template = launch_template
        """
        Launch template specification to use to launch instances.
        See [Launch Template Specification](#launch-template-specification) below for more details.
        """
        __props__['launchTemplate'] = launch_template

        if load_balancers and not isinstance(load_balancers, list):
            raise TypeError('Expected property load_balancers to be a list')
        __self__.load_balancers = load_balancers
        """
        A list of elastic load balancer names to add to the autoscaling
        group names. Only valid for classic load balancers. For ALBs, use `target_group_arns` instead.
        """
        __props__['loadBalancers'] = load_balancers

        if not max_size:
            raise TypeError('Missing required property max_size')
        elif not isinstance(max_size, int):
            raise TypeError('Expected property max_size to be a int')
        __self__.max_size = max_size
        """
        The maximum size of the auto scale group.
        """
        __props__['maxSize'] = max_size

        if metrics_granularity and not isinstance(metrics_granularity, basestring):
            raise TypeError('Expected property metrics_granularity to be a basestring')
        __self__.metrics_granularity = metrics_granularity
        """
        The granularity to associate with the metrics to collect. The only valid value is `1Minute`. Default is `1Minute`.
        """
        __props__['metricsGranularity'] = metrics_granularity

        if min_elb_capacity and not isinstance(min_elb_capacity, int):
            raise TypeError('Expected property min_elb_capacity to be a int')
        __self__.min_elb_capacity = min_elb_capacity
        """
        Setting this causes Terraform to wait for
        this number of instances to show up healthy in the ELB only on creation.
        Updates will not wait on ELB instance number changes.
        (See also [Waiting for Capacity](#waiting-for-capacity) below.)
        """
        __props__['minElbCapacity'] = min_elb_capacity

        if not min_size:
            raise TypeError('Missing required property min_size')
        elif not isinstance(min_size, int):
            raise TypeError('Expected property min_size to be a int')
        __self__.min_size = min_size
        """
        The minimum size of the auto scale group.
        (See also [Waiting for Capacity](#waiting-for-capacity) below.)
        """
        __props__['minSize'] = min_size

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the launch template. Conflicts with `id`.
        """
        __props__['name'] = name

        if name_prefix and not isinstance(name_prefix, basestring):
            raise TypeError('Expected property name_prefix to be a basestring')
        __self__.name_prefix = name_prefix
        """
        Creates a unique name beginning with the specified
        prefix. Conflicts with `name`.
        """
        __props__['namePrefix'] = name_prefix

        if placement_group and not isinstance(placement_group, basestring):
            raise TypeError('Expected property placement_group to be a basestring')
        __self__.placement_group = placement_group
        """
        The name of the placement group into which you'll launch your instances, if any.
        """
        __props__['placementGroup'] = placement_group

        if protect_from_scale_in and not isinstance(protect_from_scale_in, bool):
            raise TypeError('Expected property protect_from_scale_in to be a bool')
        __self__.protect_from_scale_in = protect_from_scale_in
        """
        Allows setting instance protection. The
        autoscaling group will not select instances with this setting for terminination
        during scale in events.
        """
        __props__['protectFromScaleIn'] = protect_from_scale_in

        if service_linked_role_arn and not isinstance(service_linked_role_arn, basestring):
            raise TypeError('Expected property service_linked_role_arn to be a basestring')
        __self__.service_linked_role_arn = service_linked_role_arn
        """
        The ARN of the service-linked role that the ASG will use to call other AWS services
        """
        __props__['serviceLinkedRoleArn'] = service_linked_role_arn

        if suspended_processes and not isinstance(suspended_processes, list):
            raise TypeError('Expected property suspended_processes to be a list')
        __self__.suspended_processes = suspended_processes
        """
        A list of processes to suspend for the AutoScaling Group. The allowed values are `Launch`, `Terminate`, `HealthCheck`, `ReplaceUnhealthy`, `AZRebalance`, `AlarmNotification`, `ScheduledActions`, `AddToLoadBalancer`.
        Note that if you suspend either the `Launch` or `Terminate` process types, it can prevent your autoscaling group from functioning properly.
        """
        __props__['suspendedProcesses'] = suspended_processes

        if tags and not isinstance(tags, list):
            raise TypeError('Expected property tags to be a list')
        __self__.tags = tags
        """
        A list of tag blocks. Tags documented below.
        """
        __props__['tags'] = tags

        if tags_collection and not isinstance(tags_collection, list):
            raise TypeError('Expected property tags_collection to be a list')
        __self__.tags_collection = tags_collection
        """
        A list of tag blocks (maps). Tags documented below.
        """
        __props__['tagsCollection'] = tags_collection

        if target_group_arns and not isinstance(target_group_arns, list):
            raise TypeError('Expected property target_group_arns to be a list')
        __self__.target_group_arns = target_group_arns
        """
        A list of `aws_alb_target_group` ARNs, for use with Application Load Balancing.
        """
        __props__['targetGroupArns'] = target_group_arns

        if termination_policies and not isinstance(termination_policies, list):
            raise TypeError('Expected property termination_policies to be a list')
        __self__.termination_policies = termination_policies
        """
        A list of policies to decide how the instances in the auto scale group should be terminated. The allowed values are `OldestInstance`, `NewestInstance`, `OldestLaunchConfiguration`, `ClosestToNextInstanceHour`, `Default`.
        """
        __props__['terminationPolicies'] = termination_policies

        if vpc_zone_identifiers and not isinstance(vpc_zone_identifiers, list):
            raise TypeError('Expected property vpc_zone_identifiers to be a list')
        __self__.vpc_zone_identifiers = vpc_zone_identifiers
        """
        A list of subnet IDs to launch resources in.
        """
        __props__['vpcZoneIdentifiers'] = vpc_zone_identifiers

        if wait_for_capacity_timeout and not isinstance(wait_for_capacity_timeout, basestring):
            raise TypeError('Expected property wait_for_capacity_timeout to be a basestring')
        __self__.wait_for_capacity_timeout = wait_for_capacity_timeout
        __props__['waitForCapacityTimeout'] = wait_for_capacity_timeout

        if wait_for_elb_capacity and not isinstance(wait_for_elb_capacity, int):
            raise TypeError('Expected property wait_for_elb_capacity to be a int')
        __self__.wait_for_elb_capacity = wait_for_elb_capacity
        """
        Setting this will cause Terraform to wait
        for exactly this number of healthy instances in all attached load balancers
        on both create and update operations. (Takes precedence over
        `min_elb_capacity` behavior.)
        (See also [Waiting for Capacity](#waiting-for-capacity) below.)
        """
        __props__['waitForElbCapacity'] = wait_for_elb_capacity

        __self__.arn = pulumi.runtime.UNKNOWN
        """
        The ARN for this AutoScaling Group
        """

        super(Group, __self__).__init__(
            'aws:autoscaling/group:Group',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'arn' in outs:
            self.arn = outs['arn']
        if 'availabilityZones' in outs:
            self.availability_zones = outs['availabilityZones']
        if 'defaultCooldown' in outs:
            self.default_cooldown = outs['defaultCooldown']
        if 'desiredCapacity' in outs:
            self.desired_capacity = outs['desiredCapacity']
        if 'enabledMetrics' in outs:
            self.enabled_metrics = outs['enabledMetrics']
        if 'forceDelete' in outs:
            self.force_delete = outs['forceDelete']
        if 'healthCheckGracePeriod' in outs:
            self.health_check_grace_period = outs['healthCheckGracePeriod']
        if 'healthCheckType' in outs:
            self.health_check_type = outs['healthCheckType']
        if 'initialLifecycleHooks' in outs:
            self.initial_lifecycle_hooks = outs['initialLifecycleHooks']
        if 'launchConfiguration' in outs:
            self.launch_configuration = outs['launchConfiguration']
        if 'launchTemplate' in outs:
            self.launch_template = outs['launchTemplate']
        if 'loadBalancers' in outs:
            self.load_balancers = outs['loadBalancers']
        if 'maxSize' in outs:
            self.max_size = outs['maxSize']
        if 'metricsGranularity' in outs:
            self.metrics_granularity = outs['metricsGranularity']
        if 'minElbCapacity' in outs:
            self.min_elb_capacity = outs['minElbCapacity']
        if 'minSize' in outs:
            self.min_size = outs['minSize']
        if 'name' in outs:
            self.name = outs['name']
        if 'namePrefix' in outs:
            self.name_prefix = outs['namePrefix']
        if 'placementGroup' in outs:
            self.placement_group = outs['placementGroup']
        if 'protectFromScaleIn' in outs:
            self.protect_from_scale_in = outs['protectFromScaleIn']
        if 'serviceLinkedRoleArn' in outs:
            self.service_linked_role_arn = outs['serviceLinkedRoleArn']
        if 'suspendedProcesses' in outs:
            self.suspended_processes = outs['suspendedProcesses']
        if 'tags' in outs:
            self.tags = outs['tags']
        if 'tagsCollection' in outs:
            self.tags_collection = outs['tagsCollection']
        if 'targetGroupArns' in outs:
            self.target_group_arns = outs['targetGroupArns']
        if 'terminationPolicies' in outs:
            self.termination_policies = outs['terminationPolicies']
        if 'vpcZoneIdentifiers' in outs:
            self.vpc_zone_identifiers = outs['vpcZoneIdentifiers']
        if 'waitForCapacityTimeout' in outs:
            self.wait_for_capacity_timeout = outs['waitForCapacityTimeout']
        if 'waitForElbCapacity' in outs:
            self.wait_for_elb_capacity = outs['waitForElbCapacity']

# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class Firewall(pulumi.CustomResource):
    """
    Manages a v1 firewall resource within OpenStack.
    """
    def __init__(__self__, __name__, __opts__=None, admin_state_up=None, associated_routers=None, description=None, name=None, no_routers=None, policy_id=None, region=None, tenant_id=None, value_specs=None):
        """Create a Firewall resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if admin_state_up and not isinstance(admin_state_up, bool):
            raise TypeError('Expected property admin_state_up to be a bool')
        __self__.admin_state_up = admin_state_up
        """
        Administrative up/down status for the firewall
        (must be "true" or "false" if provided - defaults to "true").
        Changing this updates the `admin_state_up` of an existing firewall.
        """
        __props__['adminStateUp'] = admin_state_up

        if associated_routers and not isinstance(associated_routers, list):
            raise TypeError('Expected property associated_routers to be a list')
        __self__.associated_routers = associated_routers
        """
        Router(s) to associate this firewall instance
        with. Must be a list of strings. Changing this updates the associated routers
        of an existing firewall. Conflicts with `no_routers`.
        """
        __props__['associatedRouters'] = associated_routers

        if description and not isinstance(description, basestring):
            raise TypeError('Expected property description to be a basestring')
        __self__.description = description
        """
        A description for the firewall. Changing this
        updates the `description` of an existing firewall.
        """
        __props__['description'] = description

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        A name for the firewall. Changing this
        updates the `name` of an existing firewall.
        """
        __props__['name'] = name

        if no_routers and not isinstance(no_routers, bool):
            raise TypeError('Expected property no_routers to be a bool')
        __self__.no_routers = no_routers
        """
        Should this firewall not be associated with any routers
        (must be "true" or "false" if provide - defaults to "false").
        Conflicts with `associated_routers`.
        """
        __props__['noRouters'] = no_routers

        if not policy_id:
            raise TypeError('Missing required property policy_id')
        elif not isinstance(policy_id, basestring):
            raise TypeError('Expected property policy_id to be a basestring')
        __self__.policy_id = policy_id
        """
        The policy resource id for the firewall. Changing
        this updates the `policy_id` of an existing firewall.
        """
        __props__['policyId'] = policy_id

        if region and not isinstance(region, basestring):
            raise TypeError('Expected property region to be a basestring')
        __self__.region = region
        """
        The region in which to obtain the v1 networking client.
        A networking client is needed to create a firewall. If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        firewall.
        """
        __props__['region'] = region

        if tenant_id and not isinstance(tenant_id, basestring):
            raise TypeError('Expected property tenant_id to be a basestring')
        __self__.tenant_id = tenant_id
        """
        The owner of the floating IP. Required if admin wants
        to create a firewall for another tenant. Changing this creates a new
        firewall.
        """
        __props__['tenantId'] = tenant_id

        if value_specs and not isinstance(value_specs, dict):
            raise TypeError('Expected property value_specs to be a dict')
        __self__.value_specs = value_specs
        """
        Map of additional options.
        """
        __props__['valueSpecs'] = value_specs

        super(Firewall, __self__).__init__(
            'openstack:firewall/firewall:Firewall',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'adminStateUp' in outs:
            self.admin_state_up = outs['adminStateUp']
        if 'associatedRouters' in outs:
            self.associated_routers = outs['associatedRouters']
        if 'description' in outs:
            self.description = outs['description']
        if 'name' in outs:
            self.name = outs['name']
        if 'noRouters' in outs:
            self.no_routers = outs['noRouters']
        if 'policyId' in outs:
            self.policy_id = outs['policyId']
        if 'region' in outs:
            self.region = outs['region']
        if 'tenantId' in outs:
            self.tenant_id = outs['tenantId']
        if 'valueSpecs' in outs:
            self.value_specs = outs['valueSpecs']

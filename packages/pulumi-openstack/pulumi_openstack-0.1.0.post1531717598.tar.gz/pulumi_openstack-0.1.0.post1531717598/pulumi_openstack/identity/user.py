# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class User(pulumi.CustomResource):
    """
    Manages a V3 User resource within OpenStack Keystone.
    
    Note: You _must_ have admin privileges in your OpenStack cloud to use
    this resource.
    """
    def __init__(__self__, __name__, __opts__=None, default_project_id=None, description=None, domain_id=None, enabled=None, extra=None, ignore_change_password_upon_first_use=None, ignore_lockout_failure_attempts=None, ignore_password_expiry=None, multi_factor_auth_enabled=None, multi_factor_auth_rules=None, name=None, password=None, region=None):
        """Create a User resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if default_project_id and not isinstance(default_project_id, basestring):
            raise TypeError('Expected property default_project_id to be a basestring')
        __self__.default_project_id = default_project_id
        """
        The default project this user belongs to.
        """
        __props__['defaultProjectId'] = default_project_id

        if description and not isinstance(description, basestring):
            raise TypeError('Expected property description to be a basestring')
        __self__.description = description
        """
        A description of the user.
        """
        __props__['description'] = description

        if domain_id and not isinstance(domain_id, basestring):
            raise TypeError('Expected property domain_id to be a basestring')
        __self__.domain_id = domain_id
        """
        The domain this user belongs to.
        """
        __props__['domainId'] = domain_id

        if enabled and not isinstance(enabled, bool):
            raise TypeError('Expected property enabled to be a bool')
        __self__.enabled = enabled
        """
        Whether the user is enabled or disabled. Valid
        values are `true` and `false`.
        """
        __props__['enabled'] = enabled

        if extra and not isinstance(extra, dict):
            raise TypeError('Expected property extra to be a dict')
        __self__.extra = extra
        """
        Free-form key/value pairs of extra information.
        """
        __props__['extra'] = extra

        if ignore_change_password_upon_first_use and not isinstance(ignore_change_password_upon_first_use, bool):
            raise TypeError('Expected property ignore_change_password_upon_first_use to be a bool')
        __self__.ignore_change_password_upon_first_use = ignore_change_password_upon_first_use
        """
        User will not have to
        change their password upon first use. Valid values are `true` and `false`.
        """
        __props__['ignoreChangePasswordUponFirstUse'] = ignore_change_password_upon_first_use

        if ignore_lockout_failure_attempts and not isinstance(ignore_lockout_failure_attempts, bool):
            raise TypeError('Expected property ignore_lockout_failure_attempts to be a bool')
        __self__.ignore_lockout_failure_attempts = ignore_lockout_failure_attempts
        """
        User will not have a failure
        lockout placed on their account. Valid values are `true` and `false`.
        """
        __props__['ignoreLockoutFailureAttempts'] = ignore_lockout_failure_attempts

        if ignore_password_expiry and not isinstance(ignore_password_expiry, bool):
            raise TypeError('Expected property ignore_password_expiry to be a bool')
        __self__.ignore_password_expiry = ignore_password_expiry
        """
        User's password will not expire.
        Valid values are `true` and `false`.
        """
        __props__['ignorePasswordExpiry'] = ignore_password_expiry

        if multi_factor_auth_enabled and not isinstance(multi_factor_auth_enabled, bool):
            raise TypeError('Expected property multi_factor_auth_enabled to be a bool')
        __self__.multi_factor_auth_enabled = multi_factor_auth_enabled
        """
        Whether to enable multi-factor
        authentication. Valid values are `true` and `false`.
        """
        __props__['multiFactorAuthEnabled'] = multi_factor_auth_enabled

        if multi_factor_auth_rules and not isinstance(multi_factor_auth_rules, list):
            raise TypeError('Expected property multi_factor_auth_rules to be a list')
        __self__.multi_factor_auth_rules = multi_factor_auth_rules
        """
        A multi-factor authentication rule.
        The structure is documented below. Please see the
        [Ocata release notes](https://docs.openstack.org/releasenotes/keystone/ocata.html)
        for more information on how to use mulit-factor rules.
        """
        __props__['multiFactorAuthRules'] = multi_factor_auth_rules

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the user.
        """
        __props__['name'] = name

        if password and not isinstance(password, basestring):
            raise TypeError('Expected property password to be a basestring')
        __self__.password = password
        """
        The password for the user.
        """
        __props__['password'] = password

        if region and not isinstance(region, basestring):
            raise TypeError('Expected property region to be a basestring')
        __self__.region = region
        """
        The region in which to obtain the V3 Keystone client.
        If omitted, the `region` argument of the provider is used. Changing this
        creates a new User.
        """
        __props__['region'] = region

        super(User, __self__).__init__(
            'openstack:identity/user:User',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'defaultProjectId' in outs:
            self.default_project_id = outs['defaultProjectId']
        if 'description' in outs:
            self.description = outs['description']
        if 'domainId' in outs:
            self.domain_id = outs['domainId']
        if 'enabled' in outs:
            self.enabled = outs['enabled']
        if 'extra' in outs:
            self.extra = outs['extra']
        if 'ignoreChangePasswordUponFirstUse' in outs:
            self.ignore_change_password_upon_first_use = outs['ignoreChangePasswordUponFirstUse']
        if 'ignoreLockoutFailureAttempts' in outs:
            self.ignore_lockout_failure_attempts = outs['ignoreLockoutFailureAttempts']
        if 'ignorePasswordExpiry' in outs:
            self.ignore_password_expiry = outs['ignorePasswordExpiry']
        if 'multiFactorAuthEnabled' in outs:
            self.multi_factor_auth_enabled = outs['multiFactorAuthEnabled']
        if 'multiFactorAuthRules' in outs:
            self.multi_factor_auth_rules = outs['multiFactorAuthRules']
        if 'name' in outs:
            self.name = outs['name']
        if 'password' in outs:
            self.password = outs['password']
        if 'region' in outs:
            self.region = outs['region']

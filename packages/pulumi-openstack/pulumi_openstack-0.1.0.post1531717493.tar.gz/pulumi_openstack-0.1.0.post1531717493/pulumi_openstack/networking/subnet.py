# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class Subnet(pulumi.CustomResource):
    """
    Manages a V2 Neutron subnet resource within OpenStack.
    """
    def __init__(__self__, __name__, __opts__=None, allocation_pools=None, cidr=None, dns_nameservers=None, enable_dhcp=None, gateway_ip=None, host_routes=None, ip_version=None, ipv6_address_mode=None, ipv6_ra_mode=None, name=None, network_id=None, no_gateway=None, region=None, subnetpool_id=None, tenant_id=None, value_specs=None):
        """Create a Subnet resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if allocation_pools and not isinstance(allocation_pools, list):
            raise TypeError('Expected property allocation_pools to be a list')
        __self__.allocation_pools = allocation_pools
        """
        An array of sub-ranges of CIDR available for
        dynamic allocation to ports. The allocation_pool object structure is
        documented below. Changing this creates a new subnet.
        """
        __props__['allocationPools'] = allocation_pools

        if cidr and not isinstance(cidr, basestring):
            raise TypeError('Expected property cidr to be a basestring')
        __self__.cidr = cidr
        """
        CIDR representing IP range for this subnet, based on IP
        version. Changing this creates a new subnet.
        """
        __props__['cidr'] = cidr

        if dns_nameservers and not isinstance(dns_nameservers, list):
            raise TypeError('Expected property dns_nameservers to be a list')
        __self__.dns_nameservers = dns_nameservers
        """
        An array of DNS name server names used by hosts
        in this subnet. Changing this updates the DNS name servers for the existing
        subnet.
        """
        __props__['dnsNameservers'] = dns_nameservers

        if enable_dhcp and not isinstance(enable_dhcp, bool):
            raise TypeError('Expected property enable_dhcp to be a bool')
        __self__.enable_dhcp = enable_dhcp
        """
        The administrative state of the network.
        Acceptable values are "true" and "false". Changing this value enables or
        disables the DHCP capabilities of the existing subnet. Defaults to true.
        """
        __props__['enableDhcp'] = enable_dhcp

        if gateway_ip and not isinstance(gateway_ip, basestring):
            raise TypeError('Expected property gateway_ip to be a basestring')
        __self__.gateway_ip = gateway_ip
        """
        Default gateway used by devices in this subnet.
        Leaving this blank and not setting `no_gateway` will cause a default
        gateway of `.1` to be used. Changing this updates the gateway IP of the
        existing subnet.
        """
        __props__['gatewayIp'] = gateway_ip

        if host_routes and not isinstance(host_routes, list):
            raise TypeError('Expected property host_routes to be a list')
        __self__.host_routes = host_routes
        """
        An array of routes that should be used by devices
        with IPs from this subnet (not including local subnet route). The host_route
        object structure is documented below. Changing this updates the host routes
        for the existing subnet.
        """
        __props__['hostRoutes'] = host_routes

        if ip_version and not isinstance(ip_version, int):
            raise TypeError('Expected property ip_version to be a int')
        __self__.ip_version = ip_version
        """
        IP version, either 4 (default) or 6. Changing this creates a
        new subnet.
        """
        __props__['ipVersion'] = ip_version

        if ipv6_address_mode and not isinstance(ipv6_address_mode, basestring):
            raise TypeError('Expected property ipv6_address_mode to be a basestring')
        __self__.ipv6_address_mode = ipv6_address_mode
        """
        The IPv6 address mode. Valid values are
        `dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
        """
        __props__['ipv6AddressMode'] = ipv6_address_mode

        if ipv6_ra_mode and not isinstance(ipv6_ra_mode, basestring):
            raise TypeError('Expected property ipv6_ra_mode to be a basestring')
        __self__.ipv6_ra_mode = ipv6_ra_mode
        """
        The IPv6 Router Advertisement mode. Valid values
        are `dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
        """
        __props__['ipv6RaMode'] = ipv6_ra_mode

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the subnet. Changing this updates the name of
        the existing subnet.
        """
        __props__['name'] = name

        if not network_id:
            raise TypeError('Missing required property network_id')
        elif not isinstance(network_id, basestring):
            raise TypeError('Expected property network_id to be a basestring')
        __self__.network_id = network_id
        """
        The UUID of the parent network. Changing this
        creates a new subnet.
        """
        __props__['networkId'] = network_id

        if no_gateway and not isinstance(no_gateway, bool):
            raise TypeError('Expected property no_gateway to be a bool')
        __self__.no_gateway = no_gateway
        """
        Do not set a gateway IP on this subnet. Changing
        this removes or adds a default gateway IP of the existing subnet.
        """
        __props__['noGateway'] = no_gateway

        if region and not isinstance(region, basestring):
            raise TypeError('Expected property region to be a basestring')
        __self__.region = region
        """
        The region in which to obtain the V2 Networking client.
        A Networking client is needed to create a Neutron subnet. If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        subnet.
        """
        __props__['region'] = region

        if subnetpool_id and not isinstance(subnetpool_id, basestring):
            raise TypeError('Expected property subnetpool_id to be a basestring')
        __self__.subnetpool_id = subnetpool_id
        """
        The ID of the subnetpool associated with the subnet.
        """
        __props__['subnetpoolId'] = subnetpool_id

        if tenant_id and not isinstance(tenant_id, basestring):
            raise TypeError('Expected property tenant_id to be a basestring')
        __self__.tenant_id = tenant_id
        """
        The owner of the subnet. Required if admin wants to
        create a subnet for another tenant. Changing this creates a new subnet.
        """
        __props__['tenantId'] = tenant_id

        if value_specs and not isinstance(value_specs, dict):
            raise TypeError('Expected property value_specs to be a dict')
        __self__.value_specs = value_specs
        """
        Map of additional options.
        """
        __props__['valueSpecs'] = value_specs

        super(Subnet, __self__).__init__(
            'openstack:networking/subnet:Subnet',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'allocationPools' in outs:
            self.allocation_pools = outs['allocationPools']
        if 'cidr' in outs:
            self.cidr = outs['cidr']
        if 'dnsNameservers' in outs:
            self.dns_nameservers = outs['dnsNameservers']
        if 'enableDhcp' in outs:
            self.enable_dhcp = outs['enableDhcp']
        if 'gatewayIp' in outs:
            self.gateway_ip = outs['gatewayIp']
        if 'hostRoutes' in outs:
            self.host_routes = outs['hostRoutes']
        if 'ipVersion' in outs:
            self.ip_version = outs['ipVersion']
        if 'ipv6AddressMode' in outs:
            self.ipv6_address_mode = outs['ipv6AddressMode']
        if 'ipv6RaMode' in outs:
            self.ipv6_ra_mode = outs['ipv6RaMode']
        if 'name' in outs:
            self.name = outs['name']
        if 'networkId' in outs:
            self.network_id = outs['networkId']
        if 'noGateway' in outs:
            self.no_gateway = outs['noGateway']
        if 'region' in outs:
            self.region = outs['region']
        if 'subnetpoolId' in outs:
            self.subnetpool_id = outs['subnetpoolId']
        if 'tenantId' in outs:
            self.tenant_id = outs['tenantId']
        if 'valueSpecs' in outs:
            self.value_specs = outs['valueSpecs']

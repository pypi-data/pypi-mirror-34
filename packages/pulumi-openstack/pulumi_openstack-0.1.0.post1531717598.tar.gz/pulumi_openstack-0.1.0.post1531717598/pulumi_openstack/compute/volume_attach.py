# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class VolumeAttach(pulumi.CustomResource):
    """
    Attaches a Block Storage Volume to an Instance using the OpenStack
    Compute (Nova) v2 API.
    """
    def __init__(__self__, __name__, __opts__=None, device=None, instance_id=None, region=None, volume_id=None):
        """Create a VolumeAttach resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if device and not isinstance(device, basestring):
            raise TypeError('Expected property device to be a basestring')
        __self__.device = device
        """
        The device of the volume attachment (ex: `/dev/vdc`).
        _NOTE_: Being able to specify a device is dependent upon the hypervisor in
        use. There is a chance that the device specified in Terraform will not be
        the same device the hypervisor chose. If this happens, Terraform will wish
        to update the device upon subsequent applying which will cause the volume
        to be detached and reattached indefinitely. Please use with caution.
        """
        __props__['device'] = device

        if not instance_id:
            raise TypeError('Missing required property instance_id')
        elif not isinstance(instance_id, basestring):
            raise TypeError('Expected property instance_id to be a basestring')
        __self__.instance_id = instance_id
        """
        The ID of the Instance to attach the Volume to.
        """
        __props__['instanceId'] = instance_id

        if region and not isinstance(region, basestring):
            raise TypeError('Expected property region to be a basestring')
        __self__.region = region
        """
        The region in which to obtain the V2 Compute client.
        A Compute client is needed to create a volume attachment. If omitted, the
        `region` argument of the provider is used. Changing this creates a
        new volume attachment.
        """
        __props__['region'] = region

        if not volume_id:
            raise TypeError('Missing required property volume_id')
        elif not isinstance(volume_id, basestring):
            raise TypeError('Expected property volume_id to be a basestring')
        __self__.volume_id = volume_id
        """
        The ID of the Volume to attach to an Instance.
        """
        __props__['volumeId'] = volume_id

        super(VolumeAttach, __self__).__init__(
            'openstack:compute/volumeAttach:VolumeAttach',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'device' in outs:
            self.device = outs['device']
        if 'instanceId' in outs:
            self.instance_id = outs['instanceId']
        if 'region' in outs:
            self.region = outs['region']
        if 'volumeId' in outs:
            self.volume_id = outs['volumeId']

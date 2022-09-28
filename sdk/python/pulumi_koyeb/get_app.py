# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetAppResult',
    'AwaitableGetAppResult',
    'get_app',
    'get_app_output',
]

@pulumi.output_type
class GetAppResult:
    """
    A collection of values returned by getApp.
    """
    def __init__(__self__, created_at=None, domains=None, id=None, name=None, organization_id=None, updated_at=None):
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if domains and not isinstance(domains, list):
            raise TypeError("Expected argument 'domains' to be a list")
        pulumi.set(__self__, "domains", domains)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if organization_id and not isinstance(organization_id, str):
            raise TypeError("Expected argument 'organization_id' to be a str")
        pulumi.set(__self__, "organization_id", organization_id)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        The date and time of when the app was created
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def domains(self) -> Sequence['outputs.GetAppDomainResult']:
        """
        The app domains
        """
        return pulumi.get(self, "domains")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The app ID
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The app name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> str:
        """
        The organization ID owning the app
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> str:
        """
        The date and time of when the app was last updated
        """
        return pulumi.get(self, "updated_at")


class AwaitableGetAppResult(GetAppResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAppResult(
            created_at=self.created_at,
            domains=self.domains,
            id=self.id,
            name=self.name,
            organization_id=self.organization_id,
            updated_at=self.updated_at)


def get_app(name: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAppResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_koyeb as koyeb

    my_app = koyeb.get_app(name="my-app")
    ```


    :param str name: The app name
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('koyeb:index/getApp:getApp', __args__, opts=opts, typ=GetAppResult).value

    return AwaitableGetAppResult(
        created_at=__ret__.created_at,
        domains=__ret__.domains,
        id=__ret__.id,
        name=__ret__.name,
        organization_id=__ret__.organization_id,
        updated_at=__ret__.updated_at)


@_utilities.lift_output_func(get_app)
def get_app_output(name: Optional[pulumi.Input[str]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAppResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_koyeb as koyeb

    my_app = koyeb.get_app(name="my-app")
    ```


    :param str name: The app name
    """
    ...

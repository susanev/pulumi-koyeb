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
from ._inputs import *

__all__ = [
    'GetSecretResult',
    'AwaitableGetSecretResult',
    'get_secret',
    'get_secret_output',
]

@pulumi.output_type
class GetSecretResult:
    """
    A collection of values returned by getSecret.
    """
    def __init__(__self__, azure_container_registry=None, created_at=None, digital_ocean_container_registry=None, docker_hub_registry=None, github_registry=None, gitlab_registry=None, id=None, name=None, organization_id=None, private_registry=None, type=None, updated_at=None, value=None):
        if azure_container_registry and not isinstance(azure_container_registry, dict):
            raise TypeError("Expected argument 'azure_container_registry' to be a dict")
        pulumi.set(__self__, "azure_container_registry", azure_container_registry)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if digital_ocean_container_registry and not isinstance(digital_ocean_container_registry, dict):
            raise TypeError("Expected argument 'digital_ocean_container_registry' to be a dict")
        pulumi.set(__self__, "digital_ocean_container_registry", digital_ocean_container_registry)
        if docker_hub_registry and not isinstance(docker_hub_registry, dict):
            raise TypeError("Expected argument 'docker_hub_registry' to be a dict")
        pulumi.set(__self__, "docker_hub_registry", docker_hub_registry)
        if github_registry and not isinstance(github_registry, dict):
            raise TypeError("Expected argument 'github_registry' to be a dict")
        pulumi.set(__self__, "github_registry", github_registry)
        if gitlab_registry and not isinstance(gitlab_registry, dict):
            raise TypeError("Expected argument 'gitlab_registry' to be a dict")
        pulumi.set(__self__, "gitlab_registry", gitlab_registry)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if organization_id and not isinstance(organization_id, str):
            raise TypeError("Expected argument 'organization_id' to be a str")
        pulumi.set(__self__, "organization_id", organization_id)
        if private_registry and not isinstance(private_registry, dict):
            raise TypeError("Expected argument 'private_registry' to be a dict")
        pulumi.set(__self__, "private_registry", private_registry)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)
        if value and not isinstance(value, str):
            raise TypeError("Expected argument 'value' to be a str")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="azureContainerRegistry")
    def azure_container_registry(self) -> Optional['outputs.GetSecretAzureContainerRegistryResult']:
        """
        The Azure registry configuration to use
        """
        return pulumi.get(self, "azure_container_registry")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        The date and time of when the secret was created
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="digitalOceanContainerRegistry")
    def digital_ocean_container_registry(self) -> Optional['outputs.GetSecretDigitalOceanContainerRegistryResult']:
        """
        The DigitalOcean registry configuration to use
        """
        return pulumi.get(self, "digital_ocean_container_registry")

    @property
    @pulumi.getter(name="dockerHubRegistry")
    def docker_hub_registry(self) -> Optional['outputs.GetSecretDockerHubRegistryResult']:
        """
        The DockerHub registry configuration to use
        """
        return pulumi.get(self, "docker_hub_registry")

    @property
    @pulumi.getter(name="githubRegistry")
    def github_registry(self) -> Optional['outputs.GetSecretGithubRegistryResult']:
        """
        The GitHub registry configuration to use
        """
        return pulumi.get(self, "github_registry")

    @property
    @pulumi.getter(name="gitlabRegistry")
    def gitlab_registry(self) -> Optional['outputs.GetSecretGitlabRegistryResult']:
        """
        The GitLab registry configuration to use
        """
        return pulumi.get(self, "gitlab_registry")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The secret ID
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The secret name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> str:
        """
        The organization ID owning the secret
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="privateRegistry")
    def private_registry(self) -> Optional['outputs.GetSecretPrivateRegistryResult']:
        """
        The DigitalOcean registry configuration to use
        """
        return pulumi.get(self, "private_registry")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The secret type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> str:
        """
        The date and time of when the secret was last updated
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        The secret value
        """
        return pulumi.get(self, "value")


class AwaitableGetSecretResult(GetSecretResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecretResult(
            azure_container_registry=self.azure_container_registry,
            created_at=self.created_at,
            digital_ocean_container_registry=self.digital_ocean_container_registry,
            docker_hub_registry=self.docker_hub_registry,
            github_registry=self.github_registry,
            gitlab_registry=self.gitlab_registry,
            id=self.id,
            name=self.name,
            organization_id=self.organization_id,
            private_registry=self.private_registry,
            type=self.type,
            updated_at=self.updated_at,
            value=self.value)


def get_secret(azure_container_registry: Optional[pulumi.InputType['GetSecretAzureContainerRegistryArgs']] = None,
               digital_ocean_container_registry: Optional[pulumi.InputType['GetSecretDigitalOceanContainerRegistryArgs']] = None,
               docker_hub_registry: Optional[pulumi.InputType['GetSecretDockerHubRegistryArgs']] = None,
               github_registry: Optional[pulumi.InputType['GetSecretGithubRegistryArgs']] = None,
               gitlab_registry: Optional[pulumi.InputType['GetSecretGitlabRegistryArgs']] = None,
               name: Optional[str] = None,
               private_registry: Optional[pulumi.InputType['GetSecretPrivateRegistryArgs']] = None,
               type: Optional[str] = None,
               value: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecretResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_koyeb as koyeb

    my_secret = koyeb.get_secret(name="my-secret")
    ```


    :param pulumi.InputType['GetSecretAzureContainerRegistryArgs'] azure_container_registry: The Azure registry configuration to use
    :param pulumi.InputType['GetSecretDigitalOceanContainerRegistryArgs'] digital_ocean_container_registry: The DigitalOcean registry configuration to use
    :param pulumi.InputType['GetSecretDockerHubRegistryArgs'] docker_hub_registry: The DockerHub registry configuration to use
    :param pulumi.InputType['GetSecretGithubRegistryArgs'] github_registry: The GitHub registry configuration to use
    :param pulumi.InputType['GetSecretGitlabRegistryArgs'] gitlab_registry: The GitLab registry configuration to use
    :param str name: The secret name
    :param pulumi.InputType['GetSecretPrivateRegistryArgs'] private_registry: The DigitalOcean registry configuration to use
    :param str type: The secret type
    :param str value: The secret value
    """
    __args__ = dict()
    __args__['azureContainerRegistry'] = azure_container_registry
    __args__['digitalOceanContainerRegistry'] = digital_ocean_container_registry
    __args__['dockerHubRegistry'] = docker_hub_registry
    __args__['githubRegistry'] = github_registry
    __args__['gitlabRegistry'] = gitlab_registry
    __args__['name'] = name
    __args__['privateRegistry'] = private_registry
    __args__['type'] = type
    __args__['value'] = value
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('koyeb:index/getSecret:getSecret', __args__, opts=opts, typ=GetSecretResult).value

    return AwaitableGetSecretResult(
        azure_container_registry=__ret__.azure_container_registry,
        created_at=__ret__.created_at,
        digital_ocean_container_registry=__ret__.digital_ocean_container_registry,
        docker_hub_registry=__ret__.docker_hub_registry,
        github_registry=__ret__.github_registry,
        gitlab_registry=__ret__.gitlab_registry,
        id=__ret__.id,
        name=__ret__.name,
        organization_id=__ret__.organization_id,
        private_registry=__ret__.private_registry,
        type=__ret__.type,
        updated_at=__ret__.updated_at,
        value=__ret__.value)


@_utilities.lift_output_func(get_secret)
def get_secret_output(azure_container_registry: Optional[pulumi.Input[Optional[pulumi.InputType['GetSecretAzureContainerRegistryArgs']]]] = None,
                      digital_ocean_container_registry: Optional[pulumi.Input[Optional[pulumi.InputType['GetSecretDigitalOceanContainerRegistryArgs']]]] = None,
                      docker_hub_registry: Optional[pulumi.Input[Optional[pulumi.InputType['GetSecretDockerHubRegistryArgs']]]] = None,
                      github_registry: Optional[pulumi.Input[Optional[pulumi.InputType['GetSecretGithubRegistryArgs']]]] = None,
                      gitlab_registry: Optional[pulumi.Input[Optional[pulumi.InputType['GetSecretGitlabRegistryArgs']]]] = None,
                      name: Optional[pulumi.Input[str]] = None,
                      private_registry: Optional[pulumi.Input[Optional[pulumi.InputType['GetSecretPrivateRegistryArgs']]]] = None,
                      type: Optional[pulumi.Input[Optional[str]]] = None,
                      value: Optional[pulumi.Input[Optional[str]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSecretResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_koyeb as koyeb

    my_secret = koyeb.get_secret(name="my-secret")
    ```


    :param pulumi.InputType['GetSecretAzureContainerRegistryArgs'] azure_container_registry: The Azure registry configuration to use
    :param pulumi.InputType['GetSecretDigitalOceanContainerRegistryArgs'] digital_ocean_container_registry: The DigitalOcean registry configuration to use
    :param pulumi.InputType['GetSecretDockerHubRegistryArgs'] docker_hub_registry: The DockerHub registry configuration to use
    :param pulumi.InputType['GetSecretGithubRegistryArgs'] github_registry: The GitHub registry configuration to use
    :param pulumi.InputType['GetSecretGitlabRegistryArgs'] gitlab_registry: The GitLab registry configuration to use
    :param str name: The secret name
    :param pulumi.InputType['GetSecretPrivateRegistryArgs'] private_registry: The DigitalOcean registry configuration to use
    :param str type: The secret type
    :param str value: The secret value
    """
    ...

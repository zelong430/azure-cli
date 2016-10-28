#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#---------------------------------------------------------------------------------------------
#pylint: skip-file
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.16.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from .operations.operation import Operation
from .operations.registries import Registries
from .operations.subscriptions import Subscriptions
from . import models


class ContainerRegistryConfiguration(Configuration):
    """Configuration for ContainerRegistry
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param subscription_id: Gets subscription credentials which uniquely
     identify Microsoft Azure subscription.The subscription ID forms part of
     the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: :mod:`A msrest Authentication
     object<msrest.authentication>`
    :param str base_url: Service URL
    :param str filepath: Existing config
    """

    def __init__(
            self, subscription_id, api_version, credentials, base_url=None, filepath=None):

        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not isinstance(subscription_id, str):
            raise TypeError("Parameter 'subscription_id' must be str.")
        if api_version is None:
            raise ValueError("Parameter 'api_version' must not be None.")
        if not isinstance(api_version, str):
            raise TypeError("Parameter 'api_version' must be str.")
        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(ContainerRegistryConfiguration, self).__init__(base_url, filepath)

        self.add_user_agent('containerregistry/{}'.format(VERSION))

        self.subscription_id = subscription_id
        self.api_version = api_version
        self.credentials = credentials


class ContainerRegistry(object):
    """ContainerRegistry

    :param config: Configuration for client.
    :type config: ContainerRegistryConfiguration

    :ivar operation: Operation operations
    :vartype operation: .operations.Operation
    :ivar registries: Registries operations
    :vartype registries: .operations.Registries
    :ivar subscriptions: Subscriptions operations
    :vartype subscriptions: .operations.Subscriptions
    """

    def __init__(self, config):

        self._client = ServiceClient(config.credentials, config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer()
        self._deserialize = Deserializer(client_models)

        self.config = config
        self.operation = Operation(
            self._client, self.config, self._serialize, self._deserialize)
        self.registries = Registries(
            self._client, self.config, self._serialize, self._deserialize)
        self.subscriptions = Subscriptions(
            self._client, self.config, self._serialize, self._deserialize)
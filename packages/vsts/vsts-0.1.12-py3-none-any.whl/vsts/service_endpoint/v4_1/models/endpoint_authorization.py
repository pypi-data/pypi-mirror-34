# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class EndpointAuthorization(Model):
    """EndpointAuthorization.

    :param parameters: Gets or sets the parameters for the selected authorization scheme.
    :type parameters: dict
    :param scheme: Gets or sets the scheme used for service endpoint authentication.
    :type scheme: str
    """

    _attribute_map = {
        'parameters': {'key': 'parameters', 'type': '{str}'},
        'scheme': {'key': 'scheme', 'type': 'str'}
    }

    def __init__(self, parameters=None, scheme=None):
        super(EndpointAuthorization, self).__init__()
        self.parameters = parameters
        self.scheme = scheme

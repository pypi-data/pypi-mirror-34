# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AgentPoolQueue(Model):
    """AgentPoolQueue.

    :param _links:
    :type _links: :class:`ReferenceLinks <build.v4_1.models.ReferenceLinks>`
    :param id: The ID of the queue.
    :type id: int
    :param name: The name of the queue.
    :type name: str
    :param pool: The pool used by this queue.
    :type pool: :class:`TaskAgentPoolReference <build.v4_1.models.TaskAgentPoolReference>`
    :param url: The full http link to the resource.
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'pool': {'key': 'pool', 'type': 'TaskAgentPoolReference'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, id=None, name=None, pool=None, url=None):
        super(AgentPoolQueue, self).__init__()
        self._links = _links
        self.id = id
        self.name = name
        self.pool = pool
        self.url = url

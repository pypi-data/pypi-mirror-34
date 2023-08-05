# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class WorkItemDeleteReference(Model):
    """WorkItemDeleteReference.

    :param code: The HTTP status code for work item operation in a batch request.
    :type code: int
    :param deleted_by: The user who deleted the work item type.
    :type deleted_by: str
    :param deleted_date: The work item deletion date.
    :type deleted_date: str
    :param id: Work item ID.
    :type id: int
    :param message: The exception message for work item operation in a batch request.
    :type message: str
    :param name: Name or title of the work item.
    :type name: str
    :param project: Parent project of the deleted work item.
    :type project: str
    :param type: Type of work item.
    :type type: str
    :param url: REST API URL of the resource
    :type url: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'int'},
        'deleted_by': {'key': 'deletedBy', 'type': 'str'},
        'deleted_date': {'key': 'deletedDate', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'project': {'key': 'project', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, code=None, deleted_by=None, deleted_date=None, id=None, message=None, name=None, project=None, type=None, url=None):
        super(WorkItemDeleteReference, self).__init__()
        self.code = code
        self.deleted_by = deleted_by
        self.deleted_date = deleted_date
        self.id = id
        self.message = message
        self.name = name
        self.project = project
        self.type = type
        self.url = url

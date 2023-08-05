# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from .tfvc_branch_ref import TfvcBranchRef


class TfvcBranch(TfvcBranchRef):
    """TfvcBranch.

    :param path:
    :type path: str
    :param _links:
    :type _links: :class:`ReferenceLinks <tfvc.v4_0.models.ReferenceLinks>`
    :param created_date:
    :type created_date: datetime
    :param description:
    :type description: str
    :param is_deleted:
    :type is_deleted: bool
    :param owner:
    :type owner: :class:`IdentityRef <tfvc.v4_0.models.IdentityRef>`
    :param url:
    :type url: str
    :param children:
    :type children: list of :class:`TfvcBranch <tfvc.v4_0.models.TfvcBranch>`
    :param mappings:
    :type mappings: list of :class:`TfvcBranchMapping <tfvc.v4_0.models.TfvcBranchMapping>`
    :param parent:
    :type parent: :class:`TfvcShallowBranchRef <tfvc.v4_0.models.TfvcShallowBranchRef>`
    :param related_branches:
    :type related_branches: list of :class:`TfvcShallowBranchRef <tfvc.v4_0.models.TfvcShallowBranchRef>`
    """

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'url': {'key': 'url', 'type': 'str'},
        'children': {'key': 'children', 'type': '[TfvcBranch]'},
        'mappings': {'key': 'mappings', 'type': '[TfvcBranchMapping]'},
        'parent': {'key': 'parent', 'type': 'TfvcShallowBranchRef'},
        'related_branches': {'key': 'relatedBranches', 'type': '[TfvcShallowBranchRef]'}
    }

    def __init__(self, path=None, _links=None, created_date=None, description=None, is_deleted=None, owner=None, url=None, children=None, mappings=None, parent=None, related_branches=None):
        super(TfvcBranch, self).__init__(path=path, _links=_links, created_date=created_date, description=description, is_deleted=is_deleted, owner=owner, url=url)
        self.children = children
        self.mappings = mappings
        self.parent = parent
        self.related_branches = related_branches

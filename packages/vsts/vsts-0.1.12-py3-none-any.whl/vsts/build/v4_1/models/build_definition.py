# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from .build_definition_reference import BuildDefinitionReference


class BuildDefinition(BuildDefinitionReference):
    """BuildDefinition.

    :param created_date: The date the definition was created.
    :type created_date: datetime
    :param id: The ID of the referenced definition.
    :type id: int
    :param name: The name of the referenced definition.
    :type name: str
    :param path: The folder path of the definition.
    :type path: str
    :param project: A reference to the project.
    :type project: :class:`TeamProjectReference <build.v4_1.models.TeamProjectReference>`
    :param queue_status: A value that indicates whether builds can be queued against this definition.
    :type queue_status: object
    :param revision: The definition revision number.
    :type revision: int
    :param type: The type of the definition.
    :type type: object
    :param uri: The definition's URI.
    :type uri: str
    :param url: The REST URL of the definition.
    :type url: str
    :param _links:
    :type _links: :class:`ReferenceLinks <build.v4_1.models.ReferenceLinks>`
    :param authored_by: The author of the definition.
    :type authored_by: :class:`IdentityRef <build.v4_1.models.IdentityRef>`
    :param draft_of: A reference to the definition that this definition is a draft of, if this is a draft definition.
    :type draft_of: :class:`DefinitionReference <build.v4_1.models.DefinitionReference>`
    :param drafts: The list of drafts associated with this definition, if this is not a draft definition.
    :type drafts: list of :class:`DefinitionReference <build.v4_1.models.DefinitionReference>`
    :param latest_build:
    :type latest_build: :class:`Build <build.v4_1.models.Build>`
    :param latest_completed_build:
    :type latest_completed_build: :class:`Build <build.v4_1.models.Build>`
    :param metrics:
    :type metrics: list of :class:`BuildMetric <build.v4_1.models.BuildMetric>`
    :param quality: The quality of the definition document (draft, etc.)
    :type quality: object
    :param queue: The default queue for builds run against this definition.
    :type queue: :class:`AgentPoolQueue <build.v4_1.models.AgentPoolQueue>`
    :param badge_enabled: Indicates whether badges are enabled for this definition.
    :type badge_enabled: bool
    :param build_number_format: The build number format.
    :type build_number_format: str
    :param comment: A save-time comment for the definition.
    :type comment: str
    :param counters:
    :type counters: dict
    :param demands:
    :type demands: list of :class:`object <build.v4_1.models.object>`
    :param description: The description.
    :type description: str
    :param drop_location: The drop location for the definition.
    :type drop_location: str
    :param job_authorization_scope: The job authorization scope for builds queued against this definition.
    :type job_authorization_scope: object
    :param job_cancel_timeout_in_minutes: The job cancel timeout (in minutes) for builds cancelled by user for this definition.
    :type job_cancel_timeout_in_minutes: int
    :param job_timeout_in_minutes: The job execution timeout (in minutes) for builds queued against this definition.
    :type job_timeout_in_minutes: int
    :param options:
    :type options: list of :class:`BuildOption <build.v4_1.models.BuildOption>`
    :param process: The build process.
    :type process: :class:`object <build.v4_1.models.object>`
    :param process_parameters: The process parameters for this definition.
    :type process_parameters: :class:`ProcessParameters <build.v4_1.models.ProcessParameters>`
    :param properties:
    :type properties: :class:`object <build.v4_1.models.object>`
    :param repository: The repository.
    :type repository: :class:`BuildRepository <build.v4_1.models.BuildRepository>`
    :param retention_rules:
    :type retention_rules: list of :class:`RetentionPolicy <build.v4_1.models.RetentionPolicy>`
    :param tags:
    :type tags: list of str
    :param triggers:
    :type triggers: list of :class:`object <build.v4_1.models.object>`
    :param variable_groups:
    :type variable_groups: list of :class:`VariableGroup <build.v4_1.models.VariableGroup>`
    :param variables:
    :type variables: dict
    """

    _attribute_map = {
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'queue_status': {'key': 'queueStatus', 'type': 'object'},
        'revision': {'key': 'revision', 'type': 'int'},
        'type': {'key': 'type', 'type': 'object'},
        'uri': {'key': 'uri', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'authored_by': {'key': 'authoredBy', 'type': 'IdentityRef'},
        'draft_of': {'key': 'draftOf', 'type': 'DefinitionReference'},
        'drafts': {'key': 'drafts', 'type': '[DefinitionReference]'},
        'latest_build': {'key': 'latestBuild', 'type': 'Build'},
        'latest_completed_build': {'key': 'latestCompletedBuild', 'type': 'Build'},
        'metrics': {'key': 'metrics', 'type': '[BuildMetric]'},
        'quality': {'key': 'quality', 'type': 'object'},
        'queue': {'key': 'queue', 'type': 'AgentPoolQueue'},
        'badge_enabled': {'key': 'badgeEnabled', 'type': 'bool'},
        'build_number_format': {'key': 'buildNumberFormat', 'type': 'str'},
        'comment': {'key': 'comment', 'type': 'str'},
        'counters': {'key': 'counters', 'type': '{BuildDefinitionCounter}'},
        'demands': {'key': 'demands', 'type': '[object]'},
        'description': {'key': 'description', 'type': 'str'},
        'drop_location': {'key': 'dropLocation', 'type': 'str'},
        'job_authorization_scope': {'key': 'jobAuthorizationScope', 'type': 'object'},
        'job_cancel_timeout_in_minutes': {'key': 'jobCancelTimeoutInMinutes', 'type': 'int'},
        'job_timeout_in_minutes': {'key': 'jobTimeoutInMinutes', 'type': 'int'},
        'options': {'key': 'options', 'type': '[BuildOption]'},
        'process': {'key': 'process', 'type': 'object'},
        'process_parameters': {'key': 'processParameters', 'type': 'ProcessParameters'},
        'properties': {'key': 'properties', 'type': 'object'},
        'repository': {'key': 'repository', 'type': 'BuildRepository'},
        'retention_rules': {'key': 'retentionRules', 'type': '[RetentionPolicy]'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'triggers': {'key': 'triggers', 'type': '[object]'},
        'variable_groups': {'key': 'variableGroups', 'type': '[VariableGroup]'},
        'variables': {'key': 'variables', 'type': '{BuildDefinitionVariable}'}
    }

    def __init__(self, created_date=None, id=None, name=None, path=None, project=None, queue_status=None, revision=None, type=None, uri=None, url=None, _links=None, authored_by=None, draft_of=None, drafts=None, latest_build=None, latest_completed_build=None, metrics=None, quality=None, queue=None, badge_enabled=None, build_number_format=None, comment=None, counters=None, demands=None, description=None, drop_location=None, job_authorization_scope=None, job_cancel_timeout_in_minutes=None, job_timeout_in_minutes=None, options=None, process=None, process_parameters=None, properties=None, repository=None, retention_rules=None, tags=None, triggers=None, variable_groups=None, variables=None):
        super(BuildDefinition, self).__init__(created_date=created_date, id=id, name=name, path=path, project=project, queue_status=queue_status, revision=revision, type=type, uri=uri, url=url, _links=_links, authored_by=authored_by, draft_of=draft_of, drafts=drafts, latest_build=latest_build, latest_completed_build=latest_completed_build, metrics=metrics, quality=quality, queue=queue)
        self.badge_enabled = badge_enabled
        self.build_number_format = build_number_format
        self.comment = comment
        self.counters = counters
        self.demands = demands
        self.description = description
        self.drop_location = drop_location
        self.job_authorization_scope = job_authorization_scope
        self.job_cancel_timeout_in_minutes = job_cancel_timeout_in_minutes
        self.job_timeout_in_minutes = job_timeout_in_minutes
        self.options = options
        self.process = process
        self.process_parameters = process_parameters
        self.properties = properties
        self.repository = repository
        self.retention_rules = retention_rules
        self.tags = tags
        self.triggers = triggers
        self.variable_groups = variable_groups
        self.variables = variables

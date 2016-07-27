# coding: utf-8

"""


    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from ...base_model import BaseModel
from pprint import pformat
from six import iteritems
import re


class GroupMembership(BaseModel):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, group_id=None, user_id=None, workflow_state=None, moderator=None, just_created=None, sis_import_id=None):
        """
        GroupMembership - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'group_id': 'int',
            'user_id': 'int',
            'workflow_state': 'str',
            'moderator': 'bool',
            'just_created': 'bool',
            'sis_import_id': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'group_id': 'group_id',
            'user_id': 'user_id',
            'workflow_state': 'workflow_state',
            'moderator': 'moderator',
            'just_created': 'just_created',
            'sis_import_id': 'sis_import_id'
        }

        self._id = id
        self._group_id = group_id
        self._user_id = user_id
        self._workflow_state = workflow_state
        self._moderator = moderator
        self._just_created = just_created
        self._sis_import_id = sis_import_id

    @property
    def id(self):
        """
        Gets the id of this GroupMembership.
        The id of the membership object

        :return: The id of this GroupMembership.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this GroupMembership.
        The id of the membership object

        :param id: The id of this GroupMembership.
        :type: int
        """

        self._id = id

    @property
    def group_id(self):
        """
        Gets the group_id of this GroupMembership.
        The id of the group object to which the membership belongs

        :return: The group_id of this GroupMembership.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this GroupMembership.
        The id of the group object to which the membership belongs

        :param group_id: The group_id of this GroupMembership.
        :type: int
        """

        self._group_id = group_id

    @property
    def user_id(self):
        """
        Gets the user_id of this GroupMembership.
        The id of the user object to which the membership belongs

        :return: The user_id of this GroupMembership.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this GroupMembership.
        The id of the user object to which the membership belongs

        :param user_id: The user_id of this GroupMembership.
        :type: int
        """

        self._user_id = user_id

    @property
    def workflow_state(self):
        """
        Gets the workflow_state of this GroupMembership.
        The current state of the membership. Current possible values are 'accepted', 'invited', and 'requested'

        :return: The workflow_state of this GroupMembership.
        :rtype: str
        """
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, workflow_state):
        """
        Sets the workflow_state of this GroupMembership.
        The current state of the membership. Current possible values are 'accepted', 'invited', and 'requested'

        :param workflow_state: The workflow_state of this GroupMembership.
        :type: str
        """

        self._workflow_state = workflow_state

    @property
    def moderator(self):
        """
        Gets the moderator of this GroupMembership.
        Whether or not the user is a moderator of the group (the must also be an active member of the group to moderate)

        :return: The moderator of this GroupMembership.
        :rtype: bool
        """
        return self._moderator

    @moderator.setter
    def moderator(self, moderator):
        """
        Sets the moderator of this GroupMembership.
        Whether or not the user is a moderator of the group (the must also be an active member of the group to moderate)

        :param moderator: The moderator of this GroupMembership.
        :type: bool
        """

        self._moderator = moderator

    @property
    def just_created(self):
        """
        Gets the just_created of this GroupMembership.
        optional: whether or not the record was just created on a create call (POST), i.e. was the user just added to the group, or was the user already a member

        :return: The just_created of this GroupMembership.
        :rtype: bool
        """
        return self._just_created

    @just_created.setter
    def just_created(self, just_created):
        """
        Sets the just_created of this GroupMembership.
        optional: whether or not the record was just created on a create call (POST), i.e. was the user just added to the group, or was the user already a member

        :param just_created: The just_created of this GroupMembership.
        :type: bool
        """

        self._just_created = just_created

    @property
    def sis_import_id(self):
        """
        Gets the sis_import_id of this GroupMembership.
        The id of the SIS import if created through SIS. Only included if the user has permission to manage SIS information.

        :return: The sis_import_id of this GroupMembership.
        :rtype: int
        """
        return self._sis_import_id

    @sis_import_id.setter
    def sis_import_id(self, sis_import_id):
        """
        Sets the sis_import_id of this GroupMembership.
        The id of the SIS import if created through SIS. Only included if the user has permission to manage SIS information.

        :param sis_import_id: The sis_import_id of this GroupMembership.
        :type: int
        """

        self._sis_import_id = sis_import_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
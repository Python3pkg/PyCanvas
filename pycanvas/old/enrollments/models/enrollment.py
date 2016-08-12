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


class Enrollment(BaseModel):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, course_id=None, sis_course_id=None, course_integration_id=None, course_section_id=None, section_integration_id=None, sis_section_id=None, enrollment_state=None, limit_privileges_to_course_section=None, sis_import_id=None, root_account_id=None, type=None, user_id=None, associated_user_id=None, role=None, updated_at=None, start_at=None, end_at=None, last_activity_at=None, total_activity_time=None, html_url=None, grades=None, user=None):
        """
        Enrollment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'course_id': 'int',
            'sis_course_id': 'str',
            'course_integration_id': 'str',
            'course_section_id': 'int',
            'section_integration_id': 'str',
            'sis_section_id': 'str',
            'enrollment_state': 'str',
            'limit_privileges_to_course_section': 'bool',
            'sis_import_id': 'int',
            'root_account_id': 'int',
            'type': 'str',
            'user_id': 'int',
            'associated_user_id': 'int',
            'role': 'str',
            'updated_at': 'datetime',
            'start_at': 'datetime',
            'end_at': 'datetime',
            'last_activity_at': 'datetime',
            'total_activity_time': 'int',
            'html_url': 'str',
            'grades': 'Grade',
            'user': 'User'
        }

        self.attribute_map = {
            'id': 'id',
            'course_id': 'course_id',
            'sis_course_id': 'sis_course_id',
            'course_integration_id': 'course_integration_id',
            'course_section_id': 'course_section_id',
            'section_integration_id': 'section_integration_id',
            'sis_section_id': 'sis_section_id',
            'enrollment_state': 'enrollment_state',
            'limit_privileges_to_course_section': 'limit_privileges_to_course_section',
            'sis_import_id': 'sis_import_id',
            'root_account_id': 'root_account_id',
            'type': 'type',
            'user_id': 'user_id',
            'associated_user_id': 'associated_user_id',
            'role': 'role',
            'updated_at': 'updated_at',
            'start_at': 'start_at',
            'end_at': 'end_at',
            'last_activity_at': 'last_activity_at',
            'total_activity_time': 'total_activity_time',
            'html_url': 'html_url',
            'grades': 'grades',
            'user': 'user'
        }

        self._id = id
        self._course_id = course_id
        self._sis_course_id = sis_course_id
        self._course_integration_id = course_integration_id
        self._course_section_id = course_section_id
        self._section_integration_id = section_integration_id
        self._sis_section_id = sis_section_id
        self._enrollment_state = enrollment_state
        self._limit_privileges_to_course_section = limit_privileges_to_course_section
        self._sis_import_id = sis_import_id
        self._root_account_id = root_account_id
        self._type = type
        self._user_id = user_id
        self._associated_user_id = associated_user_id
        self._role = role
        self._updated_at = updated_at
        self._start_at = start_at
        self._end_at = end_at
        self._last_activity_at = last_activity_at
        self._total_activity_time = total_activity_time
        self._html_url = html_url
        self._grades = grades
        self._user = user

    @property
    def id(self):
        """
        Gets the id of this Enrollment.
        The ID of the enrollment.

        :return: The id of this Enrollment.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Enrollment.
        The ID of the enrollment.

        :param id: The id of this Enrollment.
        :type: int
        """

        self._id = id

    @property
    def course_id(self):
        """
        Gets the course_id of this Enrollment.
        The unique id of the course.

        :return: The course_id of this Enrollment.
        :rtype: int
        """
        return self._course_id

    @course_id.setter
    def course_id(self, course_id):
        """
        Sets the course_id of this Enrollment.
        The unique id of the course.

        :param course_id: The course_id of this Enrollment.
        :type: int
        """

        self._course_id = course_id

    @property
    def sis_course_id(self):
        """
        Gets the sis_course_id of this Enrollment.
        The SIS Course ID in which the enrollment is associated. Only displayed if present. This field is only included if the user has permission to view SIS information.

        :return: The sis_course_id of this Enrollment.
        :rtype: str
        """
        return self._sis_course_id

    @sis_course_id.setter
    def sis_course_id(self, sis_course_id):
        """
        Sets the sis_course_id of this Enrollment.
        The SIS Course ID in which the enrollment is associated. Only displayed if present. This field is only included if the user has permission to view SIS information.

        :param sis_course_id: The sis_course_id of this Enrollment.
        :type: str
        """

        self._sis_course_id = sis_course_id

    @property
    def course_integration_id(self):
        """
        Gets the course_integration_id of this Enrollment.
        The Course Integration ID in which the enrollment is associated. This field is only included if the user has permission to view SIS information.

        :return: The course_integration_id of this Enrollment.
        :rtype: str
        """
        return self._course_integration_id

    @course_integration_id.setter
    def course_integration_id(self, course_integration_id):
        """
        Sets the course_integration_id of this Enrollment.
        The Course Integration ID in which the enrollment is associated. This field is only included if the user has permission to view SIS information.

        :param course_integration_id: The course_integration_id of this Enrollment.
        :type: str
        """

        self._course_integration_id = course_integration_id

    @property
    def course_section_id(self):
        """
        Gets the course_section_id of this Enrollment.
        The unique id of the user's section.

        :return: The course_section_id of this Enrollment.
        :rtype: int
        """
        return self._course_section_id

    @course_section_id.setter
    def course_section_id(self, course_section_id):
        """
        Sets the course_section_id of this Enrollment.
        The unique id of the user's section.

        :param course_section_id: The course_section_id of this Enrollment.
        :type: int
        """

        self._course_section_id = course_section_id

    @property
    def section_integration_id(self):
        """
        Gets the section_integration_id of this Enrollment.
        The Section Integration ID in which the enrollment is associated. This field is only included if the user has permission to view SIS information.

        :return: The section_integration_id of this Enrollment.
        :rtype: str
        """
        return self._section_integration_id

    @section_integration_id.setter
    def section_integration_id(self, section_integration_id):
        """
        Sets the section_integration_id of this Enrollment.
        The Section Integration ID in which the enrollment is associated. This field is only included if the user has permission to view SIS information.

        :param section_integration_id: The section_integration_id of this Enrollment.
        :type: str
        """

        self._section_integration_id = section_integration_id

    @property
    def sis_section_id(self):
        """
        Gets the sis_section_id of this Enrollment.
        The SIS Section ID in which the enrollment is associated. Only displayed if present. This field is only included if the user has permission to view SIS information.

        :return: The sis_section_id of this Enrollment.
        :rtype: str
        """
        return self._sis_section_id

    @sis_section_id.setter
    def sis_section_id(self, sis_section_id):
        """
        Sets the sis_section_id of this Enrollment.
        The SIS Section ID in which the enrollment is associated. Only displayed if present. This field is only included if the user has permission to view SIS information.

        :param sis_section_id: The sis_section_id of this Enrollment.
        :type: str
        """

        self._sis_section_id = sis_section_id

    @property
    def enrollment_state(self):
        """
        Gets the enrollment_state of this Enrollment.
        The state of the user's enrollment in the course.

        :return: The enrollment_state of this Enrollment.
        :rtype: str
        """
        return self._enrollment_state

    @enrollment_state.setter
    def enrollment_state(self, enrollment_state):
        """
        Sets the enrollment_state of this Enrollment.
        The state of the user's enrollment in the course.

        :param enrollment_state: The enrollment_state of this Enrollment.
        :type: str
        """

        self._enrollment_state = enrollment_state

    @property
    def limit_privileges_to_course_section(self):
        """
        Gets the limit_privileges_to_course_section of this Enrollment.
        User can only access his or her own course section.

        :return: The limit_privileges_to_course_section of this Enrollment.
        :rtype: bool
        """
        return self._limit_privileges_to_course_section

    @limit_privileges_to_course_section.setter
    def limit_privileges_to_course_section(self, limit_privileges_to_course_section):
        """
        Sets the limit_privileges_to_course_section of this Enrollment.
        User can only access his or her own course section.

        :param limit_privileges_to_course_section: The limit_privileges_to_course_section of this Enrollment.
        :type: bool
        """

        self._limit_privileges_to_course_section = limit_privileges_to_course_section

    @property
    def sis_import_id(self):
        """
        Gets the sis_import_id of this Enrollment.
        The unique identifier for the SIS import. This field is only included if the user has permission to manage SIS information.

        :return: The sis_import_id of this Enrollment.
        :rtype: int
        """
        return self._sis_import_id

    @sis_import_id.setter
    def sis_import_id(self, sis_import_id):
        """
        Sets the sis_import_id of this Enrollment.
        The unique identifier for the SIS import. This field is only included if the user has permission to manage SIS information.

        :param sis_import_id: The sis_import_id of this Enrollment.
        :type: int
        """

        self._sis_import_id = sis_import_id

    @property
    def root_account_id(self):
        """
        Gets the root_account_id of this Enrollment.
        The unique id of the user's account.

        :return: The root_account_id of this Enrollment.
        :rtype: int
        """
        return self._root_account_id

    @root_account_id.setter
    def root_account_id(self, root_account_id):
        """
        Sets the root_account_id of this Enrollment.
        The unique id of the user's account.

        :param root_account_id: The root_account_id of this Enrollment.
        :type: int
        """

        self._root_account_id = root_account_id

    @property
    def type(self):
        """
        Gets the type of this Enrollment.
        The enrollment type. One of 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'DesignerEnrollment', 'ObserverEnrollment'.

        :return: The type of this Enrollment.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Enrollment.
        The enrollment type. One of 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'DesignerEnrollment', 'ObserverEnrollment'.

        :param type: The type of this Enrollment.
        :type: str
        """

        self._type = type

    @property
    def user_id(self):
        """
        Gets the user_id of this Enrollment.
        The unique id of the user.

        :return: The user_id of this Enrollment.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this Enrollment.
        The unique id of the user.

        :param user_id: The user_id of this Enrollment.
        :type: int
        """

        self._user_id = user_id

    @property
    def associated_user_id(self):
        """
        Gets the associated_user_id of this Enrollment.
        The unique id of the associated user. Will be null unless type is ObserverEnrollment.

        :return: The associated_user_id of this Enrollment.
        :rtype: int
        """
        return self._associated_user_id

    @associated_user_id.setter
    def associated_user_id(self, associated_user_id):
        """
        Sets the associated_user_id of this Enrollment.
        The unique id of the associated user. Will be null unless type is ObserverEnrollment.

        :param associated_user_id: The associated_user_id of this Enrollment.
        :type: int
        """

        self._associated_user_id = associated_user_id

    @property
    def role(self):
        """
        Gets the role of this Enrollment.
        The enrollment role, for course-level permissions. This field will match `type` if the enrollment role has not been customized.

        :return: The role of this Enrollment.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this Enrollment.
        The enrollment role, for course-level permissions. This field will match `type` if the enrollment role has not been customized.

        :param role: The role of this Enrollment.
        :type: str
        """

        self._role = role

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Enrollment.
        The updated time of the enrollment, in ISO8601 format.

        :return: The updated_at of this Enrollment.
        :rtype: Datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this Enrollment.
        The updated time of the enrollment, in ISO8601 format.

        :param updated_at: The updated_at of this Enrollment.
        :type: Datetime
        """

        self._updated_at = updated_at

    @property
    def start_at(self):
        """
        Gets the start_at of this Enrollment.
        The start time of the enrollment, in ISO8601 format.

        :return: The start_at of this Enrollment.
        :rtype: Datetime
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        """
        Sets the start_at of this Enrollment.
        The start time of the enrollment, in ISO8601 format.

        :param start_at: The start_at of this Enrollment.
        :type: Datetime
        """

        self._start_at = start_at

    @property
    def end_at(self):
        """
        Gets the end_at of this Enrollment.
        The end time of the enrollment, in ISO8601 format.

        :return: The end_at of this Enrollment.
        :rtype: Datetime
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        """
        Sets the end_at of this Enrollment.
        The end time of the enrollment, in ISO8601 format.

        :param end_at: The end_at of this Enrollment.
        :type: Datetime
        """

        self._end_at = end_at

    @property
    def last_activity_at(self):
        """
        Gets the last_activity_at of this Enrollment.
        The last activity time of the user for the enrollment, in ISO8601 format.

        :return: The last_activity_at of this Enrollment.
        :rtype: Datetime
        """
        return self._last_activity_at

    @last_activity_at.setter
    def last_activity_at(self, last_activity_at):
        """
        Sets the last_activity_at of this Enrollment.
        The last activity time of the user for the enrollment, in ISO8601 format.

        :param last_activity_at: The last_activity_at of this Enrollment.
        :type: Datetime
        """

        self._last_activity_at = last_activity_at

    @property
    def total_activity_time(self):
        """
        Gets the total_activity_time of this Enrollment.
        The total activity time of the user for the enrollment, in seconds.

        :return: The total_activity_time of this Enrollment.
        :rtype: int
        """
        return self._total_activity_time

    @total_activity_time.setter
    def total_activity_time(self, total_activity_time):
        """
        Sets the total_activity_time of this Enrollment.
        The total activity time of the user for the enrollment, in seconds.

        :param total_activity_time: The total_activity_time of this Enrollment.
        :type: int
        """

        self._total_activity_time = total_activity_time

    @property
    def html_url(self):
        """
        Gets the html_url of this Enrollment.
        The URL to the Canvas web UI page for this course enrollment.

        :return: The html_url of this Enrollment.
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """
        Sets the html_url of this Enrollment.
        The URL to the Canvas web UI page for this course enrollment.

        :param html_url: The html_url of this Enrollment.
        :type: str
        """

        self._html_url = html_url

    @property
    def grades(self):
        """
        Gets the grades of this Enrollment.
        The URL to the Canvas web UI page the grades associated with this enrollment.

        :return: The grades of this Enrollment.
        :rtype: Grade
        """
        return self._grades

    @grades.setter
    def grades(self, grades):
        """
        Sets the grades of this Enrollment.
        The URL to the Canvas web UI page the grades associated with this enrollment.

        :param grades: The grades of this Enrollment.
        :type: Grade
        """

        self._grades = grades

    @property
    def user(self):
        """
        Gets the user of this Enrollment.
        A description of the user.

        :return: The user of this Enrollment.
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this Enrollment.
        A description of the user.

        :param user: The user of this Enrollment.
        :type: User
        """

        self._user = user

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
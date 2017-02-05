"""Favorites API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from base import BaseCanvasAPI
from base import BaseModel


class FavoritesAPI(BaseCanvasAPI):
    """Favorites API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for FavoritesAPI."""
        super(FavoritesAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.FavoritesAPI")

    def list_favorite_courses(self):
        """
        List favorite courses.

        Retrieve the list of favorite courses for the current user. If the user has not chosen
        any favorites, then a selection of currently enrolled courses will be returned.
        
        See the {api:CoursesController#index List courses API} for details on accepted include[] parameters.
        """
        path = {}
        payload = {}

        self.logger.debug("GET /api/v1/users/self/favorites/courses with payload: {payload}".format(payload=payload, **path))
        return self.generic_request("GET", "/api/v1/users/self/favorites/courses".format(**path), params=payload, all_pages=True)

    def add_course_to_favorites(self, id):
        """
        Add course to favorites.

        Add a course to the current user's favorites.  If the course is already
        in the user's favorites, nothing happens.
        """
        path = {}
        payload = {}

        # REQUIRED - PATH - id - The ID or SIS ID of the course to add. The current user must be registered in the course.
        path["id"] = id

        self.logger.debug("POST /api/v1/users/self/favorites/courses/{id} with payload: {payload}".format(payload=payload, **path))
        return self.generic_request("POST", "/api/v1/users/self/favorites/courses/{id}".format(**path), data=payload, single_item=True)

    def remove_course_from_favorites(self, id):
        """
        Remove course from favorites.

        Remove a course from the current user's favorites.
        """
        path = {}
        payload = {}

        # REQUIRED - PATH - id - the ID or SIS ID of the course to remove
        path["id"] = id

        self.logger.debug("DELETE /api/v1/users/self/favorites/courses/{id} with payload: {payload}".format(payload=payload, **path))
        return self.generic_request("DELETE", "/api/v1/users/self/favorites/courses/{id}".format(**path), params=payload, single_item=True)

    def reset_course_favorites(self):
        """
        Reset course favorites.

        Reset the current user's course favorites to the default
        automatically generated list of enrolled courses
        """
        path = {}
        payload = {}

        self.logger.debug("DELETE /api/v1/users/self/favorites/courses with payload: {payload}".format(payload=payload, **path))
        return self.generic_request("DELETE", "/api/v1/users/self/favorites/courses".format(**path), params=payload, no_data=True)


class Favorite(BaseModel):
    """Favorite Model."""

    def __init__(self, , context_type=None, context_id=None):
        """Init method for Favorite class."""
        self._context_type = context_type
        self._context_id = context_id

        self.logger = logging.getLogger('pycanvas.Favorite')

    @property
    def context_type(self):
        """The type of the object the Favorite refers to (currently, only 'Course' is supported)."""
        return self._context_type

    @context_type.setter
    def context_type(self, value):
        """Setter for context_type property."""
        self.logger.warn("Setting values on context_type will NOT update the remote Canvas instance.")
        self._context_type = value

    @property
    def context_id(self):
        """The ID of the object the Favorite refers to."""
        return self._context_id

    @context_id.setter
    def context_id(self, value):
        """Setter for context_id property."""
        self.logger.warn("Setting values on context_id will NOT update the remote Canvas instance.")
        self._context_id = value

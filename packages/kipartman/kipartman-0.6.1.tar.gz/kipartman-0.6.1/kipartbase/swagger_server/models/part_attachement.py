# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.upload_file_data import UploadFileData
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class PartAttachement(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, source_name=None, storage_path=None, id=None, description=None):
        """
        PartAttachement - a model defined in Swagger

        :param source_name: The source_name of this PartAttachement.
        :type source_name: str
        :param storage_path: The storage_path of this PartAttachement.
        :type storage_path: str
        :param id: The id of this PartAttachement.
        :type id: int
        :param description: The description of this PartAttachement.
        :type description: str
        """
        self.swagger_types = {
            'source_name': str,
            'storage_path': str,
            'id': int,
            'description': str
        }

        self.attribute_map = {
            'source_name': 'source_name',
            'storage_path': 'storage_path',
            'id': 'id',
            'description': 'description'
        }

        self._source_name = source_name
        self._storage_path = storage_path
        self._id = id
        self._description = description

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PartAttachement of this PartAttachement.
        :rtype: PartAttachement
        """
        return deserialize_model(dikt, cls)

    @property
    def source_name(self):
        """
        Gets the source_name of this PartAttachement.

        :return: The source_name of this PartAttachement.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """
        Sets the source_name of this PartAttachement.

        :param source_name: The source_name of this PartAttachement.
        :type source_name: str
        """

        self._source_name = source_name

    @property
    def storage_path(self):
        """
        Gets the storage_path of this PartAttachement.

        :return: The storage_path of this PartAttachement.
        :rtype: str
        """
        return self._storage_path

    @storage_path.setter
    def storage_path(self, storage_path):
        """
        Sets the storage_path of this PartAttachement.

        :param storage_path: The storage_path of this PartAttachement.
        :type storage_path: str
        """

        self._storage_path = storage_path

    @property
    def id(self):
        """
        Gets the id of this PartAttachement.

        :return: The id of this PartAttachement.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PartAttachement.

        :param id: The id of this PartAttachement.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def description(self):
        """
        Gets the description of this PartAttachement.

        :return: The description of this PartAttachement.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PartAttachement.

        :param description: The description of this PartAttachement.
        :type description: str
        """

        self._description = description


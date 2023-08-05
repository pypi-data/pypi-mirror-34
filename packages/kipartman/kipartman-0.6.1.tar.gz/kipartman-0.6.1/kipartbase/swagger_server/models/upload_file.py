# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.upload_file_data import UploadFileData
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class UploadFile(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, source_name=None, storage_path=None, id=None):
        """
        UploadFile - a model defined in Swagger

        :param source_name: The source_name of this UploadFile.
        :type source_name: str
        :param storage_path: The storage_path of this UploadFile.
        :type storage_path: str
        :param id: The id of this UploadFile.
        :type id: int
        """
        self.swagger_types = {
            'source_name': str,
            'storage_path': str,
            'id': int
        }

        self.attribute_map = {
            'source_name': 'source_name',
            'storage_path': 'storage_path',
            'id': 'id'
        }

        self._source_name = source_name
        self._storage_path = storage_path
        self._id = id

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UploadFile of this UploadFile.
        :rtype: UploadFile
        """
        return deserialize_model(dikt, cls)

    @property
    def source_name(self):
        """
        Gets the source_name of this UploadFile.

        :return: The source_name of this UploadFile.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """
        Sets the source_name of this UploadFile.

        :param source_name: The source_name of this UploadFile.
        :type source_name: str
        """

        self._source_name = source_name

    @property
    def storage_path(self):
        """
        Gets the storage_path of this UploadFile.

        :return: The storage_path of this UploadFile.
        :rtype: str
        """
        return self._storage_path

    @storage_path.setter
    def storage_path(self, storage_path):
        """
        Sets the storage_path of this UploadFile.

        :param storage_path: The storage_path of this UploadFile.
        :type storage_path: str
        """

        self._storage_path = storage_path

    @property
    def id(self):
        """
        Gets the id of this UploadFile.

        :return: The id of this UploadFile.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UploadFile.

        :param id: The id of this UploadFile.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id


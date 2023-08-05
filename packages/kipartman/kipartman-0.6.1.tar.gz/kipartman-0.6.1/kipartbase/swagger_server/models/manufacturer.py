# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.manufacturer_data import ManufacturerData
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Manufacturer(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, address=None, website=None, email=None, phone=None, comment=None, id=None):
        """
        Manufacturer - a model defined in Swagger

        :param name: The name of this Manufacturer.
        :type name: str
        :param address: The address of this Manufacturer.
        :type address: str
        :param website: The website of this Manufacturer.
        :type website: str
        :param email: The email of this Manufacturer.
        :type email: str
        :param phone: The phone of this Manufacturer.
        :type phone: str
        :param comment: The comment of this Manufacturer.
        :type comment: str
        :param id: The id of this Manufacturer.
        :type id: int
        """
        self.swagger_types = {
            'name': str,
            'address': str,
            'website': str,
            'email': str,
            'phone': str,
            'comment': str,
            'id': int
        }

        self.attribute_map = {
            'name': 'name',
            'address': 'address',
            'website': 'website',
            'email': 'email',
            'phone': 'phone',
            'comment': 'comment',
            'id': 'id'
        }

        self._name = name
        self._address = address
        self._website = website
        self._email = email
        self._phone = phone
        self._comment = comment
        self._id = id

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Manufacturer of this Manufacturer.
        :rtype: Manufacturer
        """
        return deserialize_model(dikt, cls)

    @property
    def name(self):
        """
        Gets the name of this Manufacturer.

        :return: The name of this Manufacturer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Manufacturer.

        :param name: The name of this Manufacturer.
        :type name: str
        """

        self._name = name

    @property
    def address(self):
        """
        Gets the address of this Manufacturer.

        :return: The address of this Manufacturer.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this Manufacturer.

        :param address: The address of this Manufacturer.
        :type address: str
        """

        self._address = address

    @property
    def website(self):
        """
        Gets the website of this Manufacturer.

        :return: The website of this Manufacturer.
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """
        Sets the website of this Manufacturer.

        :param website: The website of this Manufacturer.
        :type website: str
        """

        self._website = website

    @property
    def email(self):
        """
        Gets the email of this Manufacturer.

        :return: The email of this Manufacturer.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Manufacturer.

        :param email: The email of this Manufacturer.
        :type email: str
        """

        self._email = email

    @property
    def phone(self):
        """
        Gets the phone of this Manufacturer.

        :return: The phone of this Manufacturer.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this Manufacturer.

        :param phone: The phone of this Manufacturer.
        :type phone: str
        """

        self._phone = phone

    @property
    def comment(self):
        """
        Gets the comment of this Manufacturer.

        :return: The comment of this Manufacturer.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this Manufacturer.

        :param comment: The comment of this Manufacturer.
        :type comment: str
        """

        self._comment = comment

    @property
    def id(self):
        """
        Gets the id of this Manufacturer.

        :return: The id of this Manufacturer.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Manufacturer.

        :param id: The id of this Manufacturer.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id


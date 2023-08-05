# coding: utf-8

"""
    Kipartman

    Kipartman api specifications

    OpenAPI spec version: 1.0.0
    Contact: --
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Currency(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'symbol': 'str',
        'base': 'str',
        'ratio': 'float'
    }

    attribute_map = {
        'name': 'name',
        'symbol': 'symbol',
        'base': 'base',
        'ratio': 'ratio'
    }

    def __init__(self, name=None, symbol=None, base=None, ratio=None):
        """
        Currency - a model defined in Swagger
        """

        self._name = None
        self._symbol = None
        self._base = None
        self._ratio = None

        self.name = name
        self.symbol = symbol
        self.base = base
        self.ratio = ratio

    @property
    def name(self):
        """
        Gets the name of this Currency.

        :return: The name of this Currency.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Currency.

        :param name: The name of this Currency.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def symbol(self):
        """
        Gets the symbol of this Currency.

        :return: The symbol of this Currency.
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """
        Sets the symbol of this Currency.

        :param symbol: The symbol of this Currency.
        :type: str
        """
        if symbol is None:
            raise ValueError("Invalid value for `symbol`, must not be `None`")

        self._symbol = symbol

    @property
    def base(self):
        """
        Gets the base of this Currency.

        :return: The base of this Currency.
        :rtype: str
        """
        return self._base

    @base.setter
    def base(self, base):
        """
        Sets the base of this Currency.

        :param base: The base of this Currency.
        :type: str
        """
        if base is None:
            raise ValueError("Invalid value for `base`, must not be `None`")

        self._base = base

    @property
    def ratio(self):
        """
        Gets the ratio of this Currency.

        :return: The ratio of this Currency.
        :rtype: float
        """
        return self._ratio

    @ratio.setter
    def ratio(self, ratio):
        """
        Sets the ratio of this Currency.

        :param ratio: The ratio of this Currency.
        :type: float
        """
        if ratio is None:
            raise ValueError("Invalid value for `ratio`, must not be `None`")

        self._ratio = ratio

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
        if not isinstance(other, Currency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

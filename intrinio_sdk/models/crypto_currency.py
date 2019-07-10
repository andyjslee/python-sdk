# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.8.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CryptoCurrency(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'code': 'str',
        'symbol': 'str',
        'first_price_date': 'str',
        'last_price_date': 'str'
    }

    attribute_map = {
        'name': 'name',
        'code': 'code',
        'symbol': 'symbol',
        'first_price_date': 'first_price_date',
        'last_price_date': 'last_price_date'
    }

    def __init__(self, name=None, code=None, symbol=None, first_price_date=None, last_price_date=None):  # noqa: E501
        """CryptoCurrency - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._code = None
        self._symbol = None
        self._first_price_date = None
        self._last_price_date = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if code is not None:
            self.code = code
        if symbol is not None:
            self.symbol = symbol
        if first_price_date is not None:
            self.first_price_date = first_price_date
        if last_price_date is not None:
            self.last_price_date = last_price_date

    @property
    def name(self):
        """Gets the name of this CryptoCurrency.  # noqa: E501

        The common name of the crypto currency.  # noqa: E501

        :return: The name of this CryptoCurrency.  # noqa: E501
        :rtype: str
        """
        return self._name
        
    @property
    def name_dict(self):
        """Gets the name of this CryptoCurrency.  # noqa: E501

        The common name of the crypto currency. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The name of this CryptoCurrency.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.name
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'name': value }

        
        return result
        

    @name.setter
    def name(self, name):
        """Sets the name of this CryptoCurrency.

        The common name of the crypto currency.  # noqa: E501

        :param name: The name of this CryptoCurrency.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def code(self):
        """Gets the code of this CryptoCurrency.  # noqa: E501

        A code representing the crypto currency.  # noqa: E501

        :return: The code of this CryptoCurrency.  # noqa: E501
        :rtype: str
        """
        return self._code
        
    @property
    def code_dict(self):
        """Gets the code of this CryptoCurrency.  # noqa: E501

        A code representing the crypto currency. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The code of this CryptoCurrency.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.code
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'code': value }

        
        return result
        

    @code.setter
    def code(self, code):
        """Sets the code of this CryptoCurrency.

        A code representing the crypto currency.  # noqa: E501

        :param code: The code of this CryptoCurrency.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def symbol(self):
        """Gets the symbol of this CryptoCurrency.  # noqa: E501

        The symbol of the Crypto Currency.  # noqa: E501

        :return: The symbol of this CryptoCurrency.  # noqa: E501
        :rtype: str
        """
        return self._symbol
        
    @property
    def symbol_dict(self):
        """Gets the symbol of this CryptoCurrency.  # noqa: E501

        The symbol of the Crypto Currency. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The symbol of this CryptoCurrency.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.symbol
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'symbol': value }

        
        return result
        

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this CryptoCurrency.

        The symbol of the Crypto Currency.  # noqa: E501

        :param symbol: The symbol of this CryptoCurrency.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def first_price_date(self):
        """Gets the first_price_date of this CryptoCurrency.  # noqa: E501

        The earliest date that daily historical pricing is available for.  # noqa: E501

        :return: The first_price_date of this CryptoCurrency.  # noqa: E501
        :rtype: str
        """
        return self._first_price_date
        
    @property
    def first_price_date_dict(self):
        """Gets the first_price_date of this CryptoCurrency.  # noqa: E501

        The earliest date that daily historical pricing is available for. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The first_price_date of this CryptoCurrency.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.first_price_date
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'first_price_date': value }

        
        return result
        

    @first_price_date.setter
    def first_price_date(self, first_price_date):
        """Sets the first_price_date of this CryptoCurrency.

        The earliest date that daily historical pricing is available for.  # noqa: E501

        :param first_price_date: The first_price_date of this CryptoCurrency.  # noqa: E501
        :type: str
        """

        self._first_price_date = first_price_date

    @property
    def last_price_date(self):
        """Gets the last_price_date of this CryptoCurrency.  # noqa: E501

        The most recent date that daily historical pricing is available for.  # noqa: E501

        :return: The last_price_date of this CryptoCurrency.  # noqa: E501
        :rtype: str
        """
        return self._last_price_date
        
    @property
    def last_price_date_dict(self):
        """Gets the last_price_date of this CryptoCurrency.  # noqa: E501

        The most recent date that daily historical pricing is available for. as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The last_price_date of this CryptoCurrency.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.last_price_date
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'last_price_date': value }

        
        return result
        

    @last_price_date.setter
    def last_price_date(self, last_price_date):
        """Sets the last_price_date of this CryptoCurrency.

        The most recent date that daily historical pricing is available for.  # noqa: E501

        :param last_price_date: The last_price_date of this CryptoCurrency.  # noqa: E501
        :type: str
        """

        self._last_price_date = last_price_date

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CryptoCurrency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

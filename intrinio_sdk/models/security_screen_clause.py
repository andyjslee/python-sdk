# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.8.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SecurityScreenClause(object):
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
        'field': 'str',
        'operator': 'str',
        'value': 'str'
    }

    attribute_map = {
        'field': 'field',
        'operator': 'operator',
        'value': 'value'
    }

    def __init__(self, field=None, operator=None, value=None):  # noqa: E501
        """SecurityScreenClause - a model defined in Swagger"""  # noqa: E501

        self._field = None
        self._operator = None
        self._value = None
        self.discriminator = None

        if field is not None:
            self.field = field
        if operator is not None:
            self.operator = operator
        if value is not None:
            self.value = value

    @property
    def field(self):
        """Gets the field of this SecurityScreenClause.  # noqa: E501

        The field to use when screening, such as an Intrinio Data Tag  # noqa: E501

        :return: The field of this SecurityScreenClause.  # noqa: E501
        :rtype: str
        """
        return self._field
        
    @property
    def field_dict(self):
        """Gets the field of this SecurityScreenClause.  # noqa: E501

        The field to use when screening, such as an Intrinio Data Tag as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The field of this SecurityScreenClause.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.field
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
            result = { 'field': value }

        
        return result
        

    @field.setter
    def field(self, field):
        """Sets the field of this SecurityScreenClause.

        The field to use when screening, such as an Intrinio Data Tag  # noqa: E501

        :param field: The field of this SecurityScreenClause.  # noqa: E501
        :type: str
        """

        self._field = field

    @property
    def operator(self):
        """Gets the operator of this SecurityScreenClause.  # noqa: E501

        The logic operator to use when screening  # noqa: E501

        :return: The operator of this SecurityScreenClause.  # noqa: E501
        :rtype: str
        """
        return self._operator
        
    @property
    def operator_dict(self):
        """Gets the operator of this SecurityScreenClause.  # noqa: E501

        The logic operator to use when screening as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The operator of this SecurityScreenClause.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.operator
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
            result = { 'operator': value }

        
        return result
        

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this SecurityScreenClause.

        The logic operator to use when screening  # noqa: E501

        :param operator: The operator of this SecurityScreenClause.  # noqa: E501
        :type: str
        """
        allowed_values = ["eq", "gt", "gte", "lt", "lte", "contains"]  # noqa: E501
        if operator not in allowed_values:
            raise ValueError(
                "Invalid value for `operator` ({0}), must be one of {1}"  # noqa: E501
                .format(operator, allowed_values)
            )

        self._operator = operator

    @property
    def value(self):
        """Gets the value of this SecurityScreenClause.  # noqa: E501

        The value to screen by  # noqa: E501

        :return: The value of this SecurityScreenClause.  # noqa: E501
        :rtype: str
        """
        return self._value
        
    @property
    def value_dict(self):
        """Gets the value of this SecurityScreenClause.  # noqa: E501

        The value to screen by as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The value of this SecurityScreenClause.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.value
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
            result = { 'value': value }

        
        return result
        

    @value.setter
    def value(self, value):
        """Sets the value of this SecurityScreenClause.

        The value to screen by  # noqa: E501

        :param value: The value of this SecurityScreenClause.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if not isinstance(other, SecurityScreenClause):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

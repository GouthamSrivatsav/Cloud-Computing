# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SVD(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, acc=None):  # noqa: E501
        """SVD - a model defined in Swagger

        :param acc: The acc of this SVD.  # noqa: E501
        :type acc: str
        """
        self.swagger_types = {
            'acc': str
        }

        self.attribute_map = {
            'acc': 'acc'
        }

        self._acc = acc

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SVD of this SVD.  # noqa: E501
        :rtype: SVD
        """
        return util.deserialize_model(dikt, cls)

    @property
    def acc(self):
        """Gets the acc of this SVD.


        :return: The acc of this SVD.
        :rtype: str
        """
        return self._acc

    @acc.setter
    def acc(self, acc):
        """Sets the acc of this SVD.


        :param acc: The acc of this SVD.
        :type acc: str
        """
        if acc is None:
            raise ValueError("Invalid value for `acc`, must not be `None`")  # noqa: E501

        self._acc = acc
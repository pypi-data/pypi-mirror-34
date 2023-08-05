# -*- coding: utf-8 -*-

"""
    raas.models.raas_client_exception

    This file was automatically generated for Tango Card, Inc. by APIMATIC v2.0 ( https://apimatic.io )
"""
from ..api_helper import APIHelper
import raas.exceptions.api_exception
import raas.models.raas_client_error_model

class RaasClientException(raas.exceptions.api_exception.APIException):
    def __init__(self, reason, context):
        """Constructor for the RaasClientException class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            context (HttpContext):  The HttpContext of the API call.

        """
        super(RaasClientException, self).__init__(reason, context)
        dictionary = APIHelper.json_deserialize(self.context.response.raw_body)
        if isinstance(dictionary, dict):
            self.unbox(dictionary)

    def unbox(self, dictionary):
        """Populates the properties of this object by extracting them from a dictionary.

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        """
        self.timestamp = APIHelper.RFC3339DateTime.from_value(dictionary.get("timestamp")).datetime if dictionary.get("timestamp") else None
        self.request_id = dictionary.get('requestId')
        self.path = dictionary.get('path')
        self.http_code = dictionary.get('httpCode')
        self.http_phrase = dictionary.get('httpPhrase')
        self.errors = None
        if dictionary.get('errors') != None:
            self.errors = list()
            for structure in dictionary.get('errors'):
                self.errors.append(raas.models.raas_client_error_model.RaasClientErrorModel.from_dictionary(structure))

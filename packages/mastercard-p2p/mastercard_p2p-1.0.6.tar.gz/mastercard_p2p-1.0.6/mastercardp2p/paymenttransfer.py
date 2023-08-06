#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (c) 2016 MasterCard International Incorporated
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are
# permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this list of
# conditions and the following disclaimer.
# Redistributions in binary form must reproduce the above copyright notice, this list of
# conditions and the following disclaimer in the documentation and/or other materials
# provided with the distribution.
# Neither the name of the MasterCard International Incorporated nor the names of its
# contributors may be used to endorse or promote products derived from this software
# without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT
# SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
# TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
#


from __future__ import absolute_import
from mastercardapicore import BaseObject
from mastercardapicore import RequestMap
from mastercardapicore import OperationConfig
from mastercardapicore import OperationMetadata
from mastercardp2p import ResourceConfig

class PaymentTransfer(BaseObject):
    """
    
    """

    __config = {
        
        "fae92e4c-9b71-469c-92f1-802b908af391" : OperationConfig("/send/v1/partners/{partnerId}/transfers/payment", "create", [], []),
        
        "5beb0eeb-279c-4dc0-acdd-8d245279dd99" : OperationConfig("/send/v1/partners/{partnerId}/transfers/{transferId}", "read", [], []),
        
        "3350a98c-ebb2-4aff-9404-54108c09b76a" : OperationConfig("/send/v1/partners/{partnerId}/transfers", "query", [], ["ref"]),
        
    }

    def getOperationConfig(self,operationUUID):
        if operationUUID not in self.__config:
            raise Exception("Invalid operationUUID: "+operationUUID)

        return self.__config[operationUUID]

    def getOperationMetadata(self):
        return OperationMetadata(ResourceConfig.getInstance().getVersion(), ResourceConfig.getInstance().getHost(), ResourceConfig.getInstance().getContext(), ResourceConfig.getInstance().getJsonNative(), ResourceConfig.getInstance().getContentTypeOverride())


    @classmethod
    def create(cls,mapObj):
        """
        Creates object of type PaymentTransfer

        @param Dict mapObj, containing the required parameters to create a new object
        @return PaymentTransfer of the response of created instance.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("fae92e4c-9b71-469c-92f1-802b908af391", PaymentTransfer(mapObj))










    @classmethod
    def readByID(cls,id,criteria=None):
        """
        Returns objects of type PaymentTransfer by id and optional criteria
        @param str id
        @param dict criteria
        @return instance of PaymentTransfer
        @raise ApiException: raised an exception from the response status
        """
        mapObj =  RequestMap()
        if id:
            mapObj.set("id", id)

        if criteria:
            if (isinstance(criteria,RequestMap)):
                mapObj.setAll(criteria.getObject())
            else:
                mapObj.setAll(criteria)

        return BaseObject.execute("5beb0eeb-279c-4dc0-acdd-8d245279dd99", PaymentTransfer(mapObj))







    @classmethod
    def readByReference(cls,criteria):
        """
        Query objects of type PaymentTransfer by id and optional criteria
        @param type criteria
        @return PaymentTransfer object representing the response.
        @raise ApiException: raised an exception from the response status
        """

        return BaseObject.execute("3350a98c-ebb2-4aff-9404-54108c09b76a", PaymentTransfer(criteria))



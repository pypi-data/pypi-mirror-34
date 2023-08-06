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
from mastercardqkr import ResourceConfig

class Beneficiary(BaseObject):
    """
    
    """

    __config = {
        
        "024ba3da-525d-4508-ae45-e775a7a65260" : OperationConfig("/labs/proxy/qkr2/internal/api2/beneficiary", "create", ["X-Auth-Token"], []),
        
        "88a50c66-a628-46bb-815f-ab46ea447b53" : OperationConfig("/labs/proxy/qkr2/internal/api2/beneficiary/{id}", "delete", ["X-Auth-Token"], []),
        
        "7b3b7b32-6531-4a0d-8dbd-8fbe1eb086ea" : OperationConfig("/labs/proxy/qkr2/internal/api2/beneficiary", "query", ["X-Auth-Token"], ["merchantId"]),
        
        "eb950ab8-412c-4529-88f4-cdb0b91a7c77" : OperationConfig("/labs/proxy/qkr2/internal/api2/beneficiary/{id}", "update", ["X-Auth-Token"], []),
        
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
        Creates object of type Beneficiary

        @param Dict mapObj, containing the required parameters to create a new object
        @return Beneficiary of the response of created instance.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("024ba3da-525d-4508-ae45-e775a7a65260", Beneficiary(mapObj))









    @classmethod
    def deleteById(cls,id,map=None):
        """
        Delete object of type Beneficiary by id

        @param str id
        @return Beneficiary of the response of the deleted instance.
        @raise ApiException: raised an exception from the response status
        """

        mapObj =  RequestMap()
        if id:
            mapObj.set("id", id)

        if map:
            if (isinstance(map,RequestMap)):
                mapObj.setAll(map.getObject())
            else:
                mapObj.setAll(map)

        return BaseObject.execute("88a50c66-a628-46bb-815f-ab46ea447b53", Beneficiary(mapObj))

    def delete(self):
        """
        Delete object of type Beneficiary

        @return Beneficiary of the response of the deleted instance.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("88a50c66-a628-46bb-815f-ab46ea447b53", self)








    @classmethod
    def query(cls,criteria):
        """
        Query objects of type Beneficiary by id and optional criteria
        @param type criteria
        @return Beneficiary object representing the response.
        @raise ApiException: raised an exception from the response status
        """

        return BaseObject.execute("7b3b7b32-6531-4a0d-8dbd-8fbe1eb086ea", Beneficiary(criteria))


    def update(self):
        """
        Updates an object of type Beneficiary

        @return Beneficiary object representing the response.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("eb950ab8-412c-4529-88f4-cdb0b91a7c77", self)







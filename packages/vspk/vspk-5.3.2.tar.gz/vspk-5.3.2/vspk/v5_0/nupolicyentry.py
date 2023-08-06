# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc, 2017 Nokia
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its contributors
#       may be used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



from bambou import NURESTObject


class NUPolicyEntry(NURESTObject):
    """ Represents a PolicyEntry in the VSD

        Notes:
            None
    """

    __rest_name__ = "policyentry"
    __resource_name__ = "policyentries"

    

    def __init__(self, **kwargs):
        """ Initializes a PolicyEntry instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> policyentry = NUPolicyEntry(id=u'xxxx-xxx-xxx-xxx', name=u'PolicyEntry')
                >>> policyentry = NUPolicyEntry(data=my_dict)
        """

        super(NUPolicyEntry, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._match_criteria = None
        self._match_overlay_address_pool_id = None
        self._match_policy_object_group_id = None
        self._actions = None
        self._description = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="match_criteria", remote_name="matchCriteria", attribute_type=dict, is_required=False, is_unique=False)
        self.expose_attribute(local_name="match_overlay_address_pool_id", remote_name="matchOverlayAddressPoolID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="match_policy_object_group_id", remote_name="matchPolicyObjectGroupID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="actions", remote_name="actions", attribute_type=dict, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the Policy Entry

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the Policy Entry

                
        """
        self._name = value

    
    @property
    def match_criteria(self):
        """ Get match_criteria value.

            Notes:
                Match criteria BLOB

                
                This attribute is named `matchCriteria` in VSD API.
                
        """
        return self._match_criteria

    @match_criteria.setter
    def match_criteria(self, value):
        """ Set match_criteria value.

            Notes:
                Match criteria BLOB

                
                This attribute is named `matchCriteria` in VSD API.
                
        """
        self._match_criteria = value

    
    @property
    def match_overlay_address_pool_id(self):
        """ Get match_overlay_address_pool_id value.

            Notes:
                ID of Overlay Address Pool for this Policy Entry.

                
                This attribute is named `matchOverlayAddressPoolID` in VSD API.
                
        """
        return self._match_overlay_address_pool_id

    @match_overlay_address_pool_id.setter
    def match_overlay_address_pool_id(self, value):
        """ Set match_overlay_address_pool_id value.

            Notes:
                ID of Overlay Address Pool for this Policy Entry.

                
                This attribute is named `matchOverlayAddressPoolID` in VSD API.
                
        """
        self._match_overlay_address_pool_id = value

    
    @property
    def match_policy_object_group_id(self):
        """ Get match_policy_object_group_id value.

            Notes:
                ID of Policy Object Group where this Policy Entry belongs.

                
                This attribute is named `matchPolicyObjectGroupID` in VSD API.
                
        """
        return self._match_policy_object_group_id

    @match_policy_object_group_id.setter
    def match_policy_object_group_id(self, value):
        """ Set match_policy_object_group_id value.

            Notes:
                ID of Policy Object Group where this Policy Entry belongs.

                
                This attribute is named `matchPolicyObjectGroupID` in VSD API.
                
        """
        self._match_policy_object_group_id = value

    
    @property
    def actions(self):
        """ Get actions value.

            Notes:
                Action of Policy Entry

                
        """
        return self._actions

    @actions.setter
    def actions(self, value):
        """ Set actions value.

            Notes:
                Action of Policy Entry

                
        """
        self._actions = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Description of the Policy Entry

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of the Policy Entry

                
        """
        self._description = value

    

    
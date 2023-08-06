# coding: utf-8

"""
    Factern API
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from factern_client.api_client import ApiClient


class FactsApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_member(self, **kwargs):  # noqa: E501
        """Create Member  # noqa: E501

        For adding a member to an existing group, template, or scope. Note that for permissions, with respect to the new member permission changes are immediately reflected.  #### Example In this example, we have a group of logins, and add a new login. We create a group. We already have two logins with Factern Ids `00000000DC9BD86B79F3F0DFDD22D293695EE23F397449B7` and `00000000F21C36AD0211C0E859DEFFA431CAC0A425D5BAEE`. ~~~ POST /creategroup {     \"name\": \"DetectiveLogins\",     \"memberIds\": [         \"00000000DC9BD86B79F3F0DFDD22D293695EE23F397449B7\",         \"00000000F21C36AD0211C0E859DEFFA431CAC0A425D5BAEE\"     ] } ~~~ Response includes the Factern Id of the created group. ~~~ {     ...     \"nodeId\": \"000000008BE86D4383D08AA7B1F02311D76516F7312CFFA3\",     ... } ~~~ Add login with Factern Id `00000000781841F6917E1CD0F626849C47CF5392E0AFD46E` ~~~ POST /createmember {     \"parentId\": \":DetectiveLogins\",     \"memberId\": \"00000000781841F6917E1CD0F626849C47CF5392E0AFD46E\" } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_member(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateMemberRequest create_member_request:
        :return: CreateMemberResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_member_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.add_member_with_http_info(**kwargs)  # noqa: E501
            return data

    def add_member_with_http_info(self, **kwargs):  # noqa: E501
        """Create Member  # noqa: E501

        For adding a member to an existing group, template, or scope. Note that for permissions, with respect to the new member permission changes are immediately reflected.  #### Example In this example, we have a group of logins, and add a new login. We create a group. We already have two logins with Factern Ids `00000000DC9BD86B79F3F0DFDD22D293695EE23F397449B7` and `00000000F21C36AD0211C0E859DEFFA431CAC0A425D5BAEE`. ~~~ POST /creategroup {     \"name\": \"DetectiveLogins\",     \"memberIds\": [         \"00000000DC9BD86B79F3F0DFDD22D293695EE23F397449B7\",         \"00000000F21C36AD0211C0E859DEFFA431CAC0A425D5BAEE\"     ] } ~~~ Response includes the Factern Id of the created group. ~~~ {     ...     \"nodeId\": \"000000008BE86D4383D08AA7B1F02311D76516F7312CFFA3\",     ... } ~~~ Add login with Factern Id `00000000781841F6917E1CD0F626849C47CF5392E0AFD46E` ~~~ POST /createmember {     \"parentId\": \":DetectiveLogins\",     \"memberId\": \"00000000781841F6917E1CD0F626849C47CF5392E0AFD46E\" } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_member_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateMemberRequest create_member_request:
        :return: CreateMemberResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'create_member_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_member" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/createmember', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateMemberResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def bid(self, **kwargs):  # noqa: E501
        """Create Bid  # noqa: E501

        Any agent that has access to an entity and to the entity's price can place a bid on the facts covered by the price. If accepted, the bidder agent is given access to the facts based on the policy specified in the price, and the bidder agent's account balance is debited with value of the price.  #### Example ~~~ POST /createbid {     \"priceId\": \"00000000A5645604E38CC4CF6353919F5D23CBC62A3FB7CE\" } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.bid(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateBidRequest create_bid_request:
        :return: StandardNodeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.bid_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.bid_with_http_info(**kwargs)  # noqa: E501
            return data

    def bid_with_http_info(self, **kwargs):  # noqa: E501
        """Create Bid  # noqa: E501

        Any agent that has access to an entity and to the entity's price can place a bid on the facts covered by the price. If accepted, the bidder agent is given access to the facts based on the policy specified in the price, and the bidder agent's account balance is debited with value of the price.  #### Example ~~~ POST /createbid {     \"priceId\": \"00000000A5645604E38CC4CF6353919F5D23CBC62A3FB7CE\" } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.bid_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateBidRequest create_bid_request:
        :return: StandardNodeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'create_bid_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bid" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/createbid', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StandardNodeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_alias(self, **kwargs):  # noqa: E501
        """Create Alias  # noqa: E501

        For creating a node alias. Once created, the node can be referenced by its alias in any place where it could be referenced by its Factern Id using the syntax `@alias`.  Aliases, by default, are globally unique. However, they can be reassigned by deleting the alias node and creating a new alias that targets a different entity.  Local aliases can be created by setting the `local` property to `true`. A local alias is visible only within the scope of the alias creating login. Note that local aliases can be used to hide global aliases. That is, a local alias can use the same name as a global alias, effectively making that global alias inaccessible from the local alias creating login.  A node can have more than one alias. Deleting a node with an alias does not delete the alias. An alias node can itself have an alias.  #### Example In this example, we create an alias for an entity, having Factern Id \"0000000024CAD703CD904D88EDD10DE4543F7925E70B5BDC\", and then describe that entity using its alias. We then delete the alias and create an alias for a different entity, having Factern Id \"00000000E2A5842459DC89B85BA0BEC554CD1A37FCF84B55\". ~~~ POST /createalias {     \"targetNodeId\": \"0000000024CAD703CD904D88EDD10DE4543F7925E70B5BDC\",     \"name\": \"Watson\",     \"description\": \"Alias for the Dr. Watson entity\" } ~~~ Response ~~~ {     ...     \"nodeId\": \"000000008D315993C02F32DEE13637CCD4A1280F34A79D50\",     \"parentId\": \"0000000024CAD703CD904D88EDD10DE4543F7925E70B5BDC\",     \"name\": \"Watson\",     \"description\": \"Alias for the Dr. Watson entity\",     ... } ~~~ We describe the entity, using the alias instead of the entity's Factern Id. ~~~ POST /describe {     ...     \"nodeId\": \"@Watson\",     ... } ~~~ Response ~~~ {     ...     \"nodeId\": \"0000000024CAD703CD904D88EDD10DE4543F7925E70B5BDC\",     ... } ~~~ We delete the alias. Take care that you use the nodeId of the alias and not the entity! ~~~ POST /deletenode {     \"nodeId\": \"000000008D315993C02F32DEE13637CCD4A1280F34A79D50\" } ~~~ We create the alias, targeting a different entity. ~~~ POST /createalias {     \"targetNodeId\": \"00000000E2A5842459DC89B85BA0BEC554CD1A37FCF84B55\",     \"name\": \"Watson\",     \"description\": \"Alias for the Dr. Watson entity\" } ~~~ Response ~~~ {     ...     \"nodeId\": \"00000000A29EAEA33949E326DAA8D1550F3FA856BB1AC894\",     \"parentId\": \"00000000E2A5842459DC89B85BA0BEC554CD1A37FCF84B55\",     \"name\": \"Watson\",     \"description\": \"Alias for the Dr. Watson entity\",     ... } ~~~ ### Subaliases  A subalias is just an alias containing one or more periods. For example, the alias `@london.detectives` is a subalias of the base alias `@detectives`. A subalias can be created just like a regular alias, but with the additional restriction that the creating login must also have been the creator of the base alias.  #### Example In this example, we create an alias for a group of people entities. The group has the name `PeopleEntities`, and we assign the alias `people` to it. We then create a subalias for another group of people entities associated with the city of London. The group has the name `LondonPeopleEntities`, and we assign the subalias `london.people` to it. ~~~ POST /createalias {     \"targetNodeId\": \"frn:group::PeopleEntities\",     \"name\": \"people\",     \"description\": \"Alias for the collection of all people entities\" } ~~~ ~~~ POST /createalias {     \"targetNodeId\": \"frn:group::LondonPeopleEntities\",     \"name\": \"london.people\",     \"description\": \"Alias for the collection of all people entities associated with the city of London\" } ~~~ If the creator of the `london.people` alias was any login other than the creator of the `people` alias, the create would have failed with status code 400.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_alias(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateAliasRequest create_alias_request:
        :return: CreateAliasResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_alias_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_alias_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_alias_with_http_info(self, **kwargs):  # noqa: E501
        """Create Alias  # noqa: E501

        For creating a node alias. Once created, the node can be referenced by its alias in any place where it could be referenced by its Factern Id using the syntax `@alias`.  Aliases, by default, are globally unique. However, they can be reassigned by deleting the alias node and creating a new alias that targets a different entity.  Local aliases can be created by setting the `local` property to `true`. A local alias is visible only within the scope of the alias creating login. Note that local aliases can be used to hide global aliases. That is, a local alias can use the same name as a global alias, effectively making that global alias inaccessible from the local alias creating login.  A node can have more than one alias. Deleting a node with an alias does not delete the alias. An alias node can itself have an alias.  #### Example In this example, we create an alias for an entity, having Factern Id \"0000000024CAD703CD904D88EDD10DE4543F7925E70B5BDC\", and then describe that entity using its alias. We then delete the alias and create an alias for a different entity, having Factern Id \"00000000E2A5842459DC89B85BA0BEC554CD1A37FCF84B55\". ~~~ POST /createalias {     \"targetNodeId\": \"0000000024CAD703CD904D88EDD10DE4543F7925E70B5BDC\",     \"name\": \"Watson\",     \"description\": \"Alias for the Dr. Watson entity\" } ~~~ Response ~~~ {     ...     \"nodeId\": \"000000008D315993C02F32DEE13637CCD4A1280F34A79D50\",     \"parentId\": \"0000000024CAD703CD904D88EDD10DE4543F7925E70B5BDC\",     \"name\": \"Watson\",     \"description\": \"Alias for the Dr. Watson entity\",     ... } ~~~ We describe the entity, using the alias instead of the entity's Factern Id. ~~~ POST /describe {     ...     \"nodeId\": \"@Watson\",     ... } ~~~ Response ~~~ {     ...     \"nodeId\": \"0000000024CAD703CD904D88EDD10DE4543F7925E70B5BDC\",     ... } ~~~ We delete the alias. Take care that you use the nodeId of the alias and not the entity! ~~~ POST /deletenode {     \"nodeId\": \"000000008D315993C02F32DEE13637CCD4A1280F34A79D50\" } ~~~ We create the alias, targeting a different entity. ~~~ POST /createalias {     \"targetNodeId\": \"00000000E2A5842459DC89B85BA0BEC554CD1A37FCF84B55\",     \"name\": \"Watson\",     \"description\": \"Alias for the Dr. Watson entity\" } ~~~ Response ~~~ {     ...     \"nodeId\": \"00000000A29EAEA33949E326DAA8D1550F3FA856BB1AC894\",     \"parentId\": \"00000000E2A5842459DC89B85BA0BEC554CD1A37FCF84B55\",     \"name\": \"Watson\",     \"description\": \"Alias for the Dr. Watson entity\",     ... } ~~~ ### Subaliases  A subalias is just an alias containing one or more periods. For example, the alias `@london.detectives` is a subalias of the base alias `@detectives`. A subalias can be created just like a regular alias, but with the additional restriction that the creating login must also have been the creator of the base alias.  #### Example In this example, we create an alias for a group of people entities. The group has the name `PeopleEntities`, and we assign the alias `people` to it. We then create a subalias for another group of people entities associated with the city of London. The group has the name `LondonPeopleEntities`, and we assign the subalias `london.people` to it. ~~~ POST /createalias {     \"targetNodeId\": \"frn:group::PeopleEntities\",     \"name\": \"people\",     \"description\": \"Alias for the collection of all people entities\" } ~~~ ~~~ POST /createalias {     \"targetNodeId\": \"frn:group::LondonPeopleEntities\",     \"name\": \"london.people\",     \"description\": \"Alias for the collection of all people entities associated with the city of London\" } ~~~ If the creator of the `london.people` alias was any login other than the creator of the `people` alias, the create would have failed with status code 400.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_alias_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateAliasRequest create_alias_request:
        :return: CreateAliasResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'create_alias_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_alias" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/createalias', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateAliasResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_application(self, **kwargs):  # noqa: E501
        """Create Application  # noqa: E501

        All data created must be associated with a creating application. All data accessed are accessed using the permissions associated with an application.  #### Example In this example, we create an application. ~~~ POST /createapplication {     \"name\": \"PayrollApp\",     redirectUris: [\"http://acme.com/profile\"] } ~~~ Response includes the Factern Id of the created application. ~~~ {     \"nodeId\": \"000000007A69840D125F1664C0921E73BDEAE0D66D8C9829\" } ~~~ Note that like any request, the application creation is done in the context of an authenticated login and application. As such, your first application must be created using the Dev Portal `https://portal.factern.com/#/login`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_application(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateApplicationRequest create_application_request:
        :return: CreateApplicationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_application_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_application_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_application_with_http_info(self, **kwargs):  # noqa: E501
        """Create Application  # noqa: E501

        All data created must be associated with a creating application. All data accessed are accessed using the permissions associated with an application.  #### Example In this example, we create an application. ~~~ POST /createapplication {     \"name\": \"PayrollApp\",     redirectUris: [\"http://acme.com/profile\"] } ~~~ Response includes the Factern Id of the created application. ~~~ {     \"nodeId\": \"000000007A69840D125F1664C0921E73BDEAE0D66D8C9829\" } ~~~ Note that like any request, the application creation is done in the context of an authenticated login and application. As such, your first application must be created using the Dev Portal `https://portal.factern.com/#/login`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_application_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateApplicationRequest create_application_request:
        :return: CreateApplicationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'create_application_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_application" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/createapplication', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateApplicationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_domain(self, **kwargs):  # noqa: E501
        """Create Domain  # noqa: E501

        By default, all facts are created in the local fact table.  However, it is possible to create facts in remote fact tables by defining and using a *domain*. A domain definition will declare endpoints for adding, retrieving, and (optionally) querying facts. It is up to the remote domain to implement proper semantics.  When creating login or entity nodes, the Domain Id can be specified. The node will be created in that domain, provided the remote service is correctly implemented. Login and entity nodes with no Domain Id specified will be created in the domain of their parent. All other nodes will also be created in the domain of their parent.  A node's domain can be inferred from its Factern Id by the most significant 32 bits. For example, a node with Factern Id `2D51FAC37A69840D125F1664C0921E73BDEAE0D66D8C9829` has a Domain Id of `2D51FAC3`.  #### Example In this example, we create a domain, give it a name (optional), and create an entity in that domain. We will then create a child entity without specifying a Domain Id and see that it inherits the Domain Id of its parent. We create a domain. ~~~ POST /createdomain {     ...     \"addFact\": {\"url\": \"https://facts.acme.com/add\"},     \"getFact\": {\"url\": \"https://facts.com/get\"},     \"queryFacts\": {\"url\": \"https://facts.com/query\"},     \"name\": \"AcmeDomain\"     ... } ~~~ The response contains the created domains's Domain Id. Note the domain's Factern Id is its Domain Id, left padded with 0s. Response ~~~ {     ...     \"nodeId\": \"00000000000000000000000000000000000000002D51FAC3\",     \"domainId\": \"2D51FAC3\",     ... } ~~~ In a subsequent creation of an entity node, we specify the domain's Factern Id. ~~~ POST /createentity {     ...     \"domainId\": \"00000000000000000000000000000000000000002D51FAC3\", } ~~~ The entity's Factern Id is returned. Note that the upper 32 bits are its Domain Id `2D51FAC3`. Response ~~~ {     ...     \"nodeId\": \"2D51FAC379C27D120B58F74C683639EE72EA2E33B93293CB\",     ... } ~~~ Factern will have called the domain ADD endpoint with a fact that corresponds to the entity node. It is up to the endpoint's implementation to implement proper creation semantics. In a subsequent creation of an entity node, we specify the parent's Factern Id. ~~~ POST /createentity {     ...     \"parentId\": \"2D51FAC379C27D120B58F74C683639EE72EA2E33B93293CB\", } ~~~ The entity is created in the same domain. ~~~ Response {     ...     \"nodeId\": \"2D51FAC3926097BF7B85454CDB078293E67E620A719A2CC2\",     ... } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_domain(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateDomainRequest create_domain_request:
        :return: CreateDomainResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_domain_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_domain_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_domain_with_http_info(self, **kwargs):  # noqa: E501
        """Create Domain  # noqa: E501

        By default, all facts are created in the local fact table.  However, it is possible to create facts in remote fact tables by defining and using a *domain*. A domain definition will declare endpoints for adding, retrieving, and (optionally) querying facts. It is up to the remote domain to implement proper semantics.  When creating login or entity nodes, the Domain Id can be specified. The node will be created in that domain, provided the remote service is correctly implemented. Login and entity nodes with no Domain Id specified will be created in the domain of their parent. All other nodes will also be created in the domain of their parent.  A node's domain can be inferred from its Factern Id by the most significant 32 bits. For example, a node with Factern Id `2D51FAC37A69840D125F1664C0921E73BDEAE0D66D8C9829` has a Domain Id of `2D51FAC3`.  #### Example In this example, we create a domain, give it a name (optional), and create an entity in that domain. We will then create a child entity without specifying a Domain Id and see that it inherits the Domain Id of its parent. We create a domain. ~~~ POST /createdomain {     ...     \"addFact\": {\"url\": \"https://facts.acme.com/add\"},     \"getFact\": {\"url\": \"https://facts.com/get\"},     \"queryFacts\": {\"url\": \"https://facts.com/query\"},     \"name\": \"AcmeDomain\"     ... } ~~~ The response contains the created domains's Domain Id. Note the domain's Factern Id is its Domain Id, left padded with 0s. Response ~~~ {     ...     \"nodeId\": \"00000000000000000000000000000000000000002D51FAC3\",     \"domainId\": \"2D51FAC3\",     ... } ~~~ In a subsequent creation of an entity node, we specify the domain's Factern Id. ~~~ POST /createentity {     ...     \"domainId\": \"00000000000000000000000000000000000000002D51FAC3\", } ~~~ The entity's Factern Id is returned. Note that the upper 32 bits are its Domain Id `2D51FAC3`. Response ~~~ {     ...     \"nodeId\": \"2D51FAC379C27D120B58F74C683639EE72EA2E33B93293CB\",     ... } ~~~ Factern will have called the domain ADD endpoint with a fact that corresponds to the entity node. It is up to the endpoint's implementation to implement proper creation semantics. In a subsequent creation of an entity node, we specify the parent's Factern Id. ~~~ POST /createentity {     ...     \"parentId\": \"2D51FAC379C27D120B58F74C683639EE72EA2E33B93293CB\", } ~~~ The entity is created in the same domain. ~~~ Response {     ...     \"nodeId\": \"2D51FAC3926097BF7B85454CDB078293E67E620A719A2CC2\",     ... } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_domain_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateDomainRequest create_domain_request:
        :return: CreateDomainResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'create_domain_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_domain" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/createdomain', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateDomainResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_entity(self, **kwargs):  # noqa: E501
        """Create Entity  # noqa: E501

        Entities are basic element for representing permissionable items. Permissions set on entities are inherited by all associated information nodes.  #### Example In this example, we create an entity under another entity having Factern Id `00000000AF555988FBD9494419C26BBCD299A6314EAC0844` ~~~ POST /createentity {     \"parentId\": \"000000001A800FF23D27E58B90DD1008B3E5547E235B77F4\",     \"name\": \"JohnWatsonNode\" } ~~~ Response includes the Factern Id of the created entity. ~~~ {     \"nodeId\": \"00000000B87881B8F1187838A10D27B9E2A4A1AFD92D861A\" } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_entity(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateEntityRequest create_entity_request:
        :return: CreateEntityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_entity_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_entity_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_entity_with_http_info(self, **kwargs):  # noqa: E501
        """Create Entity  # noqa: E501

        Entities are basic element for representing permissionable items. Permissions set on entities are inherited by all associated information nodes.  #### Example In this example, we create an entity under another entity having Factern Id `00000000AF555988FBD9494419C26BBCD299A6314EAC0844` ~~~ POST /createentity {     \"parentId\": \"000000001A800FF23D27E58B90DD1008B3E5547E235B77F4\",     \"name\": \"JohnWatsonNode\" } ~~~ Response includes the Factern Id of the created entity. ~~~ {     \"nodeId\": \"00000000B87881B8F1187838A10D27B9E2A4A1AFD92D861A\" } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_entity_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateEntityRequest create_entity_request:
        :return: CreateEntityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'create_entity_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_entity" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/createentity', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateEntityResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_field(self, **kwargs):  # noqa: E501
        """Create Field  # noqa: E501

        Every information node must have an associated field type that describes the information. Note that there are two major types of field types: branch and leaf. An information node having a branch field type has no associated data, but can parent other information. A information node having a leaf field type must have associated data and cannot parent other information.  The field type *name* must be unique within the associated *login*.  #### Example In this example, we create a *searchable* field type We create the searchable type. ~~~ POST /createfield {     \"name\": \"FullName\"     \"searchable\": \"true\",     ... } ~~~ Response includes the Factern Id of the created field type. ~~~ {     ...     \"nodeId\": \"000000000D9955617980254688D7A0F138A94CA8D3ECB0B5\",     ... } ~~~ We create an information node under an entity having Factern Id `000000007B85454CDB078293E67E620A719A2CC24530F504`. ~~~ POST /createinformation {     ...     \"parentId\": \"000000007B85454CDB078293E67E620A719A2CC24530F504\",     \"fieldId\": \":FullName\",     \"data\": \"Alice Holmes\" } ~~~ The information's Factern Id is returned. ~~~ Response {     ...     \"nodeId\": \"00000000B8E2BDED46BBDDEA98D842316435CD0B890E54E3\",     ... } ~~~ We now search for all entities having an information node starting with value \"Alice\". ~~~ POST /searchentity {     ...     \"fieldId\": \":FullName\",     \"operator\": \"startsWith\",     \"term\": \"Alice\" } ~~~ Response includes the matching entity. ~~~ {     \"nodes\": [{         \"nodeId\": \"000000007B85454CDB078293E67E620A719A2CC24530F504\",         ...     }] } ~~~ #### Example In this example, we create a *branch* field type ~~~ POST /createfield {     \"name\": \"SalesLeads\"     \"branch\": \"true\",     ... } ~~~ Response includes the Factern Id of the created field type. ~~~ {     ...     \"nodeId\": \"00000000A45B1AF797D8BD7FFF9646E28FFDCCA5DF993E1C\",     ... } ~~~ We create an information node under the entity. ~~~ POST /createinformation {     ...     \"parentId\": \"00000000AF555988FBD9494419C26BBCD299A6314EAC0844\",     \"fieldId\": \":SalesLeads\" } ~~~ The branch information's Factern Id is returned. ~~~ Response {     ...     \"nodeId\": \"00000000043F63F456185E40CEC633593ABCD93200B54583\",     ... } ~~~ And a searchable information node under the branch information. ~~~ POST /createinformation {     ...     \"parentId\": \"00000000043F63F456185E40CEC633593ABCD93200B54583\",     \"fieldId\": \":FullName\",     \"data\": \"Alice Holmes\" } ~~~ We now search for all entities having an information node with value \"abc\". ~~~ POST /searchentity {     ...     \"fieldId\": \":FullName\",     \"operator\": \"startsWith\",     \"term\": \"Alice\" } ~~~ Response includes the matching entity. Note that even though the information was not directly under the entity, the entity is still matched. ~~~ {     \"nodes\": [{         \"nodeId\": \"00000000AF555988FBD9494419C26BBCD299A6314EAC0844\",         ...     }] } ~~~ #### Example In this example, we create a *uniqueByParent* field type ~~~ POST /createfield {     \"name\": \"EyeColour\"     \"uniqueByParent\": true,     ... } ~~~ Response includes the Factern Id of the created field type. ~~~ {     ...     \"nodeId\": \"000000008BE86D4383D08AA7B1F02311D76516F7312CFFA3\",     ... } ~~~ We create an information node under entity with Factern Id `00000000AF555988FBD9494419C26BBCD299A6314EAC0844`. ~~~ POST /createinformation {     ...     \"parentId\": \"00000000AF555988FBD9494419C26BBCD299A6314EAC0844\",     \"fieldId\": \":EyeColour\",     \"data\": \"Blue\" } ~~~ But if we repeat the previous information node creation, the response is HTTP status 409, Conflict, due to the fact that we can only have one information node directly under that entity with the given field type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_field(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateFieldRequest create_field_request:
        :return: CreateFieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_field_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_field_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_field_with_http_info(self, **kwargs):  # noqa: E501
        """Create Field  # noqa: E501

        Every information node must have an associated field type that describes the information. Note that there are two major types of field types: branch and leaf. An information node having a branch field type has no associated data, but can parent other information. A information node having a leaf field type must have associated data and cannot parent other information.  The field type *name* must be unique within the associated *login*.  #### Example In this example, we create a *searchable* field type We create the searchable type. ~~~ POST /createfield {     \"name\": \"FullName\"     \"searchable\": \"true\",     ... } ~~~ Response includes the Factern Id of the created field type. ~~~ {     ...     \"nodeId\": \"000000000D9955617980254688D7A0F138A94CA8D3ECB0B5\",     ... } ~~~ We create an information node under an entity having Factern Id `000000007B85454CDB078293E67E620A719A2CC24530F504`. ~~~ POST /createinformation {     ...     \"parentId\": \"000000007B85454CDB078293E67E620A719A2CC24530F504\",     \"fieldId\": \":FullName\",     \"data\": \"Alice Holmes\" } ~~~ The information's Factern Id is returned. ~~~ Response {     ...     \"nodeId\": \"00000000B8E2BDED46BBDDEA98D842316435CD0B890E54E3\",     ... } ~~~ We now search for all entities having an information node starting with value \"Alice\". ~~~ POST /searchentity {     ...     \"fieldId\": \":FullName\",     \"operator\": \"startsWith\",     \"term\": \"Alice\" } ~~~ Response includes the matching entity. ~~~ {     \"nodes\": [{         \"nodeId\": \"000000007B85454CDB078293E67E620A719A2CC24530F504\",         ...     }] } ~~~ #### Example In this example, we create a *branch* field type ~~~ POST /createfield {     \"name\": \"SalesLeads\"     \"branch\": \"true\",     ... } ~~~ Response includes the Factern Id of the created field type. ~~~ {     ...     \"nodeId\": \"00000000A45B1AF797D8BD7FFF9646E28FFDCCA5DF993E1C\",     ... } ~~~ We create an information node under the entity. ~~~ POST /createinformation {     ...     \"parentId\": \"00000000AF555988FBD9494419C26BBCD299A6314EAC0844\",     \"fieldId\": \":SalesLeads\" } ~~~ The branch information's Factern Id is returned. ~~~ Response {     ...     \"nodeId\": \"00000000043F63F456185E40CEC633593ABCD93200B54583\",     ... } ~~~ And a searchable information node under the branch information. ~~~ POST /createinformation {     ...     \"parentId\": \"00000000043F63F456185E40CEC633593ABCD93200B54583\",     \"fieldId\": \":FullName\",     \"data\": \"Alice Holmes\" } ~~~ We now search for all entities having an information node with value \"abc\". ~~~ POST /searchentity {     ...     \"fieldId\": \":FullName\",     \"operator\": \"startsWith\",     \"term\": \"Alice\" } ~~~ Response includes the matching entity. Note that even though the information was not directly under the entity, the entity is still matched. ~~~ {     \"nodes\": [{         \"nodeId\": \"00000000AF555988FBD9494419C26BBCD299A6314EAC0844\",         ...     }] } ~~~ #### Example In this example, we create a *uniqueByParent* field type ~~~ POST /createfield {     \"name\": \"EyeColour\"     \"uniqueByParent\": true,     ... } ~~~ Response includes the Factern Id of the created field type. ~~~ {     ...     \"nodeId\": \"000000008BE86D4383D08AA7B1F02311D76516F7312CFFA3\",     ... } ~~~ We create an information node under entity with Factern Id `00000000AF555988FBD9494419C26BBCD299A6314EAC0844`. ~~~ POST /createinformation {     ...     \"parentId\": \"00000000AF555988FBD9494419C26BBCD299A6314EAC0844\",     \"fieldId\": \":EyeColour\",     \"data\": \"Blue\" } ~~~ But if we repeat the previous information node creation, the response is HTTP status 409, Conflict, due to the fact that we can only have one information node directly under that entity with the given field type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_field_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateFieldRequest create_field_request:
        :return: CreateFieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'create_field_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_field" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/createfield', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateFieldResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_filter(self, **kwargs):  # noqa: E501
        """Create Filter  # noqa: E501

        A filter is set of statements that can be evaluated against a node. The filter evaluates to true if all statements evaluate to true, and false otherwise.  A filter statement consists of a *field* and an *argument* list.  #### Example In this example, we create a *filter* that evalutes to true for all nodes that are children of `00000000AF555988FBD9494419C26BBCD299A6314EAC0844` and have a Factern Id that are either `000000008BE86D4383D08AA7B1F02311D76516F7312CFFA3` OR `00000000043F63F456185E40CEC633593ABCD93200B54583`. ~~~ POST /createfilter {   ...     \"statements\": \"[       {         \"field\":\"Target\",         \"arguments\":[\"00000000AF555988FBD9494419C26BBCD299A6314EAC0844\"]       },       {         \"field\":\"Id\",         \"arguments\":[\"000000008BE86D4383D08AA7B1F02311D76516F7312CFFA3\", \"00000000043F63F456185E40CEC633593ABCD93200B54583\"]       }     ]\"     ... } ~~~ Response includes the Factern Id of the created filter. ~~~ {     ...     \"nodeId\": \"000000000D9955617980254688D7A0F138A94CA8D3ECB0B5\",     ... } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_filter(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateFilterRequest create_filter_request:
        :return: CreateFilterResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_filter_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_filter_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_filter_with_http_info(self, **kwargs):  # noqa: E501
        """Create Filter  # noqa: E501

        A filter is set of statements that can be evaluated against a node. The filter evaluates to true if all statements evaluate to true, and false otherwise.  A filter statement consists of a *field* and an *argument* list.  #### Example In this example, we create a *filter* that evalutes to true for all nodes that are children of `00000000AF555988FBD9494419C26BBCD299A6314EAC0844` and have a Factern Id that are either `000000008BE86D4383D08AA7B1F02311D76516F7312CFFA3` OR `00000000043F63F456185E40CEC633593ABCD93200B54583`. ~~~ POST /createfilter {   ...     \"statements\": \"[       {         \"field\":\"Target\",         \"arguments\":[\"00000000AF555988FBD9494419C26BBCD299A6314EAC0844\"]       },       {         \"field\":\"Id\",         \"arguments\":[\"000000008BE86D4383D08AA7B1F02311D76516F7312CFFA3\", \"00000000043F63F456185E40CEC633593ABCD93200B54583\"]       }     ]\"     ... } ~~~ Response includes the Factern Id of the created filter. ~~~ {     ...     \"nodeId\": \"000000000D9955617980254688D7A0F138A94CA8D3ECB0B5\",     ... } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_filter_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateFilterRequest create_filter_request:
        :return: CreateFilterResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'create_filter_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_filter" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/createfilter', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateFilterResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_group(self, **kwargs):  # noqa: E501
        """Create Group  # noqa: E501

        Groups are collections of nodes. All nodes in a group must be of a particular fact type, if one is specified, or may contain members of all types if the group's fact type is left unspe. For groups of logins, permissions can be granted on groups in the same way that they can be granted on individual entities.  #### Example In this example, we create a group of logins, and set permissions, accordingly. We create a group. We already have two logins with Factern Ids `00000000DC9BD86B79F3F0DFDD22D293695EE23F397449B7` and `00000000F21C36AD0211C0E859DEFFA431CAC0A425D5BAEE`. ~~~ POST /creategroup {     \"name\": \"DetectiveLogins\",     \"memberFactType\": \"Login\",     \"memberIds\": [         \"00000000DC9BD86B79F3F0DFDD22D293695EE23F397449B7\",         \"00000000F21C36AD0211C0E859DEFFA431CAC0A425D5BAEE\"     ] } ~~~ Response includes the Factern Id of the created group. ~~~ {     ...     \"nodeId\": \"0000000078F098BDE117D9831865E08AE77B5F0866A2568E\",     ... } ~~~ Group Factern Id can be used in `grantee` of permission request ~~~ POST /permission {     ...     \"policy\": {         ...         \"granteeId\": \":DetectiveLogins\"     } } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_group(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateGroupRequest create_group_request:
        :return: CreateGroupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_group_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_group_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_group_with_http_info(self, **kwargs):  # noqa: E501
        """Create Group  # noqa: E501

        Groups are collections of nodes. All nodes in a group must be of a particular fact type, if one is specified, or may contain members of all types if the group's fact type is left unspe. For groups of logins, permissions can be granted on groups in the same way that they can be granted on individual entities.  #### Example In this example, we create a group of logins, and set permissions, accordingly. We create a group. We already have two logins with Factern Ids `00000000DC9BD86B79F3F0DFDD22D293695EE23F397449B7` and `00000000F21C36AD0211C0E859DEFFA431CAC0A425D5BAEE`. ~~~ POST /creategroup {     \"name\": \"DetectiveLogins\",     \"memberFactType\": \"Login\",     \"memberIds\": [         \"00000000DC9BD86B79F3F0DFDD22D293695EE23F397449B7\",         \"00000000F21C36AD0211C0E859DEFFA431CAC0A425D5BAEE\"     ] } ~~~ Response includes the Factern Id of the created group. ~~~ {     ...     \"nodeId\": \"0000000078F098BDE117D9831865E08AE77B5F0866A2568E\",     ... } ~~~ Group Factern Id can be used in `grantee` of permission request ~~~ POST /permission {     ...     \"policy\": {         ...         \"granteeId\": \":DetectiveLogins\"     } } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_group_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateGroupRequest create_group_request:
        :return: CreateGroupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'create_group_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_group" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/creategroup', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateGroupResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_information(self, **kwargs):  # noqa: E501
        """Create Information  # noqa: E501

        An information node always has an associated field type. If the field type is a leaf, then the information node has associated data. If the field type is a branch, then the information node has no associated data but instead can be used to parent other information nodes.  An information node with a leaf field type can optionally be created with a storageId, which specifies an alternative storage for the associated data. If a storageId is not specified, the data is stored in the Factern default storage.  Note that the storageId is the Factern Id of an interface created using the /createinterface endpoint.  #### Example In this example, we create a branch information node and then a leaf information node under the branch We create the field type. ~~~ POST /createfield {     \"name\": \"Detectives\",     \"branch\": \"true\",     ... } ~~~ Response includes the Factern Id of the created field type. ~~~ {     ...     \"nodeId\": \"000000008029289F643854A1FE32F2EB69DEDFDD54B40EA9\",     ... } ~~~ We create an information node under the entity with Factern Id `00000000AF555988FBD9494419C26BBCD299A6314EAC0844`. ~~~ POST /createinformation {     ...     \"parentId\": \"00000000AF555988FBD9494419C26BBCD299A6314EAC0844\",     \"fieldId\": \":Detectives\", } ~~~ Response includes the Factern Id of the created information. ~~~ {     ...     \"nodeId\": \"00000000EC3C7555E09D4C2F1744E8E5E4F7794C3054051B\",     ... } ~~~ We create a second leaf field type. ~~~ POST /createfield {     \"name\": \"FullName\"     \"branch\": \"false\",     ... } ~~~ Response includes the Factern Id of the created field type. ~~~ {     ...     \"nodeId\": \"000000002FD4CF69CDC086CE295095A5F44167B9491B2836\",     ... } ~~~ We create an information node under the previously created information node having a branch field type. ~~~ POST /createinformation {     ...     \"parentId\": \"00000000EC3C7555E09D4C2F1744E8E5E4F7794C3054051B\",     \"fieldId\": \":FullName\",     \"data\": \"Sherlock Holmes\" } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_information(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateInformationRequest create_information_request:
        :return: CreateInformationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_information_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_information_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_information_with_http_info(self, **kwargs):  # noqa: E501
        """Create Information  # noqa: E501

        An information node always has an associated field type. If the field type is a leaf, then the information node has associated data. If the field type is a branch, then the information node has no associated data but instead can be used to parent other information nodes.  An information node with a leaf field type can optionally be created with a storageId, which specifies an alternative storage for the associated data. If a storageId is not specified, the data is stored in the Factern default storage.  Note that the storageId is the Factern Id of an interface created using the /createinterface endpoint.  #### Example In this example, we create a branch information node and then a leaf information node under the branch We create the field type. ~~~ POST /createfield {     \"name\": \"Detectives\",     \"branch\": \"true\",     ... } ~~~ Response includes the Factern Id of the created field type. ~~~ {     ...     \"nodeId\": \"000000008029289F643854A1FE32F2EB69DEDFDD54B40EA9\",     ... } ~~~ We create an information node under the entity with Factern Id `00000000AF555988FBD9494419C26BBCD299A6314EAC0844`. ~~~ POST /createinformation {     ...     \"parentId\": \"00000000AF555988FBD9494419C26BBCD299A6314EAC0844\",     \"fieldId\": \":Detectives\", } ~~~ Response includes the Factern Id of the created information. ~~~ {     ...     \"nodeId\": \"00000000EC3C7555E09D4C2F1744E8E5E4F7794C3054051B\",     ... } ~~~ We create a second leaf field type. ~~~ POST /createfield {     \"name\": \"FullName\"     \"branch\": \"false\",     ... } ~~~ Response includes the Factern Id of the created field type. ~~~ {     ...     \"nodeId\": \"000000002FD4CF69CDC086CE295095A5F44167B9491B2836\",     ... } ~~~ We create an information node under the previously created information node having a branch field type. ~~~ POST /createinformation {     ...     \"parentId\": \"00000000EC3C7555E09D4C2F1744E8E5E4F7794C3054051B\",     \"fieldId\": \":FullName\",     \"data\": \"Sherlock Holmes\" } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_information_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateInformationRequest create_information_request:
        :return: CreateInformationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'create_information_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_information" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/createinformation', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateInformationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_interface(self, **kwargs):  # noqa: E501
        """Create Interface  # noqa: E501

        An interface is a representation of an externally callable web API.  An interface is simply a triplet of http endpoints: an endpoint for writing data; an endpoint for reading data; and an endpoint for removing data. What those endpoints should expect payload-wise depends on how the interface is being used.  #### Example In this example, we create an interface, give it a name (optional), and use that interface as a storage for information node data. We create an interface. ~~~ POST /createinterface {     ...     \"addData\": {\"url\": \"https://acme.com/add\"},     \"getData\": {\"url\": \"https://acme.com/get\"},     \"deleteData\": {\"url\": \"https://acme.com/delete\"},     \"name\": \"BulkStorageInterface\"     ... } ~~~ The response contains the created interface's Factern Id Response ~~~ {     ...     \"nodeId\": \"00000000C4F8891E18CED1C62ACE2ABC2BC0BBF8C6DFBFCC\",     ... } ~~~ In a subsequent creation of a information node, we specify the interface's Factern Id. ~~~ POST /createinformation {     \"parentId\":\"0000000005D460B37CB008CA9476876DB924F1F7B0D7DDAE\",     \"fieldId\":\"0000000017CE2CED136F2F8EF27DDBBF6DD2EEBE8CF00871\",     \"storageId\": \"00000000C4F8891E18CED1C62ACE2ABC2BC0BBF8C6DFBFCC\",     \"data\": \"Baker Street\" } ~~~ The information's Factern Id is returned. ~~~ Response {     ...     \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\",     ... } ~~~ Factern will have called the interface ADD endpoint with the information's Factern Id and value. It is up to the endpoint's implementation to implement proper storage semantics. ~~~ POST https://acme.com/add?nodeId=0000000079C27D120B58F74C683639EE72EA2E33B93293CB my value ~~~ Now we read the information value, specifying the information's Factern Id. ~~~ POST /readinformation {     \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\" } ~~~ The interface GET endpoint will be called with the information's Factern Id. The field type and owning entity IDs are also included in the query string. ~~~ POST https://acme.com/get?nodeId=0000000079C27D120B58F74C683639EE72EA2E33B93293CB&x-factern-fieldTypeId=0000000017CE2CED136F2F8EF27DDBBF6DD2EEBE8CF00871&x-factern-owningEntityId=0000000005D460B37CB008CA9476876DB924F1F7B0D7DDAE ~~~ If the interface has properly implemented storage semantics, we would expect the following value to be returned from the interface as well as from Factern. ~~~ {     \"data\": \"Baker Street\" } ~~~ #### Example In this example we show how to make an indirect call using an interface. In this case, the external endpoint is of form `https://example.com/users/{userId}/name`. Additionally, let us say this endpoint requires we make a GET and specify a header to indicate we accept \"application/json\". We create the interface. ~~~ POST /createinterface {     ...     \"addData\": {         \"type\": \"Indirect\",         \"url\": \"https://acme.com/users/{userId}/name\",     },     \"getData\": {         \"type\": \"Indirect\",         \"url\": \"https://acme.com/users/{userId}/name\",         \"method\": \"GET\",         \"headers\": [{             \"key\": \"Accepts\",             \"value\": \"application/json\"         }]     },     \"name\": \"AcmeNameSource\"     ... } ~~~ Note that the URL for both the addData and getData must be identical. Note that URL has a parameter userId that we will supply when we write to the interface. When we write an information node having that storage interface, we are writing the parameters that are to be used on subsequent reads against the interface. For example, ~~~ POST /createentity {     ...     \"name\": \"Moriarty\" } POST /createfield {     ...     \"name\": \"AcmeName\" } POST /write {     ...     \"nodeId\": \"frn:entity::Moriarty\",     \"document\": [         {             \":AcmeName\": {                 \"data\": \"{\\\"userId\\\": \\\"moriarty-123\\\"}\",                 \"storageId\": \"frn:interface::AcmeNameSource\"             }         }     ] } ~~~ We are actually writing a fully escaped JSON document to the node of the parameters to be used subsequently on the interface getData endpoint. In this case, we are supplying a single parameter, `usedId` having value \"moriarty-123\". A subsequent read uses the written parameters to call against the interface. Example: ~~~ POST /read {    \"nodeId\":\"frn:entity::Moriarty\",    \"template\": [         \":AcmeName\"     ] } ~~~ actually makes a call against the interface read endpoint: ~~~ POST https://acme.com/users/moriarty-123/name ~~~ Depending on the implementation of the read endpoint the read response might contain: ~~~ {     \"items\": [{         \"readItem\": {             \"fieldId\": \"000000006EA460441ED31AF4B111567E6C3C4DB45E07F234\",             \"nodes\": [],             \"nodeId\": \"00000000F010BFBA02DAD6F4290CD335E8D5F4F2764109D5\",             \"data\": \"{\\\"first\\\": \\\"James\\\", \\\"last\\\": \\\"Moriarty\\\"}\",             \"children\": []         },         \"status\": 200     }] } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_interface(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateInterfaceRequest create_interface_request:
        :return: CreateInterfaceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_interface_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_interface_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_interface_with_http_info(self, **kwargs):  # noqa: E501
        """Create Interface  # noqa: E501

        An interface is a representation of an externally callable web API.  An interface is simply a triplet of http endpoints: an endpoint for writing data; an endpoint for reading data; and an endpoint for removing data. What those endpoints should expect payload-wise depends on how the interface is being used.  #### Example In this example, we create an interface, give it a name (optional), and use that interface as a storage for information node data. We create an interface. ~~~ POST /createinterface {     ...     \"addData\": {\"url\": \"https://acme.com/add\"},     \"getData\": {\"url\": \"https://acme.com/get\"},     \"deleteData\": {\"url\": \"https://acme.com/delete\"},     \"name\": \"BulkStorageInterface\"     ... } ~~~ The response contains the created interface's Factern Id Response ~~~ {     ...     \"nodeId\": \"00000000C4F8891E18CED1C62ACE2ABC2BC0BBF8C6DFBFCC\",     ... } ~~~ In a subsequent creation of a information node, we specify the interface's Factern Id. ~~~ POST /createinformation {     \"parentId\":\"0000000005D460B37CB008CA9476876DB924F1F7B0D7DDAE\",     \"fieldId\":\"0000000017CE2CED136F2F8EF27DDBBF6DD2EEBE8CF00871\",     \"storageId\": \"00000000C4F8891E18CED1C62ACE2ABC2BC0BBF8C6DFBFCC\",     \"data\": \"Baker Street\" } ~~~ The information's Factern Id is returned. ~~~ Response {     ...     \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\",     ... } ~~~ Factern will have called the interface ADD endpoint with the information's Factern Id and value. It is up to the endpoint's implementation to implement proper storage semantics. ~~~ POST https://acme.com/add?nodeId=0000000079C27D120B58F74C683639EE72EA2E33B93293CB my value ~~~ Now we read the information value, specifying the information's Factern Id. ~~~ POST /readinformation {     \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\" } ~~~ The interface GET endpoint will be called with the information's Factern Id. The field type and owning entity IDs are also included in the query string. ~~~ POST https://acme.com/get?nodeId=0000000079C27D120B58F74C683639EE72EA2E33B93293CB&x-factern-fieldTypeId=0000000017CE2CED136F2F8EF27DDBBF6DD2EEBE8CF00871&x-factern-owningEntityId=0000000005D460B37CB008CA9476876DB924F1F7B0D7DDAE ~~~ If the interface has properly implemented storage semantics, we would expect the following value to be returned from the interface as well as from Factern. ~~~ {     \"data\": \"Baker Street\" } ~~~ #### Example In this example we show how to make an indirect call using an interface. In this case, the external endpoint is of form `https://example.com/users/{userId}/name`. Additionally, let us say this endpoint requires we make a GET and specify a header to indicate we accept \"application/json\". We create the interface. ~~~ POST /createinterface {     ...     \"addData\": {         \"type\": \"Indirect\",         \"url\": \"https://acme.com/users/{userId}/name\",     },     \"getData\": {         \"type\": \"Indirect\",         \"url\": \"https://acme.com/users/{userId}/name\",         \"method\": \"GET\",         \"headers\": [{             \"key\": \"Accepts\",             \"value\": \"application/json\"         }]     },     \"name\": \"AcmeNameSource\"     ... } ~~~ Note that the URL for both the addData and getData must be identical. Note that URL has a parameter userId that we will supply when we write to the interface. When we write an information node having that storage interface, we are writing the parameters that are to be used on subsequent reads against the interface. For example, ~~~ POST /createentity {     ...     \"name\": \"Moriarty\" } POST /createfield {     ...     \"name\": \"AcmeName\" } POST /write {     ...     \"nodeId\": \"frn:entity::Moriarty\",     \"document\": [         {             \":AcmeName\": {                 \"data\": \"{\\\"userId\\\": \\\"moriarty-123\\\"}\",                 \"storageId\": \"frn:interface::AcmeNameSource\"             }         }     ] } ~~~ We are actually writing a fully escaped JSON document to the node of the parameters to be used subsequently on the interface getData endpoint. In this case, we are supplying a single parameter, `usedId` having value \"moriarty-123\". A subsequent read uses the written parameters to call against the interface. Example: ~~~ POST /read {    \"nodeId\":\"frn:entity::Moriarty\",    \"template\": [         \":AcmeName\"     ] } ~~~ actually makes a call against the interface read endpoint: ~~~ POST https://acme.com/users/moriarty-123/name ~~~ Depending on the implementation of the read endpoint the read response might contain: ~~~ {     \"items\": [{         \"readItem\": {             \"fieldId\": \"000000006EA460441ED31AF4B111567E6C3C4DB45E07F234\",             \"nodes\": [],             \"nodeId\": \"00000000F010BFBA02DAD6F4290CD335E8D5F4F2764109D5\",             \"data\": \"{\\\"first\\\": \\\"James\\\", \\\"last\\\": \\\"Moriarty\\\"}\",             \"children\": []         },         \"status\": 200     }] } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_interface_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateInterfaceRequest create_interface_request:
        :return: CreateInterfaceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'create_interface_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_interface" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/createinterface', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateInterfaceResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_label_list(self, **kwargs):  # noqa: E501
        """Create Label List  # noqa: E501

        A label list is a collection of logically consistent labels. The label members can be used in the `/label` endpoint to label data.  #### Example We create a label list representing the confirmation status of a information node's data. ~~~ POST /createlabellist {     ...     \"name\": \"ConfirmationStatus\",     \"members\": [         \"Unconfirmed\",         \"Rejected\",         \"Confirmed\"     ] } ~~~ Response ~~~ {     ...     \"nodeId\": \"00000000C125606D13DCE6AD6A1D2B6969C2863C4FAB050B\",     \"members\": [{         ...         \"name\": \"Confirmed\",         \"nodeId\": \"00000000A1AF37B270DE7EED4EE881021B678D4D8518D4ED\"     },...] } ~~~ We now label an existing information node with Factern Id `00000000FB76E443E8F923ED5B43CFEF7233F3E278836D70` as Confirmed by using the Factern Id of the Confirmed label. ~~~ POST /label {     \"targetNodeId\": \"00000000FB76E443E8F923ED5B43CFEF7233F3E278836D70\",     \"labelId\": \"00000000A1AF37B270DE7EED4EE881021B678D4D8518D4ED\" } ~~~ We could also use the FRN of the Confirmed label. ~~~ POST /label {     \"targetNodeId\": \"00000000FB76E443E8F923ED5B43CFEF7233F3E278836D70\",     \"labelId\": \"frn:labellistmember::ConfirmationStatus/Confirmed\" } ~~~ Finally we list the labels of the information node filtering results using the ConfirmationStatus label list. ~~~ POST /describe {     ...     \"nodeId\": \"00000000FB76E443E8F923ED5B43CFEF7233F3E278836D70\",     \"listChildren\": {         \"factType\": \"Label\",         \"labelListId\": \":ConfirmationStatus\"     } } ~~~ Response ~~~ {     ...     \"children\": [{         \"targetNodeId\": \"00000000FB76E443E8F923ED5B43CFEF7233F3E278836D70\",         \"memberId\": \"00000000A1AF37B270DE7EED4EE881021B678D4D8518D4ED\"     }] } ~~~ Showing that the information node was labelled with the label corresponding to the Confirmed status.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_label_list(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateLabelListRequest create_label_list_request:
        :return: CreateLabelListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_label_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_label_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_label_list_with_http_info(self, **kwargs):  # noqa: E501
        """Create Label List  # noqa: E501

        A label list is a collection of logically consistent labels. The label members can be used in the `/label` endpoint to label data.  #### Example We create a label list representing the confirmation status of a information node's data. ~~~ POST /createlabellist {     ...     \"name\": \"ConfirmationStatus\",     \"members\": [         \"Unconfirmed\",         \"Rejected\",         \"Confirmed\"     ] } ~~~ Response ~~~ {     ...     \"nodeId\": \"00000000C125606D13DCE6AD6A1D2B6969C2863C4FAB050B\",     \"members\": [{         ...         \"name\": \"Confirmed\",         \"nodeId\": \"00000000A1AF37B270DE7EED4EE881021B678D4D8518D4ED\"     },...] } ~~~ We now label an existing information node with Factern Id `00000000FB76E443E8F923ED5B43CFEF7233F3E278836D70` as Confirmed by using the Factern Id of the Confirmed label. ~~~ POST /label {     \"targetNodeId\": \"00000000FB76E443E8F923ED5B43CFEF7233F3E278836D70\",     \"labelId\": \"00000000A1AF37B270DE7EED4EE881021B678D4D8518D4ED\" } ~~~ We could also use the FRN of the Confirmed label. ~~~ POST /label {     \"targetNodeId\": \"00000000FB76E443E8F923ED5B43CFEF7233F3E278836D70\",     \"labelId\": \"frn:labellistmember::ConfirmationStatus/Confirmed\" } ~~~ Finally we list the labels of the information node filtering results using the ConfirmationStatus label list. ~~~ POST /describe {     ...     \"nodeId\": \"00000000FB76E443E8F923ED5B43CFEF7233F3E278836D70\",     \"listChildren\": {         \"factType\": \"Label\",         \"labelListId\": \":ConfirmationStatus\"     } } ~~~ Response ~~~ {     ...     \"children\": [{         \"targetNodeId\": \"00000000FB76E443E8F923ED5B43CFEF7233F3E278836D70\",         \"memberId\": \"00000000A1AF37B270DE7EED4EE881021B678D4D8518D4ED\"     }] } ~~~ Showing that the information node was labelled with the label corresponding to the Confirmed status.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_label_list_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateLabelListRequest create_label_list_request:
        :return: CreateLabelListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'create_label_list_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_label_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/createlabellist', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateLabelListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_login(self, **kwargs):  # noqa: E501
        """Create Login  # noqa: E501

        All data created must be associated with a creating login. All data accessed are accessed using the permissions associated with a login.  #### Example In this example, we create a login. ~~~ POST /createlogin {     \"email\": \"alice@acme.com\",     \"password\": \"mypassword\",     \"workflow\": \"APP_INITIATED\" } ~~~ Response includes the Factern Id of the created login. ~~~ {     \"nodeId\": \"000000008CE3F53C41ED38CD958DE6F8D485525D02AF6944\" } ~~~ Note that like any request, the login creation is done in the context of an authenticated login and application. As such, your first login must be created using the Dev Portal `https://portal.factern.com/#/login`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_login(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateLoginRequest create_login_request:
        :return: CreateLoginResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_login_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_login_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_login_with_http_info(self, **kwargs):  # noqa: E501
        """Create Login  # noqa: E501

        All data created must be associated with a creating login. All data accessed are accessed using the permissions associated with a login.  #### Example In this example, we create a login. ~~~ POST /createlogin {     \"email\": \"alice@acme.com\",     \"password\": \"mypassword\",     \"workflow\": \"APP_INITIATED\" } ~~~ Response includes the Factern Id of the created login. ~~~ {     \"nodeId\": \"000000008CE3F53C41ED38CD958DE6F8D485525D02AF6944\" } ~~~ Note that like any request, the login creation is done in the context of an authenticated login and application. As such, your first login must be created using the Dev Portal `https://portal.factern.com/#/login`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_login_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateLoginRequest create_login_request:
        :return: CreateLoginResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'create_login_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_login" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/createlogin', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateLoginResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_mirror(self, **kwargs):  # noqa: E501
        """Create Mirror  # noqa: E501

        A mirror consists of a source entity node, a destination entity node, and a template. Any updates to the source entity that is covered by the mirror's template will be automatically propagated to the destination entity node.  #### Example In this example, we create two entities, a template and a mirror. Then we write to the source entity using the template and see that the destination entity is also changed to reflect that write. We create two entities, each representing John Watson. The first entity is created under Her Majesty's Revenue and Customs and the second entity is created under London Police Department Consultants. The purpose of the mirror is to automatically update the latter whenever the former is updated. ~~~ POST /createentity {     \"parentId\": \"@HMRevenueAndCustoms\" } ~~~ Response ~~~ {     ...     \"nodeId\": \"00000000A797A4951E939886BA465B9EFABFCD2E5B9131A7\",     ... } ~~~ ~~~ POST /createentity {     \"parentId\": \"@LondonPDConsultants\" } ~~~ Response ~~~ {     ...     \"nodeId\": \"00000000020E67C874812302B5967F0458452B7432F8E89B\",     ... } ~~~ Create some fields and a template. ~~~ POST /createfield {     \"name\": \"Spouse\"     \"branch\": \"true\",     ... } ~~~ ~~~ POST /createfield {     \"name\": \"FullName\"     \"branch\": \"true\",     ... } ~~~ ~~~ POST /createfield {     \"name\": \"FirstName\"     \"branch\": \"false\",     ... } ~~~ ~~~ POST /createfield {     \"name\": \"LastName\"     \"branch\": \"false\",     ... } ~~~ ~~~ POST /createtemplate {     ...     \"name\": \"SpouseProfile\",     \"memberIds\": [         \":Spouse\": {             \":FullName\": [                 \":FirstName\",                 \":LastName\"             ]         }     ] } ~~~ Create the mirror. ~~~ POST /createmirror {   \"sourceNodeId\": \"00000000A797A4951E939886BA465B9EFABFCD2E5B9131A7\",   \"destinationNodeId\": \"00000000020E67C874812302B5967F0458452B7432F8E89B\",   \"templateId\": \":SpouseProfile\" } ~~~ Update the entity under *@HMRevenueAndCustoms* using the *SpouseProfile* template. ~~~ POST /write {     \"templateId\": \":SpouseProfile\",     \"nodeId\": \"00000000A797A4951E939886BA465B9EFABFCD2E5B9131A7\",     \"values\": [         \"Mary\",         \"Morstan\"     ] } ~~~ Reading the entity under *@LondonPDConsultants* would verify that it has been updated with spousal information. ~~~ POST /read {     \"templateId\": \":SpouseProfile\",     \"nodeId\": \"00000000020E67C874812302B5967F0458452B7432F8E89B\" } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_mirror(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateMirrorRequest create_mirror_request:
        :return: CreateMirrorResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_mirror_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_mirror_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_mirror_with_http_info(self, **kwargs):  # noqa: E501
        """Create Mirror  # noqa: E501

        A mirror consists of a source entity node, a destination entity node, and a template. Any updates to the source entity that is covered by the mirror's template will be automatically propagated to the destination entity node.  #### Example In this example, we create two entities, a template and a mirror. Then we write to the source entity using the template and see that the destination entity is also changed to reflect that write. We create two entities, each representing John Watson. The first entity is created under Her Majesty's Revenue and Customs and the second entity is created under London Police Department Consultants. The purpose of the mirror is to automatically update the latter whenever the former is updated. ~~~ POST /createentity {     \"parentId\": \"@HMRevenueAndCustoms\" } ~~~ Response ~~~ {     ...     \"nodeId\": \"00000000A797A4951E939886BA465B9EFABFCD2E5B9131A7\",     ... } ~~~ ~~~ POST /createentity {     \"parentId\": \"@LondonPDConsultants\" } ~~~ Response ~~~ {     ...     \"nodeId\": \"00000000020E67C874812302B5967F0458452B7432F8E89B\",     ... } ~~~ Create some fields and a template. ~~~ POST /createfield {     \"name\": \"Spouse\"     \"branch\": \"true\",     ... } ~~~ ~~~ POST /createfield {     \"name\": \"FullName\"     \"branch\": \"true\",     ... } ~~~ ~~~ POST /createfield {     \"name\": \"FirstName\"     \"branch\": \"false\",     ... } ~~~ ~~~ POST /createfield {     \"name\": \"LastName\"     \"branch\": \"false\",     ... } ~~~ ~~~ POST /createtemplate {     ...     \"name\": \"SpouseProfile\",     \"memberIds\": [         \":Spouse\": {             \":FullName\": [                 \":FirstName\",                 \":LastName\"             ]         }     ] } ~~~ Create the mirror. ~~~ POST /createmirror {   \"sourceNodeId\": \"00000000A797A4951E939886BA465B9EFABFCD2E5B9131A7\",   \"destinationNodeId\": \"00000000020E67C874812302B5967F0458452B7432F8E89B\",   \"templateId\": \":SpouseProfile\" } ~~~ Update the entity under *@HMRevenueAndCustoms* using the *SpouseProfile* template. ~~~ POST /write {     \"templateId\": \":SpouseProfile\",     \"nodeId\": \"00000000A797A4951E939886BA465B9EFABFCD2E5B9131A7\",     \"values\": [         \"Mary\",         \"Morstan\"     ] } ~~~ Reading the entity under *@LondonPDConsultants* would verify that it has been updated with spousal information. ~~~ POST /read {     \"templateId\": \":SpouseProfile\",     \"nodeId\": \"00000000020E67C874812302B5967F0458452B7432F8E89B\" } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_mirror_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateMirrorRequest create_mirror_request:
        :return: CreateMirrorResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'create_mirror_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_mirror" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/createmirror', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateMirrorResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_price(self, **kwargs):  # noqa: E501
        """Create Price  # noqa: E501

        Prices can be set upon entities. An entity forms the root of a document. For example, there may be an “Alice” entity that roots the document describing Alice’s name, address and contact info. The price attached to the entity can either be for selling access to all facts off the entity, or just a subset of the facts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_price(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreatePriceRequest create_price_request:
        :return: CreatePriceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_price_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_price_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_price_with_http_info(self, **kwargs):  # noqa: E501
        """Create Price  # noqa: E501

        Prices can be set upon entities. An entity forms the root of a document. For example, there may be an “Alice” entity that roots the document describing Alice’s name, address and contact info. The price attached to the entity can either be for selling access to all facts off the entity, or just a subset of the facts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_price_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreatePriceRequest create_price_request:
        :return: CreatePriceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'create_price_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_price" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/createprice', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreatePriceResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_scope(self, **kwargs):  # noqa: E501
        """Create Scope  # noqa: E501

        Scopes are collections of templates or filters. Scopes are used in permissioning to bring together a set of nodes all having the same permissions.  The scope *name* must be unique within the associated *logins*.  #### Example In this example, we create a scope containing templates with Factern Ids `00000000A5ABACFABC029D2A526291DDF04559242F286757` and `00000000AE5AA31410B5AABEEE9E981A890CD932F21C3204` and filters with Factern IDs `000000002B46D4331F76C89EE12CC82E9CA87EFFFA695CC0` and `00000000F33F1BBE66809D4B5682A6823744AB253AE99F51`. The scope is created ~~~ POST /createscope {     \"name\": \"NameAndAddressScope\",     \"templateIds\": [         \"00000000A5ABACFABC029D2A526291DDF04559242F286757\",         \"00000000AE5AA31410B5AABEEE9E981A890CD932F21C3204\"     ],     \"filterIds\": [         \"000000002B46D4331F76C89EE12CC82E9CA87EFFFA695CC0\",         \"00000000F33F1BBE66809D4B5682A6823744AB253AE99F51\"     ] } ~~~ Response ~~~ {     ...     \"nodeId\": \"000000006FAEA1DC636C002361474CC34C022EE68F8A8844\",     \"name\": \"NameAndAddressScope\",     \"memberIds\": [         \"00000000A5ABACFABC029D2A526291DDF04559242F286757\",         \"00000000AE5AA31410B5AABEEE9E981A890CD932F21C3204\",         \"000000002B46D4331F76C89EE12CC82E9CA87EFFFA695CC0\",         \"00000000F33F1BBE66809D4B5682A6823744AB253AE99F51\"     ] } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_scope(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateScopeRequest create_scope_request:
        :return: CreateScopeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_scope_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_scope_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_scope_with_http_info(self, **kwargs):  # noqa: E501
        """Create Scope  # noqa: E501

        Scopes are collections of templates or filters. Scopes are used in permissioning to bring together a set of nodes all having the same permissions.  The scope *name* must be unique within the associated *logins*.  #### Example In this example, we create a scope containing templates with Factern Ids `00000000A5ABACFABC029D2A526291DDF04559242F286757` and `00000000AE5AA31410B5AABEEE9E981A890CD932F21C3204` and filters with Factern IDs `000000002B46D4331F76C89EE12CC82E9CA87EFFFA695CC0` and `00000000F33F1BBE66809D4B5682A6823744AB253AE99F51`. The scope is created ~~~ POST /createscope {     \"name\": \"NameAndAddressScope\",     \"templateIds\": [         \"00000000A5ABACFABC029D2A526291DDF04559242F286757\",         \"00000000AE5AA31410B5AABEEE9E981A890CD932F21C3204\"     ],     \"filterIds\": [         \"000000002B46D4331F76C89EE12CC82E9CA87EFFFA695CC0\",         \"00000000F33F1BBE66809D4B5682A6823744AB253AE99F51\"     ] } ~~~ Response ~~~ {     ...     \"nodeId\": \"000000006FAEA1DC636C002361474CC34C022EE68F8A8844\",     \"name\": \"NameAndAddressScope\",     \"memberIds\": [         \"00000000A5ABACFABC029D2A526291DDF04559242F286757\",         \"00000000AE5AA31410B5AABEEE9E981A890CD932F21C3204\",         \"000000002B46D4331F76C89EE12CC82E9CA87EFFFA695CC0\",         \"00000000F33F1BBE66809D4B5682A6823744AB253AE99F51\"     ] } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_scope_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateScopeRequest create_scope_request:
        :return: CreateScopeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'create_scope_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_scope" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/createscope', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateScopeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_statement(self, **kwargs):  # noqa: E501
        """Create Statement  # noqa: E501

        Statements are facts that bring together a target node with some specific *action*. The *action* id must be chosen from a list of supported actions, as there is not a way to create new actions at this time. Depending on the action, the statement may require an additional qualifying node.  #### Example In this example, we create a statement to indicate that the entity with id `000000001ADE8A80023B7E090594227905A5D8DC5C1212A0` has an interface that will be called prior to any template read applied to the entity. In this case it is an interface that loads information nodes under the entity as needed. ~~~ POST /createstatement {     \"targetNodeId\": \"000000001ADE8A80023B7E090594227905A5D8DC5C1212A0\",     \"actionId\": \"000000000000000034375CE3851C457F96D7D4C6115EB91E\",     \"actionQualifierId\": \"frn:interface::LazyLoadProfileData\" } ~~~ Response ~~~ {     ...     \"nodeId\": \"000000006FAEA1DC636C002361474CC34C022EE68F8A8844\",     \"targetNodeId\": \"000000001ADE8A80023B7E090594227905A5D8DC5C1212A0\",     \"actionId\": \"000000000000000034375CE3851C457F96D7D4C6115EB91E\",     \"actionQualifierId\": \"00000000DF4E39037F12CE796786C1217BDC72A6FC1B43DE\" } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_statement(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param AddStatementRequest add_statement_request:
        :return: AddStatementResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_statement_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_statement_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_statement_with_http_info(self, **kwargs):  # noqa: E501
        """Create Statement  # noqa: E501

        Statements are facts that bring together a target node with some specific *action*. The *action* id must be chosen from a list of supported actions, as there is not a way to create new actions at this time. Depending on the action, the statement may require an additional qualifying node.  #### Example In this example, we create a statement to indicate that the entity with id `000000001ADE8A80023B7E090594227905A5D8DC5C1212A0` has an interface that will be called prior to any template read applied to the entity. In this case it is an interface that loads information nodes under the entity as needed. ~~~ POST /createstatement {     \"targetNodeId\": \"000000001ADE8A80023B7E090594227905A5D8DC5C1212A0\",     \"actionId\": \"000000000000000034375CE3851C457F96D7D4C6115EB91E\",     \"actionQualifierId\": \"frn:interface::LazyLoadProfileData\" } ~~~ Response ~~~ {     ...     \"nodeId\": \"000000006FAEA1DC636C002361474CC34C022EE68F8A8844\",     \"targetNodeId\": \"000000001ADE8A80023B7E090594227905A5D8DC5C1212A0\",     \"actionId\": \"000000000000000034375CE3851C457F96D7D4C6115EB91E\",     \"actionQualifierId\": \"00000000DF4E39037F12CE796786C1217BDC72A6FC1B43DE\" } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_statement_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param AddStatementRequest add_statement_request:
        :return: AddStatementResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'add_statement_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_statement" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/createstatement', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AddStatementResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_template(self, **kwargs):  # noqa: E501
        """Create Template  # noqa: E501

        Templates are collections of field types. They are used in the `/read` and `/write` endpoints for reading and writing data in bulk.  The template *name* must be unique within the associated *login*.  #### Example In this example we have created a set of fields that define a Person's name, and basic street address with street and city parts. The responses from the creation of the fields: ~~~ {     ...     \"branch\": false,     \"uniqueByParent\": true,     \"nodeId\": \"000000008BFE6BB9A2A3F80F23DC6E738470F24B95E5102A\",     \"name\": \"PersonName\" } {     ...     \"branch\": true,     \"uniqueByParent\": true,     \"nodeId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA\",     \"name\": \"BasicAddress\" } {     ...     \"branch\": false,     \"uniqueByParent\": true,     \"nodeId\": \"0000000095E0F6B9F5480FD75DA9520E480AD3E89DC35D9A\",     \"name\": \"Street\" } {     ...     \"branch\": false,     \"uniqueByParent\": true,     \"nodeId\": \"00000000F6EFF0C416BE603531C8BA77C36E8A9B29368FB5\",     \"name\": \"City\" } ~~~ A template is created with the fields. ~~~ POST /createtemplate {     ...     \"name\": \"PersonProfile\",     \"memberIds\": [         \":PersonName\",         {             \":BasicAddress\": [                 \":Street\",                 \":City\"             ]         }     ] } ~~~ Note that the *BasicAddress* has sub-fields for the *City* and *Street*. The response includes a description of the template as well as its nodeId. Response ~~~ {     ...     \"nodeId\": \"00000000674AF75DB0F4F1DF9713E09296687718E8157EA3\",     \"name\": \"PersonProfile\",     \"memberIds\": [         \"000000000F1CF39B817D2845799BA7A143C5772336730EE6\",         {             \"0000000021C7084D540A7029E7A7E0ED036C7F466B252F9A\": [                 \"00000000D3D5AF38B916AF963CF25ADCAE74ABFD11C3E583\",                 \"00000000DDD315F7078EDEBC403D7C22C9436524F012C67B\"             ]         }     ] } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_template(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateTemplateRequest create_template_request:
        :return: CreateTemplateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_template_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_template_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_template_with_http_info(self, **kwargs):  # noqa: E501
        """Create Template  # noqa: E501

        Templates are collections of field types. They are used in the `/read` and `/write` endpoints for reading and writing data in bulk.  The template *name* must be unique within the associated *login*.  #### Example In this example we have created a set of fields that define a Person's name, and basic street address with street and city parts. The responses from the creation of the fields: ~~~ {     ...     \"branch\": false,     \"uniqueByParent\": true,     \"nodeId\": \"000000008BFE6BB9A2A3F80F23DC6E738470F24B95E5102A\",     \"name\": \"PersonName\" } {     ...     \"branch\": true,     \"uniqueByParent\": true,     \"nodeId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA\",     \"name\": \"BasicAddress\" } {     ...     \"branch\": false,     \"uniqueByParent\": true,     \"nodeId\": \"0000000095E0F6B9F5480FD75DA9520E480AD3E89DC35D9A\",     \"name\": \"Street\" } {     ...     \"branch\": false,     \"uniqueByParent\": true,     \"nodeId\": \"00000000F6EFF0C416BE603531C8BA77C36E8A9B29368FB5\",     \"name\": \"City\" } ~~~ A template is created with the fields. ~~~ POST /createtemplate {     ...     \"name\": \"PersonProfile\",     \"memberIds\": [         \":PersonName\",         {             \":BasicAddress\": [                 \":Street\",                 \":City\"             ]         }     ] } ~~~ Note that the *BasicAddress* has sub-fields for the *City* and *Street*. The response includes a description of the template as well as its nodeId. Response ~~~ {     ...     \"nodeId\": \"00000000674AF75DB0F4F1DF9713E09296687718E8157EA3\",     \"name\": \"PersonProfile\",     \"memberIds\": [         \"000000000F1CF39B817D2845799BA7A143C5772336730EE6\",         {             \"0000000021C7084D540A7029E7A7E0ED036C7F466B252F9A\": [                 \"00000000D3D5AF38B916AF963CF25ADCAE74ABFD11C3E583\",                 \"00000000DDD315F7078EDEBC403D7C22C9436524F012C67B\"             ]         }     ] } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_template_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateTemplateRequest create_template_request:
        :return: CreateTemplateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'create_template_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_template" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/createtemplate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateTemplateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete(self, **kwargs):  # noqa: E501
        """Deleting  # noqa: E501

        For deleting information data.  The nodeId must be an entity and the template is used to find the information nodes to delete relative to the entity.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param DeleteRequest delete_request:
        :return: DeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_with_http_info(**kwargs)  # noqa: E501
            return data

    def delete_with_http_info(self, **kwargs):  # noqa: E501
        """Deleting  # noqa: E501

        For deleting information data.  The nodeId must be an entity and the template is used to find the information nodes to delete relative to the entity.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param DeleteRequest delete_request:
        :return: DeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'delete_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/delete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeleteResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_node(self, **kwargs):  # noqa: E501
        """Delete Node  # noqa: E501

        Delete marks a node as deleted. It will no longer be listable via the /describe endpoint. The data is not actually deleted. To remove data, see Obliterate.  #### Example In this example, we create and then delete an information node. The information node has field type with Factern Id and parent entity having Factern Ids `0000000016270565667CE604DD4DF499C2A31FF6D2072FD7` and `00000000571749C62247EC65D43151C296366C4EF48658A9`, respectively. ~~~ POST /createinformation {     ...     \"parentId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\",     \"fieldId\": \":Street\",     \"data\": \"Inverness Terrace\" } ~~~ The information node's Factern Id is returned. ~~~ Response {     ...     \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\",     ... } ~~~ We list the information nodes of the entity filtering results using the field type. ~~~ POST /describe {     ...     \"nodeId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\",     \"listChildren\": {         \"factType\": \"Information\",         \"fieldId\": \":Street\"     } } ~~~ The response ~~~ {     ...     \"children\": [{         \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\",         ...     }] } ~~~ Now we delete the previously created information node. ~~~ POST /deletenode {     ...     \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\" } ~~~ The same describe as before is invoked and now returns an empty list. Response ~~~ {     ...     \"children\": [] } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_node(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param NodeIdRequest node_id_request:
        :return: StandardNodeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_node_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_node_with_http_info(**kwargs)  # noqa: E501
            return data

    def delete_node_with_http_info(self, **kwargs):  # noqa: E501
        """Delete Node  # noqa: E501

        Delete marks a node as deleted. It will no longer be listable via the /describe endpoint. The data is not actually deleted. To remove data, see Obliterate.  #### Example In this example, we create and then delete an information node. The information node has field type with Factern Id and parent entity having Factern Ids `0000000016270565667CE604DD4DF499C2A31FF6D2072FD7` and `00000000571749C62247EC65D43151C296366C4EF48658A9`, respectively. ~~~ POST /createinformation {     ...     \"parentId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\",     \"fieldId\": \":Street\",     \"data\": \"Inverness Terrace\" } ~~~ The information node's Factern Id is returned. ~~~ Response {     ...     \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\",     ... } ~~~ We list the information nodes of the entity filtering results using the field type. ~~~ POST /describe {     ...     \"nodeId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\",     \"listChildren\": {         \"factType\": \"Information\",         \"fieldId\": \":Street\"     } } ~~~ The response ~~~ {     ...     \"children\": [{         \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\",         ...     }] } ~~~ Now we delete the previously created information node. ~~~ POST /deletenode {     ...     \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\" } ~~~ The same describe as before is invoked and now returns an empty list. Response ~~~ {     ...     \"children\": [] } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_node_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param NodeIdRequest node_id_request:
        :return: StandardNodeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'node_id_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_node" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/deletenode', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StandardNodeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def describe(self, **kwargs):  # noqa: E501
        """Describe  # noqa: E501

        Describe is used to describe nodes and statements as well as optionally the children of nodes and statements. List includes arguments for allowing paging in the case of large numbers of children. To receive associated statements of a node, the field type of the statement must be explicitly added via the filter.  #### Example In this example, we create several information nodes under an entity, and then describe the information nodes. ~~~ POST /createinformation {     ...     \"parentId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\",     \"fieldId\": \":Street\",     \"data\": \"Inverness Terrace\" } ~~~ ~~~ POST /createinformation {     ...     \"parentId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\",     \"fieldId\": \":Street\",     \"data\": \"Gloucester Place\" } ~~~ ~~~ POST /createinformation {     ...     \"parentId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\",     \"fieldId\": \":Street\",     \"data\": \"Baker Street\" } ~~~ We describe the entity. ~~~ POST /describe {     ...     \"nodeId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\" } ~~~ The response includes only a description of the entity ~~~ {     \"nodeId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\",     \"factType\": \"Entity\",     ... } ~~~ We list the information nodes of the entity filtering results using the field type. ~~~ POST /describe {     ...     \"nodeId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\",     \"listChildren\": {         \"factType\": \"Information\",         \"fieldId\": \":Street\"     } } ~~~ The response includes a description of the entity and the information nodes having the given field type. ~~~ {     \"nodeId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\",     \"factType\": \"Entity\",     ...     \"children\": [{         \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\",         ...     },     {         \"nodeId\": \"00000000A2019243964B5E357392DC5C0A5DEF074F3ED504\",         ...     }] } ~~~ We can also describe the entity with generateTemplate=true. ~~~ POST /describe {     \"nodeId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\",     \"generateTemplate\": true } ~~~ The response will include a template that describes the fields of the information nodes under it. ~~~ {     \"nodeId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\",     \"factType\": \"Entity\",     \"memberIds\": [\"<nodeId of Street field type>\"]     ... } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.describe(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param DescribeRequest describe_request:
        :return: DescribeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.describe_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.describe_with_http_info(**kwargs)  # noqa: E501
            return data

    def describe_with_http_info(self, **kwargs):  # noqa: E501
        """Describe  # noqa: E501

        Describe is used to describe nodes and statements as well as optionally the children of nodes and statements. List includes arguments for allowing paging in the case of large numbers of children. To receive associated statements of a node, the field type of the statement must be explicitly added via the filter.  #### Example In this example, we create several information nodes under an entity, and then describe the information nodes. ~~~ POST /createinformation {     ...     \"parentId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\",     \"fieldId\": \":Street\",     \"data\": \"Inverness Terrace\" } ~~~ ~~~ POST /createinformation {     ...     \"parentId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\",     \"fieldId\": \":Street\",     \"data\": \"Gloucester Place\" } ~~~ ~~~ POST /createinformation {     ...     \"parentId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\",     \"fieldId\": \":Street\",     \"data\": \"Baker Street\" } ~~~ We describe the entity. ~~~ POST /describe {     ...     \"nodeId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\" } ~~~ The response includes only a description of the entity ~~~ {     \"nodeId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\",     \"factType\": \"Entity\",     ... } ~~~ We list the information nodes of the entity filtering results using the field type. ~~~ POST /describe {     ...     \"nodeId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\",     \"listChildren\": {         \"factType\": \"Information\",         \"fieldId\": \":Street\"     } } ~~~ The response includes a description of the entity and the information nodes having the given field type. ~~~ {     \"nodeId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\",     \"factType\": \"Entity\",     ...     \"children\": [{         \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\",         ...     },     {         \"nodeId\": \"00000000A2019243964B5E357392DC5C0A5DEF074F3ED504\",         ...     }] } ~~~ We can also describe the entity with generateTemplate=true. ~~~ POST /describe {     \"nodeId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\",     \"generateTemplate\": true } ~~~ The response will include a template that describes the fields of the information nodes under it. ~~~ {     \"nodeId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\",     \"factType\": \"Entity\",     \"memberIds\": [\"<nodeId of Street field type>\"]     ... } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.describe_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param DescribeRequest describe_request:
        :return: DescribeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'describe_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method describe" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/describe', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DescribeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def history(self, **kwargs):  # noqa: E501
        """History  # noqa: E501

        History runs the replace statements up and down the chain to return the full history of a node. The node given can be any node in the chain of replacements. Giving any point from \"version 1\" to \"version n\" nodeId will produce the same result.  The node list returned is not guaranteed to be ordered but does provide a `sequenceNumber` property which you can sort by to find the first/last or in between version. Sort ascending for old to new, descending for new to old.  History on non-info nodes may return a list of two versions if, and only if, the non-info node has been deleted. This is because *replace* is not exposed for non-info nodes at this time.  #### Example In this example, we create and replace an information node, and then list the information versions. The information has field type and parent entity having Factern Ids `0000000016270565667CE604DD4DF499C2A31FF6D2072FD7` and `00000000571749C62247EC65D43151C296366C4EF48658A9`, respectively. ~~~ POST /createinformation {     ...     \"parentId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\",     \"fieldId\": \"0000000016270565667CE604DD4DF499C2A31FF6D2072FD7\",     \"data\": \"Alice\" } ~~~ The information node's Factern Id is returned. ~~~ Response {     ...     \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\",     ... } ~~~ Now we replace the information node. ~~~ POST /replaceinformation {     ...     \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\",     \"data\": \"Allison\" } ~~~ The replacement information node's Factern Id is returned. ~~~ Response {     ...     \"nodeId\": \"000000007611AD504DBF600078DF929DD98EAE4787B4D87A\",     ... } ~~~ The history of the information node is called, and shows the Factern Ids of the original and replacement. ~~~ POST /history {     ...     \"nodeId\": \"000000007611AD504DBF600078DF929DD98EAE4787B4D87A\" } ~~~ Response ~~~ {     \"nodes\": [{         \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\",         \"sequenceNo\": \"0\"         ...     },     {         \"nodeId\": \"000000007611AD504DBF600078DF929DD98EAE4787B4D87A\",         \"sequenceNo\": \"1\"         ...     }] } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.history(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param NodeIdRequest node_id_request:
        :return: NodeListing
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.history_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.history_with_http_info(**kwargs)  # noqa: E501
            return data

    def history_with_http_info(self, **kwargs):  # noqa: E501
        """History  # noqa: E501

        History runs the replace statements up and down the chain to return the full history of a node. The node given can be any node in the chain of replacements. Giving any point from \"version 1\" to \"version n\" nodeId will produce the same result.  The node list returned is not guaranteed to be ordered but does provide a `sequenceNumber` property which you can sort by to find the first/last or in between version. Sort ascending for old to new, descending for new to old.  History on non-info nodes may return a list of two versions if, and only if, the non-info node has been deleted. This is because *replace* is not exposed for non-info nodes at this time.  #### Example In this example, we create and replace an information node, and then list the information versions. The information has field type and parent entity having Factern Ids `0000000016270565667CE604DD4DF499C2A31FF6D2072FD7` and `00000000571749C62247EC65D43151C296366C4EF48658A9`, respectively. ~~~ POST /createinformation {     ...     \"parentId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\",     \"fieldId\": \"0000000016270565667CE604DD4DF499C2A31FF6D2072FD7\",     \"data\": \"Alice\" } ~~~ The information node's Factern Id is returned. ~~~ Response {     ...     \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\",     ... } ~~~ Now we replace the information node. ~~~ POST /replaceinformation {     ...     \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\",     \"data\": \"Allison\" } ~~~ The replacement information node's Factern Id is returned. ~~~ Response {     ...     \"nodeId\": \"000000007611AD504DBF600078DF929DD98EAE4787B4D87A\",     ... } ~~~ The history of the information node is called, and shows the Factern Ids of the original and replacement. ~~~ POST /history {     ...     \"nodeId\": \"000000007611AD504DBF600078DF929DD98EAE4787B4D87A\" } ~~~ Response ~~~ {     \"nodes\": [{         \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\",         \"sequenceNo\": \"0\"         ...     },     {         \"nodeId\": \"000000007611AD504DBF600078DF929DD98EAE4787B4D87A\",         \"sequenceNo\": \"1\"         ...     }] } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.history_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param NodeIdRequest node_id_request:
        :return: NodeListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'node_id_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method history" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/history', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodeListing',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def label(self, **kwargs):  # noqa: E501
        """Label a Node  # noqa: E501

        #### Example  We create a label list representing the confirmation status of an information node's data.  ~~~  POST /createlabellist {     ...     \"name\": \"ConfirmationStatus\",     \"members\": [         \"Unconfirmed\",         \"Rejected\",         \"Confirmed\"     ] }  ~~~  Response  ~~~  {     ...     \"nodeId\": \"00000000C125606D13DCE6AD6A1D2B6969C2863C4FAB050B\",     \"members\": [{         ...         \"name\": \"Confirmed\",         \"nodeId\": \"00000000A1AF37B270DE7EED4EE881021B678D4D8518D4ED\"     },...] }  ~~~  We now label an existing information node with Factern Id `00000000FB76E443E8F923ED5B43CFEF7233F3E278836D70` as Confirmed by using the Factern Id of the Confirmed label.  ~~~  POST /label {     \"targetNodeId\": \"00000000FB76E443E8F923ED5B43CFEF7233F3E278836D70\",     \"labelId\": \"00000000A1AF37B270DE7EED4EE881021B678D4D8518D4ED\" }  ~~~  We could also use the FRN (or short FRN) of the Confirmed label to do the same thing.  ~~~  POST /label {     \"targetNodeId\": \"00000000FB76E443E8F923ED5B43CFEF7233F3E278836D70\",     \"labelId\": \":ConfirmationStatus/Confirmed\" }  ~~~  Finally we list the labels of the information node filtering results using the ConfirmationStatus label list.  ~~~  POST /describe {     ...     \"nodeId\": \"00000000FB76E443E8F923ED5B43CFEF7233F3E278836D70\",     \"listChildren\": {         \"factType\": \"Label\",         \"labelListId\": \":ConfirmationStatus\"     } }  ~~~  Response  ~~~  {     ...     \"children\": [{         \"targetNodeId\": \"00000000FB76E443E8F923ED5B43CFEF7233F3E278836D70\",         \"memberId\": \"00000000A1AF37B270DE7EED4EE881021B678D4D8518D4ED\"     }] }  ~~~  Showing that the information node was labelled with the label corresponding to the Confirmed status.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.label(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param AddLabelRequest add_label_request:
        :return: AddLabelResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.label_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.label_with_http_info(**kwargs)  # noqa: E501
            return data

    def label_with_http_info(self, **kwargs):  # noqa: E501
        """Label a Node  # noqa: E501

        #### Example  We create a label list representing the confirmation status of an information node's data.  ~~~  POST /createlabellist {     ...     \"name\": \"ConfirmationStatus\",     \"members\": [         \"Unconfirmed\",         \"Rejected\",         \"Confirmed\"     ] }  ~~~  Response  ~~~  {     ...     \"nodeId\": \"00000000C125606D13DCE6AD6A1D2B6969C2863C4FAB050B\",     \"members\": [{         ...         \"name\": \"Confirmed\",         \"nodeId\": \"00000000A1AF37B270DE7EED4EE881021B678D4D8518D4ED\"     },...] }  ~~~  We now label an existing information node with Factern Id `00000000FB76E443E8F923ED5B43CFEF7233F3E278836D70` as Confirmed by using the Factern Id of the Confirmed label.  ~~~  POST /label {     \"targetNodeId\": \"00000000FB76E443E8F923ED5B43CFEF7233F3E278836D70\",     \"labelId\": \"00000000A1AF37B270DE7EED4EE881021B678D4D8518D4ED\" }  ~~~  We could also use the FRN (or short FRN) of the Confirmed label to do the same thing.  ~~~  POST /label {     \"targetNodeId\": \"00000000FB76E443E8F923ED5B43CFEF7233F3E278836D70\",     \"labelId\": \":ConfirmationStatus/Confirmed\" }  ~~~  Finally we list the labels of the information node filtering results using the ConfirmationStatus label list.  ~~~  POST /describe {     ...     \"nodeId\": \"00000000FB76E443E8F923ED5B43CFEF7233F3E278836D70\",     \"listChildren\": {         \"factType\": \"Label\",         \"labelListId\": \":ConfirmationStatus\"     } }  ~~~  Response  ~~~  {     ...     \"children\": [{         \"targetNodeId\": \"00000000FB76E443E8F923ED5B43CFEF7233F3E278836D70\",         \"memberId\": \"00000000A1AF37B270DE7EED4EE881021B678D4D8518D4ED\"     }] }  ~~~  Showing that the information node was labelled with the label corresponding to the Confirmed status.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.label_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param AddLabelRequest add_label_request:
        :return: AddLabelResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'add_label_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method label" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/label', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AddLabelResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def obliterate(self, **kwargs):  # noqa: E501
        """Obliterating Information Nodes  # noqa: E501

        Obliterate removes the data associated with a node. Only information nodes can be targeted by obliterate. After a call to obliterate you will not be able to retrieve the data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.obliterate(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param NodeIdRequest node_id_request:
        :return: StandardNodeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.obliterate_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.obliterate_with_http_info(**kwargs)  # noqa: E501
            return data

    def obliterate_with_http_info(self, **kwargs):  # noqa: E501
        """Obliterating Information Nodes  # noqa: E501

        Obliterate removes the data associated with a node. Only information nodes can be targeted by obliterate. After a call to obliterate you will not be able to retrieve the data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.obliterate_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param NodeIdRequest node_id_request:
        :return: StandardNodeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'node_id_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method obliterate" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/obliterate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StandardNodeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def permission(self, **kwargs):  # noqa: E501
        """Create Permission  # noqa: E501

        By default, a login's data is not accessible in any way by any other login. It is only by creating permissions that a login can make its data accessible. Permissions can either be created with an explicit policy, or can be created asynchronously via an external interface. In either case, a policy can always have an expiry. In the asynchronous case, the policy is only created as each attempted access occurs.    Permissions specified with a *requestInterfaceId* are called *Requestable Permissions*. If an agent otherwise matches the permission policy, then the status code returned when reading the target node will be the special status code 477. The `/requestpermission` endpoint can be used for requesting the permission be granted.    In the case that a node has more than one associated *Requestable Permission* the most specific matching requestable permission is used. If there is more than one such requestable permission, then the requestable permission used is arbitrary.    Note that requestable permissions only matter if an agent is not otherwise allowed by non-requestable permissions.  #### Example In this example, we grant login with Factern Id `00000000301D1F22157CE46BAAB422C13F0F368218027D50` using application with Factern Id `00000000DAB38B0E3390E09DFF52EF2AED6833F11BBC8896` to be able to read information node with Factern Id `000000001ADE8A80023B7E090594227905A5D8DC5C1212A0` ~~~ POST /permission {     \"targetNodeId\": \"00000000FCDF978BA9BFAE5D1DEC365B59A249A6B01E3987\",     \"policy\": {         \"effect\": \"Allow\",         \"granteeId\": \"00000000301D1F22157CE46BAAB422C13F0F368218027D50\",         \"applicationId\": \"00000000DAB38B0E3390E09DFF52EF2AED6833F11BBC8896\",         \"actions\": [\"Read\"]     } } ~~~ #### Example In this example, an `application` is not specified so login with Factern Id `00000000301D1F22157CE46BAAB422C13F0F368218027D50` can use any application to read information node with Factern Id `000000001ADE8A80023B7E090594227905A5D8DC5C1212A0` ~~~ POST /permission {     \"targetNodeId\": \"00000000FCDF978BA9BFAE5D1DEC365B59A249A6B01E3987\",     \"policy\": {         \"effect\": \"Allow\",         \"granteeId\": \"00000000301D1F22157CE46BAAB422C13F0F368218027D50\",         \"actions\": [\"Read\"]     } } ~~~ #### Example In this example, a `grantee` is not specified so any login using application with Factern Id `00000000DAB38B0E3390E09DFF52EF2AED6833F11BBC8896` will be able to read information node with Factern Id `000000001ADE8A80023B7E090594227905A5D8DC5C1212A0` ~~~ POST /permission {     \"targetNodeId\": \"00000000FCDF978BA9BFAE5D1DEC365B59A249A6B01E3987\",     \"policy\": {         \"effect\": \"Allow\",         \"applicationId\": \"00000000DAB38B0E3390E09DFF52EF2AED6833F11BBC8896\",         \"actions\": [\"Read\"]     } } ~~~ #### Example In this example, no `grantee` or `application` is specified so any login using any will be able to read information node with Factern Id `000000001ADE8A80023B7E090594227905A5D8DC5C1212A0` ~~~ POST /permission {     \"targetNodeId\": \"00000000FCDF978BA9BFAE5D1DEC365B59A249A6B01E3987\",     \"policy\": {         \"effect\": \"Allow\",         \"actions\": [\"Read\"]     } } ~~~ #### Example In this example, we grant login with Factern Id `00000000301D1F22157CE46BAAB422C13F0F368218027D50` to be able to request *Read* permission on information node with Factern Id `000000001ADE8A80023B7E090594227905A5D8DC5C1212A0`. ~~~ POST /permission {     \"targetNodeId\": \"00000000FCDF978BA9BFAE5D1DEC365B59A249A6B01E3987\",     \"policy\": {         \"effect\": \"Allow\",         \"granteeId\": \"00000000301D1F22157CE46BAAB422C13F0F368218027D50\",         \"requestInterfaceId\": \"00000000C4F8891E18CED1C62ACE2ABC2BC0BBF8C6DFBFCC\",         \"actions\": [\"Read\"]     } } ~~~ #### Example In this example, we grant application with Factern Id `00000000DAB38B0E3390E09DFF52EF2AED6833F11BBC8896` permission to be used with login with Factern Id `000000001ADE8A80023B7E090594227905A5D8DC5C1212A0`. This type of permission is necessary to allow this login/application pairing on any API request. ~~~ POST /permission {     \"targetNodeId\": \"000000001ADE8A80023B7E090594227905A5D8DC5C1212A0\",     \"policy\": {         \"effect\": \"Allow\",         \"applicationId\": \"00000000DAB38B0E3390E09DFF52EF2AED6833F11BBC8896\",         \"actions\": [\"Application\"]     } } ~~~ #### Example In this example, we grant login with Factern Id `00000000DAB38B0E3390E09DFF52EF2AED6833F11BBC8896` permission to be represent entity with Factern Id `000000001ADE8A80023B7E090594227905A5D8DC5C1212A0`. This type of permission is necessary to allow this login/representing pairing on any API request. ~~~ POST /permission {     \"targetNodeId\": \"000000001ADE8A80023B7E090594227905A5D8DC5C1212A0\",     \"policy\": {         \"effect\": \"Allow\",         \"granteeId\": \"00000000DAB38B0E3390E09DFF52EF2AED6833F11BBC8896\",         \"actions\": [\"Act\"]     } } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.permission(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreatePermissionRequest create_permission_request:
        :return: CreatePermissionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.permission_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.permission_with_http_info(**kwargs)  # noqa: E501
            return data

    def permission_with_http_info(self, **kwargs):  # noqa: E501
        """Create Permission  # noqa: E501

        By default, a login's data is not accessible in any way by any other login. It is only by creating permissions that a login can make its data accessible. Permissions can either be created with an explicit policy, or can be created asynchronously via an external interface. In either case, a policy can always have an expiry. In the asynchronous case, the policy is only created as each attempted access occurs.    Permissions specified with a *requestInterfaceId* are called *Requestable Permissions*. If an agent otherwise matches the permission policy, then the status code returned when reading the target node will be the special status code 477. The `/requestpermission` endpoint can be used for requesting the permission be granted.    In the case that a node has more than one associated *Requestable Permission* the most specific matching requestable permission is used. If there is more than one such requestable permission, then the requestable permission used is arbitrary.    Note that requestable permissions only matter if an agent is not otherwise allowed by non-requestable permissions.  #### Example In this example, we grant login with Factern Id `00000000301D1F22157CE46BAAB422C13F0F368218027D50` using application with Factern Id `00000000DAB38B0E3390E09DFF52EF2AED6833F11BBC8896` to be able to read information node with Factern Id `000000001ADE8A80023B7E090594227905A5D8DC5C1212A0` ~~~ POST /permission {     \"targetNodeId\": \"00000000FCDF978BA9BFAE5D1DEC365B59A249A6B01E3987\",     \"policy\": {         \"effect\": \"Allow\",         \"granteeId\": \"00000000301D1F22157CE46BAAB422C13F0F368218027D50\",         \"applicationId\": \"00000000DAB38B0E3390E09DFF52EF2AED6833F11BBC8896\",         \"actions\": [\"Read\"]     } } ~~~ #### Example In this example, an `application` is not specified so login with Factern Id `00000000301D1F22157CE46BAAB422C13F0F368218027D50` can use any application to read information node with Factern Id `000000001ADE8A80023B7E090594227905A5D8DC5C1212A0` ~~~ POST /permission {     \"targetNodeId\": \"00000000FCDF978BA9BFAE5D1DEC365B59A249A6B01E3987\",     \"policy\": {         \"effect\": \"Allow\",         \"granteeId\": \"00000000301D1F22157CE46BAAB422C13F0F368218027D50\",         \"actions\": [\"Read\"]     } } ~~~ #### Example In this example, a `grantee` is not specified so any login using application with Factern Id `00000000DAB38B0E3390E09DFF52EF2AED6833F11BBC8896` will be able to read information node with Factern Id `000000001ADE8A80023B7E090594227905A5D8DC5C1212A0` ~~~ POST /permission {     \"targetNodeId\": \"00000000FCDF978BA9BFAE5D1DEC365B59A249A6B01E3987\",     \"policy\": {         \"effect\": \"Allow\",         \"applicationId\": \"00000000DAB38B0E3390E09DFF52EF2AED6833F11BBC8896\",         \"actions\": [\"Read\"]     } } ~~~ #### Example In this example, no `grantee` or `application` is specified so any login using any will be able to read information node with Factern Id `000000001ADE8A80023B7E090594227905A5D8DC5C1212A0` ~~~ POST /permission {     \"targetNodeId\": \"00000000FCDF978BA9BFAE5D1DEC365B59A249A6B01E3987\",     \"policy\": {         \"effect\": \"Allow\",         \"actions\": [\"Read\"]     } } ~~~ #### Example In this example, we grant login with Factern Id `00000000301D1F22157CE46BAAB422C13F0F368218027D50` to be able to request *Read* permission on information node with Factern Id `000000001ADE8A80023B7E090594227905A5D8DC5C1212A0`. ~~~ POST /permission {     \"targetNodeId\": \"00000000FCDF978BA9BFAE5D1DEC365B59A249A6B01E3987\",     \"policy\": {         \"effect\": \"Allow\",         \"granteeId\": \"00000000301D1F22157CE46BAAB422C13F0F368218027D50\",         \"requestInterfaceId\": \"00000000C4F8891E18CED1C62ACE2ABC2BC0BBF8C6DFBFCC\",         \"actions\": [\"Read\"]     } } ~~~ #### Example In this example, we grant application with Factern Id `00000000DAB38B0E3390E09DFF52EF2AED6833F11BBC8896` permission to be used with login with Factern Id `000000001ADE8A80023B7E090594227905A5D8DC5C1212A0`. This type of permission is necessary to allow this login/application pairing on any API request. ~~~ POST /permission {     \"targetNodeId\": \"000000001ADE8A80023B7E090594227905A5D8DC5C1212A0\",     \"policy\": {         \"effect\": \"Allow\",         \"applicationId\": \"00000000DAB38B0E3390E09DFF52EF2AED6833F11BBC8896\",         \"actions\": [\"Application\"]     } } ~~~ #### Example In this example, we grant login with Factern Id `00000000DAB38B0E3390E09DFF52EF2AED6833F11BBC8896` permission to be represent entity with Factern Id `000000001ADE8A80023B7E090594227905A5D8DC5C1212A0`. This type of permission is necessary to allow this login/representing pairing on any API request. ~~~ POST /permission {     \"targetNodeId\": \"000000001ADE8A80023B7E090594227905A5D8DC5C1212A0\",     \"policy\": {         \"effect\": \"Allow\",         \"granteeId\": \"00000000DAB38B0E3390E09DFF52EF2AED6833F11BBC8896\",         \"actions\": [\"Act\"]     } } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.permission_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreatePermissionRequest create_permission_request:
        :return: CreatePermissionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'create_permission_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method permission" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/permission', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreatePermissionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read(self, **kwargs):  # noqa: E501
        """Reading  # noqa: E501

        For reading information data.  The nodeId must be an entity and the template is used to find and return information nodes relative to the entity.  #### Example  In this example, we read information nodes previously written in the `/write` examples.  ~~~  POST /read {     \"templateId\": \":PersonProfile\",     \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\" }  ~~~  Response  ~~~  {   \"items\": [     {       \"status\": 200,       \"readItem\": {         \"fieldId\": \"000000008BFE6BB9A2A3F80F23DC6E738470F24B95E5102A\",         \"nodeId\": \"0000000043F912B92911FFE2A52E31066E8B653D3F7E8DE7\",         \"data\": \"Bob Watson\"       }     },     {       \"status\": 200,       \"readItem\": {         \"fieldId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA\",         \"nodeId\": \"000000002B3CABC1694B029442124526A5B6137E9EABCAD1v\",         \"children\": [           {             \"status\": 200,             \"readItem\": {               \"fieldId\": \"0000000095E0F6B9F5480FD75DA9520E480AD3E89DC35D9A\",               \"nodeId\": \"0000000099A8B1E3605B77F3EDB62B475DE739646041DFB9\",               \"data\": \"Inverness Terrace\"             }           },           {             \"status\": 200,             \"readItem\": {               \"fieldId\": \"00000000F6EFF0C416BE603531C8BA77C36E8A9B29368FB5\",               \"nodeId\": \"00000000F76AF7DFD004F6C321636CE9A53F62B05F009BFA\",               \"data\": \"London\"             }           }         ]       }     }   ] }  ~~~  #### Example  In this example, we read information nodes with callback interface we created previously. If a callback is specified, then we use the addData endpoint of the callback interface to receive the result of the read.  ~~~  POST /read {     \"templateId\": \":PersonProfile\",     \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\",     \"callback\": \"00000000C4F8891E18CED1C62ACE2ABC2BC0BBF8C6DFBFCC\" }  ~~~  Response  ~~~  {   \"responseId\": \"000000004AEAD52FCD523113931573071C0B23C33B70E5D9\",   \"items\": [] }  ~~~  A request with a callback returns immediately including a unique context id, while the read onto the callback interface occurs asynchronously.   #### Example  In this example, rather than specifying a templateId, we specify an inline template. We want to read the person's name and city but not street. We also specify another field, `00000000B6BEDDE768D3202057EF824A1923E7FCD26FD74F` for a person's house number. In the person's data, however, the house number was not written, so nothing is returned for that field.  ~~~  POST /read {     \"template\": [         \":PersonName\",         {             \":BasicAddress\": [                 \":Street\",                 \":City\"             ]         }],     \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\" }  ~~~  Response  ~~~  {   \"items\": [     {       \"status\": 200,       \"readItem\": {         \"fieldId\": \"000000008BFE6BB9A2A3F80F23DC6E738470F24B95E5102A\",         \"nodeId\": \"0000000043F912B92911FFE2A52E31066E8B653D3F7E8DE7\",         \"data\": \"Bob Watson\"       }     },     {       \"status\": 200,       \"readItem\": {         \"fieldId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA\",         \"nodeId\": \"000000002B3CABC1694B029442124526A5B6137E9EABCAD1v\",         \"children\": [           {             \"status\": 200,             \"readItem\": {               \"fieldId\": \"00000000F6EFF0C416BE603531C8BA77C36E8A9B29368FB5\",               \"nodeId\": \"00000000F76AF7DFD004F6C321636CE9A53F62B05F009BFA\",               \"data\": \"London\"             }           },           {             \"status\": 404,             \"readItem\": {               \"fieldId\": \"0000000095E0F6B9F5480FD75DA9520E480AD3E89DC35D9A\"             }           }         ]       }     }   ] }  ~~~  #### Example  In the previous example, we saw that a 404 was returned for the house number field since the data had not yet been written. However, if we specify a `defaultStorageId` when making the request, then an information node will be created and an attempt will be made to fetch the data. It is the responsibility of the interface given by `defaultStorageId` to determine the data that should be returned.  ~~~  POST /read {     \"template\": [         \":PersonName\",         {             \":BasicAddress\": [                 \":Street\",                 \":City\"             ]         }],     \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\",     \"defaultStorageId\": \":LazyLoadInterface\" }  ~~~  We could also create a template with a `defaultStorageId`, in which case all reads will behave like the above request.  ~~~  POST /createtemplate {     ...     \"name\": \"PersonProfile\",     \"defaultStorageId\": \":LazyLoadInterface\",     \"memberIds\": [         \":PersonName\",         {             \":BasicAddress\": [                 \":Street\",                 \":City\"             ]         }     ] }  ~~~  #### Example  In this example, we demonstrate the behaviour when fields are not *uniqueByParent. In this case, all fields are *uniqueByParent* except *ClientProfile*.  ~~~  POST /read {     \"template\": [         {\":ClientList\": [             {\":ClientProfile\": [                 {\":BasicAddress\": [                     \":Street\"                 ]}             ]}         ]}     ],     \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\" }  ~~~  Response  ~~~  {   \"items\": [     {       \"status\": 200,       \"readItem\": {         \"fieldId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA\",         \"nodeId\": \"000000002B3CABC1694B029442124526A5B6137E9EABCAD1\",         \"children\": [           {             \"readItem\": {               \"fieldId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\",               \"nodes\": [                 {                   \"status\": 200,                   \"readItem\": {                     \"fieldId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA\",                     \"nodeId\": \"000000002B3CABC1694B029442124526A5B6137E9EABCAD1\",                     \"children\": [                       {                         \"status\": 200,                         \"readItem\": {                           \"fieldId\": \"0000000095E0F6B9F5480FD75DA9520E480AD3E89DC35D9A\",                           \"nodeId\": \"0000000099A8B1E3605B77F3EDB62B475DE739646041DFB9\",                           \"data\": \"Inverness Terrace\"                         }                       }                     ]                   }                 },                 {                   \"status\": 200,                   \"readItem\": {                     \"fieldId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA\",                     \"nodeId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\",                     \"children\": [                       {                         \"status\": 200,                         \"readItem\": {                           \"fieldId\": \"0000000095E0F6B9F5480FD75DA9520E480AD3E89DC35D9A\",                           \"nodeId\": \"0000000016270565667CE604DD4DF499C2A31FF6D2072FD7\",                           \"data\": \"Baker Street\"                         }                       }                     ]                   }                 }               ]             }           }         ]       }     }   ] }  ~~~  Data returned for non-*uniqueByParent* fields is contained under a *nodes* property within the *readItem*.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.read(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param ReadRequest read_request:
        :return: ReadResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.read_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.read_with_http_info(**kwargs)  # noqa: E501
            return data

    def read_with_http_info(self, **kwargs):  # noqa: E501
        """Reading  # noqa: E501

        For reading information data.  The nodeId must be an entity and the template is used to find and return information nodes relative to the entity.  #### Example  In this example, we read information nodes previously written in the `/write` examples.  ~~~  POST /read {     \"templateId\": \":PersonProfile\",     \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\" }  ~~~  Response  ~~~  {   \"items\": [     {       \"status\": 200,       \"readItem\": {         \"fieldId\": \"000000008BFE6BB9A2A3F80F23DC6E738470F24B95E5102A\",         \"nodeId\": \"0000000043F912B92911FFE2A52E31066E8B653D3F7E8DE7\",         \"data\": \"Bob Watson\"       }     },     {       \"status\": 200,       \"readItem\": {         \"fieldId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA\",         \"nodeId\": \"000000002B3CABC1694B029442124526A5B6137E9EABCAD1v\",         \"children\": [           {             \"status\": 200,             \"readItem\": {               \"fieldId\": \"0000000095E0F6B9F5480FD75DA9520E480AD3E89DC35D9A\",               \"nodeId\": \"0000000099A8B1E3605B77F3EDB62B475DE739646041DFB9\",               \"data\": \"Inverness Terrace\"             }           },           {             \"status\": 200,             \"readItem\": {               \"fieldId\": \"00000000F6EFF0C416BE603531C8BA77C36E8A9B29368FB5\",               \"nodeId\": \"00000000F76AF7DFD004F6C321636CE9A53F62B05F009BFA\",               \"data\": \"London\"             }           }         ]       }     }   ] }  ~~~  #### Example  In this example, we read information nodes with callback interface we created previously. If a callback is specified, then we use the addData endpoint of the callback interface to receive the result of the read.  ~~~  POST /read {     \"templateId\": \":PersonProfile\",     \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\",     \"callback\": \"00000000C4F8891E18CED1C62ACE2ABC2BC0BBF8C6DFBFCC\" }  ~~~  Response  ~~~  {   \"responseId\": \"000000004AEAD52FCD523113931573071C0B23C33B70E5D9\",   \"items\": [] }  ~~~  A request with a callback returns immediately including a unique context id, while the read onto the callback interface occurs asynchronously.   #### Example  In this example, rather than specifying a templateId, we specify an inline template. We want to read the person's name and city but not street. We also specify another field, `00000000B6BEDDE768D3202057EF824A1923E7FCD26FD74F` for a person's house number. In the person's data, however, the house number was not written, so nothing is returned for that field.  ~~~  POST /read {     \"template\": [         \":PersonName\",         {             \":BasicAddress\": [                 \":Street\",                 \":City\"             ]         }],     \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\" }  ~~~  Response  ~~~  {   \"items\": [     {       \"status\": 200,       \"readItem\": {         \"fieldId\": \"000000008BFE6BB9A2A3F80F23DC6E738470F24B95E5102A\",         \"nodeId\": \"0000000043F912B92911FFE2A52E31066E8B653D3F7E8DE7\",         \"data\": \"Bob Watson\"       }     },     {       \"status\": 200,       \"readItem\": {         \"fieldId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA\",         \"nodeId\": \"000000002B3CABC1694B029442124526A5B6137E9EABCAD1v\",         \"children\": [           {             \"status\": 200,             \"readItem\": {               \"fieldId\": \"00000000F6EFF0C416BE603531C8BA77C36E8A9B29368FB5\",               \"nodeId\": \"00000000F76AF7DFD004F6C321636CE9A53F62B05F009BFA\",               \"data\": \"London\"             }           },           {             \"status\": 404,             \"readItem\": {               \"fieldId\": \"0000000095E0F6B9F5480FD75DA9520E480AD3E89DC35D9A\"             }           }         ]       }     }   ] }  ~~~  #### Example  In the previous example, we saw that a 404 was returned for the house number field since the data had not yet been written. However, if we specify a `defaultStorageId` when making the request, then an information node will be created and an attempt will be made to fetch the data. It is the responsibility of the interface given by `defaultStorageId` to determine the data that should be returned.  ~~~  POST /read {     \"template\": [         \":PersonName\",         {             \":BasicAddress\": [                 \":Street\",                 \":City\"             ]         }],     \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\",     \"defaultStorageId\": \":LazyLoadInterface\" }  ~~~  We could also create a template with a `defaultStorageId`, in which case all reads will behave like the above request.  ~~~  POST /createtemplate {     ...     \"name\": \"PersonProfile\",     \"defaultStorageId\": \":LazyLoadInterface\",     \"memberIds\": [         \":PersonName\",         {             \":BasicAddress\": [                 \":Street\",                 \":City\"             ]         }     ] }  ~~~  #### Example  In this example, we demonstrate the behaviour when fields are not *uniqueByParent. In this case, all fields are *uniqueByParent* except *ClientProfile*.  ~~~  POST /read {     \"template\": [         {\":ClientList\": [             {\":ClientProfile\": [                 {\":BasicAddress\": [                     \":Street\"                 ]}             ]}         ]}     ],     \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\" }  ~~~  Response  ~~~  {   \"items\": [     {       \"status\": 200,       \"readItem\": {         \"fieldId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA\",         \"nodeId\": \"000000002B3CABC1694B029442124526A5B6137E9EABCAD1\",         \"children\": [           {             \"readItem\": {               \"fieldId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\",               \"nodes\": [                 {                   \"status\": 200,                   \"readItem\": {                     \"fieldId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA\",                     \"nodeId\": \"000000002B3CABC1694B029442124526A5B6137E9EABCAD1\",                     \"children\": [                       {                         \"status\": 200,                         \"readItem\": {                           \"fieldId\": \"0000000095E0F6B9F5480FD75DA9520E480AD3E89DC35D9A\",                           \"nodeId\": \"0000000099A8B1E3605B77F3EDB62B475DE739646041DFB9\",                           \"data\": \"Inverness Terrace\"                         }                       }                     ]                   }                 },                 {                   \"status\": 200,                   \"readItem\": {                     \"fieldId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA\",                     \"nodeId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\",                     \"children\": [                       {                         \"status\": 200,                         \"readItem\": {                           \"fieldId\": \"0000000095E0F6B9F5480FD75DA9520E480AD3E89DC35D9A\",                           \"nodeId\": \"0000000016270565667CE604DD4DF499C2A31FF6D2072FD7\",                           \"data\": \"Baker Street\"                         }                       }                     ]                   }                 }               ]             }           }         ]       }     }   ] }  ~~~  Data returned for non-*uniqueByParent* fields is contained under a *nodes* property within the *readItem*.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.read_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param ReadRequest read_request:
        :return: ReadResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'read_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/read', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReadResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read_information(self, **kwargs):  # noqa: E501
        """Read Information  # noqa: E501

        For reading information data.  The nodeId must be an information node.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.read_information(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param ReadInformationRequest read_information_request:
        :return: ReadInformationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.read_information_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.read_information_with_http_info(**kwargs)  # noqa: E501
            return data

    def read_information_with_http_info(self, **kwargs):  # noqa: E501
        """Read Information  # noqa: E501

        For reading information data.  The nodeId must be an information node.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.read_information_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param ReadInformationRequest read_information_request:
        :return: ReadInformationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'read_information_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_information" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/readinformation', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReadInformationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def replace_information(self, **kwargs):  # noqa: E501
        """Replace  # noqa: E501

        Replace is used to change the value of a leaf information node. Note that the new value has a new node id. One can use the /history endpoint to list all historical versions of a leaf information node.  #### Example In this example, we create and then replace an information node. The node has field type and parent entity having Factern Ids `0000000016270565667CE604DD4DF499C2A31FF6D2072FD7` and `00000000571749C62247EC65D43151C296366C4EF48658A9`, respectively. ~~~ POST /createinformation {     ...     \"parentId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\",     \"fieldId\": \"0000000016270565667CE604DD4DF499C2A31FF6D2072FD7\",     \"data\": \"Alice\" } ~~~ The information node's Factern Id is returned. ~~~ Response {     ...     \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\",     ... } ~~~ We list the information nodes of the entity filtering results using the field type. ~~~ POST /describe {     ...     \"nodeId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\",     \"listChildren\": {         \"factType\": \"Information\",         \"fieldId\": \"0000000016270565667CE604DD4DF499C2A31FF6D2072FD7\"     } } ~~~ The response ~~~ {     ...     \"children\": [{         \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\",         ...     }] } ~~~ Now we replace the previously created information node. ~~~ POST /replaceinformation {     ...     \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\",     \"data\": \"Alison\" } ~~~ The replacement information node's Factern Id is returned. ~~~ Response {     ...     \"nodeId\": \"000000007611AD504DBF600078DF929DD98EAE4787B4D87A\",     ... } ~~~ The same describe as before is invoked, but now shows only the Factern Id of the replacement. Response ~~~ {     ...     \"children\": [{         \"nodeId\": \"000000007611AD504DBF600078DF929DD98EAE4787B4D87A\",         ...     }] } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_information(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param ReplaceFieldRequest replace_field_request:
        :return: Information
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.replace_information_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.replace_information_with_http_info(**kwargs)  # noqa: E501
            return data

    def replace_information_with_http_info(self, **kwargs):  # noqa: E501
        """Replace  # noqa: E501

        Replace is used to change the value of a leaf information node. Note that the new value has a new node id. One can use the /history endpoint to list all historical versions of a leaf information node.  #### Example In this example, we create and then replace an information node. The node has field type and parent entity having Factern Ids `0000000016270565667CE604DD4DF499C2A31FF6D2072FD7` and `00000000571749C62247EC65D43151C296366C4EF48658A9`, respectively. ~~~ POST /createinformation {     ...     \"parentId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\",     \"fieldId\": \"0000000016270565667CE604DD4DF499C2A31FF6D2072FD7\",     \"data\": \"Alice\" } ~~~ The information node's Factern Id is returned. ~~~ Response {     ...     \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\",     ... } ~~~ We list the information nodes of the entity filtering results using the field type. ~~~ POST /describe {     ...     \"nodeId\": \"00000000571749C62247EC65D43151C296366C4EF48658A9\",     \"listChildren\": {         \"factType\": \"Information\",         \"fieldId\": \"0000000016270565667CE604DD4DF499C2A31FF6D2072FD7\"     } } ~~~ The response ~~~ {     ...     \"children\": [{         \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\",         ...     }] } ~~~ Now we replace the previously created information node. ~~~ POST /replaceinformation {     ...     \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\",     \"data\": \"Alison\" } ~~~ The replacement information node's Factern Id is returned. ~~~ Response {     ...     \"nodeId\": \"000000007611AD504DBF600078DF929DD98EAE4787B4D87A\",     ... } ~~~ The same describe as before is invoked, but now shows only the Factern Id of the replacement. Response ~~~ {     ...     \"children\": [{         \"nodeId\": \"000000007611AD504DBF600078DF929DD98EAE4787B4D87A\",         ...     }] } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_information_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param ReplaceFieldRequest replace_field_request:
        :return: Information
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'replace_field_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method replace_information" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/replaceinformation', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Information',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def request_permission(self, **kwargs):  # noqa: E501
        """Request Permission  # noqa: E501

        Permissions specified with a *requestInterfaceId* are called *Requestable Permissions*. If an agent otherwise matches the permission policy, then the status code returned when reading the target node will be the special status code 477. The `/requestpermission` endpoint can be used for requesting the permission be granted.   In the case that a node has more than one associated *Requestable Permission* the most specific matching requestable permission is used. If there is more than one such requestable permission, then the requestable permission used is arbitrary.  #### Example In this example we use requestable permissions to get access to the *FullName* field of the *Bob Watson* entity having Factern Id *0000000079C27D120B58F74C683639EE72EA2E33B93293CB*. The *Bob Watson* entity and fields were created by the HumanResources login, having Factern Id *00000000F101AB12CC65E5CE2F42E0C9FEC9CBEEEEC03AA3*.  We start by attempting to read the *FullName* field from the Payroll login, having Factern Id *00000000B04BCB6670E3E4F35EDCE6CD8AF77111C74150AE*. ~~~ POST /read {     \"template\": [\"frn:field:00000000F101AB12CC65E5CE2F42E0C9FEC9CBEEEEC03AA3:FullName\"],     \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\" } ~~~ The response is 403, Forbidden, since the Payroll login has no permission on the *Bob Watson* entity.  Acme wants to make personnel entities available if the reading login is Payroll, but only on a case-by-case basis approved by the Hunam Resources director. They have set up a webservice for receiving permission requests that translates the request to an email to the director. If approved, the requested permission will be created.  We first register the webservice with Factern. ~~~ POST /createinterface {     ...     \"addData\": {\"url\": \"https://hr.acme.com/permreq\"},     \"getData\": {\"url\": \"https://hr.acme.com/get\"},     \"deleteData\": {\"url\": \"https://hr.acme.com/delete\"},     ... } ~~~ The response contains the created interface's Factern Id ~~~ Response ~~~ ~~~ {     ...     \"nodeId\": \"00000000C4F8891E18CED1C62ACE2ABC2BC0BBF8C6DFBFCC\",     ... } ~~~ We now create the requestable permission, indicating that *Read* requests from the Payroll login will be sent to the approval webservice. ~~~ POST /permission {     \"targetNodeId\": \"0000000043F912B92911FFE2A52E31066E8B653D3F7E8DE7\",     \"policy\": {         \"effect\": \"Allow\",         \"grantee\": \"00000000B04BCB6670E3E4F35EDCE6CD8AF77111C74150AE\",         \"requestInterfaceId\": \"00000000C4F8891E18CED1C62ACE2ABC2BC0BBF8C6DFBFCC\",         \"actions\": [\"Read\"]     } } ~~~ Now, when the Payroll login attempts a *Read*, the response is the special Http status code 477, indicating that the permission is requestable.  The Payroll login now requests the permission. ~~~ POST /requestpermission {     \"nodeId\": \"0000000043F912B92911FFE2A52E31066E8B653D3F7E8DE7\" } ~~~ The Human Resources webservice is called with a payload indicating the permission request. ~~~ POST https://hr.acme.com/permreq?nodeId=0000000001290F75C24695FA55F40D85843EA40FCB5B49F2 {     \"targetNodeId\": \"0000000043F912B92911FFE2A52E31066E8B653D3F7E8DE7\",     \"policy\": {         \"effect\": \"Allow\",         \"grantee\": \"00000000B04BCB6670E3E4F35EDCE6CD8AF77111C74150AE\",         \"applicationId\": \"00000000DAB38B0E3390E09DFF52EF2AED6833F11BBC8896\",         \"actions\": [\"Read\"]     } } ~~~ Assuming the director approves, the Human Resources app is used to create the permission. ~~~ POST /permission {     \"targetNodeId\": \"0000000043F912B92911FFE2A52E31066E8B653D3F7E8DE7\",     \"policy\": {         \"effect\": \"Allow\",         \"grantee\": \"00000000B04BCB6670E3E4F35EDCE6CD8AF77111C74150AE\",         \"applicationId\": \"00000000DAB38B0E3390E09DFF52EF2AED6833F11BBC8896\",         \"actions\": [\"Read\"]     } } ~~~ Now, when the Payroll login can make the requested read. Response ~~~ [{     \"status\": 200,     \"readItem\": {         \"fieldId\": \"000000008BFE6BB9A2A3F80F23DC6E738470F24B95E5102A\",         \"nodeId\": \"0000000043F912B92911FFE2A52E31066E8B653D3F7E8DE7\",         \"data\": \"Bob Watson\"     } }] ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.request_permission(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param NodeIdRequest node_id_request:
        :return: StandardNodeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.request_permission_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.request_permission_with_http_info(**kwargs)  # noqa: E501
            return data

    def request_permission_with_http_info(self, **kwargs):  # noqa: E501
        """Request Permission  # noqa: E501

        Permissions specified with a *requestInterfaceId* are called *Requestable Permissions*. If an agent otherwise matches the permission policy, then the status code returned when reading the target node will be the special status code 477. The `/requestpermission` endpoint can be used for requesting the permission be granted.   In the case that a node has more than one associated *Requestable Permission* the most specific matching requestable permission is used. If there is more than one such requestable permission, then the requestable permission used is arbitrary.  #### Example In this example we use requestable permissions to get access to the *FullName* field of the *Bob Watson* entity having Factern Id *0000000079C27D120B58F74C683639EE72EA2E33B93293CB*. The *Bob Watson* entity and fields were created by the HumanResources login, having Factern Id *00000000F101AB12CC65E5CE2F42E0C9FEC9CBEEEEC03AA3*.  We start by attempting to read the *FullName* field from the Payroll login, having Factern Id *00000000B04BCB6670E3E4F35EDCE6CD8AF77111C74150AE*. ~~~ POST /read {     \"template\": [\"frn:field:00000000F101AB12CC65E5CE2F42E0C9FEC9CBEEEEC03AA3:FullName\"],     \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\" } ~~~ The response is 403, Forbidden, since the Payroll login has no permission on the *Bob Watson* entity.  Acme wants to make personnel entities available if the reading login is Payroll, but only on a case-by-case basis approved by the Hunam Resources director. They have set up a webservice for receiving permission requests that translates the request to an email to the director. If approved, the requested permission will be created.  We first register the webservice with Factern. ~~~ POST /createinterface {     ...     \"addData\": {\"url\": \"https://hr.acme.com/permreq\"},     \"getData\": {\"url\": \"https://hr.acme.com/get\"},     \"deleteData\": {\"url\": \"https://hr.acme.com/delete\"},     ... } ~~~ The response contains the created interface's Factern Id ~~~ Response ~~~ ~~~ {     ...     \"nodeId\": \"00000000C4F8891E18CED1C62ACE2ABC2BC0BBF8C6DFBFCC\",     ... } ~~~ We now create the requestable permission, indicating that *Read* requests from the Payroll login will be sent to the approval webservice. ~~~ POST /permission {     \"targetNodeId\": \"0000000043F912B92911FFE2A52E31066E8B653D3F7E8DE7\",     \"policy\": {         \"effect\": \"Allow\",         \"grantee\": \"00000000B04BCB6670E3E4F35EDCE6CD8AF77111C74150AE\",         \"requestInterfaceId\": \"00000000C4F8891E18CED1C62ACE2ABC2BC0BBF8C6DFBFCC\",         \"actions\": [\"Read\"]     } } ~~~ Now, when the Payroll login attempts a *Read*, the response is the special Http status code 477, indicating that the permission is requestable.  The Payroll login now requests the permission. ~~~ POST /requestpermission {     \"nodeId\": \"0000000043F912B92911FFE2A52E31066E8B653D3F7E8DE7\" } ~~~ The Human Resources webservice is called with a payload indicating the permission request. ~~~ POST https://hr.acme.com/permreq?nodeId=0000000001290F75C24695FA55F40D85843EA40FCB5B49F2 {     \"targetNodeId\": \"0000000043F912B92911FFE2A52E31066E8B653D3F7E8DE7\",     \"policy\": {         \"effect\": \"Allow\",         \"grantee\": \"00000000B04BCB6670E3E4F35EDCE6CD8AF77111C74150AE\",         \"applicationId\": \"00000000DAB38B0E3390E09DFF52EF2AED6833F11BBC8896\",         \"actions\": [\"Read\"]     } } ~~~ Assuming the director approves, the Human Resources app is used to create the permission. ~~~ POST /permission {     \"targetNodeId\": \"0000000043F912B92911FFE2A52E31066E8B653D3F7E8DE7\",     \"policy\": {         \"effect\": \"Allow\",         \"grantee\": \"00000000B04BCB6670E3E4F35EDCE6CD8AF77111C74150AE\",         \"applicationId\": \"00000000DAB38B0E3390E09DFF52EF2AED6833F11BBC8896\",         \"actions\": [\"Read\"]     } } ~~~ Now, when the Payroll login can make the requested read. Response ~~~ [{     \"status\": 200,     \"readItem\": {         \"fieldId\": \"000000008BFE6BB9A2A3F80F23DC6E738470F24B95E5102A\",         \"nodeId\": \"0000000043F912B92911FFE2A52E31066E8B653D3F7E8DE7\",         \"data\": \"Bob Watson\"     } }] ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.request_permission_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param NodeIdRequest node_id_request:
        :return: StandardNodeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'node_id_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method request_permission" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/requestpermission', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StandardNodeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def reset_login(self, **kwargs):  # noqa: E501
        """Changing Login Password  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.reset_login(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param ResetLoginCredentialsRequest reset_login_credentials_request:
        :return: ResetLoginResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.reset_login_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.reset_login_with_http_info(**kwargs)  # noqa: E501
            return data

    def reset_login_with_http_info(self, **kwargs):  # noqa: E501
        """Changing Login Password  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.reset_login_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param ResetLoginCredentialsRequest reset_login_credentials_request:
        :return: ResetLoginResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'reset_login_credentials_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reset_login" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/resetlogin', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResetLoginResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_alias(self, **kwargs):  # noqa: E501
        """Search For Alias  # noqa: E501

        For checking if a (globally unique) alias is in use or not.  #### Example  In this example, we create an an alias, and check to see that the alias exists.  We create the alias.  ~~~  POST /createalias {     \"name\": \"Moriarty\"     ... }  ~~~  We now search for the alias.  ~~~  POST /searchalias {     \"name\": \"Moriarty\" }  ~~~  Response returns true since the alias exists.  ~~~  {     \"exists\": true }  ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_alias(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param SearchAliasRequest search_alias_request:
        :return: SearchAliasResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.search_alias_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_alias_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_alias_with_http_info(self, **kwargs):  # noqa: E501
        """Search For Alias  # noqa: E501

        For checking if a (globally unique) alias is in use or not.  #### Example  In this example, we create an an alias, and check to see that the alias exists.  We create the alias.  ~~~  POST /createalias {     \"name\": \"Moriarty\"     ... }  ~~~  We now search for the alias.  ~~~  POST /searchalias {     \"name\": \"Moriarty\" }  ~~~  Response returns true since the alias exists.  ~~~  {     \"exists\": true }  ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_alias_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param SearchAliasRequest search_alias_request:
        :return: SearchAliasResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'search_alias_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_alias" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/searchalias', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SearchAliasResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_entity(self, **kwargs):  # noqa: E501
        """Search For Entity  # noqa: E501

        In the case of entities, we do not search for them directly. Rather we search for a value of an information node parented by the entity of a particular field type.  The results can be restricted by specifying the `restrictTo` property. The value can specify an entity or a group.  | restrictTo Fact Type | Example | Description | |:---------------------|---------|:------------| | Entity | frn:entity::rootEntity | The found entities must descend from this entity or be this entity | | Group  | frn:group::adminEntities | The found entities must be among the entities of this group or descend from one of them |  #### Example In this example, we create a *searchable* field type, an information node of that type under an entity, and find that entity We create the searchable type. ~~~ POST /createfield {     \"name\": \"FamilyName\"     \"searchable\": true,     ... } ~~~ Response includes the Factern Id of the created field type. ~~~ {     ...     \"nodeId\": \"000000008029289F643854A1FE32F2EB69DEDFDD54B40EA9\",     ... } ~~~ We create an information node under entity with Factern Id \"00000000AF555988FBD9494419C26BBCD299A6314EAC0844\". ~~~ POST /createinformation {     ...     \"parentId\": \"00000000AF555988FBD9494419C26BBCD299A6314EAC0844\",     \"fieldId\": \":FamilyName\",     \"data\": \"Holmes\" } ~~~ The information node's Factern Id is returned. ~~~ Response {     ...     \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\",     ... } ~~~ We now search for all entities having information node with value \"Holmes\". ~~~ POST /searchentity {     ...     \"fieldId\": \":FamilyName\",     \"operator\": \"equals\",     \"term\": \"Holmes\",     \"maxResults\": 1 } ~~~ Response includes the matching entity and a token that can used for scrolling through the rest of the results. ~~~ {     \"nodes\": [{         \"nodeId\": \"00000000AF555988FBD9494419C26BBCD299A6314EAC0844\",         ...     }],     \"totalResults\": 42,     \"nextToken\": \"c29tZWJhc2U2NGVuY29kZWRzdHJpbmc=\" } ~~~ A subsequent request to `/searchentity` with the token will return the next batch of results. ~~~ POST /searchentity {     \"nextToken\": \"c29tZWJhc2U2NGVuY29kZWRzdHJpbmc=\" } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_entity(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param SearchEntityRequest search_entity_request:
        :return: EntityListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.search_entity_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_entity_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_entity_with_http_info(self, **kwargs):  # noqa: E501
        """Search For Entity  # noqa: E501

        In the case of entities, we do not search for them directly. Rather we search for a value of an information node parented by the entity of a particular field type.  The results can be restricted by specifying the `restrictTo` property. The value can specify an entity or a group.  | restrictTo Fact Type | Example | Description | |:---------------------|---------|:------------| | Entity | frn:entity::rootEntity | The found entities must descend from this entity or be this entity | | Group  | frn:group::adminEntities | The found entities must be among the entities of this group or descend from one of them |  #### Example In this example, we create a *searchable* field type, an information node of that type under an entity, and find that entity We create the searchable type. ~~~ POST /createfield {     \"name\": \"FamilyName\"     \"searchable\": true,     ... } ~~~ Response includes the Factern Id of the created field type. ~~~ {     ...     \"nodeId\": \"000000008029289F643854A1FE32F2EB69DEDFDD54B40EA9\",     ... } ~~~ We create an information node under entity with Factern Id \"00000000AF555988FBD9494419C26BBCD299A6314EAC0844\". ~~~ POST /createinformation {     ...     \"parentId\": \"00000000AF555988FBD9494419C26BBCD299A6314EAC0844\",     \"fieldId\": \":FamilyName\",     \"data\": \"Holmes\" } ~~~ The information node's Factern Id is returned. ~~~ Response {     ...     \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\",     ... } ~~~ We now search for all entities having information node with value \"Holmes\". ~~~ POST /searchentity {     ...     \"fieldId\": \":FamilyName\",     \"operator\": \"equals\",     \"term\": \"Holmes\",     \"maxResults\": 1 } ~~~ Response includes the matching entity and a token that can used for scrolling through the rest of the results. ~~~ {     \"nodes\": [{         \"nodeId\": \"00000000AF555988FBD9494419C26BBCD299A6314EAC0844\",         ...     }],     \"totalResults\": 42,     \"nextToken\": \"c29tZWJhc2U2NGVuY29kZWRzdHJpbmc=\" } ~~~ A subsequent request to `/searchentity` with the token will return the next batch of results. ~~~ POST /searchentity {     \"nextToken\": \"c29tZWJhc2U2NGVuY29kZWRzdHJpbmc=\" } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_entity_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param SearchEntityRequest search_entity_request:
        :return: EntityListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'search_entity_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_entity" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/searchentity', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EntityListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def settle_account(self, **kwargs):  # noqa: E501
        """Settle Account  # noqa: E501

        To settle an account we sign a hash of the value and send the signature and value to be resolved on the blockchain.  Calls to *&#47;settleaccount* are exempt from API balance checking, it is possible to use *&#47;settleaccount* even if the account has hit the hard limit.  See [Signing](#header-signing) for example code to generate the signature.  #### Example ~~~ POST /settleaccount {     \"tokenPayment\": {         \"publickey\": \"0x16e9718e7a55b523df5e30d9fce568b92586ef89\",         \"signature\": \"0xfd9d03cea3afad97900318a25894ce88c25a634f47dd158b3f4fce7c1d39da950e6089c69f32a36392f731727ab3b190c115c462640584e46808dbd13d2420cd1c\",         \"value\": \"42\"     } } ~~~ The settlement node's Factern ID is returned ~~~ {     \"settlementId\": \"0000000057DBB7C63F128D14060866ADAD9D23C20F3E4507\" } ~~~ The settlement is processed by the blockchain asynchronously and the resulting transaction ID and result will be returned when describing the settlement node ~~~ POST /describe {     \"nodeId\": \"0000000057DBB7C63F128D14060866ADAD9D23C20F3E4507\" } ~~~ When the transaction is complete (usually around 15 seconds) the transaction details and latest nonce will be returned. The possible values returned by settlementStatus are: <table>     <thead>         <tr>             <td>settlementStatus</td>             <td>Description</td>         </tr>     </thead>     <tr>         <td>CREATED</td>         <td>Transaction has been created and is asynchronously being processed.</td>     </tr>     <tr>         <td>SUCCESS</td>         <td>Transaction completed successfully, the transactionId can be used to confirm the successful transaction.</td>     </tr>     <tr>         <td>FAILED</td>         <td>Transaction failed, the transactionId can be used to view the failed transaction.</td>     </tr> </table>  ~~~ {     \"node\": {         \"nodeId\": \"0000000057DBB7C63F128D14060866ADAD9D23C20F3E4507\",         \"factType\": \"Statement\",         ...         \"settlementStatus\": \"SUCCESS\",         \"settlementTransactionId\": \"0x5695a0bf217c71dd87f590aadc70bdd16cf16f58e324944722d58c8b045ae891\",         \"nonce\": \"0x00d02acf6ba17e48c95ea0a3e78502ee24f122f1f488f42e34dea967bf2807ce\"     } } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.settle_account(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param SettleAccountRequest settle_account_request:
        :return: SettleAccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.settle_account_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.settle_account_with_http_info(**kwargs)  # noqa: E501
            return data

    def settle_account_with_http_info(self, **kwargs):  # noqa: E501
        """Settle Account  # noqa: E501

        To settle an account we sign a hash of the value and send the signature and value to be resolved on the blockchain.  Calls to *&#47;settleaccount* are exempt from API balance checking, it is possible to use *&#47;settleaccount* even if the account has hit the hard limit.  See [Signing](#header-signing) for example code to generate the signature.  #### Example ~~~ POST /settleaccount {     \"tokenPayment\": {         \"publickey\": \"0x16e9718e7a55b523df5e30d9fce568b92586ef89\",         \"signature\": \"0xfd9d03cea3afad97900318a25894ce88c25a634f47dd158b3f4fce7c1d39da950e6089c69f32a36392f731727ab3b190c115c462640584e46808dbd13d2420cd1c\",         \"value\": \"42\"     } } ~~~ The settlement node's Factern ID is returned ~~~ {     \"settlementId\": \"0000000057DBB7C63F128D14060866ADAD9D23C20F3E4507\" } ~~~ The settlement is processed by the blockchain asynchronously and the resulting transaction ID and result will be returned when describing the settlement node ~~~ POST /describe {     \"nodeId\": \"0000000057DBB7C63F128D14060866ADAD9D23C20F3E4507\" } ~~~ When the transaction is complete (usually around 15 seconds) the transaction details and latest nonce will be returned. The possible values returned by settlementStatus are: <table>     <thead>         <tr>             <td>settlementStatus</td>             <td>Description</td>         </tr>     </thead>     <tr>         <td>CREATED</td>         <td>Transaction has been created and is asynchronously being processed.</td>     </tr>     <tr>         <td>SUCCESS</td>         <td>Transaction completed successfully, the transactionId can be used to confirm the successful transaction.</td>     </tr>     <tr>         <td>FAILED</td>         <td>Transaction failed, the transactionId can be used to view the failed transaction.</td>     </tr> </table>  ~~~ {     \"node\": {         \"nodeId\": \"0000000057DBB7C63F128D14060866ADAD9D23C20F3E4507\",         \"factType\": \"Statement\",         ...         \"settlementStatus\": \"SUCCESS\",         \"settlementTransactionId\": \"0x5695a0bf217c71dd87f590aadc70bdd16cf16f58e324944722d58c8b045ae891\",         \"nonce\": \"0x00d02acf6ba17e48c95ea0a3e78502ee24f122f1f488f42e34dea967bf2807ce\"     } } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.settle_account_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param SettleAccountRequest settle_account_request:
        :return: SettleAccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'settle_account_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method settle_account" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/settleaccount', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SettleAccountResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_application(self, **kwargs):  # noqa: E501
        """Resetting Application Secret  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_application(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param UpdateApplicationRequest update_application_request:
        :return: UpdateApplicationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_application_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.update_application_with_http_info(**kwargs)  # noqa: E501
            return data

    def update_application_with_http_info(self, **kwargs):  # noqa: E501
        """Resetting Application Secret  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_application_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param UpdateApplicationRequest update_application_request:
        :return: UpdateApplicationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'update_application_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_application" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/updateapplication', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UpdateApplicationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_status(self, **kwargs):  # noqa: E501
        """Enabling/Disabling Nodes  # noqa: E501

        Some nodes can be enabled or disabled. Currently, only mirrors support enabling and disabling. This endpoint is used to enable or disable a node after it has been created.  #### Example In this example, we create a mirror and then update its status to *disabled*. ~~~ POST /createmirror {   \"sourceNodeId\": \"00000000A797A4951E939886BA465B9EFABFCD2E5B9131A7\",   \"destinationNodeId\": \"00000000020E67C874812302B5967F0458452B7432F8E89B\",   \"templateId\": \":SpouseProfile\" } ~~~ Response ~~~ {   \"nodeId\": \"00000000D74249B4F013FED3B7438C2E4252EE821E3F2C98\",   ...   \"enabled\": true } ~~~ Now disable and describe the mirror. ~~~ POST /updatestatus {   \"nodeId\": \"00000000D74249B4F013FED3B7438C2E4252EE821E3F2C98\",   \"status\": \"DISABLED\" } ~~~ ~~~ POST /describe {   \"nodeId\": \"00000000D74249B4F013FED3B7438C2E4252EE821E3F2C98\" } ~~~ Response ~~~ {   \"nodeId\": \"00000000D74249B4F013FED3B7438C2E4252EE821E3F2C98\",   ...   \"enabled\": false } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_status(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param UpdateStatusRequest update_status_request:
        :return: StandardNodeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_status_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.update_status_with_http_info(**kwargs)  # noqa: E501
            return data

    def update_status_with_http_info(self, **kwargs):  # noqa: E501
        """Enabling/Disabling Nodes  # noqa: E501

        Some nodes can be enabled or disabled. Currently, only mirrors support enabling and disabling. This endpoint is used to enable or disable a node after it has been created.  #### Example In this example, we create a mirror and then update its status to *disabled*. ~~~ POST /createmirror {   \"sourceNodeId\": \"00000000A797A4951E939886BA465B9EFABFCD2E5B9131A7\",   \"destinationNodeId\": \"00000000020E67C874812302B5967F0458452B7432F8E89B\",   \"templateId\": \":SpouseProfile\" } ~~~ Response ~~~ {   \"nodeId\": \"00000000D74249B4F013FED3B7438C2E4252EE821E3F2C98\",   ...   \"enabled\": true } ~~~ Now disable and describe the mirror. ~~~ POST /updatestatus {   \"nodeId\": \"00000000D74249B4F013FED3B7438C2E4252EE821E3F2C98\",   \"status\": \"DISABLED\" } ~~~ ~~~ POST /describe {   \"nodeId\": \"00000000D74249B4F013FED3B7438C2E4252EE821E3F2C98\" } ~~~ Response ~~~ {   \"nodeId\": \"00000000D74249B4F013FED3B7438C2E4252EE821E3F2C98\",   ...   \"enabled\": false } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_status_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param UpdateStatusRequest update_status_request:
        :return: StandardNodeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'update_status_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_status" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/updatestatus', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StandardNodeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def watch(self, **kwargs):  # noqa: E501
        """Create Watch Trigger  # noqa: E501

        For placing a watch on a node. Once placed, and modification to the node causes a watch event to be created. Examples of modifications that can generate a watch event include replacing an information node, or adding a child.  Watch events are parented by the watch and can be accessed using the /describe endpoint on the watch with a childNodeClass of WatchEvent.  If a filter is specified, a WatchEvent will only be created if the modifications to the watched node match the arguments of the filter.  If an external interface is specified, the corresponding watch events are sent there.  #### Example In this example, we place a watch on an entity, having Factern Id \"00000000217DDE302076BFCB4DF075577DFA0C4AABC728DD\", and then add an information node under the entity. ~~~ POST /watch {     \"targetNodeId\": \"00000000217DDE302076BFCB4DF075577DFA0C4AABC728DD\" } ~~~ Response ~~~ {     ...     \"nodeId\": \"00000000DD0248D31A8418C62078D7A716EBA9A39F2C3A81\",     ... } ~~~ We add an information node under the entity ~~~ POST /createinformation {     ...     \"parentId\": \"00000000217DDE302076BFCB4DF075577DFA0C4AABC728DD\",     \"fieldId\": \":FullName\",     \"data\": \"Alice Watson\" } ~~~ Response ~~~ {     ...     \"nodeId\": \"00000000C78EAB913627799CE4EB15227EA0A2FDD2EEF001\",     ... } ~~~ We list the watch events under the watch. ~~~ POST /describe {     ...     \"nodeId\": \"00000000DD0248D31A8418C62078D7A716EBA9A39F2C3A81\",     \"listChildren\": {         \"factType\": \"WatchEvent\"     } } ~~~ The response contains a single watch event that references both the watch and the created information. ~~~ {     ...     \"children\": [{         \"parentId\": \"00000000DD0248D31A8418C62078D7A716EBA9A39F2C3A81\",         \"factType\": \"WatchEvent\",         \"nodeId\": \"00000000AEFFDB5F8A4C745A0E002736D625FC76903888D9\",         \"source\": \"00000000C78EAB913627799CE4EB15227EA0A2FDD2EEF001\",         ...     }] } ~~~ #### Example Watches can use an optional *Filter* to specify the types of actions that create a watch event. In this example, we place a watch on an entity, having Factern Id \"00000000217DDE302076BFCB4DF075577DFA0C4AABC728DD\", and then add two information nodes under the entity with only one matching the *Filter*. First we create a *filter* that evalutes to true for all child nodes that are a 'creates' action.  The 'creates' action has a built in FacterId of \"0000000000000000D7CE4E3D25DF4F698AFD0545FFDF4136\". ~~~ POST /createfilter {   ...     \"statements\": \"[       {         \"field\": \"Action\",         \"arguments\" : [\"0000000000000000D7CE4E3D25DF4F698AFD0545FFDF4136\"]       }     ]\"     ... } ~~~ Response includes the Factern Id of the created filter. ~~~ {     ...     \"nodeId\": \"000000000D9955617980254688D7A0F138A94CA8D3ECB0B5\",     ... } ~~~ Then we create a watch with the *filter* that we just created. ~~~ POST /watch {     \"targetNodeId\": \"00000000217DDE302076BFCB4DF075577DFA0C4AABC728DD\",     \"filterId\": \"000000000D9955617980254688D7A0F138A94CA8D3ECB0B5\" } ~~~ Response will include the filterId ~~~ {     ...     \"nodeId\": \"00000000DD0248D31A8418C62078D7A716EBA9A39F2C3A81\",     \"filterId\": \"000000000D9955617980254688D7A0F138A94CA8D3ECB0B5\"     ... } ~~~ Now we create an information node under the watched node and then delete it. ~~~ POST /createinformation {     ...     \"parentId\": \"00000000217DDE302076BFCB4DF075577DFA0C4AABC728DD\",     \"fieldId\": \":Street\",     \"data\": \"Inverness Terrace\" } ~~~ The information node's Factern Id is returned. ~~~ Response {     ...     \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\",     ... } ~~~ Now we delete the information node we just created. ~~~ POST /deletenode {     ...     \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\" } ~~~ We list the watch events under the watch. ~~~ POST /describe {     ...     \"nodeId\": \"00000000DD0248D31A8418C62078D7A716EBA9A39F2C3A81\",     \"listChildren\": {         \"factType\": \"WatchEvent\"     } } ~~~ The response contains a single watch event that references only the created information node. ~~~ {     ...     \"children\": [{         \"parentId\": \"00000000DD0248D31A8418C62078D7A716EBA9A39F2C3A81\",         \"factType\": \"WatchEvent\",         \"nodeId\": \"00000000AEFFDB5F8A4C745A0E002736D625FC76903888D9\",         \"source\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\",         ...     }] } ~~~ #### Example The watch in this example includes an outbound call interface. We create an interface for accepting the watch event. ~~~ POST /createinterface {     ...     \"addData\": {\"url\": \"https://acme.com/addwatch\"},     \"getData\": {\"url\": \"https://acme.com/get\"},     \"deleteData\": {\"url\": \"https://acme.com/delete\"},     ... } ~~~ Response ~~~ {     ...     \"nodeId\": \"00000000C4F8891E18CED1C62ACE2ABC2BC0BBF8C6DFBFCC\",     ... } ~~~ And we create a watch on the entity that references the interface. ~~~ POST /watch {     \"targetNodeId\": \"00000000217DDE302076BFCB4DF075577DFA0C4AABC728DD\",     \"watchInterfaceId\": \"00000000C4F8891E18CED1C62ACE2ABC2BC0BBF8C6DFBFCC\" } ~~~ We add an information node under the entity ~~~ POST /createinformation {     ...     \"parentId\": \"00000000217DDE302076BFCB4DF075577DFA0C4AABC728DD\",     \"fieldId\": \":FullName\",     \"data\": \"Alice Moriarty\" } ~~~ Response ~~~ {     ...     \"nodeId\": \"00000000C78EAB913627799CE4EB15227EA0A2FDD2EEF001\",     ... } ~~~ If properly implemented, the interface will receive a POST with payload being the watch event. ~~~ POST https://acme.com/addwatch?nodeId=000000009F30B3440E8B768D34552CA45786CDB2AF2959B1 {     ...     \"parentId\": \"00000000DD0248D31A8418C62078D7A716EBA9A39F2C3A81\",     \"factType\": \"WatchEvent\",     \"nodeId\": \"00000000AEFFDB5F8A4C745A0E002736D625FC76903888D9\",     \"source\": \"00000000C78EAB913627799CE4EB15227EA0A2FDD2EEF001\", } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.watch(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateWatchRequest create_watch_request:
        :return: CreateWatchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.watch_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.watch_with_http_info(**kwargs)  # noqa: E501
            return data

    def watch_with_http_info(self, **kwargs):  # noqa: E501
        """Create Watch Trigger  # noqa: E501

        For placing a watch on a node. Once placed, and modification to the node causes a watch event to be created. Examples of modifications that can generate a watch event include replacing an information node, or adding a child.  Watch events are parented by the watch and can be accessed using the /describe endpoint on the watch with a childNodeClass of WatchEvent.  If a filter is specified, a WatchEvent will only be created if the modifications to the watched node match the arguments of the filter.  If an external interface is specified, the corresponding watch events are sent there.  #### Example In this example, we place a watch on an entity, having Factern Id \"00000000217DDE302076BFCB4DF075577DFA0C4AABC728DD\", and then add an information node under the entity. ~~~ POST /watch {     \"targetNodeId\": \"00000000217DDE302076BFCB4DF075577DFA0C4AABC728DD\" } ~~~ Response ~~~ {     ...     \"nodeId\": \"00000000DD0248D31A8418C62078D7A716EBA9A39F2C3A81\",     ... } ~~~ We add an information node under the entity ~~~ POST /createinformation {     ...     \"parentId\": \"00000000217DDE302076BFCB4DF075577DFA0C4AABC728DD\",     \"fieldId\": \":FullName\",     \"data\": \"Alice Watson\" } ~~~ Response ~~~ {     ...     \"nodeId\": \"00000000C78EAB913627799CE4EB15227EA0A2FDD2EEF001\",     ... } ~~~ We list the watch events under the watch. ~~~ POST /describe {     ...     \"nodeId\": \"00000000DD0248D31A8418C62078D7A716EBA9A39F2C3A81\",     \"listChildren\": {         \"factType\": \"WatchEvent\"     } } ~~~ The response contains a single watch event that references both the watch and the created information. ~~~ {     ...     \"children\": [{         \"parentId\": \"00000000DD0248D31A8418C62078D7A716EBA9A39F2C3A81\",         \"factType\": \"WatchEvent\",         \"nodeId\": \"00000000AEFFDB5F8A4C745A0E002736D625FC76903888D9\",         \"source\": \"00000000C78EAB913627799CE4EB15227EA0A2FDD2EEF001\",         ...     }] } ~~~ #### Example Watches can use an optional *Filter* to specify the types of actions that create a watch event. In this example, we place a watch on an entity, having Factern Id \"00000000217DDE302076BFCB4DF075577DFA0C4AABC728DD\", and then add two information nodes under the entity with only one matching the *Filter*. First we create a *filter* that evalutes to true for all child nodes that are a 'creates' action.  The 'creates' action has a built in FacterId of \"0000000000000000D7CE4E3D25DF4F698AFD0545FFDF4136\". ~~~ POST /createfilter {   ...     \"statements\": \"[       {         \"field\": \"Action\",         \"arguments\" : [\"0000000000000000D7CE4E3D25DF4F698AFD0545FFDF4136\"]       }     ]\"     ... } ~~~ Response includes the Factern Id of the created filter. ~~~ {     ...     \"nodeId\": \"000000000D9955617980254688D7A0F138A94CA8D3ECB0B5\",     ... } ~~~ Then we create a watch with the *filter* that we just created. ~~~ POST /watch {     \"targetNodeId\": \"00000000217DDE302076BFCB4DF075577DFA0C4AABC728DD\",     \"filterId\": \"000000000D9955617980254688D7A0F138A94CA8D3ECB0B5\" } ~~~ Response will include the filterId ~~~ {     ...     \"nodeId\": \"00000000DD0248D31A8418C62078D7A716EBA9A39F2C3A81\",     \"filterId\": \"000000000D9955617980254688D7A0F138A94CA8D3ECB0B5\"     ... } ~~~ Now we create an information node under the watched node and then delete it. ~~~ POST /createinformation {     ...     \"parentId\": \"00000000217DDE302076BFCB4DF075577DFA0C4AABC728DD\",     \"fieldId\": \":Street\",     \"data\": \"Inverness Terrace\" } ~~~ The information node's Factern Id is returned. ~~~ Response {     ...     \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\",     ... } ~~~ Now we delete the information node we just created. ~~~ POST /deletenode {     ...     \"nodeId\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\" } ~~~ We list the watch events under the watch. ~~~ POST /describe {     ...     \"nodeId\": \"00000000DD0248D31A8418C62078D7A716EBA9A39F2C3A81\",     \"listChildren\": {         \"factType\": \"WatchEvent\"     } } ~~~ The response contains a single watch event that references only the created information node. ~~~ {     ...     \"children\": [{         \"parentId\": \"00000000DD0248D31A8418C62078D7A716EBA9A39F2C3A81\",         \"factType\": \"WatchEvent\",         \"nodeId\": \"00000000AEFFDB5F8A4C745A0E002736D625FC76903888D9\",         \"source\": \"0000000079C27D120B58F74C683639EE72EA2E33B93293CB\",         ...     }] } ~~~ #### Example The watch in this example includes an outbound call interface. We create an interface for accepting the watch event. ~~~ POST /createinterface {     ...     \"addData\": {\"url\": \"https://acme.com/addwatch\"},     \"getData\": {\"url\": \"https://acme.com/get\"},     \"deleteData\": {\"url\": \"https://acme.com/delete\"},     ... } ~~~ Response ~~~ {     ...     \"nodeId\": \"00000000C4F8891E18CED1C62ACE2ABC2BC0BBF8C6DFBFCC\",     ... } ~~~ And we create a watch on the entity that references the interface. ~~~ POST /watch {     \"targetNodeId\": \"00000000217DDE302076BFCB4DF075577DFA0C4AABC728DD\",     \"watchInterfaceId\": \"00000000C4F8891E18CED1C62ACE2ABC2BC0BBF8C6DFBFCC\" } ~~~ We add an information node under the entity ~~~ POST /createinformation {     ...     \"parentId\": \"00000000217DDE302076BFCB4DF075577DFA0C4AABC728DD\",     \"fieldId\": \":FullName\",     \"data\": \"Alice Moriarty\" } ~~~ Response ~~~ {     ...     \"nodeId\": \"00000000C78EAB913627799CE4EB15227EA0A2FDD2EEF001\",     ... } ~~~ If properly implemented, the interface will receive a POST with payload being the watch event. ~~~ POST https://acme.com/addwatch?nodeId=000000009F30B3440E8B768D34552CA45786CDB2AF2959B1 {     ...     \"parentId\": \"00000000DD0248D31A8418C62078D7A716EBA9A39F2C3A81\",     \"factType\": \"WatchEvent\",     \"nodeId\": \"00000000AEFFDB5F8A4C745A0E002736D625FC76903888D9\",     \"source\": \"00000000C78EAB913627799CE4EB15227EA0A2FDD2EEF001\", } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.watch_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param CreateWatchRequest create_watch_request:
        :return: CreateWatchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'create_watch_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method watch" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/watch', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateWatchResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def write(self, **kwargs):  # noqa: E501
        """Writing by Template  # noqa: E501

        For writing information. The nodeId must be an entity. Data is written using field types as specified in the Template with associated storage ids and values.  Where an information node of the required field type relative to the entity already exists, the result depends on the node field type. If the field is *uniqueByParent*, then the information node is replaced by the new value. Otherwise, a new information node is created.  #### Example In this example, we write information nodes using a template and then update them using the same template. We use the previously created template from the `/createtemplate` example with id `00000000674AF75DB0F4F1DF9713E09296687718E8157EA3`. We write information nodes under some entity with Factern Id `000000004CCE0E488BA795B084CDED1844779A0CB37A87C4` also providing the Factern Id of the template. In this example we store address data in the default store, but use `interfaceId` `00000000BBA2A97903D1338286F1BBA117D6F48F68A996B5` for storing name data. ~~~ POST /write {     \"templateId\": \":PersonProfile\",     \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\",     \"values\": [         {             \"data\": \"Bob Watson\",             \"storageId\": \"00000000BBA2A97903D1338286F1BBA117D6F48F68A996B5\"         },         \"Inverness Terrace\",         \"London\"     ] } ~~~ Response ~~~ {     \"nodes\": [{             \"fieldId\": \"000000008BFE6BB9A2A3F80F23DC6E738470F24B95E5102A\",             \"nodeId\": \"0000000043F912B92911FFE2A52E31066E8B653D3F7E8DE7\"         },         {             \"fieldId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA,             \"nodeId\": \"000000002B3CABC1694B029442124526A5B6137E9EABCAD1v\",             \"children\": [{                     \"fieldId\": \"0000000095E0F6B9F5480FD75DA9520E480AD3E89DC35D9A\",                     \"nodeId\": \"0000000099A8B1E3605B77F3EDB62B475DE739646041DFB9\"                 },                 {                     \"fieldId\": \"00000000F6EFF0C416BE603531C8BA77C36E8A9B29368FB5\",                     \"nodeId\": \"00000000F76AF7DFD004F6C321636CE9A53F62B05F009BFA\"                 }]         }] } ~~~ We now update those values using the same template. Because each of the fields is *uniqueByParent*, writing the data causes the existing data to be replaced. ~~~ POST /write {     \"templateId\": \":PersonProfile\",     \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\",     \"values\": [         {             \"data\": \"Robert Watson\",             \"storageId\": \"00000000BBA2A97903D1338286F1BBA117D6F48F68A996B5\"         },         \"Gloucester Place\",         \"London\"     ] } ~~~ Response ~~~ {     \"nodes\": [{             \"fieldId\": \"000000008BFE6BB9A2A3F80F23DC6E738470F24B95E5102A,             \"nodeId\": \"00000000CD3D53A29F9547FBC1DD3871C5F1B57580C0A4BD\"         },         {             \"fieldId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA\",             \"nodeId\": \"000000002B3CABC1694B029442124526A5B6137E9EABCAD1v\",             \"children\": [{                     \"fieldId\": \"0000000095E0F6B9F5480FD75DA9520E480AD3E89DC35D9A\",                     \"nodeId\": \"00000000C216B111BD06EDC263314D8ED448FC6A2AF97E10\"                 },                 {                     \"fieldId\": \"00000000F6EFF0C416BE603531C8BA77C36E8A9B29368FB5\",                     \"nodeId\": \"00000000A037E8C23E7681C8B5172464D45CD093BE7AEEB2\"                 }]         }] } ~~~ #### Example In this example, rather than specifying a templateId, we specify an inline template. We want to update the person's name and city but not street. ~~~ POST /write {     \"template\": [         \":PersonName\",         {             \":BasicAddress\": [                 \":City\"             ]         }],     \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\",     \"values\": [         {             \"data\": \"Bob Watson\",             \"storageId\": \"00000000BBA2A97903D1338286F1BBA117D6F48F68A996B5\"         },         \"Exeter\"     ] } ~~~ Response ~~~ {     \"nodes\": [{             \"fieldId\": \"000000008BFE6BB9A2A3F80F23DC6E738470F24B95E5102A\",             \"nodeId\": \"00000000F832B4AB8E1E2598800572EFFA1B390A75EAF717\"         },         {             \"fieldId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA\",             \"nodeId\": \"000000002B3CABC1694B029442124526A5B6137E9EABCAD1v\",             \"children\": [{                     \"fieldId\": \"00000000F6EFF0C416BE603531C8BA77C36E8A9B29368FB5\",                     \"nodeId\": \"000000004C61B66FBD267D0150D7D32AD9E1CCBA267845FE\"                 }]         }] } ~~~ #### Example In this example, we specify an inline template with a shorter syntax for referring to the city field. The syntax uses a forward slash to reference a nested field. ~~~ POST /write {     \"template\": [         \":PersonName\",         \":BasicAddress/:City\"         ],     \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\",     \"values\": [         {             \"data\": \"Bob Watson\",             \"storageId\": \"00000000BBA2A97903D1338286F1BBA117D6F48F68A996B5\"         },         \"Exeter\"     ] } ~~~ Response ~~~ {     \"nodes\": [{             \"fieldId\": \"000000008BFE6BB9A2A3F80F23DC6E738470F24B95E5102A\",             \"nodeId\": \"00000000F832B4AB8E1E2598800572EFFA1B390A75EAF717\"         },         {             \"fieldId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA\",             \"nodeId\": \"000000002B3CABC1694B029442124526A5B6137E9EABCAD1v\",             \"children\": [{                     \"fieldId\": \"00000000F6EFF0C416BE603531C8BA77C36E8A9B29368FB5\",                     \"nodeId\": \"000000004C61B66FBD267D0150D7D32AD9E1CCBA267845FE\"                 }]         }] } ~~~ #### Example In this example, We update the person's profile in a single document, without the need of separate `template` and `values`. ~~~ POST /write {     \"document\": [{             \":PersonName\": {                     \"data\": \"Bob Watson\",                     \"storageId\": \"00000000BBA2A97903D1338286F1BBA117D6F48F68A996B5\"                 },             },             {                 \":BasicAddress\": [{                     \":City\": \"Plymouth\"                     }]             }],     \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\" } ~~~ Response ~~~ {     \"nodes\": [{             \"fieldId\": \"000000008BFE6BB9A2A3F80F23DC6E738470F24B95E5102A\",             \"nodeId\": \"00000000EAED228D036D1176CA4FA596D6F360F998009D8A\"         },         {             \"fieldId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA\",             \"nodeId\": \"000000002B3CABC1694B029442124526A5B6137E9EABCAD1v\",             \"children\": [{                     \"fieldId\": \"00000000F6EFF0C416BE603531C8BA77C36E8A9B29368FB5\",                     \"nodeId\": \"0000000043D9D5305739F86B05E540DECEA24C5B7FDB16FA\"             }]         }] } ~~~ #### Example In this example, we specify an inline document with the shorter syntax for changing the name city. ~~~ POST /write {     \"document\": [{             \":PersonName\": {                     \"data\": \"Bob Watson\",                     \"storageId\": \"00000000BBA2A97903D1338286F1BBA117D6F48F68A996B5\"                 },             },             {                 \":BasicAddress/:City\": \"Plymouth\"             }],     \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\" } ~~~ Response ~~~ {     \"nodes\": [{             \"fieldId\": \"000000008BFE6BB9A2A3F80F23DC6E738470F24B95E5102A\",             \"nodeId\": \"00000000EAED228D036D1176CA4FA596D6F360F998009D8A\"         },         {             \"fieldId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA\",             \"nodeId\": \"000000002B3CABC1694B029442124526A5B6137E9EABCAD1v\",             \"children\": [{                     \"fieldId\": \"00000000F6EFF0C416BE603531C8BA77C36E8A9B29368FB5\",                     \"nodeId\": \"0000000043D9D5305739F86B05E540DECEA24C5B7FDB16FA\"             }]         }] } ~~~ #### Example In this example, we write information nodes using a template and then copy those information nodes under some different entity. We use the previously created template from the `/createtemplate` example with id `00000000674AF75DB0F4F1DF9713E09296687718E8157EA3`. We write information nodes under some entity with Factern Id `000000004CCE0E488BA795B084CDED1844779A0CB37A87C4` also providing the Factern Id of the template. ~~~ POST /write {     \"templateId\": \"00000000674AF75DB0F4F1DF9713E09296687718E8157EA3\",     \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\",     \"values\": [         \"Bob Watson\",         \"Inverness Terrace\",         \"London\"     ] } ~~~ Response ~~~ {     \"nodes\": [{             \"fieldId\": \"000000008BFE6BB9A2A3F80F23DC6E738470F24B95E5102A\",             \"nodeId\": \"0000000043F912B92911FFE2A52E31066E8B653D3F7E8DE7\"         },         {             \"fieldId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA,             \"nodeId\": \"000000002B3CABC1694B029442124526A5B6137E9EABCAD1v\",             \"children\": [{                     \"fieldId\": \"0000000095E0F6B9F5480FD75DA9520E480AD3E89DC35D9A\",                     \"nodeId\": \"0000000099A8B1E3605B77F3EDB62B475DE739646041DFB9\"                 },                 {                     \"fieldId\": \"00000000F6EFF0C416BE603531C8BA77C36E8A9B29368FB5\",                     \"nodeId\": \"00000000F76AF7DFD004F6C321636CE9A53F62B05F009BFA\"                 }]         }] } ~~~ We now copy those nodes under a different entity `000000006F54C21F6215EBFD46354D87600BD06B9DA61E10`, using the original entity `000000004CCE0E488BA795B084CDED1844779A0CB37A87C4` as the copy source. ~~~ POST /write {     \"templateId\": \"00000000674AF75DB0F4F1DF9713E09296687718E8157EA3\",     \"nodeId\": \"000000006F54C21F6215EBFD46354D87600BD06B9DA61E10\",     \"sourceNodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\" } ~~~ Response ~~~ {     \"nodes\": [{             \"fieldId\": \"000000008BFE6BB9A2A3F80F23DC6E738470F24B95E5102A\",             \"nodeId\": \"000000009EBDB39BB9D5058733809D468DF4BD12A54E58FE\"         },         {             \"fieldId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA,             \"nodeId\": \"0000000079CDD8C926AD8A26E5438FF43AAF3D75170DABC1\",             \"children\": [{                     \"fieldId\": \"0000000095E0F6B9F5480FD75DA9520E480AD3E89DC35D9A\",                     \"nodeId\": \"00000000B733BFE8C52CE1C0078B15A6CD1D4E78249D80E4\"                 },                 {                     \"fieldId\": \"00000000F6EFF0C416BE603531C8BA77C36E8A9B29368FB5\",                     \"nodeId\": \"00000000A71188E1FDFF66403839C9B12F36FC8F3A182212\"                 }]         }] } ~~~ #### Example In this example, we perform a copy that applies a json transform to the copied value. Create the data to be copied: ~~~ POST /write {   \"nodeId\": \":sourceEntity\"   \"document\": [{           \":PersonData\": {               \"data\": {                 \"full_name\": \"Bob Watson\",                 \"streetAddress\": \"Baker Street\"               }             }           }] } ~~~ Perform the copy, specifying a jolt transform. This particular transform will map the streetAddress json field to the field address.street and add a default value of London for address.city. ~~~ POST /write {   \"nodeId\": \":destinationEntity\",   \"sourceNodeId\": \":sourceEntity\",   \"template\": [\":PersonData\"],   \"transform\": [{     \"operation\": \"shift\",     \"spec\": {         \"full_name\": \"full_name\",         \"streetAddress\": \"address.street\"       }     },   {     \"operation\": \"default\",     \"spec\": {         \"address\": {             \"city\": \"London\"           }       }   }] } ~~~ Note that this is a fairly simple transform. To view the full documentation for jolt transforms see (https://github.com/bazaarvoice/jolt). Now we perform a read on the destination entity and see the transformed data. ~~~ POST /read {   \"nodeId\": \":destinationEntity\",   \"template\": [\":PersonData\"] } ~~~ The data would be copied as follows: ~~~ {   \"full_name\": \"Bob Watson\",   \"address\": {     \"street\": \"Baker Street\",     \"city\": \"London\"     } } ~~~  #### Example In this example, we update the person's profile in a single document. However, we will also specify the optional field `defaultStorageId` as `00000000FE5B4011E7FF923EA1652C5CEA59C1CEB897BC2B`, which will be used as the `storageId` for any item that does not specify a `storageId` explicitly. In this case, it would apply to the `City` field but not the `PersonName` field. Note that while this example uses a document as input, the `defaultStorageId` field can be specified for any `/write` request. ~~~ POST /write {     \"document\": [{             \":PersonName\": {                     \"data\": \"Bob Watson\",                     \"storageId\": \"00000000BBA2A97903D1338286F1BBA117D6F48F68A996B5\"                 },             },             {                 \":BasicAddress\": [{                     \":City\": \"Plymouth\"                     }]             }],     \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\",     \"defaultStorageId\": \"00000000FE5B4011E7FF923EA1652C5CEA59C1CEB897BC2B\" } ~~~ Response ~~~ {     \"nodes\": [{             \"fieldId\": \"000000008BFE6BB9A2A3F80F23DC6E738470F24B95E5102A\",             \"nodeId\": \"00000000EAED228D036D1176CA4FA596D6F360F998009D8A\"         },         {             \"fieldId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA\",             \"nodeId\": \"000000002B3CABC1694B029442124526A5B6137E9EABCAD1v\",             \"children\": [{                     \"fieldId\": \"00000000F6EFF0C416BE603531C8BA77C36E8A9B29368FB5\",                     \"nodeId\": \"0000000043D9D5305739F86B05E540DECEA24C5B7FDB16FA\"             }]         }] } ~~~ #### Example In this example, we introduce two new fields: *ClientList* and *ClientProfile*, where *ClientList* is a *branch* and *uniqueByParent*, as usual, but *ClientProfile* is not *uniqueByParent*. ~~~ POST /write {     \"document\": [{         \":ClientList\": [             {\":ClientProfile\": [                 {\":PersonName\": \"Bob Watson\"},                 {\":BasicAddress\": [                     {\":Street\": \"Baker Street\"}                 ]}             ]},             {\":ClientProfile\": [                 {\":PersonName\": \"Stan Moriarty\"},                 {\":BasicAddress\": [                     {\":Street\": \"Inverness Terrace\"}                 ]}             ]},         ]     }],     \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\" } ~~~ Note the use of multiple *ClientProfile* fields, which is allowed because it is not *uniqueByParent*. #### Example In this example, we take the previous example, but write the *ClientProfile* as references instead of direct values. For simplicity, we will assume that Bob Watson is the only client. Create a template that indicates that *ClientList* will contain references. ~~~ POST /createtemplate { ...   \"memberIds\": [     \":ClientList\": [       \":ClientProfile\": {           \"reference\":true         }     ]   ] } ~~~ Populate the entity. ~~~ \"nodeId\": \":BobWatsonEntity\" \"document\": [           {\":PersonName\": \"Bob Watson\"},           {\":BasicAddress\": [             {\":Street\": \"Baker Street\"}           ]}         ] }], ~~~ Write using the template, using a reference to BobWatsonEntity in place of the values. ~~~ POST /write {   \"document\": [{       \":ClientList\": [         \":ClientProfile\": {             \"nodeId\":\":BobWatsonEntity\"           }       ]   }],   \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\" } ~~~ Now we can perform a read, with the reference being automatically followed. ~~~ POST /read {   \"document\": [{       \":ClientList\": [         \":ClientProfile\": [           {\":PersonName\": \"Bob Watson\"},           {\":BasicAddress\": [             {\":Street\": \"Baker Street\"}           ]}         ]       ]   }],   \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\" } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.write(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param WriteRequest write_request:
        :return: WriteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.write_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.write_with_http_info(**kwargs)  # noqa: E501
            return data

    def write_with_http_info(self, **kwargs):  # noqa: E501
        """Writing by Template  # noqa: E501

        For writing information. The nodeId must be an entity. Data is written using field types as specified in the Template with associated storage ids and values.  Where an information node of the required field type relative to the entity already exists, the result depends on the node field type. If the field is *uniqueByParent*, then the information node is replaced by the new value. Otherwise, a new information node is created.  #### Example In this example, we write information nodes using a template and then update them using the same template. We use the previously created template from the `/createtemplate` example with id `00000000674AF75DB0F4F1DF9713E09296687718E8157EA3`. We write information nodes under some entity with Factern Id `000000004CCE0E488BA795B084CDED1844779A0CB37A87C4` also providing the Factern Id of the template. In this example we store address data in the default store, but use `interfaceId` `00000000BBA2A97903D1338286F1BBA117D6F48F68A996B5` for storing name data. ~~~ POST /write {     \"templateId\": \":PersonProfile\",     \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\",     \"values\": [         {             \"data\": \"Bob Watson\",             \"storageId\": \"00000000BBA2A97903D1338286F1BBA117D6F48F68A996B5\"         },         \"Inverness Terrace\",         \"London\"     ] } ~~~ Response ~~~ {     \"nodes\": [{             \"fieldId\": \"000000008BFE6BB9A2A3F80F23DC6E738470F24B95E5102A\",             \"nodeId\": \"0000000043F912B92911FFE2A52E31066E8B653D3F7E8DE7\"         },         {             \"fieldId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA,             \"nodeId\": \"000000002B3CABC1694B029442124526A5B6137E9EABCAD1v\",             \"children\": [{                     \"fieldId\": \"0000000095E0F6B9F5480FD75DA9520E480AD3E89DC35D9A\",                     \"nodeId\": \"0000000099A8B1E3605B77F3EDB62B475DE739646041DFB9\"                 },                 {                     \"fieldId\": \"00000000F6EFF0C416BE603531C8BA77C36E8A9B29368FB5\",                     \"nodeId\": \"00000000F76AF7DFD004F6C321636CE9A53F62B05F009BFA\"                 }]         }] } ~~~ We now update those values using the same template. Because each of the fields is *uniqueByParent*, writing the data causes the existing data to be replaced. ~~~ POST /write {     \"templateId\": \":PersonProfile\",     \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\",     \"values\": [         {             \"data\": \"Robert Watson\",             \"storageId\": \"00000000BBA2A97903D1338286F1BBA117D6F48F68A996B5\"         },         \"Gloucester Place\",         \"London\"     ] } ~~~ Response ~~~ {     \"nodes\": [{             \"fieldId\": \"000000008BFE6BB9A2A3F80F23DC6E738470F24B95E5102A,             \"nodeId\": \"00000000CD3D53A29F9547FBC1DD3871C5F1B57580C0A4BD\"         },         {             \"fieldId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA\",             \"nodeId\": \"000000002B3CABC1694B029442124526A5B6137E9EABCAD1v\",             \"children\": [{                     \"fieldId\": \"0000000095E0F6B9F5480FD75DA9520E480AD3E89DC35D9A\",                     \"nodeId\": \"00000000C216B111BD06EDC263314D8ED448FC6A2AF97E10\"                 },                 {                     \"fieldId\": \"00000000F6EFF0C416BE603531C8BA77C36E8A9B29368FB5\",                     \"nodeId\": \"00000000A037E8C23E7681C8B5172464D45CD093BE7AEEB2\"                 }]         }] } ~~~ #### Example In this example, rather than specifying a templateId, we specify an inline template. We want to update the person's name and city but not street. ~~~ POST /write {     \"template\": [         \":PersonName\",         {             \":BasicAddress\": [                 \":City\"             ]         }],     \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\",     \"values\": [         {             \"data\": \"Bob Watson\",             \"storageId\": \"00000000BBA2A97903D1338286F1BBA117D6F48F68A996B5\"         },         \"Exeter\"     ] } ~~~ Response ~~~ {     \"nodes\": [{             \"fieldId\": \"000000008BFE6BB9A2A3F80F23DC6E738470F24B95E5102A\",             \"nodeId\": \"00000000F832B4AB8E1E2598800572EFFA1B390A75EAF717\"         },         {             \"fieldId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA\",             \"nodeId\": \"000000002B3CABC1694B029442124526A5B6137E9EABCAD1v\",             \"children\": [{                     \"fieldId\": \"00000000F6EFF0C416BE603531C8BA77C36E8A9B29368FB5\",                     \"nodeId\": \"000000004C61B66FBD267D0150D7D32AD9E1CCBA267845FE\"                 }]         }] } ~~~ #### Example In this example, we specify an inline template with a shorter syntax for referring to the city field. The syntax uses a forward slash to reference a nested field. ~~~ POST /write {     \"template\": [         \":PersonName\",         \":BasicAddress/:City\"         ],     \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\",     \"values\": [         {             \"data\": \"Bob Watson\",             \"storageId\": \"00000000BBA2A97903D1338286F1BBA117D6F48F68A996B5\"         },         \"Exeter\"     ] } ~~~ Response ~~~ {     \"nodes\": [{             \"fieldId\": \"000000008BFE6BB9A2A3F80F23DC6E738470F24B95E5102A\",             \"nodeId\": \"00000000F832B4AB8E1E2598800572EFFA1B390A75EAF717\"         },         {             \"fieldId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA\",             \"nodeId\": \"000000002B3CABC1694B029442124526A5B6137E9EABCAD1v\",             \"children\": [{                     \"fieldId\": \"00000000F6EFF0C416BE603531C8BA77C36E8A9B29368FB5\",                     \"nodeId\": \"000000004C61B66FBD267D0150D7D32AD9E1CCBA267845FE\"                 }]         }] } ~~~ #### Example In this example, We update the person's profile in a single document, without the need of separate `template` and `values`. ~~~ POST /write {     \"document\": [{             \":PersonName\": {                     \"data\": \"Bob Watson\",                     \"storageId\": \"00000000BBA2A97903D1338286F1BBA117D6F48F68A996B5\"                 },             },             {                 \":BasicAddress\": [{                     \":City\": \"Plymouth\"                     }]             }],     \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\" } ~~~ Response ~~~ {     \"nodes\": [{             \"fieldId\": \"000000008BFE6BB9A2A3F80F23DC6E738470F24B95E5102A\",             \"nodeId\": \"00000000EAED228D036D1176CA4FA596D6F360F998009D8A\"         },         {             \"fieldId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA\",             \"nodeId\": \"000000002B3CABC1694B029442124526A5B6137E9EABCAD1v\",             \"children\": [{                     \"fieldId\": \"00000000F6EFF0C416BE603531C8BA77C36E8A9B29368FB5\",                     \"nodeId\": \"0000000043D9D5305739F86B05E540DECEA24C5B7FDB16FA\"             }]         }] } ~~~ #### Example In this example, we specify an inline document with the shorter syntax for changing the name city. ~~~ POST /write {     \"document\": [{             \":PersonName\": {                     \"data\": \"Bob Watson\",                     \"storageId\": \"00000000BBA2A97903D1338286F1BBA117D6F48F68A996B5\"                 },             },             {                 \":BasicAddress/:City\": \"Plymouth\"             }],     \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\" } ~~~ Response ~~~ {     \"nodes\": [{             \"fieldId\": \"000000008BFE6BB9A2A3F80F23DC6E738470F24B95E5102A\",             \"nodeId\": \"00000000EAED228D036D1176CA4FA596D6F360F998009D8A\"         },         {             \"fieldId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA\",             \"nodeId\": \"000000002B3CABC1694B029442124526A5B6137E9EABCAD1v\",             \"children\": [{                     \"fieldId\": \"00000000F6EFF0C416BE603531C8BA77C36E8A9B29368FB5\",                     \"nodeId\": \"0000000043D9D5305739F86B05E540DECEA24C5B7FDB16FA\"             }]         }] } ~~~ #### Example In this example, we write information nodes using a template and then copy those information nodes under some different entity. We use the previously created template from the `/createtemplate` example with id `00000000674AF75DB0F4F1DF9713E09296687718E8157EA3`. We write information nodes under some entity with Factern Id `000000004CCE0E488BA795B084CDED1844779A0CB37A87C4` also providing the Factern Id of the template. ~~~ POST /write {     \"templateId\": \"00000000674AF75DB0F4F1DF9713E09296687718E8157EA3\",     \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\",     \"values\": [         \"Bob Watson\",         \"Inverness Terrace\",         \"London\"     ] } ~~~ Response ~~~ {     \"nodes\": [{             \"fieldId\": \"000000008BFE6BB9A2A3F80F23DC6E738470F24B95E5102A\",             \"nodeId\": \"0000000043F912B92911FFE2A52E31066E8B653D3F7E8DE7\"         },         {             \"fieldId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA,             \"nodeId\": \"000000002B3CABC1694B029442124526A5B6137E9EABCAD1v\",             \"children\": [{                     \"fieldId\": \"0000000095E0F6B9F5480FD75DA9520E480AD3E89DC35D9A\",                     \"nodeId\": \"0000000099A8B1E3605B77F3EDB62B475DE739646041DFB9\"                 },                 {                     \"fieldId\": \"00000000F6EFF0C416BE603531C8BA77C36E8A9B29368FB5\",                     \"nodeId\": \"00000000F76AF7DFD004F6C321636CE9A53F62B05F009BFA\"                 }]         }] } ~~~ We now copy those nodes under a different entity `000000006F54C21F6215EBFD46354D87600BD06B9DA61E10`, using the original entity `000000004CCE0E488BA795B084CDED1844779A0CB37A87C4` as the copy source. ~~~ POST /write {     \"templateId\": \"00000000674AF75DB0F4F1DF9713E09296687718E8157EA3\",     \"nodeId\": \"000000006F54C21F6215EBFD46354D87600BD06B9DA61E10\",     \"sourceNodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\" } ~~~ Response ~~~ {     \"nodes\": [{             \"fieldId\": \"000000008BFE6BB9A2A3F80F23DC6E738470F24B95E5102A\",             \"nodeId\": \"000000009EBDB39BB9D5058733809D468DF4BD12A54E58FE\"         },         {             \"fieldId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA,             \"nodeId\": \"0000000079CDD8C926AD8A26E5438FF43AAF3D75170DABC1\",             \"children\": [{                     \"fieldId\": \"0000000095E0F6B9F5480FD75DA9520E480AD3E89DC35D9A\",                     \"nodeId\": \"00000000B733BFE8C52CE1C0078B15A6CD1D4E78249D80E4\"                 },                 {                     \"fieldId\": \"00000000F6EFF0C416BE603531C8BA77C36E8A9B29368FB5\",                     \"nodeId\": \"00000000A71188E1FDFF66403839C9B12F36FC8F3A182212\"                 }]         }] } ~~~ #### Example In this example, we perform a copy that applies a json transform to the copied value. Create the data to be copied: ~~~ POST /write {   \"nodeId\": \":sourceEntity\"   \"document\": [{           \":PersonData\": {               \"data\": {                 \"full_name\": \"Bob Watson\",                 \"streetAddress\": \"Baker Street\"               }             }           }] } ~~~ Perform the copy, specifying a jolt transform. This particular transform will map the streetAddress json field to the field address.street and add a default value of London for address.city. ~~~ POST /write {   \"nodeId\": \":destinationEntity\",   \"sourceNodeId\": \":sourceEntity\",   \"template\": [\":PersonData\"],   \"transform\": [{     \"operation\": \"shift\",     \"spec\": {         \"full_name\": \"full_name\",         \"streetAddress\": \"address.street\"       }     },   {     \"operation\": \"default\",     \"spec\": {         \"address\": {             \"city\": \"London\"           }       }   }] } ~~~ Note that this is a fairly simple transform. To view the full documentation for jolt transforms see (https://github.com/bazaarvoice/jolt). Now we perform a read on the destination entity and see the transformed data. ~~~ POST /read {   \"nodeId\": \":destinationEntity\",   \"template\": [\":PersonData\"] } ~~~ The data would be copied as follows: ~~~ {   \"full_name\": \"Bob Watson\",   \"address\": {     \"street\": \"Baker Street\",     \"city\": \"London\"     } } ~~~  #### Example In this example, we update the person's profile in a single document. However, we will also specify the optional field `defaultStorageId` as `00000000FE5B4011E7FF923EA1652C5CEA59C1CEB897BC2B`, which will be used as the `storageId` for any item that does not specify a `storageId` explicitly. In this case, it would apply to the `City` field but not the `PersonName` field. Note that while this example uses a document as input, the `defaultStorageId` field can be specified for any `/write` request. ~~~ POST /write {     \"document\": [{             \":PersonName\": {                     \"data\": \"Bob Watson\",                     \"storageId\": \"00000000BBA2A97903D1338286F1BBA117D6F48F68A996B5\"                 },             },             {                 \":BasicAddress\": [{                     \":City\": \"Plymouth\"                     }]             }],     \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\",     \"defaultStorageId\": \"00000000FE5B4011E7FF923EA1652C5CEA59C1CEB897BC2B\" } ~~~ Response ~~~ {     \"nodes\": [{             \"fieldId\": \"000000008BFE6BB9A2A3F80F23DC6E738470F24B95E5102A\",             \"nodeId\": \"00000000EAED228D036D1176CA4FA596D6F360F998009D8A\"         },         {             \"fieldId\": \"00000000AA512DD53AAB152FBFBBB03AEA078368351CBCBA\",             \"nodeId\": \"000000002B3CABC1694B029442124526A5B6137E9EABCAD1v\",             \"children\": [{                     \"fieldId\": \"00000000F6EFF0C416BE603531C8BA77C36E8A9B29368FB5\",                     \"nodeId\": \"0000000043D9D5305739F86B05E540DECEA24C5B7FDB16FA\"             }]         }] } ~~~ #### Example In this example, we introduce two new fields: *ClientList* and *ClientProfile*, where *ClientList* is a *branch* and *uniqueByParent*, as usual, but *ClientProfile* is not *uniqueByParent*. ~~~ POST /write {     \"document\": [{         \":ClientList\": [             {\":ClientProfile\": [                 {\":PersonName\": \"Bob Watson\"},                 {\":BasicAddress\": [                     {\":Street\": \"Baker Street\"}                 ]}             ]},             {\":ClientProfile\": [                 {\":PersonName\": \"Stan Moriarty\"},                 {\":BasicAddress\": [                     {\":Street\": \"Inverness Terrace\"}                 ]}             ]},         ]     }],     \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\" } ~~~ Note the use of multiple *ClientProfile* fields, which is allowed because it is not *uniqueByParent*. #### Example In this example, we take the previous example, but write the *ClientProfile* as references instead of direct values. For simplicity, we will assume that Bob Watson is the only client. Create a template that indicates that *ClientList* will contain references. ~~~ POST /createtemplate { ...   \"memberIds\": [     \":ClientList\": [       \":ClientProfile\": {           \"reference\":true         }     ]   ] } ~~~ Populate the entity. ~~~ \"nodeId\": \":BobWatsonEntity\" \"document\": [           {\":PersonName\": \"Bob Watson\"},           {\":BasicAddress\": [             {\":Street\": \"Baker Street\"}           ]}         ] }], ~~~ Write using the template, using a reference to BobWatsonEntity in place of the values. ~~~ POST /write {   \"document\": [{       \":ClientList\": [         \":ClientProfile\": {             \"nodeId\":\":BobWatsonEntity\"           }       ]   }],   \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\" } ~~~ Now we can perform a read, with the reference being automatically followed. ~~~ POST /read {   \"document\": [{       \":ClientList\": [         \":ClientProfile\": [           {\":PersonName\": \"Bob Watson\"},           {\":BasicAddress\": [             {\":Street\": \"Baker Street\"}           ]}         ]       ]   }],   \"nodeId\": \"000000004CCE0E488BA795B084CDED1844779A0CB37A87C4\" } ~~~  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.write_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str login:
        :param str representing:
        :param WriteRequest write_request:
        :return: WriteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['login', 'representing', 'write_request']  # noqa: E501
        all_params.append('async')
        all_params.append('body')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method write" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'login' in params:
            query_params.append(('login', params['login']))  # noqa: E501
        if 'representing' in params:
            query_params.append(('representing', params['representing']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/write', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WriteResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

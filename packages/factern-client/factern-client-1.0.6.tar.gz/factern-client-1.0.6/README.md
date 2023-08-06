# @factern/factern-client
[![Build Status](https://travis-ci.org/Factern/factern-client-python.svg?branch=master)](https://travis-ci.org/Factern/factern-client-python)

## Python Client for Factern API v2

- API version: 2.0.0
- Package version: 1.0.6
For more information, please visit [https://next.factern.com/company/contact](https://next.factern.com/company/contact)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

The python package is hosted on pypi, you can install directly from command line

```sh
pip install factern_client
```
(you may need to run `pip` with root permission: `sudo pip install factern_client`)

Then import the package:
```python
import factern_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import factern_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import factern_client
from factern_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = factern_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = factern_client.FactsApi(factern_client.ApiClient(configuration))
login = 'login_example' # str |  (optional)
representing = 'representing_example' # str |  (optional)
create_member_request = factern_client.CreateMemberRequest() # CreateMemberRequest |  (optional)

try:
    # Create Member
    api_response = api_instance.add_member(login=login, representing=representing, create_member_request=create_member_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FactsApi->add_member: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.factern.com/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FactsApi* | [**add_member**](docs/FactsApi.md#add_member) | **POST** /createmember | Create Member
*FactsApi* | [**bid**](docs/FactsApi.md#bid) | **POST** /createbid | Create Bid
*FactsApi* | [**create_alias**](docs/FactsApi.md#create_alias) | **POST** /createalias | Create Alias
*FactsApi* | [**create_application**](docs/FactsApi.md#create_application) | **POST** /createapplication | Create Application
*FactsApi* | [**create_domain**](docs/FactsApi.md#create_domain) | **POST** /createdomain | Create Domain
*FactsApi* | [**create_entity**](docs/FactsApi.md#create_entity) | **POST** /createentity | Create Entity
*FactsApi* | [**create_field**](docs/FactsApi.md#create_field) | **POST** /createfield | Create Field
*FactsApi* | [**create_filter**](docs/FactsApi.md#create_filter) | **POST** /createfilter | Create Filter
*FactsApi* | [**create_group**](docs/FactsApi.md#create_group) | **POST** /creategroup | Create Group
*FactsApi* | [**create_information**](docs/FactsApi.md#create_information) | **POST** /createinformation | Create Information
*FactsApi* | [**create_interface**](docs/FactsApi.md#create_interface) | **POST** /createinterface | Create Interface
*FactsApi* | [**create_label_list**](docs/FactsApi.md#create_label_list) | **POST** /createlabellist | Create Label List
*FactsApi* | [**create_login**](docs/FactsApi.md#create_login) | **POST** /createlogin | Create Login
*FactsApi* | [**create_mirror**](docs/FactsApi.md#create_mirror) | **POST** /createmirror | Create Mirror
*FactsApi* | [**create_price**](docs/FactsApi.md#create_price) | **POST** /createprice | Create Price
*FactsApi* | [**create_scope**](docs/FactsApi.md#create_scope) | **POST** /createscope | Create Scope
*FactsApi* | [**create_statement**](docs/FactsApi.md#create_statement) | **POST** /createstatement | Create Statement
*FactsApi* | [**create_template**](docs/FactsApi.md#create_template) | **POST** /createtemplate | Create Template
*FactsApi* | [**delete**](docs/FactsApi.md#delete) | **POST** /delete | Deleting
*FactsApi* | [**delete_node**](docs/FactsApi.md#delete_node) | **POST** /deletenode | Delete Node
*FactsApi* | [**describe**](docs/FactsApi.md#describe) | **POST** /describe | Describe
*FactsApi* | [**history**](docs/FactsApi.md#history) | **POST** /history | History
*FactsApi* | [**label**](docs/FactsApi.md#label) | **POST** /label | Label a Node
*FactsApi* | [**obliterate**](docs/FactsApi.md#obliterate) | **POST** /obliterate | Obliterating Information Nodes
*FactsApi* | [**permission**](docs/FactsApi.md#permission) | **POST** /permission | Create Permission
*FactsApi* | [**read**](docs/FactsApi.md#read) | **POST** /read | Reading
*FactsApi* | [**read_information**](docs/FactsApi.md#read_information) | **POST** /readinformation | Read Information
*FactsApi* | [**replace_information**](docs/FactsApi.md#replace_information) | **POST** /replaceinformation | Replace
*FactsApi* | [**request_permission**](docs/FactsApi.md#request_permission) | **POST** /requestpermission | Request Permission
*FactsApi* | [**reset_login**](docs/FactsApi.md#reset_login) | **POST** /resetlogin | Changing Login Password
*FactsApi* | [**search_alias**](docs/FactsApi.md#search_alias) | **POST** /searchalias | Search For Alias
*FactsApi* | [**search_entity**](docs/FactsApi.md#search_entity) | **POST** /searchentity | Search For Entity
*FactsApi* | [**settle_account**](docs/FactsApi.md#settle_account) | **POST** /settleaccount | Settle Account
*FactsApi* | [**update_application**](docs/FactsApi.md#update_application) | **POST** /updateapplication | Resetting Application Secret
*FactsApi* | [**update_status**](docs/FactsApi.md#update_status) | **POST** /updatestatus | Enabling/Disabling Nodes
*FactsApi* | [**watch**](docs/FactsApi.md#watch) | **POST** /watch | Create Watch Trigger
*FactsApi* | [**write**](docs/FactsApi.md#write) | **POST** /write | Writing by Template


## Documentation For Models

 - [Account](docs/Account.md)
 - [AddLabelRequest](docs/AddLabelRequest.md)
 - [AddLabelResponse](docs/AddLabelResponse.md)
 - [AddStatementRequest](docs/AddStatementRequest.md)
 - [AddStatementResponse](docs/AddStatementResponse.md)
 - [Agent](docs/Agent.md)
 - [Alias](docs/Alias.md)
 - [AliasNode](docs/AliasNode.md)
 - [ApiEndpoint](docs/ApiEndpoint.md)
 - [Application](docs/Application.md)
 - [ApplicationNode](docs/ApplicationNode.md)
 - [BaseRequest](docs/BaseRequest.md)
 - [BaseResponse](docs/BaseResponse.md)
 - [Bid](docs/Bid.md)
 - [BidNode](docs/BidNode.md)
 - [Cost](docs/Cost.md)
 - [CreateAliasRequest](docs/CreateAliasRequest.md)
 - [CreateAliasResponse](docs/CreateAliasResponse.md)
 - [CreateApplicationRequest](docs/CreateApplicationRequest.md)
 - [CreateApplicationResponse](docs/CreateApplicationResponse.md)
 - [CreateBidRequest](docs/CreateBidRequest.md)
 - [CreateBidResponse](docs/CreateBidResponse.md)
 - [CreateChildRequest](docs/CreateChildRequest.md)
 - [CreateDomainRequest](docs/CreateDomainRequest.md)
 - [CreateDomainResponse](docs/CreateDomainResponse.md)
 - [CreateEntityRequest](docs/CreateEntityRequest.md)
 - [CreateEntityResponse](docs/CreateEntityResponse.md)
 - [CreateFieldRequest](docs/CreateFieldRequest.md)
 - [CreateFieldResponse](docs/CreateFieldResponse.md)
 - [CreateFilterRequest](docs/CreateFilterRequest.md)
 - [CreateFilterResponse](docs/CreateFilterResponse.md)
 - [CreateGroupRequest](docs/CreateGroupRequest.md)
 - [CreateGroupResponse](docs/CreateGroupResponse.md)
 - [CreateInformationRequest](docs/CreateInformationRequest.md)
 - [CreateInformationResponse](docs/CreateInformationResponse.md)
 - [CreateInterfaceRequest](docs/CreateInterfaceRequest.md)
 - [CreateInterfaceResponse](docs/CreateInterfaceResponse.md)
 - [CreateLabelListRequest](docs/CreateLabelListRequest.md)
 - [CreateLabelListResponse](docs/CreateLabelListResponse.md)
 - [CreateLoginRequest](docs/CreateLoginRequest.md)
 - [CreateLoginResponse](docs/CreateLoginResponse.md)
 - [CreateMemberRequest](docs/CreateMemberRequest.md)
 - [CreateMemberResponse](docs/CreateMemberResponse.md)
 - [CreateMirrorRequest](docs/CreateMirrorRequest.md)
 - [CreateMirrorResponse](docs/CreateMirrorResponse.md)
 - [CreateNamedRequest](docs/CreateNamedRequest.md)
 - [CreatePermissionRequest](docs/CreatePermissionRequest.md)
 - [CreatePermissionResponse](docs/CreatePermissionResponse.md)
 - [CreatePriceRequest](docs/CreatePriceRequest.md)
 - [CreatePriceResponse](docs/CreatePriceResponse.md)
 - [CreateScopeRequest](docs/CreateScopeRequest.md)
 - [CreateScopeResponse](docs/CreateScopeResponse.md)
 - [CreateTemplateRequest](docs/CreateTemplateRequest.md)
 - [CreateTemplateResponse](docs/CreateTemplateResponse.md)
 - [CreateWatchRequest](docs/CreateWatchRequest.md)
 - [CreateWatchResponse](docs/CreateWatchResponse.md)
 - [DeleteRequest](docs/DeleteRequest.md)
 - [DeleteResponse](docs/DeleteResponse.md)
 - [DeletedItem](docs/DeletedItem.md)
 - [DeletedStatusItem](docs/DeletedStatusItem.md)
 - [DescribeRequest](docs/DescribeRequest.md)
 - [DescribeResponse](docs/DescribeResponse.md)
 - [Domain](docs/Domain.md)
 - [DomainNode](docs/DomainNode.md)
 - [Entity](docs/Entity.md)
 - [EntityListResponse](docs/EntityListResponse.md)
 - [EntityNode](docs/EntityNode.md)
 - [ExternalDataUsage](docs/ExternalDataUsage.md)
 - [FactCount](docs/FactCount.md)
 - [Field](docs/Field.md)
 - [FieldNode](docs/FieldNode.md)
 - [FieldStoreValues](docs/FieldStoreValues.md)
 - [Filter](docs/Filter.md)
 - [FilterNode](docs/FilterNode.md)
 - [FilterStatement](docs/FilterStatement.md)
 - [GasCost](docs/GasCost.md)
 - [Group](docs/Group.md)
 - [GroupNode](docs/GroupNode.md)
 - [HttpHeader](docs/HttpHeader.md)
 - [Information](docs/Information.md)
 - [InformationListResponse](docs/InformationListResponse.md)
 - [InformationNode](docs/InformationNode.md)
 - [Interface](docs/Interface.md)
 - [InterfaceNode](docs/InterfaceNode.md)
 - [Label](docs/Label.md)
 - [LabelList](docs/LabelList.md)
 - [LabelListMember](docs/LabelListMember.md)
 - [LabelListMemberNode](docs/LabelListMemberNode.md)
 - [LabelListNode](docs/LabelListNode.md)
 - [LabelStatement](docs/LabelStatement.md)
 - [ListCriteria](docs/ListCriteria.md)
 - [Login](docs/Login.md)
 - [LoginNode](docs/LoginNode.md)
 - [Member](docs/Member.md)
 - [MemberNode](docs/MemberNode.md)
 - [Mirror](docs/Mirror.md)
 - [MirrorNode](docs/MirrorNode.md)
 - [NamedNode](docs/NamedNode.md)
 - [NodeIdRequest](docs/NodeIdRequest.md)
 - [NodeListing](docs/NodeListing.md)
 - [Permission](docs/Permission.md)
 - [PermissionAction](docs/PermissionAction.md)
 - [PermissionEffect](docs/PermissionEffect.md)
 - [PermissionNode](docs/PermissionNode.md)
 - [PermissionPolicyDocument](docs/PermissionPolicyDocument.md)
 - [Price](docs/Price.md)
 - [PriceDetails](docs/PriceDetails.md)
 - [PriceNode](docs/PriceNode.md)
 - [ReadInformationRequest](docs/ReadInformationRequest.md)
 - [ReadInformationResponse](docs/ReadInformationResponse.md)
 - [ReadItem](docs/ReadItem.md)
 - [ReadRequest](docs/ReadRequest.md)
 - [ReadResponse](docs/ReadResponse.md)
 - [ReadStatusItem](docs/ReadStatusItem.md)
 - [ReplaceFieldRequest](docs/ReplaceFieldRequest.md)
 - [ResetLoginCredentialsRequest](docs/ResetLoginCredentialsRequest.md)
 - [ResetLoginResponse](docs/ResetLoginResponse.md)
 - [Scope](docs/Scope.md)
 - [ScopeNode](docs/ScopeNode.md)
 - [SearchAliasRequest](docs/SearchAliasRequest.md)
 - [SearchAliasResponse](docs/SearchAliasResponse.md)
 - [SearchEntityRequest](docs/SearchEntityRequest.md)
 - [Searches](docs/Searches.md)
 - [SettleAccountRequest](docs/SettleAccountRequest.md)
 - [SettleAccountResponse](docs/SettleAccountResponse.md)
 - [StandardNode](docs/StandardNode.md)
 - [StandardNodeResponse](docs/StandardNodeResponse.md)
 - [Statement](docs/Statement.md)
 - [StatementStatement](docs/StatementStatement.md)
 - [Summary](docs/Summary.md)
 - [Template](docs/Template.md)
 - [TemplateNode](docs/TemplateNode.md)
 - [TokenPayment](docs/TokenPayment.md)
 - [TransformElement](docs/TransformElement.md)
 - [UpdateApplicationRequest](docs/UpdateApplicationRequest.md)
 - [UpdateApplicationResponse](docs/UpdateApplicationResponse.md)
 - [UpdateStatusRequest](docs/UpdateStatusRequest.md)
 - [Watch](docs/Watch.md)
 - [WatchEvent](docs/WatchEvent.md)
 - [WatchEventNode](docs/WatchEventNode.md)
 - [WatchNode](docs/WatchNode.md)
 - [WriteItem](docs/WriteItem.md)
 - [WriteRequest](docs/WriteRequest.md)
 - [WriteResponse](docs/WriteResponse.md)


## Documentation For Authorization


## OAuth2

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://factern-test.eu.auth0.com/oauth/token
- **Scopes**: 
 - **address**: Grants read access
 - **email**: Grants read and write access to administrative information
 - **openid**: Grants read and write access to administrative information
 - **phone**: Grants write access
 - **profile**: Grants read and write access to administrative information


## Author

Factern Ltd.
mailto:support@factern.com


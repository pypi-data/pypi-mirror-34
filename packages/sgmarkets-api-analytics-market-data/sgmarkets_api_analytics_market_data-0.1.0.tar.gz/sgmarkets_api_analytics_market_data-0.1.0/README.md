# SG Markets Analytics API - SG Market Data v2

 **SG Analytics Data API gives access to quotes and descriptions of more than 500k intruments** covering a wide cross-asset scope: Equity, Bonds, Credit, Forex, Commodities. 

Data comes from either SG research and SG trading desks or external sources such as ICAP or Markit.

The Market Data Analytics API provides endpoints to retrieve:
+ descriptions and indicators for each asset
+ assets using enhanced criteria and filters.
+ Historical quotes
+ Intraday quotes
+ Real time data (user needs privileged rights)

For more informations check out the [API descrition (swagger)](https://analytics-api.sgmarkets.com/data/swagger/ui/index#/)

## 1 - Introduction

This repo is meant to help clients (and employees) to tap SG Research APIs.  

This is a work in a progress and subject to change. All the major endpoints are covered and more notebooks are in coming soon.

The usual way to expose an API is to make a swagger available and also a GUI, typically a web page.

These have the following drawbacks:

A swagger is as precise as it is dull. Unless clients are (working with) IT savvy people they will have a hard time taking advantage of it. In short it is not enough. 
A GUI is easy to use but often as much a help as a hindrance: They are very slow/costly to build/adapt, are seldom as flexible as the underlying API, and are no help for industrial use of the API.


To fill the gap, we introduce the Jupyter notebook as an API consumption tool (It as many other uses).
The associated Python package used here has a very simple interface, but can be arbitrarily modified for (and by) an advanced user. It has the same display capabilities as a web page (being one itself). Most importantly is is written in Python so can be evolved by a business user (as opposed to a web frontend which is invariably delegated to specialist developpers).

## 2 - Repository

This repo contains:
+ a ready-to-use demo notebook
+ the underlying library in folder sgmarkets_api_analytics_market_data

The demo Jupyter notebook is a convenient and versatile interface to:
+ 'hide the plumbing'
+ authenticate through the corporate proxy
+ get the SG API access token (Auth v1.0)
+ make API calls explicit and readable
+ analyze the API response
+ display the results as tables and graphs - and save them


## 3 - Install

From terminal:

```python
# download and install package from pypi.org
pip install sgmarkets_api_analytics_market_data

#launch notebook
jupyter notebook
```

Create a notebook or run the demo notebook and modify it to your own use case.


## 4 - User guide

To use this library, authentication is required.

Authentication is made easy with the [sgmarkets-api-auth library](https://gitlab.com/sgmarkets/sgmarkets-api-auth).  
All you need is your [SG-markets](https://www.sgmarkets.com/services) credentials. If you don't have access, please contact your sales person. 

Read the [demo notebook](TBD) for a hands-on introduction.

The key steps are the following.

### 4.1 - Read the info

The package contains the corresponding [API swagger url](https://analytics-api.sgmarkets.com/data/swagger/ui/index#/) and contact info:

```python
import sgmarkets_api_analytics_market_data as SGMD

# info about SGMD
SGMD.info()
```

### 4.2 - Define you credentials

See the [user guide](https://gitlab.com/sgmarkets/sgmarkets-api-auth/blob/master/README.md) in the sgmarkets-api-auth repo.


### 4.3 - Pick an endpoint

Select it from the list of those available in the package.  

```python
import sgmarkets_api_analytics_market_data as SG

# Examples
ep = SGMD.endpoint.v2_quotas
ep = SGMD.endpoint.v2_quotes
ep = SGMD.endpoint.v2_product
```

### 4.4 - Create the associated request

Each end point comes with a Request object.  

```python
# For all endpoints
rq = ep.request()
```

And fill the object with the necessary data.
This part is specific to the endpoint selected.
See the demo notebook for examples.  

Then explore your Request object to make sure it is properly set.
```python
# For all endpoints
# display the structure of the object
rq.info()
```

### 4.5 - Call the API

You can call the API directly from the Request object.  

```python
# For all endpoints
# a is an Api object (see 4.2)
res = rq.call_api(a)
```

The returned object is a Response object associated to this endpoint.
You can explore it starting with

```python
# For all endpoints
# display the structure of the object
res.info()
```


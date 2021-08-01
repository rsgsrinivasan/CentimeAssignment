from utilities.configurations import *
from utilities.resources import *
import requests
from behave import *
import json
import time
import behave

@given('the name of the company for stock history')
def stepImplementation(context):
    context.requestCount = 1
    context.URL = getConfig()['API']['endpoint'] + ApiResources.get + "?" + "function=" + getConfig()['FUNCTION']['function'] + "&" + "symbol=" + "IBM" + "&" + "apikey=" + context.ApiKey

@given('the name of the company for stock history (no APIKEY)')
def stepImplementation(context):
    context.URL = getConfig()['API']['endpoint'] + ApiResources.get + "?" + "function=" + getConfig()['FUNCTION']['function'] + "&" + "symbol=" + "IBM" + "&" + "apikey=" + context.ApiKey

@when('we get the response from API')
def stepImplementation(context):
    context.response = requests.get(context.URL)

@then('the stock price query is succefull')
def stepImplementation(context):
    responseData = context.response.json()
    context.log.info(responseData)
    assert "Meta Data" in responseData

@given('the name of the invalid company code {symbol} for stock history')
def stepImplementation(context,symbol):
    context.requestCount = 1
    context.ApiKey = open("ApiKey.txt","r").read()
    context.URL = getConfig()['API']['endpoint'] + ApiResources.get + "?" + "function=" + getConfig()['FUNCTION']['function'] + "&" + "symbol=" + symbol + "&" + "apikey=" + context.ApiKey


@then('the stock price query is unsuccefull')
def stepImplementation(context):
    context.log.info(context.response.text)
    assert "Invalid API call" in context.response.text


@given('the name of the {symbol} for stock history')
def stepImplementation(context,symbol):
    context.URL = getConfig()['API']['endpoint'] + ApiResources.get + "?" + "function=" + getConfig()['FUNCTION']['function'] + "&" + "symbol=" + symbol + "&" + "apikey=" + context.ApiKey


@then('the 6th stock price query is unsuccessfull {count}')
def stepImplementation(context,count):
    context.log.info(context.response.text)
    if int(count) > 5:
        assert ("Thank you for using Alpha Vantage!" in context.response.text)
    else:
        assert ("Meta Data" in context.response.text)


@then('the json response should contain previous days stock price low and high')
def stepImplementation(context):
    data = context.response.json()
    context.log.info(data['Meta Data']['3. Last Refreshed'],list(data['Time Series (Daily)'].keys())[0])
    # comparing dates
    assert (data['Meta Data']['3. Last Refreshed'] == list(data['Time Series (Daily)'].keys())[0])


@then('the stock price query is unsuccessfull with error invalid key')
def stepImplementation(context):
    context.log.info(context.response.text)
    # comparing dates
    assert "the parameter apikey is invalid or missing" in context.response.text

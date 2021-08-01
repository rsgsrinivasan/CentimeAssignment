from utilities.configurations import *
from utilities.resources import *
import requests
from behave import *
import json
import time


@given('the name of the company for stock history')
def stepImplementation(context):
    context.requestCount = 1
    context.ApiKey = open("ApiKey.txt","r").read()
    context.URL = getConfig()['API']['endpoint'] + ApiResources.get + "?" + "function=" + getConfig()['FUNCTION']['function'] + "&" + "symbol=" + "IBM" + "&" + "apikey=" + context.ApiKey

@when('we get the stock price history')
def stepImplementation(context):
    context.response = requests.get(context.URL)

@then('the stock price query is succefull')
def stepImplementation(context):
    responseData = context.response.json()
    assert "Meta Data" in responseData


@given('the name of the invalid company code {symbol} for stock history')
def stepImplementation(context,symbol):
    context.requestCount = 1
    context.ApiKey = open("ApiKey.txt","r").read()
    context.URL = getConfig()['API']['endpoint'] + ApiResources.get + "?" + "function=" + getConfig()['FUNCTION']['function'] + "&" + "symbol=" + symbol + "&" + "apikey=" + context.ApiKey


@then('the stock price query is unsuccefull')
def stepImplementation(context):
    assert "Invalid API call" in context.response.text


@given('the name of the {symbol} for stock history')
def stepImplementation(context,symbol):
    context.ApiKey = open("ApiKey.txt","r").read()
    context.URL = getConfig()['API']['endpoint'] + ApiResources.get + "?" + "function=" + getConfig()['FUNCTION']['function'] + "&" + "symbol=" + symbol + "&" + "apikey=" + context.ApiKey


@then('the 6th stock price query is unsuccessfull {count}')
def stepImplementation(context,count):
    if int(count) > 5:
        assert ("Thank you for using Alpha Vantage!" in context.response.text)
    else:
        assert ("Meta Data" in context.response.text)


@then('the json response should contain previous days stock price low and high')
def stepImplementation(context):
    data = context.response.json()
    # comparing dates
    assert (data['Meta Data']['3. Last Refreshed'] == list(data['Time Series (Daily)'].keys())[0])

# Alpha Vantage daily stock time series API testing Library

The present library tests the alpha vantage api for daily time series data.

The library is designed to be used with the behave BDD test framework

## Prerequisites
Python 3.8.5

## Installation

```bash
$ cd centime/Scripts
$ activate
$ cd ../..
$ pip install -r requirements.txt
```


## Basic usage
- In the present library, the API endpoint and function type are defined as `https://www.alphavantage.co/` and `function = TIME_SERIES_DAILY` in `utilities/properties.ini` file. The function can be changed based on requirement. 
- Refer [alphavantage Documentation](https://www.alphavantage.co/documentation/) for information on other functions.
- Set the ApiKey in `ApiKey.txt`. Claim your free apikey from [here](https://www.alphavantage.co/support/#api-key) and replace it with your own `ApiKey`
- The API testing is written in `BDD framework`. All the test case scenarios are defined in `features/StocksTest.feature`.
- The daily stock series data query url contains `symbol` which is the company symbol. The test case company `symbols` are defined in the `Examples` of the `Scenario: Verify json response from API for last refreshed stock price data`.
```bash
Examples:
| symbol |
|  IBM   |
| DAI.DEX|
|TSCO.LON|
|SHOP.TRT|
|RELIANCE.BSE|
```
- The testing library tests the alphavantage API for the following five scenarios
    - **Scenario 1**: Verify response from API
    - **Scenario 2**: Verify json response from API for last refreshed stock price data
    - **Scenario 3**: Verify response from API with Invalid company code
    - **Scenario 4**: Verify throttling limit of API by requesting more than 5 requests per minute
- **Note**: It is not recomended to change any of the symbols already defined in `Examples` of other `scenarios` other than the `Scenario: Verify json response from API for last refreshed stock price data`.. 

## Running all test cases together
To run all the test cases together and generate html report use the command:
```bash
$ behave -f html -o Reports/behave-report.html
```
**Note**: There will be a `60 seconds` pause before executing the `throttling test` of `5 requests per minute`.

## Running a single test
The test cases are defined with certain tags namely `@regularTests` and `@throttlingTest5RPM`.
```bash
$ behave --tags="@throttlingTest5RPM" -f html -o Reports/behave-report.html
```

## Adding more scenarios
Some more additional scenrios can be added. Refer [behave](https://behave.readthedocs.io/en/stable/) documentation for more information. 


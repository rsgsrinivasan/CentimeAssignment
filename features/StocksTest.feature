Feature: Get daily stock price time series data from API
    @regularTests
    Scenario: Verify response from API
        Given the name of the company for stock history
        When we get the stock price history
        Then the stock price query is succefull
    
    @regularTests
    Scenario: Verify json response from API for last refreshed stock price data
        Given the name of the company for stock history
        When we get the stock price history
        Then the json response should contain previous days stock price low and high

    @regularTests
    Scenario Outline: Verify response from API with Invalid company code
        Given the name of the invalid company code <symbol> for stock history
        When we get the stock price history
        Then the stock price query is unsuccefull
        Examples:
        | symbol |
        |  IBMSA |

    @throttlingTest5RPM
    Scenario Outline: Requesting 5 requests per minute
        Given the name of the <symbol> for stock history
        When we get the stock price history
        Then the 6th stock price query is unsuccessfull <count>
        Examples:
        |count| symbol |
        |1    |  IBM   |
        |2    | DAI.DEX|
        |3    |TSCO.LON|
        |4    |SHOP.TRT|
        |5    |RELIANCE.BSE|
        |6    |600104|


   
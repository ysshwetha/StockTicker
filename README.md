# Stock Ticker Application
This application receives a ticker input from a user and provides the latest stock value as the output

## Key Points:
1. This program calls Yahoo Finance API https://www.yahoofinanceapi.com/ to get the stock results 
2. This API needs an access token, a free version of token is used within the program, **it has a hard limit of 100 requests per day**
3. This programs expects one or more(upto 10) ticker value in a comma separated format as input from console 
4. If no input is provided, program exits with a meaningful message. If the ticker value provided is not valid, program displays a helpful message
5. Stock value is rounded to 2 digits 

## Pre requisites:
1. Python 3 installation
2. This program uses 2 libraries, Please install these libraries by uncommenting the first two lines of code
    - requests : To make a HTTP call
    - json : To format the results
  
## Usage:

```
python3 StockPrice.py
Please enter the ticker(s) separated by comma : AMZN,AAPL
The latest stock value for Amazon.com, Inc.(AMZN) is : 3152.79
The latest stock value for Apple Inc.(AAPL) is : 172.39
```

## Assumptions:

1. From the API response, ‘regularMarketPrice’ is displayed as the latest stock output, this is based on my best judgement
2. Application will work if the API schema remains same as when the program was written 
3. This program does not provide historical data or full stock details (such as high price, low price etc), however it can be included easily if needed

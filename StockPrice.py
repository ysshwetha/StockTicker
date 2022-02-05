# Install library if already not present, uncomment the 2 lines below for installation

#pip install "requests"
#pip install "json"

import requests # HTTP Library
import json

access_token = 'vHdL4dVNO7abKi7kr5WxA9l02hEhSXsq2SJbUkvF'

# Get the input from user
ticker_inp = input("Please enter the ticker(s) separated by comma : ")

# If no input is entered, exit the application
if ticker_inp=='':
	print("No input entered,application will exit")
	quit()

# Define a function to get stock details from YahooFinance API, # Website : https://www.yahoofinanceapi.com/
def getStock(inp):
	inp = inp.replace(" ","")
	# We use access token generated from Yahoo Finance Website, Free access token provides 100 API requests per day
	header_value={'accept':'application/json' , 'X-API-KEY':access_token}
	url_value=('https://yfapi.net/v6/finance/quote?region=US&lang=en&symbols={0}'.format(inp)) # We use the ticker input provided by user
	apiresponse = requests.get(url=url_value,headers=header_value) # HTTPS call to the website
	jsonresponse = json.loads(apiresponse.text) # Convert the results to JSON
	jsonresult = jsonresponse['quoteResponse']['result'] # Extract the results
	return jsonresult


def printResult(stk_results, ticker_inp):
	# Now let us do some validation
	if len(stk_results) == 0:
		print('No Stock details found for Ticker {0}'.format(ticker_inp))
		quit()

	# Split the tickers into individual values to validate each one
	individual_ticker = ticker_inp.split(',')

	for i in (individual_ticker):
		found = False
		for j in list(stk_results):		
			if i.upper().strip() == j['symbol']:
				print("The latest stock value for {0}({1}) is : {2:.2f}".format(j['longName'],j['symbol'],j['regularMarketPrice']))
				found = True
				break
			
		if found == False:
			print('No Stock details found for Ticker ' + i )	

# Call the Stock Function
stk_results=getStock(ticker_inp)
printResult(stk_results, ticker_inp)
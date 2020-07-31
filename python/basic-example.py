# if you haven't installed requests, get it via 'pip install requests'
import requests
# if you haven't installed pandas, get it via 'pip install pandas'
import pandas as pd

# here you have to enter your actual API key from SimFin
api_key = "YOUR_API_KEY"

# list of tickers we want to get data for
tickers = ["AAPL", "NVDA", "WMT"]

# define the periods that we want to retrieve
periods = ["q1", "q2", "q3", "q4"]
year_start = 2012
year_end = 2020

# request url for all financial statements
request_url = 'https://simfin.com/api/v2/companies/statements'

# variable to store the names of the columns
columns = []
# variable to store our data
output = []

# if you don't have a SimFin+ subscription, you can only request data for single companies and one period at a time (with SimFin+, you can request multiple tickers and periods at once)
for ticker in tickers:
    # loop through years:
    for year in range(year_start, year_end + 1):
        # loop through periods
        for period in periods:

            # define the parameters for the query
            parameters = {"statement": "pl", "ticker": ticker, "period": period, "fyear": year, "api-key": api_key}
            # make the request
            request = requests.get(request_url, parameters)

            # convert response to json and take 0th index as we only requested one ticker (if more than one ticker is requested, the data for the nth ticker will be at the nth position in the result returned from the API)
            data = request.json()[0]

            # make sure that data was found
            if data['found'] and len(data['data']) > 0:
                # add the column descriptions once only
                if len(columns) == 0:
                    columns = data['columns']
                # add the data
                output += data['data']

# make dataframe from output
df = pd.DataFrame(output, columns=columns)

# save to XLSX
# set up the XLSX writer
writer = pd.ExcelWriter("simfin_data.xlsx", engine='xlsxwriter')
# write data and close file
df.to_excel(writer)
writer.save()
writer.close()

# if you haven't installed requests, get it via 'pip install requests'
import requests
# if you haven't installed pandas, get it via 'pip install pandas'
import pandas as pd

# here you have to enter your actual API key from SimFin
# note: for this example, you need a SimFin+ subscription, otherwise the API will return an error.
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

# with simfin+, we can retrieve all data in just one call; this is much faster than making individual requests
# define the parameters for the query
parameters = {"statement": "pl", "ticker": ",".join(tickers), "period": "quarters", "fyear": ",".join([str(x) for x in list(range(year_start,year_end+1))]), "api-key": api_key}
# make the request
request = requests.get(request_url, parameters)

# convert response to json
all_data = request.json()

# in the data that is returned, each index represents one of the requested tickers
for response_index, data in enumerate(all_data):

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

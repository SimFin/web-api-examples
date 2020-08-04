library(httr)
library(jsonlite)

# define ticker, for SimFin+ users, this can be multiple tickers separated with a comma
ticker <- "AAPL"
# the API key from SimFin: https://simfin.com/data/api
apiKey <- "YOUR_API_KEY"
# the statement to retrieve, SimFin+ users can also retrieve all statements via statement=all
statement <- "pl"
# the period & financial year to retrieve, SimFin+ users can omit this parameter to retrieve all statements
period <- "q1"
fyear <- 2020

# make url
url <- paste("https://simfin.com/api/v2/companies/statements?api-key=",apiKey,"&ticker=",ticker,"&statement=",statement,"&period=",period,"&fyear=",fyear,sep="")

# make request
get_data <- GET(url)

# convert JSON
data <- fromJSON(content(get_data, "text"),flatten = TRUE)

# print columns
columns <- data[,c("columns")]
print(columns)

# print statement data
statement_data <- data[,c("data")]
print(statement_data)
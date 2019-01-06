ticker <- "AAPL"
apiKey <- "fgOZWUlhmZvcwxOJ2PYqaKaNA3zNrVJ2"
url <- paste("https://simfin.com/api/v1/info/find-id/ticker/",ticker,"?api-key=",apiKey,sep="")

get_data <- GET(url)

data <- fromJSON(content(get_data, "text"),flatten = TRUE)

simfinID <- data[,c("simId")]

statement <- "pl"
ptype <- "TTM"
fyear <- ""

url <- paste("https://simfin.com/api/v1/companies/id/",simfinID,"/statements/standardised","?api-key=",apiKey,
"&stype=",statement,"&ptype=",ptype,"&fyear=",fyear,
sep="")

get_data <- GET(url)

data <- fromJSON(content(get_data, "text"),flatten = TRUE)

print(data)
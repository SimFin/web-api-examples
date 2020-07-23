# SimFin Web-API Tutorial files

These are some examples how the SimFin web-API can be used to retrieve data. For our official Python API that works with the bulk data files, please visit this repository: https://github.com/SimFin/simfin

The v1 folder contains the examples for the web-API v1.

## Python
Full beginners tutorial for the web-API can be found here: https://medium.com/@SimFin_official/simfin-api-tutorial-6626c6c1dbeb

## Google Sheets
In order to get the data into a Google Sheet spreadsheet, copy the structure of this file (the blue area is the input and can be changed at your wish): 
https://docs.google.com/spreadsheets/d/1-LYHf71VgU7L8mqD_Ha_BWytJbALAJjk3qN-hBND9uI/edit#gid=0

In your Google Sheet, go to the menu and choose "Tools" > "Script Editor". In the window that opens, paste the code that you can find in the google-sheets folder in this repository:
https://github.com/SimFin/api-tutorial/blob/master/google-sheets/Code.gs

Replace in line 4 in Code.gs YOUR_API_KEY with your API key from SimFin.

Now in the menu of the Google Apps Scripts dashboard select "Run" > "Run Function" > "ADD_SIMFIN". If you go back to your Google Sheet, there should be a new menu item called "SimFin API" with which you can load the data.

## R
There is a short example for R in the R-examples folder that illustrates the general approach.

Feel free to commit more examples to this repository.
function callApi() {

  //PUT YOUR SIMFIN API KEY HERE
  var apiKey = "YOUR_API_KEY";
  ///////////////////////////////

  //SETTINGS FOR INPUT ROWS AND START COLUMN

  var startColumn = 1;
  var tickerRow = 2;
  var periodRow = 3;
  var yearRow = 4;

  var valuesStartRow = 6;

  // if you don't want all statements, change this variable
  var statements = ["pl","bs","cf"];
  // this is just for styling
  var statementCaptions = ["Profit & Loss", "Balance Sheet", "Cash Flow"];

  ///////////////////////////////

  var sheet = SpreadsheetApp.getActiveSheet();

  var lastCol = sheet.getLastColumn();

  var ticker = null;
  var year = null;
  var period = null;
  var simId = null;
  var wroteLineItems = [false,false,false];
  var startRows = [null,null,null];
  for(var a = startColumn+1;a<=lastCol;a++){
    ticker = sheet.getRange(tickerRow,a).getDisplayValue();
    year = sheet.getRange(yearRow,a).getDisplayValue();
    period = sheet.getRange(periodRow,a).getDisplayValue();

    //get SimFin ID
    var response = UrlFetchApp.fetch("https://simfin.com/api/v1/info/find-id/ticker/"+ticker+"?api-key="+apiKey);
    response = JSON.parse(response);
    if(response.length > 0 && parseInt(response[0]['simId']) > 0){
      simId = response[0]['simId'];
    } else {
      simId = null;
    }

    if(simId === null){
      continue;
    }

    for(var s = 0,sx=statements.length;s<sx;s++){

      // get statement data
      var response = UrlFetchApp.fetch("https://simfin.com/api/v1/companies/id/"+simId+"/statements/standardised?api-key="+apiKey+"&stype="+statements[s]+"&ptype="+period+"&fyear="+year, {muteHttpExceptions:true});
      response = JSON.parse(response);
      if(response.hasOwnProperty("values") && response['values'].length > 0){
        if(!wroteLineItems[s]){
          wroteLineItems[s] = true;

          if(s === 0){
            startRows[s] = valuesStartRow
          } else {
            startRows[s] = sheet.getLastRow()+2;
          }

          sheet.getRange(startRows[s],startColumn).setValue([statementCaptions[s]]);
          for(var b = 0,bx=response['values'].length;b<bx;b++){
           sheet.getRange(startRows[s]+1+b,startColumn).setValue([response['values'][b]['standardisedName']]);
          }
        }

        for(var b = 0,bx=response['values'].length;b<bx;b++){
           sheet.getRange(startRows[s]+1+b,a).setValue([response['values'][b]['valueChosen']]);
        }
      } else {
        continue;
      }
    }

  }
}


function ADD_SIMFIN() {
  var ui = SpreadsheetApp.getUi();
  ui.createMenu('SimFin API')
      .addItem('Load data','callApi')
      .addToUi();
}
def updatedaily(row, column, client, finnhub_client):

    # Open a workbook sheetname
    spreadsheetName = "Long Term Stocks"
    sheetName = "Healthcare"
    spreadsheet = client.open(spreadsheetName)
    sheet = spreadsheet.worksheet(sheetName)

    # Stock Lists
    healthcare_list = ['ILMN', 'ZTS', 'UNH', 'IQV', 'BGNE']
    table = []

    # Stock candles
    for l in range(len(healthcare_list)):
        line = [healthcare_list[l], finnhub_client.quote(healthcare_list[l])['o'], finnhub_client.quote(healthcare_list[l])['c'], finnhub_client.quote(healthcare_list[l])['h'], finnhub_client.quote(healthcare_list[l])['l']]
        table.append(line)

    for i in range(len(healthcare_list)):
        for j in range(5):
            sheet.update_cell(row + i, column + j, table[i][j])

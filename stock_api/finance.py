def updatedaily(row, column, client, finnhub_client):

    # Open a workbook sheetname
    spreadsheetName = "Long Term Stocks"
    sheetName = "Finance"
    spreadsheet = client.open(spreadsheetName)
    sheet = spreadsheet.worksheet(sheetName)

    # Stock Lists
    finance_list = ['MA', 'RPAY', 'TD', 'KBH', 'V']
    table = []

    # Stock candles
    for l in range(len(finance_list)):
        line = [finance_list[l], finnhub_client.quote(finance_list[l])['o'], finnhub_client.quote(finance_list[l])['c'], finnhub_client.quote(finance_list[l])['h'], finnhub_client.quote(finance_list[l])['l']]
        table.append(line)

    for i in range(len(finance_list)):
        for j in range(5):
            sheet.update_cell(row + i, column + j, table[i][j])

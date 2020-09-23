def updatedaily(row, column, client, finnhub_client):

    # Open a workbook sheetname
    spreadsheetName = "Long Term Stocks"
    sheetName = "Manufacturing"
    spreadsheet = client.open(spreadsheetName)
    sheet = spreadsheet.worksheet(sheetName)

    # Stock Lists
    manufacturing_list = ['GD', 'NEM', 'CAT', 'LIN', 'DE']
    table = []

    # Stock candles
    for l in range(len(manufacturing_list)):
        line = [manufacturing_list[l], finnhub_client.quote(manufacturing_list[l])['o'], finnhub_client.quote(manufacturing_list[l])['c'], finnhub_client.quote(manufacturing_list[l])['h'], finnhub_client.quote(manufacturing_list[l])['l']]
        table.append(line)

    for i in range(len(manufacturing_list)):
        for j in range(5):
            sheet.update_cell(row + i, column + j, table[i][j])

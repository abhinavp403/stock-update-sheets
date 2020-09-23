def updatedaily(row, column, client, finnhub_client):

    # Open a workbook sheetname
    spreadsheetName = "Long Term Stocks"
    sheetName = "Consumer Goods"
    spreadsheet = client.open(spreadsheetName)
    sheet = spreadsheet.worksheet(sheetName)

    # Stock Lists
    consumer_list = ['CRM', 'SQ', 'TTD', 'ETSY', 'AKAM']
    table = []

    # Stock candles
    for l in range(len(consumer_list)):
        line = [consumer_list[l], finnhub_client.quote(consumer_list[l])['o'], finnhub_client.quote(consumer_list[l])['c'], finnhub_client.quote(consumer_list[l])['h'], finnhub_client.quote(consumer_list[l])['l']]
        table.append(line)

    for i in range(len(consumer_list)):
        for j in range(5):
            sheet.update_cell(row + i, column + j, table[i][j])

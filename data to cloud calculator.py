import xlsxwriter

book = xlsxwriter.Workbook('price by company.xlsx')

a = {'ADVPIPE': 728, 'AIRFRGH': 65, 'BELVOIR': 926, 'CAMSRVC': 236, 'CHELCON': 2620, 'FIRSTCL': 16, 'GFURNIT': 5140,
     'HVJCOMP': 10900, 'HVJSCTX': 2660,'JVFCOMP': 16200, 'KEEPHOU': 3430, 'LEGACYT': 1950, 'MCSURG': 2080,
     'MORTCOO': 78,
     'MRAMBIN': 5640, 'PLASTEC': 647, 'RAMALLO': 1310, 'REACHUN': 5550, 'SMFADPC': 7750, 'STERLIN': 6910,
     'WFLASH': 3030,
     'XDEMO': 1, 'XKIEV': 1000, 'XVAND': 1390}

# for value in a.values():
#     print(value)
for key, value in a.items():
    # print(key, value)
    sheet = book.add_worksheet(key)

    header = ['COMPANY', 'FILE SERVER DATA, GB', 'VHDX SIZE, GB', '20% growth 1st year, GB',
              '20% growth 2nd year, GB', '20% growth 3rd year, GB', '20% growth 4th year, GB',
              '20% growth 5th year, GB', '20% growth 6th year, GB', '20% growth 7th year, GB',
              '7 YEARS PRICE, $']
    header2 = ['MONTH PRICE, $', 'YEARLY PRICE, $']

    row = 0
    column = 0
    # iterating through the content list
    for item in header:
        # write operation perform
        sheet.write(row, column, item)

        # incrementing the value of row by one with each iterations.
        row += 1

    row = 0
    column = 2
    for item in header2:
        sheet.write(row, column, item)
        column += 1
    #
    #
    col2 = []
    col2.append(key)
    col2.append(value)
    col2.append(value)
    # print(col2)
    data = value
    # print(data)
    year = 1
    y7 = 0
    mp = []
    yp = []
    # print("YEAR     DATA    MONTH    YEARLY    7YEARS")
    for _ in range(0, 7):
        m_p = 0
        yearlyCount = m_p * 12
        data += (data / 100 * 20)
        col2.append(round(data))
        if data <= 1000:
            m_p = 6
        elif (data > 1000) and (data % 1000 != 0):
            count = (data // 1000) + 1
            m_p = count * 6
        mp.append(m_p)
        yearlyCount = m_p * 12
        yp.append(yearlyCount)
        # print(f'{year}      {round(data, 2)}     {m_c}       {yearlyCount}')
        year += 1
        y7 += yearlyCount

    # print(f"7 years will cost: {y7}")
    #
    #     # Rows and columns are zero indexed.

    row = 0
    column = 1
    # iterating through the content list
    for item in col2:
        # write operation perform
        sheet.write(row, column, item)

        # incrementing the value of row by one with each iterations.
        row += 1

    row = 10
    column = 1
    sheet.write(row, column, y7)

    row = 3
    column = 2
    # iterating through the content list
    for item in mp:
        # write operation perform
        sheet.write(row, column, item)

        # incrementing the value of row by one with each iterations.
        row += 1

    row = 3
    column = 3
    # iterating through the content list
    for item in yp:
        # write operation perform
        sheet.write(row, column, item)

        # incrementing the value of row by one with each iterations.
        row += 1

book.close()

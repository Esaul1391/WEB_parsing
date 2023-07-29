import xlrd

path_ex = "/home/user/PycharmProjects/WEB_parsing/others/exzemple.xls"
ex_data_file = xlrd.open_workbook(path_ex)
sheet = ex_data_file.sheet_by_index(0)

row_number = sheet.nrows  # len row

for row in range(1, row_number):
    structure = str(list(sheet.row(row))[0]).replace("empty:", "").replace("'", '')
    post = str(list(sheet.row(row))[1]).replace("empty:''", '').replace("text:", '').replace("'", "")
    rank_name = str(list(sheet.row(row))[3]).replace("empty:''", '').replace("text:", '').replace("'", "")
    rank = ''
    name = ''
    if rank_name != "":

        try:
            rank_name = rank_name.split('полиции')
            rank = rank_name[0] + 'полиции'
            name = rank_name[1].strip().split(' ')
        except:
            print(rank_name)

        # rank = rank_name[0] + rank_name[1]
        # name = rank_name[2] + rank_name[3] + rank_name[4]
    print(rank, name)
    # print(rank_name)
    # print(list(sheet.row(row))[3])
print(row_number)

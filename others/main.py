import xlrd
import csv
import re

def data_name():
    path_ex = "/home/esal/PycharmProjects/WEB_parsing/others/exsemple.xls"
    ex_data_file = xlrd.open_workbook(path_ex)
    sheet = ex_data_file.sheet_by_index(0)


    with open("sp.csv", "w") as file:
        writer = csv.writer(file)

        writer.writerow(
            (
                'Должность',
                'Звание',
                'ИФО',
                'Позвной'
                'Телефон'
            )
        )
    row_number = sheet.nrows  # len row
    print(row_number)
    data_list = []
    for row in range(1, row_number):
        ls = []
        structure = list(sheet.row(row))
        # structure = str(list(sheet.row(row))).replace("empty:", "").replace("'", '')
        post = str(structure[2]).strip().replace('text:', '').replace("'", '').replace('empty:', '')

        rank_name = str(structure[3]).strip().replace('text:', '').replace("'", '').replace('empty:', '')

        name = str(structure[4]).strip().replace('text:', '').replace("'", '').replace('empty:', '')
        name = re.sub('[1234567890()\n]', '', name).strip().split(' ')
        if len(name[-1]) == 1:
            name.pop(-1)


        print(name)
        # post = str(list(sheet.row(row))[1]).replace("empty:''", '').replace("text:", '').replace("'", "")
        # rank_name = str(list(sheet.row(row))[3]).replace("empty:''", '').replace("text:", '').replace("'", "")
        # rank = ''
        # name = ''
        # if rank_name != "":
        #     try:
        #         rank_name = rank_name.split('полиции')
        #         rank = rank_name[0] + 'полиции'
        #         name = rank_name[1].strip().split(' ')
        #     except:
        #         print(f"Error {row}", rank_name)
        #
        #     rank = rank_name[0] + rank_name[1]
        #     # name = rank_name[2] + rank_name[3] + rank_name[4]
        #     # name = rank_name[2]
        # print(post, rank, name)
        # data_list.append(
        #     {
        #         'Должность': post,
        #         'Звание': rank,
        #         'ИФО': name
        #     }
        # )
        # data_list.append([post, rank, name])
        # with open("sp.csv", "a") as file:
        #     writer = csv.writer(file)
        #
        #     writer.writerow(
        #         (
        #             post,
        #             rank,
        #             name,
        #
        #         )
        #     )
    # print(*data_list)


# def data_cal_num():
#     sp1 = []
#     with open("/home/user/PycharmProjects/WEB_parsing/others/call", 'r') as file:
#         sp1 = file.read().replace('\n', ' ').replace("-", '').split(' ')  # Убираю ненужные символы, создаю список.
#     sp1 = [item for item in sp1 if item != '']
#     for item in range(len(sp1)):  # перевел номера к тип int
#         if sp1[item].isdigit():
#             sp1[item] = int(sp1[item])
#
#     print(sp1)
#     list_name_tel = []
#     sp = []
#     last_item = ""
#     for item in sp1:
#
#         if type(item) != int:
#             if type(last_item) == int:
#                 list_name_tel.append(sp)
#                 sp = []
#             sp.append(item)
#             last_item = item
#         else:
#             sp.append(item)
#             last_item = item
#
#     print(list_name_tel)
#     # file = open("/home/user/PycharmProjects/WEB_parsing/others/call")
#     # print(file.read())

# def data_nickname():
#     path_ex = "/home/user/PycharmProjects/WEB_parsing/others/позывные.xls"
#     ex_data_file = xlrd.open_workbook(path_ex)
#     sheet = ex_data_file.sheet_by_index(0)
#     sp_row = []
#     for item in sheet:
#         sp = []
#         if str(item[-1]) != "empty:''":
#             sp.append(str(item[-1]).replace('text:', '').replace("'", ''))
#             sp.append(str(item[-2]).replace('text:', '').replace("'", ''))
#             sp_row.append(sp)
#     print(sp_row)

def add_data():
    pass

def main():
    # data_cal_num()
    # data_nickname()
    data_name()

if __name__ == "__main__":
    main()

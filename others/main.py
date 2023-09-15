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
        data_list.append(sheet.row(row))
    data_list_fin = []
    for row in data_list:
        ls = []
        for r in row:
            i = re.sub('[^а-яА-ЯёЁ]', ' ', str(r))
            ls.append(i)
        ls = [item for item in ls if item.strip() != '']
        ls = [item.strip() for item in ls]

        if len(ls) > 1 and 'полиции' in ls[-2]:
            ls[-2] = ls[-2].split('полиции')
            ls[-2][0] += 'полиции'
            print(ls)


        print(ls)
        data_list_fin.append(ls)

    return data_list_fin


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

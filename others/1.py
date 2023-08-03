import xlrd
import csv


def data_name():
    path_ex = "/home/user/PycharmProjects/WEB_parsing/others/exzemple.xls"
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
            )
        )
    row_number = sheet.nrows  # len row
    data_list = []
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
                print("Error ", rank_name)

            # rank = rank_name[0] + rank_name[1]
            # name = rank_name[2] + rank_name[3] + rank_name[4]
        # print(post, rank, name)
        data_list.append(
            {
                'Должность': post,
                'Звание': rank,
                'ИФО': name
            }
        )

        with open("sp.csv", "a") as file:
            writer = csv.writer(file)

            writer.writerow(
                (
                    post,
                    rank,
                    name,

                )
            )
    print(*data_list)


def data_cal():
    sp1 = []
    with open("/home/user/PycharmProjects/WEB_parsing/others/call", 'r') as file:
        sp1 = file.read().replace('\n', ' ').replace("-", '').split(' ')  # Убираю ненужные символы, создаю список.
    sp1 = [item for item in sp1 if item != '']
    for item in range(len(sp1)):  # перевел номера к тип int
        if sp1[item].isdigit():
            sp1[item] = int(sp1[item])

    print(sp1)
    list_name_tel = []
    sp = []
    last_item = ""
    for item in sp1:

        if type(item) != int:
            if type(last_item) == int:

                list_name_tel.append(sp)
                sp = []
            sp.append(item)
            last_item = item
        else:
            sp.append(item)
            last_item = item

    print(list_name_tel)
    # file = open("/home/user/PycharmProjects/WEB_parsing/others/call")
    # print(file.read())


def main():
    data_cal()


if __name__ == "__main__":
    main()

import xlsxwriter
from main import array

def writer(parametr):
    book = xlsxwriter.Workbook(r'/PR_HUB/Parser_tutorial/data.xlsx') # сохдаю файл таблицы
    page = book.add_worksheet('товары')     # создаю новую страницу в иксель

    row = 0
    column = 0

    page.set_column("A:A", 20)   # устанавливаю размер колонок
    page.set_column("B:B", 20)
    page.set_column("C:C", 50)
    page.set_column("D:D", 50)

    for item in parametr():     #   записываю значеия в колонки
        page.write(row, column, item[0])
        page.write(row, column + 1, item[1])
        page.write(row, column + 2, item[2])
        page.write(row, column + 3, item[3])
        row += 1

    book.close()

writer(array)
from docx import Document

# Открываем файл
doc = Document('//home/esal/PycharmProjects/WEB_parsing/others/1.docx')

# Читаем строки из файла
# Читаем таблицы
tables = doc.tables
sp = []
# Выводим содержимое таблиц
row_sp = []
for table in tables:
    for row in table.rows:

        for cell in row.cells:
            row_sp.append(cell.text)

print(row_sp)

# for item in row_sp:
#     print(item)
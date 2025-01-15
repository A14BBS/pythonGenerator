import pdfplumber
import pandas as pd
import os
print("Пока я конвертирую файлы можно выпить кофе)")

def pdf_to_excel(dir, excel_file):
    tit = os.listdir(dir)
    for t in tit:


        with pdfplumber.open("{}/{}".format(dir, t)) as pdf:
            all_tables = []
            for page in pdf.pages:              #ЭТИ ДВЕ СТРОЧКИ ИЗВЛЕКАЮТ
                tables = page.extract_tables()  #ТАБЛИЦЫ ИЗ КАЖДОЙ ТАБЛИЦЫ пдф ФАЙЛА
                for table in tables:
                    if table:
                        df = pd.DataFrame(table)  #создаёт DataFrame (двумерный массив) на основе переданного списка списков
                        all_tables.append(df)

            if not all_tables:
                all_tables.append(pd.DataFrame([["No tables found"]]))

            # print("{}_{}.xlsx".format(excel_file, tit.index(t)))

            with pd.ExcelWriter("{}.xlsx".format(os.path.basename(t).split('.')[0]), engine='openpyxl') as writer:
                for idx, df in enumerate(all_tables):
                    df.to_excel(writer, sheet_name=f'Sheet{idx+1})', index=False)


dirr = r"C:/Users/Monik/PycharmProjects/New/pProje/1"
file_xl = "1"

pdf_to_excel(dir=dirr,
             excel_file=file_xl)
print('готово')
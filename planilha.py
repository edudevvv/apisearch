from openpyxl import load_workbook

file_path = "Dados_Contatos.xlsx"
workbook = load_workbook(file_path)
sheet = workbook.active

for column in sheet.columns:
    max_length = 0
    col_letter = column[0].column_letter  
    for cell in column:
        try:
            if cell.value:
                max_length = max(max_length, len(str(cell.value)))
        except:
            pass
    adjusted_width = max_length + 2 
    sheet.column_dimensions[col_letter].width = adjusted_width

formatted_file_path = "Dados_Contatos_Formatado.xlsx"
workbook.save(formatted_file_path)
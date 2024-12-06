import gspread
from google.oauth2.service_account import Credentials

credentials = Credentials.from_service_account_file(
    "GOOGLE_CREDENTIALS.json.exemple",
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ],
)

client = gspread.authorize(credentials)

spreadsheetName = "ADD_NAME_HERE"
spreadsheet = client.open(spreadsheetName)

sheet = spreadsheet.sheet1

valor = sheet.cell(1, 1).value
print(f"Valor na célula A1: {valor}")

sheet.update_cell(2, 1, "Novo Valor")

sheet.append_row(["Coluna 1", "Coluna 2", "Coluna 3"])

print("Planilha atualizada com sucesso!")

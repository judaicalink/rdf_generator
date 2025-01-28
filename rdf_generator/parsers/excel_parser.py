import pandas as pd


class ExcelParser:
    def __init__(self, file_path):
        """
        Initialize the Excel parser with the file path.
        """
        self.file_path = file_path

    def list_sheets(self):
        """
        List all sheet names in the Excel file.
        """
        try:
            excel_file = pd.ExcelFile(self.file_path)
            return excel_file.sheet_names
        except Exception as e:
            raise Exception(f"Error reading Excel file: {e}")

    def read_sheet(self, sheet_name=None, sheet_index=0):
        """
        Read data from a specific sheet by name or index.
        Returns data as a list of dictionaries, where keys are column headers.
        """
        try:
            if sheet_name:
                df = pd.read_excel(self.file_path, sheet_name=sheet_name)
            else:
                df = pd.read_excel(self.file_path, sheet_name=sheet_index)

            return df.to_dict(orient='records')
        except Exception as e:
            raise Exception(f"Error reading sheet: {e}")

    def read_all_sheets(self):
        """
        Read all sheets in the Excel file.
        Returns a dictionary with sheet names as keys and data as list of dictionaries.
        """
        try:
            excel_data = pd.read_excel(self.file_path, sheet_name=None)
            return {sheet: data.to_dict(orient='records') for sheet, data in excel_data.items()}
        except Exception as e:
            raise Exception(f"Error reading all sheets: {e}")

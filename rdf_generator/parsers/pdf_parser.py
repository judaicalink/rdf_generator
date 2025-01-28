import pdfplumber


class PDFParser:
    def __init__(self, file_path):
        """
        Initialize the PDF parser with the file path.
        """
        self.file_path = file_path

    def extract_text(self):
        """
        Extracts and returns the text content of the entire PDF.
        """
        try:
            text = ""
            with pdfplumber.open(self.file_path) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() + "\n"
            return text.strip()
        except Exception as e:
            raise Exception(f"Error extracting text from PDF: {e}")

    def extract_table(self, page_number):
        """
        Extracts table data from a specific page as a list of rows.
        """
        try:
            with pdfplumber.open(self.file_path) as pdf:
                if page_number < 1 or page_number > len(pdf.pages):
                    raise IndexError("Page number out of range.")
                page = pdf.pages[page_number - 1]
                return page.extract_table()
        except Exception as e:
            raise Exception(f"Error extracting table from page {page_number}: {e}")

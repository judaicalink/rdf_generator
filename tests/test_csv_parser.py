import unittest
from rdf_generator.parsers.csv_parser import CSVParser

class TestCSVParser(unittest.TestCase):
    def test_csv_reading(self):
        parser = CSVParser("tests/sample.csv")
        data = parser.read_csv()
        self.assertGreater(len(data), 0)

if __name__ == "__main__":
    unittest.main()
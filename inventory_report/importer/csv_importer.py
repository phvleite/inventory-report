from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, filepath: str):
        try:
            data = CsvImporter.__type_file(filepath)
            return data
        except ValueError:
            print("Arquivo inválido")

    def __type_file(filepath):
        if filepath.endswith(".csv"):
            data = CsvImporter.__read_file_csv(filepath)
        else:
            raise ValueError("Arquivo inválido")
        return data

    def __read_file_csv(filepath):
        with open(filepath, encoding="utf8", mode="r") as csv_file:
            CsvImporter_reader = csv.reader(csv_file, delimiter=",")
            cab, *data = CsvImporter_reader
            data_csv = []
            data_csv = []
            for prd in data:
                csv_dict = {}
                for ind, elem in enumerate(prd):
                    csv_dict[cab[ind]] = elem
                data_csv.append(csv_dict)
        return data_csv

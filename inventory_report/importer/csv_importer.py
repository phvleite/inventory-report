from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(filepath: str):
        if filepath.endswith(".csv"):
            data = CsvImporter.__read_file(filepath)
        else:
            raise ValueError("Arquivo inválido")
        return data

    def __read_file(filepath):
        with open(filepath, encoding="utf8", mode="r") as csv_file:
            csv_importer_dict_reader = csv.DictReader(csv_file, delimiter=",")
            data_csv = list(csv_importer_dict_reader)
        return data_csv

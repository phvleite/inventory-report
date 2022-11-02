from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, filepath: str):
        if filepath.endswith(".json"):
            data = JsonImporter.__read_file(filepath)
        else:
            raise ValueError("Arquivo inválido")
        return data

    def __read_file(filepath):
        with open(filepath) as json_file:
            inventory_reader = json.load(json_file)
        return inventory_reader

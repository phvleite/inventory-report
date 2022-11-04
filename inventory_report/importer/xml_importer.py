from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    def import_data(filepath: str):
        if filepath.endswith(".xml"):
            data = XmlImporter.__read_file(filepath)
        else:
            raise ValueError("Arquivo inválido")
        return data

    def __read_file(filepath):
        with open(filepath, "r") as xml_file:
            inventory_reader = xmltodict.parse(xml_file.read())["dataset"][
                "record"
            ]
        return inventory_reader

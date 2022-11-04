from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, filepath: str, type: str):
        try:
            self.data.extend(self.importer.import_data(filepath))
            report = self.__verify_type_inventory(self.data, type)
            return report
        except ValueError:
            raise ValueError("Arquivo inválido")

    def __iter__(self):
        return InventoryIterator(self.data)

    def __verify_type_inventory(self, data: list, type: str):
        if type == "simples":
            report = SimpleReport.generate(data)
        elif type == "completo":
            report = CompleteReport.generate(data)
        else:
            raise ValueError("Tipo de relatório inválido")
        return report

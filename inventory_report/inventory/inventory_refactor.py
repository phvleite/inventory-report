from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer

    def import_data(self, filepath: str, type: str):
        try:
            self.data = self.importer.import_data(filepath)
            report = InventoryRefactor.__verify_type_inventory(self.data, type)
            return report
        except ValueError:
            print("Invalid file!")

    def __verify_type_inventory(data, type):
        if type == "simples":
            report = SimpleReport.generate(data)
        elif type == "completo":
            report = CompleteReport.generate(data)
        else:
            raise ValueError("Tipo de relatório inválido")
        return report

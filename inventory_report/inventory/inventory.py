import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def import_data(filepath: str, type: str):
        try:
            report = Inventory.__type_inventory(filepath, type)
            return report
        except ValueError:
            print("Invalid file!")

    def __type_inventory(filepath, type):
        if filepath.endswith(".csv"):
            report = Inventory.__read_file_csv(filepath, type)
        elif filepath.endswith(".json"):
            report = Inventory.__read_file_json(filepath, type)
        elif filepath.endswith(".xml"):
            pass
        else:
            raise ValueError("Padrão de arquivo não reconhecido")
        return report

    def __read_file_csv(filepath, type):
        with open(filepath, encoding="utf8", mode="r") as csv_file:
            inventory_reader = csv.reader(csv_file, delimiter=",")
            cab, *data = inventory_reader
            data_csv = []
            data_csv = []
            for prd in data:
                csv_dict = {}
                for ind, elem in enumerate(prd):
                    csv_dict[cab[ind]] = elem
                data_csv.append(csv_dict)
            report = Inventory.__verify_type_inventory(data_csv, type)
        return report

    def __read_file_json(filepath, type):
        with open(filepath) as json_file:
            inventory_reader = json.load(json_file)
            report = Inventory.__verify_type_inventory(inventory_reader, type)
        return report

    def __verify_type_inventory(data, type):
        if type == "simples":
            report = SimpleReport.generate(data)
        elif type == "completo":
            report = CompleteReport.generate(data)
        else:
            raise ValueError("Tipo de relatório inválido")
        return report


if __name__ == "__main__":
    print(
        Inventory.import_data(
            "inventory_report/data/inventory.json",
            "completo",
        )
    )

from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer

    def import_data(self, filepath: str, type: str):
        try:
            self.data = self.importer.import_data(filepath, type)
        except ValueError:
            print("Invalid file!")

    def __iter__(self):
        return InventoryIterator(self.data, type)

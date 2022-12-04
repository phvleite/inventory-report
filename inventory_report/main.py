from inventory_report.inventory.inventory_refactor import InventoryRefactor
import sys


def main(*args):
    if len(args) != 3:
        sys.stderr.write("Verique os argumentos\n")

    importer, filepath, type = args

    data = InventoryRefactor(importer)
    data.import_data(filepath, type)

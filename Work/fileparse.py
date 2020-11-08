# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        headers = next(rows) if has_headers else []
        records = []
        if not headers and select:
            raise RuntimeError("select argument requires column headers")
        for index, row in enumerate(rows, start=1):
            if not row:
                continue
            try:
                if select:
                    record = {header: func(data) for header, data, func in zip(
                        headers, row, types) if header in select}
                else:
                    record = {header: func(data) for header, data, func in zip(
                        headers, row, types)}
                records.append(record)
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {index}: Could't convert {row}")
                    print(f"Row {index}: Reason {e}")
                continue
    return records

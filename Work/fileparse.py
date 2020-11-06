# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        headers = next(rows) if has_headers else []
        records = []
        if not headers and select:
            raise RuntimeError("select argument requires column headers")
        for row in rows:
            if not row:
                continue
            if select:
                record = {header: func(data) for header, data, func in zip(
                    headers, row, types) if header in select}
            else:
                record = {header: func(data) for header,
                          data, func in zip(headers, row, types)}
            records.append(record)
    return records

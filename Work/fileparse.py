# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, select=None):
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        records = []
        for row in rows:
            if not row:
                continue
            if select:
                record = {header: data for header, data in zip(
                    headers, row) if header in select}
            else:
                record = dict(zip(headers, row))
            records.append(record)
    return records

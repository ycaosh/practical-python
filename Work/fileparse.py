# fileparse.py
#
# Exercise 3.3
import csv
import logging
log = logging.getLogger(__name__)


def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    rows = csv.reader(lines, delimiter=delimiter)
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
                if has_headers:
                    record = {header: func(data) for header, data, func in zip(
                        headers, row, types)}
                else:
                    record = tuple([func(data)
                                    for data, func in zip(row, types)])
            records.append(record)
        except ValueError as e:
            if not silence_errors:
                log.warning("Row %d: Couldn't convert %s", index, row)
                log.debug("Row %d: Reason %s", index, e)
            continue
    return records

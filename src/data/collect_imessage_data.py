import sqlite3
import csv


if __name__ == "__main__":
    conn = sqlite3.connect("/Users/switkowski/PycharmProjects/iMessages/data/raw/chat.db")
    cur = conn.cursor()

    tables = []
    for table in cur.execute("""SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"""):
        tables.append(table[0])

    for table in tables:
        data = cur.execute(f'SELECT * FROM {table}')
        columns = [d[0] for d in data.description]
        with open('/Users/switkowski/PycharmProjects/iMessages/data/raw/{}.csv'.format(table), 'w') as f:
            writer = csv.writer(f)
            writer.writerow(columns)
            writer.writerows(data)

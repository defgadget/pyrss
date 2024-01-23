import csv
import os
import sys
import argparse

def save_to_csv(filename, data):
    exists = os.path.isfile(filename)
    with open(filename, "a", newline="") as csvfile:
        w = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        if not exists:
            header = ["Name", "URL"]
            w.writerow(header)
        w.writerow(data)

def read_from_csv(filename):
    with open(filename, newline="") as csvfile:
        r = csv.reader(csvfile)
        r.__next__()
        for row in r:
            print(", ".join(row))
            

def main():
    parser = argparse.ArgumentParser(description="PyRSS Manager")
    parser.add_argument("--file", nargs="?", default="database.csv")
    parser.add_argument("action", choices=["add", "delete", "list"])
    parser.add_argument
    args = parser.parse_args()
    db = args.file.lower()
    data = ["Sports Illustrated", "https://www.sportsillustrated.com"]

    if args.action.lower() == "add":
        save_to_csv(db, data)
    elif args.action.lower() == "list":
        read_from_csv(db)
    else:
        print("Unknow action")
        return

if __name__ == "__main__":
    main()

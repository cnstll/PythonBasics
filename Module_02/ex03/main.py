from csvreader import CsvReader

if __name__ == "__main__":
    with CsvReader('bad.csv') as file:
        print(file)
        if file is None:
            print("File is corrupted")

    with CsvReader('good.csv') as file:
        data = file.getdata()
        header = file.getheader()
        for record in data:
            print(record, '\n')
        if header is None:
            print("Please set 'header=True', if you csv as fields")

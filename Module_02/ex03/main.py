from csvreader import CsvReader

if __name__ == "__main__":
    with CsvReader('space_avocado.csv', header=True, skip_bottom=5, skip_top=2) as file:
        print("file opened")
        file.filename
        print(file.getheader())
        print(file.getheader())
        data = file.getdata()
        for l in data:
            print(l, sep='\n')
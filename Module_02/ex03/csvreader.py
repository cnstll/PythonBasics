import csv

class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        print("Init")

    def __enter__(self):
        print("Enter")
        self.file_fd = open(self.filename)
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.file_fd.close()
        print("Done")

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        self.file_fd.seek(self.skip_top)
        csv_reader = csv.reader(self.file_fd, delimiter=self.sep)
        data = [row for line, row in enumerate(csv_reader) if line < self.skip_bottom]
        return data


    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        if self.header == False:
            return None
        else:
            self.file_fd.seek(0)
            csv_reader = csv.reader(self.file_fd, delimiter=self.sep)
            header = csv_reader.__next__()
            return header
            
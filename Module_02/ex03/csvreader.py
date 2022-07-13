import csv


class CsvReader():
    def __init__(self, filename=None, sep=',',
                 header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.file_fd = None

    def check_csv(self):
        csv_reader = csv.reader(self.file_fd, delimiter=self.sep)
        first_row = csv_reader.__next__()
        first_row_len = len(first_row)
        if any(e in (None, '') for row in csv_reader for e in row):
            return False
        for i, row in enumerate(csv_reader):
            if first_row_len != len(row):
                return False
        return True

    def __enter__(self):
        print("...Enter")
        try:
            self.file_fd = open(self.filename)
            if not self.check_csv():
                raise RuntimeError(f"File '{self.filename}' badly formated")
            return self
        except Exception as e:
            return None

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.file_fd:
            self.file_fd.close()
        print("Exit...")

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        self.file_fd.seek(0)
        csv_reader = csv.reader(self.file_fd, delimiter=self.sep)
        if self.skip_bottom == 0:
            data = [row for line, row in enumerate(csv_reader)
                    if line > self.skip_top]
        else:
            rg = range(self.skip_top, self.skip_bottom)
            data = [row for line, row in enumerate(csv_reader) if line in rg]
        return data

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        if not self.header:
            return None
        else:
            self.file_fd.seek(0)
            csv_reader = csv.reader(self.file_fd, delimiter=self.sep)
            header = csv_reader.__next__()
            return header

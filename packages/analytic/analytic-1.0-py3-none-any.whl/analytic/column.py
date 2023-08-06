import csv

#  small liberay which helps to extract column
# from csv and stor it in new csv

#*******     HELP     *******
#   classInstance = column('CSV file name')
#   classInstance.getColumn('n Column Names with comma')
#   classInstance.specifyRow('column name','specific element')
#   classInstance.dataCleansing('column name','old Data','new data')
#   classInstance.dataCleansing('column name','old Data','new data')
#   classInstance.toCSV('new csv file name')


class column:
    
    def __init__(self):
        self.csv_name = ""
        self.data = []
        self.header = []
        self.fullHeader = []

    def getCSV(self,csv_file_name):
        self.csv_name = csv_file_name
    
    def getColumn(self, *columns):
        columnWithQuotes = [] 
        for col in columns:
            self.header.append(col)
            columnWithQuotes.append("row['"+col+"']")
            column = str(columnWithQuotes).replace('"',"")
        with open(self.csv_name) as f:
            reader = csv.DictReader(f)
            for row in reader:
                 self.data.append(eval(column))
        return self.data
        
    def specifyRow(self, column, specifyBy):
        count = 0
        if self.data == []:
            
            with open(self.csv_name) as f:
                reader = csv.reader(f)
                self.fullHeader = next(reader)
                for row in reader:
                    if count >= 1:
                        self.data.append(row)
                    count += 1
            columnPosition = self.fullHeader.index(column)
            getColumnData = self.data
            self.data = []
            for rows in getColumnData:
                if rows[columnPosition] == specifyBy:
                    self.data.append(rows)
        else:
            columnPosition = self.header.index(column)
            getColumnData = self.data
            self.data = []
            for row in getColumnData:
                if row[columnPosition] == specifyBy:
                    self.data.append(row)
        return self.data

    def dataCleansing(self, column, oldData, newData):
        count = 0
        if self.data == []:
            with open(self.csv_name) as f:
                reader = csv.reader(f)
                self.fullHeader = next(reader)
                for row in reader:
                    if count >= 1:
                        self.data.append(row)
                    count += 1
            columnPosition = self.fullHeader.index(column)
            getColumnData = self.data
            self.data = []
            for rows in getColumnData:
                if rows[columnPosition] == oldData:
                    row[columnPosition] = newData
                self.data.append(rows)
        else:
            columnPosition = self.header.index(column)
            getColumnData = self.data
            self.data = []
            for row in getColumnData:
                if row[columnPosition] == oldData:
                    row[columnPosition] = newData
                self.data.append(row)
        return self.data

    def toCSV(self,file_name):
        fileOpen = open(file_name,'w',newline='')
        writer = csv.writer(fileOpen)
        if len(self.fullHeader) == len(self.data[0]):
            writer.writerow(self.fullHeader)
        else:
            writer.writerow(self.header)
        for row in self.data:
            writer.writerow(row)








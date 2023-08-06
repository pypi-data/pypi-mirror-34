import csv

class mapp:
    def __init__(self):
        self.csv_name = ''
        mapp.data = []
        mapp.seperator = ''

    def getFile(self,csv_file_name):
        self.csv_name = csv_file_name

    def mapper(self,key,seperator,value):
        mapp.seperator = seperator
        headOpen = open(self.csv_name)
        forHeader = csv.reader(headOpen)
        Header = next(forHeader)
        with open(self.csv_name) as openFile:
            dataRead = csv.DictReader(openFile)
            if value in Header:
                for row in dataRead:
                    mapp.data.append(row[key]+mapp.seperator+row[value])
            else:  
                for row in dataRead:
                    mapp.data.append(row[key]+mapp.seperator+value)
        return mapp.data

    def toFile(self,fileName):
        file = open(fileName,"w")
        for datas in mapp.data:
            file.write(datas+"\n")

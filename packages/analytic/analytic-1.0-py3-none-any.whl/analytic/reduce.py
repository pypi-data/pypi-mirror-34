from analytic.mapp import*


class reduce(mapp):
    def __init__(self,source):
        self.source = source
        self.csv_name = ''
        reduce.data = []
        self.header = bool

    def getFile(self,csv_file_name,header):
        self.csv_name = csv_file_name
        self.header = header
        
    def reducer(self):
        self.tempData = reduce.data
        reduce.data = []
        previousKey = None
        doList = []
        for sortedData in self.tempData:
            key,value = sortedData[0],sortedData[1]
            if key == previousKey:
                doList.append(value)
            else:
                if previousKey is not None:
                    reduce.data.append([previousKey,doList])
                previousKey = key
                doList = []
                doList.append(value)
        if previousKey is not None:
            reduce.data.append([previousKey,doList])
        return reduce.data
        

    def sorter(self,order=bool,**keyValue):
        data = []
        if self.source == "file":
            count = 0
            if self.header == True:
                fileOpen = open(self.csv_name)
                reader = fileOpen.readlines()
                
                for dataRead in reader:
                    keys,values = dataRead.split(keyValue['seperator'])
                    if count is not 0:
                        data.append([keys,values])
                    count+=1
                    
            else:
                fileOpen = open(self.csv_name)
                reader = fileOpen.readlines()
                for dataRead in reader:
                    keys,values = dataRead.split(keyValue['seperator'])
                    data.append([keys,values])
            reduce.data = sorted(data,reverse=order,key = keyValue['key'])
  
        elif self.source == "mapper":
            finalData = []
            datas = mapp.data
            seperator = mapp.seperator
            for d in datas:
                keys,values = d.split(seperator)
                finalData.append([keys,values])
            reduce.data = sorted(finalData,reverse=order,key=keyValue['key'])
        return reduce.data

    def toFile(self,fileName,**seperator):
        file = open(fileName,"w")
        for sortData in reduce.data:
            file.write(str(sortData[0])+seperator['seperator']+str(sortData[1])+'\n')


    

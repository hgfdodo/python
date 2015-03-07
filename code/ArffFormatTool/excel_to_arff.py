import xlrd


arff_name='weather'
path='e:\\'
excel_file='a.xlsx'
class Switch:

    def __init__(self,source,target):
        self.filepath=source
        self.targetpath=target
        arff_file_name=target.split('\\')[-1]
        self.arff_name='.'.join(arff_file_name.split('.')[0:-1])
        
    
    def trans(self):
        books=xlrd.open_workbook(self.filepath)
        table=books.sheet_by_index(0)
        
        attribute=table.row_values(0)

        arff_file=open(self.targetpath,'w')
        arff_file.write('@relation '+self.arff_name + '\n\n')

    
        for i in range(0, len(attribute)):
            attribute_value=list(set( table.col_values(i)[1:])-set(['']) )
            print attribute_value
            arff_file.write('@attribute ' + attribute[i] + ' {')
            for j in range(0, len(attribute_value)-1 ):
                arff_file.write(str(attribute_value[j]) + ', ')
            arff_file.write(str(attribute_value[-1]) + '}\n')

        arff_file.write('\n@data' + '\n')
        for i in range(1, table.nrows):
            value_data=table.row_values(i)
            for j in range(0, len(value_data)-1):
                if value_data[j]=='':
                    arff_file.write('?,')
                else:
                    arff_file.write(str(value_data[j]) + ',')
            if value_data[-1]=='':
                arff_file.write('?' + '\n')
            else:
                arff_file.write(str(value_data[-1]) + '\n')
    
        arff_file.close()

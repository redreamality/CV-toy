# -*-coding:utf-8-*-
from xlrd import open_workbook,empty_cell
from xlwt import Workbook
# from xlwt import easyxf
from xlutils.copy import copy
from translate import Translator


def main():
    translate_excel()

def translate_excel():
    translator= Translator(from_lang="zh",to_lang="en")

    # sXXX for SOURCExxx
    sbook = open_workbook('source.xls',formatting_info= False )

    # translation = translator.translate("")
    
    tbook = Workbook(encoding='utf-8')#write

    # read and write per sheet
    
    for s in sbook.sheets():# s is a sheet handle
        utf_name = s.name.encode('utf8') #sheet names are all in unicode, translation need utf8
        tsheet_name = translator.translate(utf_name) #translator.translate method only accepts utf-8
    
        # tXXX means translatedXXX
        print s.name,tsheet_name
        
        tsheet = tbook.add_sheet(tsheet_name) # write sheet in tbook, name in english
        
        for row in range(s.nrows):
            print "row:",row
            for col in range(s.ncols):
                try:
                    
                    utf_cell = s.cell(row,col).value.encode('utf8')
                    tcell_value = translator.translate(utf_cell)
                    tsheet.write(row,col,tcell_value)
                except: #the value might be float
                    tsheet.write(row,col,s.cell(row,col).value)
            tsheet.flush_row_data()
    print "saving..."    
    tbook.save('english_output.xls')
    print "saved."

 
if __name__ == "__main__":
    main()
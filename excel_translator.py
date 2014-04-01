# -*-coding:utf-8-*-
from xlrd import open_workbook,empty_cell
from xlwt import Workbook
# from xlwt import easyxf
from xlutils.copy import copy
from translate import Translator
from main_inverse_md import *

def main():
    
    translate_excel()

def translate_excel():
    outfile = open("english_cv.md",'w')
    
    translator= Translator(from_lang="zh",to_lang="en")

    # sXXX for SOURCExxx
    sbook = open_workbook('source.xls',formatting_info= False )
    # tXXX means translatedXXX
    tbook = Workbook(encoding='utf-8')#write
    
    # read and write per sheet
    book_content = []
    for s in sbook.sheets():# s is a source sheet handle for read
        
        #add sheet
        try:
            utf_name = s.name.encode('utf8') #sheet names are all in unicode, translation need utf8
            tsheet_name = translator.translate(utf_name) #translator.translate method only accepts utf-8
            print s.name,tsheet_name
            tsheet = tbook.add_sheet(tsheet_name) # write sheet in tbook, name in english
            print_title(tsheet_name,outfile)#write
        except:
            print "error in sheet:",s.name,"\n"
            print_title(s.name,outfile)
            
        #add content
        
        rows_content = []
        for row in range(s.nrows):
            print "row:",row
            col_content = []
            for col in range(s.ncols):
                try:
                    utf_cell = s.cell(row,col).value.encode('utf8')
                    tcell_value = translator.translate(utf_cell)
                    tsheet.write(row,col,tcell_value)
                    col_content.append(tcell_value)
                except: #the value might be float
                    # print "row:",row,"col:",col,s.cell(row,col).value
                    # tsheet.write(row,col,s.cell(row,col).value)
                    
                    nontexts = s.cell(row,col).value
                    col_content.append(str(nontexts))
            row_value = "\t".join(col_content)
            rows_content.append(row_value)
            tsheet.flush_row_data()
            
        try:
            sheet_txt = "\n".join(rows_content).encode('utf8')
        except:
            sheet_txt = "\n".join(rows_content)
        all_lines = invert_txt_table(sheet_txt)
        print_table(all_lines,outfile)

    outfile.close()
    
    print "saving..."
    tbook.save('english_output.xls')
    print "saved."

     
if __name__ == "__main__":
    main()
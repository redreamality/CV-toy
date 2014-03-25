# -*- coding:utf-8 -*-

import codecs

#打印表格头
def print_head(f):
    f.write("<table>\n")
    
#打印表行
def print_line(line,f):
    tr = "<tr>\n"
    tds = ""
    if line is not None and len(line) > 0:
        fields = abstract_fields(line)
        for filed in fields:
            td = "\t<td>%s</td>\n" % filed  
            tds += td

        tr += "{0}</tr>\n".format(tds)
        f.write(tr)
   
    
def abstract_fields(line):
    line = line.strip()
    fields = line.split("\t")
    return fields
    
#打印表格尾
def print_end(f):
    f.write("</table>\n")

if __name__=="__main__":
    
    #file input
    txtfile = open("table.txt",'r')

    #file output
    outfile = open("tabhtml.html",'w')
    print_head(outfile)
    #read and output table by line
    while 1:
        line = txtfile.readline()
        if not line:
            break 
        #print table
        print_line(line,outfile)
    
    print_end(outfile)

    
    #close
    txtfile.close()
    outfile.close()

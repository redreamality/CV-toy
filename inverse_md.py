# -*- coding:utf-8 -*-
#auther:redreamality 谢晨昊

# what this code doing?
# 读取表格状记录的简历，导出成简易html（markdown）格式
import codecs

def main():    
    #file read and process
    txtfile = open("table.txt",'r')
    alltexts = invert_table(txtfile)
    txtfile.close()

    #file output
    outfile = open("tabhtml.html",'w')
    print_table(alltexts,outfile)
    outfile.close()



#read and process table by line
def invert_table(txtfile):
    alltexts = [] #储存表格内容
    count = 0
    while 1:
        line = txtfile.readline()
        if not line:
            break
        count += 1 #表头不参与逆序排列
        
        if count == 1:
            alltexts.insert(0,line)#表头            
        else:
            alltexts.insert(1,line)#完成倒序
            
    return alltexts

#打印表格
def print_table(alltexts,outfile):
    print_head(outfile)
        
    for alltext in alltexts:
        print_line(alltext,outfile)

    print_end(outfile)


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
    main()
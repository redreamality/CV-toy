# -*- coding:utf-8 -*-
#author:redreamality л���

import codecs

def main():    
    #file read and process
    txtfile = open("table.txt",'r')
    all_lines = invert_table(txtfile)
    txtfile.close()

    #file output
    outfile = open("tabhtml.html",'w')
    print_table(all_lines,outfile)
    outfile.close()



#read and process table by line
def invert_table(txtfile):
    all_lines = [] #���������������
    count = 0 #��ͷ��������������
    while 1:
        line = txtfile.readline()
        if not line:
            break
        count += 1 
        
        if count == 1:
            all_lines.insert(0,line)#��ͷ            
        else:
            all_lines.insert(1,line)#��ɵ���
            
    return all_lines

#��ӡ���
def print_table(all_lines,outfile):
    print_head(outfile)
        
    for line in all_lines:
        print_line(line,outfile)

    print_end(outfile)


#��ӡ���ͷ
def print_head(f):
    f.write("<table>\n")

#��ӡ����
def print_line(line,f):
    tr = "<tr>\n"
    tds = ""
    if line is not None and len(line) > 0:
        elements = abstract_elements(line)
        for element in elements:
            td = "\t<td>%s</td>\n" % element  
            tds += td

        tr += "{0}</tr>\n".format(tds)
        f.write(tr)
   
    
def abstract_elements(line):
    line = line.strip("\n")
    elements = line.split("\t")
    return elements
    
#��ӡ���β
def print_end(f):
    f.write("</table>\n")

if __name__=="__main__":
    main()
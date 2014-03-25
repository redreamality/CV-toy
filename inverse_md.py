# -*- coding:utf-8 -*-
#auther:redreamality л���

# what this code doing?
# ��ȡ���״��¼�ļ����������ɼ���html��markdown����ʽ
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
    alltexts = [] #����������
    count = 0
    while 1:
        line = txtfile.readline()
        if not line:
            break
        count += 1 #��ͷ��������������
        
        if count == 1:
            alltexts.insert(0,line)#��ͷ            
        else:
            alltexts.insert(1,line)#��ɵ���
            
    return alltexts

#��ӡ���
def print_table(alltexts,outfile):
    print_head(outfile)
        
    for alltext in alltexts:
        print_line(alltext,outfile)

    print_end(outfile)


#��ӡ���ͷ
def print_head(f):
    f.write("<table>\n")

#��ӡ����
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
    
#��ӡ���β
def print_end(f):
    f.write("</table>\n")

if __name__=="__main__":
    main()
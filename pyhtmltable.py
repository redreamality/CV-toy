# -*- coding:utf-8 -*-
#Author Tandaly
#Date 2013-04-09
#File Csv2html.py

import string

#������
def main():
    print_head()
    maxWidth = 100
    count = 0
    while True:
        try:
            print "aha"
            line = str(raw_input())
            if count == 0:
                color = "lightgreen"
            elif count%2 == 0:
                color = "white"
            else:
                color = "lightyellow"
            print_line(line, color, maxWidth)
            count += 1
        except EOFError:
            break
    print_end()

#��ӡ���ͷ
def print_head():
    print("<table border=\"1\">")

#��ӡ����
def print_line(line, color, maxWidth):
    tr = "<tr bgcolor=\"{0}\">".format(color)
    tds = ""
    if line is not None and len(line) > 0:
        fields = axtract_fields(line)
        for filed in fields:
            td = "<td align=\"right\">{0}</td>".format(filed if (len(str(filed)) <= maxWidth) else (str(filed)[:100] + "..."))  
            tds += td

        tr += "{0}</tr>".format(tds)
        print(tr)
    
#��ӡ���β
def print_end():
    print("</table>")

#��ȡ��ֵ
def axtract_fields(line):
    line = escape_html(line)
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"":
            if quote is None:
                quote = c
            elif quote == c:
                quote = None
            continue
        if quote is not None:
            field += c
            continue
        if c in ",":
            fields.append(field)
            field = ""
        else:
            field += c
    if len(field) > 0:
        fields.append(field)
    return fields

#�����������
def escape_html(text):
    text = text.replace("&", "&")
    text = text.replace(">", ">")
    text = text.replace("<", "<")
    return text

#�������
if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*
import codecs #防止编码问题

#传入的参数为path和code，path表示txt文件的绝对或相对路径，code表示该txt的编码，一般为utf-8无bom，两个参数的数据类型都为str。
def readtxt(path, code):
    with codecs.open(path, 'r', encoding=code)as f:
        txt_lines = f.readlines()
    return txt_lines

#传入参数为path、content和code，path和code和上述相同，content即为写入的内容，数据类型为字符串。
def writetxt(path, content, code):
    with codecs.open(path, 'a', encoding=code)as f:
        f.write(content)
    return path+' is ok!'

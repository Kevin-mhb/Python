#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-24 17:55:09
# @Author  : kevin ma (mahaibin97@gmail.com)
# @Link    : http://www.aduxingzhe.com
# @Version : $Id$

#多文件合并实例
#将联系人的姓名、电话、邮箱做到一个文件中


def main():
    ftele1=open('TeleAddressBook.txt','rb')#打开文件
    ftele2=open('EmailAddressBook.txt','rb')
 

    ftele1.readline()#跳过第一行
    ftele2.readline()
    lines1 = ftele1.readlines()#读取除第一行以外的所有内容
    lines2 = ftele2.readlines()
 

    list1_name = []  #建立空列表，用于接收读取到的信息
    list1_tele = []
    list2_name = []  
    list2_email = []
 

    for line in lines1:#获取第一个文本中的姓名和电话信息
        elements = line.split()
        list1_name.append(str(elements[0].decode('gbk')))
        list1_tele.append(str(elements[1].decode('gbk')))    #将文本读出来的bytes转换为str类型
 
    for line in lines2:#获取第二个文本中的姓名和邮件信息
        elements = line.split()
        list2_name.append(str(elements[0].decode('gbk')))
        list2_email.append(str(elements[1].decode('gbk')))
 

    ###开始处理###
    lines = []#建立新的了列表3
    lines.append('姓名\t   电话\t\t           邮箱\n')#生成新的表头
 

    #按索引方式遍历姓名列表1
    for i in range(len(list1_name)): 
        s= ''
        if list1_name[i] in list2_name:#如果list1中的人在list2中也存在
                j = list2_name.index(list1_name[i]) #找到姓名列表1对应列表2中的姓名索引位置
                s = '\t'.join([list1_name[i], list1_tele[i], list2_email[j]])
                s += '\n'
        else:#如果list1中的人在list2中不存在
                s = '\t'.join([list1_name[i], list1_tele[i], str('   ------------   ')])
                s += '\n'
        lines.append(s)#将信息添加到列表3中
         
    #处理姓名列表2中剩余人的信息       
    for i in range(len(list2_name)): 
        s= ''
        if list2_name[i] not in list1_name:
                s = '\t'.join([list2_name[i], str('   ------------   '), list2_email[i]])
                s += '\n'
        lines.append(s)


 #将lines中的信息写入文件
    ftele3 = open('AddressBook.txt', 'w')
    ftele3.writelines(lines)
    ftele3.close()#关闭文件
    ftele1.close()
    ftele2.close()
 
 #输出一条提示语
    print("The addressBooks are merged!\nYou can watch AdderssBook in folder.\n")
 
 #执行函数
if __name__ == "__main__":
    main()

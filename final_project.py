#coding:gbk
'''
作者：刘奇
目的：对文本人物关系间的提取
2019/12/25
'''
string_connection=""
string_node=""
names={"渡部","秋叶","有美子","园美","新谷","古崎","黑泽","达也","绫子","妙子","彩色夫人","丽子","真纪子","刑事警察"}#建立名字的字典
for name1 in names:
    for name2 in names:#产生人物之间关系
        times = 0
        passage=open("黎明的街道.txt",'r',encoding='gbk')
        for x in passage.readlines():
            if (set(list(name1)) < set(list(x))) and (set(list(name2)) < set(list(x))):#判断名字是否是段落的子集
                times += 1
        if name1==name2 and times!=0:
          string=("%s %s %s\n"%(name1,name2,times))
          string_node += string
        elif name1!=name2 and times!=0:
            string = ("%s %s %s\n" % (name1, name2, times))
            string_connection += string
        passage.close()
print(string_connection,string_node)
file1=open("string_connection.txt","w",encoding="gbk")#写入文件
file1.write(string_connection)
file1.close()
file2=open("string_node.txt","w",encoding="gbk")
file2.write(string_node)
file2.close()


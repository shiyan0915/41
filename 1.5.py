id = ['1','2','3','4','5','6']
name = ['赵一','陈二','张三','李四','王五','马六']
dic = dict(zip(id,name))
for id in dic:
    if (int(id) % 2 == 0):
        del dic[id]
    print(dic)



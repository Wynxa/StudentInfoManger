# 学员信息展示连接后台
from DataBase.model import Model
import math


# 数据展示
def myshow(stulist):
    print()
    print("="*16,"学员信息展示","="*16)
    print("|{:<4}|{:<8}|{:<4}|{:<8}|{:<3}|" .format("id","name","sex","classid","age"))
    print("="*46)
    for stu in stulist:
        print("|{:<4}|{:<8}|{:<4}|{:<8}|{:<3}|".format(stu["id"],stu["name"],stu["sex"],stu["classid"],stu["age"]))
    print()

if __name__ == "__main__":
    mod = Model("stu")
    # 主循环体
    while True:
        print("="*16,"学员信息管理","="*16)
        print("1.查看    2.搜索   3.分页   4.添加   5.删除   6.退出")
        print("="*46)
        c = input("请输入对应的操作：")
        if c=="1":
            myshow(mod.findAll())
            input("请输入回车键进行后续操作")
        elif c=="2":
            where = []
            kw = input("请输入要搜索的关键词（姓名/班级号）：")
            if kw is not None:
                where.append("(name like '%{0}' or classid like '%{0}')".format(kw)) 
            myshow(mod.select(where= where))
        elif c=="3": #分页
            pagesize = 4 #number of every pages
            page = 1 #now page number
            while True:
                total = mod.total()
                max_page = math.ceil(total / pagesize) # the number of total page
                limit = "%d,%d"%((page-1)*pagesize,pagesize)
                myshow(mod.select(limit=limit))
                print("总计：%d条，当前是第%d/%d页"%(total,page,max_page))
                p = input("请输入q退出")
                if p == "q":
                    break
                else :
                    page = int(p)
        elif c=="4": #添加
            print()
            print("="*16,"学员信息添加","="*16)
            stu = {}
            stu["name"] = input("请输入添加的姓名：")
            stu["sex"] = input("请输入添加的性别（w/m）：")
            stu["classid"] = input("请输入添加的班级号：")
            stu["age"] = input("请输入添加的年龄：")
            mod.save(stu)
            myshow(mod.findAll())
            input("请输入回车键进行后续操作")
        elif c=="5": #删除
            print()
            myshow(mod.findAll())
            sid = int(input("请输入要删除的id号："))
            mod.delete(sid)
            myshow(mod.findAll())
            input("请输入回车键进行后续操作")
        elif c=="6": #退出
            break
        else :
            input("输入内容无效请重新输入：")















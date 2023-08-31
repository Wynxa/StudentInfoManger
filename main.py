'''GitHub地址：https://github.com/Wynxa/StudentInfoManger.git'''

import function as func

def main():
    while True:
        func.show_menu()   
        n = int(input("请输入对应操作："))
        if n == 1 :                     #查看当前插入学生
            func.show_student()
        elif n == 2 :                   #添加学生信息并保存
            func.info_student()
            func.save()
            func.show_student()
        elif n == 3 :
            func.removeStudent()       #删除学生信息并保存
            func.save()
            func.show_student()
        elif n == 4 :                   #查看所有学生信息，包括之前插入以及当前插入
            #func.show_all()            #以一般形式输出学生信息
            func.load_file()            #DataFrame形式输出学生信息（更美观）
        elif n == 5 :
            break
        else:
            print("输入无效请重新输入")                       #退出


            

if __name__ == '__main__':
    main()
 
 
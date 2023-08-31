import pandas as pd
import csv

#插入数据
#空列表用于存储学生信息，该列表元素为字典
student_list = []                                          
def info_student(name = "  ",age =None,classid = "  "):#设置默认参数
    #使用input获取信息
    ssid = input("请输入学生学号：")
    name = input("请输入要添加的学生姓名：")
    age = input("请输入要添加的学生年龄：")
    classid = input("请输入要添加的学生的班级号：")
    #每个学生信息以字典形式存储
    student_dict = {'ssid' : ssid, 'name': name, 'age': age, 'classid': classid}
    #将学生信息添加到学生表里
    student_list.append(student_dict)
    print("\n")
    print("添加成功")
    print("\n")

#删除数据
# def remove_student():
#     n = input("请输入要删除学生学号：")
#     for i in student_list:
#         if n == i['ssid']:
#             student_list.remove(i)
#             print("\n")
#             print("删除成功")
#         else:
#             print("\n")
#             print("该学生不存在")

#读取数据
def show_student():
    #判断有无学生信息
    if len(student_list) > 0:
        print("================================学员信息浏览===============================\n")
        for i in student_list:
            #格式化输出（这里中文字符输出形式不齐）
            print("|ssid:{ssid:<25}  |name:{name:<25}  |age:{age:<25}  |classid:{classid:<25}\n".format(**i))
        print("==========================================================================\n")
    else:
        print("\n")
        print("没有学生")

#操作菜单
def show_menu():
    print("========================学员信息管理=======================\n")
    print("1.查看     2.添加      3.删除      4.查看已有学生     5.退出\n")
    print("==========================================================\n")


#保存数据
def save():
    csv_file_path = "D:/pythonProject/shixi/day03/StudentInfoManger/student.csv"
    student_list1 = [] 
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            student_list1.append(row)
    existing_data = set()
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                existing_data.add(row['ssid'])  # 假设 'ssid' 是数据中的唯一标识
    except FileNotFoundError:
        pass

    with open(csv_file_path, 'a', newline='', encoding='utf-8') as csv_file:
        fieldnames = ["ssid", "name", "age", "classid"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # 如果文件为空，写入列名
        if csv_file.tell() == 0:
            writer.writeheader()

        # 逐行写入数据
        for item in student_list:
            if item['ssid'] not in existing_data:
                writer.writerow(item)
                existing_data.add(item['ssid'])

def removeStudent():
    csv_file_path = "D:/pythonProject/shixi/day03/StudentInfoManger/student.csv"

# 读取CSV文件并存储数据到列表中
    data = []
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append(row)

    # 找到要删除的行（示例：根据某个字段来删除）
    row_to_delete = None
    for row in data:
        n = input("请输入要删除学生学号：")
        if row["ssid"] == n:  # 指定要删除的行的标识
            row_to_delete = row
            break

    # 如果找到了要删除的行，则从数据列表中移除
    if row_to_delete:
        data.remove(row_to_delete)

    # 将更新后的数据写回到CSV文件
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ["ssid", "name", "age", "classid"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for row in data:
            writer.writerow(row)

#读取数据，按行展示学生数据
def load_file():
    file_path = "D:/pythonProject/shixi/day03/StudentInfoManger/student.csv"
    with open(file_path, 'r') as file:
        for line in file:
            print(line, end='')

#展示已有学生
# 将学生数据按DataFrame形式输出，DataFrame形式有较好的可读性      
def show_all():
    csv_file_path = "D:/pythonProject/shixi/day03/StudentInfoManger/student.csv"  # 指定 CSV 文件路径
    df = pd.read_csv(csv_file_path)                       # 读取 CSV 文件并转换为 DataFrame
    print(df)
    print("\n")                                             # 打印 DataFrame

# def modify_info():
#     """
#     修改学生信息
#     :return:
#     """
#     # 使用input()获取要修改的学生学号
#     sno = input('请输入要修改的学生的学号:')
#     # 判断学生信息是否存在
#     for stu in student_list:
#         if stu['ssid'] == sno:
#             # 学生信息存在,对学生进行修改操作
#             stu['name'] = input('请输入修改后的姓名:\n')
#             stu['ssid'] = input('请输入修改后的学号:\n')
#             stu['age'] = input('请输入修改后的年龄:')
#             stu['classid'] = input('请输入修改后的班级:\n')
#             break
#     # 学生信息不存在,直接结束
#     else:
#         print('该学生信息不存在!!!\n')

# def search_info():
#     """
#     查询单个学生信息
#     :return:
#     """
#     # 使用input()获取要查询的学生学号
#     sno = input('请输入要查询的学生的学号:')
#     # 判断学生信息是否存在
#     for stu in student_list:
#         if stu['ssid'] == sno:
#             # 学生信息存在,对学生进行查询操作
#             print('\n' +  f'姓名:{stu["name"]},学号:{stu["ssid"]},年龄:{stu["age"]},班级:{stu["classid"]}')
#             break
#     # 学生信息不存在,直接结束
#     else:
#         print('\n' + '该学生信息不存在!!!')

        

    
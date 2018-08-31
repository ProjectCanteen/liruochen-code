#文件操作模块     主要定义涉及文件IO的函数
import pickle       #导入pickle模块
import os       #导入os模块

#函数login，参数：用户名，密码，用户身份，访问存放用户登录信息的文件，返回布尔值。
def login(user_name,key,user_identity):
    if user_identity=='student':
        with open('../data/user_info/student.pickle') as f:
            stu_file=pickle.load(f)     #stu_file是存放学生类的列表
            for each_stu in stu_file:
                if each_stu.user_name==user_name and each_stu.key==key:
                    i=True      #判断是否找到对应用户
                    break
            if i==True:
                return(True)
            else:
                return(False)
    elif user_identity=='stuff':
        with open('../data/user_info/stuff.pickle') as f:
            stuff_file=pickle.load(f)
            for each_stuff in stuff_file:
                if each_stuff.user_name==user_name and each_stuff.key==key:
                    i=True
                    break
            if i==True:
                return(True)
            else:
                return(False)
    elif user_identity=='admin':
        with open('../data/user_info/admin.pickle') as f:
            admin_file=pickle.load(f)
            for each_admin in admin_file:
                if each_admin.user_name==user_name and each_admin.key==key:
                    i=True
                    break
            if i==True:
                return(True)
            else:
                return(False)
    else:
        print('User_identity is illegal!')

#函数creat_stumenu，参数：学生订单和日期，一个学生类，创建字典，key为学生类，value为订单列表，用pickle保存在本地
def creat_stumenu(stu,order_list,date):
    #项目的日期格式均为"18-8-31"的格式，便于字符串操作
    with open('../data/order_info/'+date+'.pickle') as f:
        today_stumenu=pickle.load(f)
        #today_stumenu是列表，各元素是字典，key为学生类，value为订单字典
        order_dict=dict()
        order_dict[stu]=order_list
        today_stumenu.append(order_dict)        #新增数据
    pickle.dump(today_stumenu,'../data/order_info/'+date+'_order.pickle')
    #保存更改后的文件

#函数create_menu，参数：员工创建的菜单列表和日期，创建字典，key为日期，value为菜单列表，用pickle保存在本地
def creat_menu(menu_list,date):
    menu_dict=dict()
    menu_dict[date]=menu_list
    pickle.dump(menu_dict,'../data/menu_info/'+date+'_menu.pickle')

#函数get_menu，参数：日期，返回存放菜单的列表
def get_menu(date):
    with open('../data/menu_info/'+date+'_menu.pickle') as f:
        menu_file=pickle.load(f)    #menu_list是菜单列表
    return(menu_file)

#函数delete_stumenu,参数：日期，用户名，删除该学生该日的订单,若该学生该日无订单，则返回False
def delete_stumenu(date,user_name):
    with open('../data/order_info/'+date+'_order.pickle') as f:
        order_file=pickle.load(f)       #order_file是一个列表，元素是字典，详细内容参上
        for each_order in order_file:
            key_list=list(each_order.keys())
            key=key_list[0]
            if user_name==key.user_name:
                order_file.remove(each_order)
                i=True
                break
        if i!=True:
            return(False)

#函数delete_menu,参数：日期，删除该日的菜单
def delete_menu(date):
    try:
        file='../data/menu_list'+date+'_menu.pickle'
        os.remove(file)
    except:
        print('文件删除出错！')

#函数creat_newstu,参数：一个学生类，打开存放学生类的pickle，向列表中新增元素
def creat_newstu(stu):
    with open('../data/user_info/student.pickle') as f:
        stu_file=pickle.load(f)     #stu_file是存放学生类的列表
    stu_file.append(stu)
    pickle.dump(stu_file,'../data/user_info/student.pickle')

#函数creat_newstuff,参数：一个员工类，打开存放员工类的pickle，向列表中新增元素
def creat_newstuff(stuff):
    with open('../data/user_info/stuff.pickle') as f:
        stuff_file=pickle.load(f)
    stuff_file.append(stuff)
    pickle.dump(stuff_file,'../data/user_info/stuff.pickle')

#函数creat_combine,参数：一个数组，一个key，产生菜品的组合以字典形式保存在本地
def creat_combine(menu_list,key):
    menu_dict=dict()
    menu_dict[key]=menu_list
    pickle.dump(menu_dict,'../data/menu_combine/'+key+'.pickle')

#函数delete_combine,参数：key，删除该组合
def delete_combine(key):
    try:
        file='../data/menu_combine/'+key+'.pickle'
        os.remove(file)
    except:
        print('文件删除出错！')

#函数get_combine,返回菜品组合,参数：key
def get_combine(key):
    try:
        combine=pickle.load('../data/menu_combine/'+key+'.pickle')
        return(combine)
    except:
        print('文件读取出错！')

#END
        


       






#类模块（class.py）      对学生，员工和管理员的数据建模供主模块调用
#本模块需调用B模块

import file_operate     #导入B模块
#定义学生类
class student():
    def __init__(self,user_name,key,name,identity):
        '''
        定义学生类属性
        user_name用户名
        key密码
        name姓名
        identity身份
        '''
        self.user_name=user_name
        self.key=key
        self.user_name=name
        self.identity='student'

    def get_today_menu(self,date,window):
        #定义获取今日菜单的方法
        #需要调用B模块
        #参数：date（日期）,window(窗口号）
        return(file_operate.get_menu(date,window))      #返回菜单列表
        
    def creat_order(self,order_list,date,window):
        #定义创建订单的方法
        #参数：order_list（含订单的列表），date（日期），window（窗口号）
        #将数据结构保存
        file_operate.creat_stumenu(self,order_list,date,window)

    def change_order(self,delete_item,add_item,stu,window,date):
        #定义更改订单的方法
        #参数：delete_item（删除项）,add_item（新增项）,old_order_list（原订单列表），stu（学生对象），window（窗口号），date（日期）
        #返回一个字典，key为日期，value为新订单列表,并将新的数据结构保存
        old_order_dict=file_operate.delete_stumenu(date,stu.user_name,window)       #旧订单已删除
        old_order_list=old_order_dict.values()[0]
        new_order_list=old_order_list.copy()
        new_order_list.remove(delete_item)
        new_order_list.append(add_item)     #进行数据的删改
        new_order_dict=file_operate.creat_stumenu(stu,new_order_list,date,window)       #创建新订单
        return(new_order_dict)      #返回新订单

    def delete_order(self,date,stu,window):
        #定义删除订单的方法
        #参数：date日期，stu学生对象，window窗口号
        #返回已删除的数据
        #需调用B模块
        old_order_dict=file_operate.delete_stumenu(date,stu.user_name,window)       #删除数据
        return(old_order_dict)  #返回已删除的数据
                        
#定义员工类
class stuff():
    def __init__(self,user_name,key,name,identity):
        self.user_name=user_name
        self.key=key
        self.user_name=name
        self.identity='stuff'
        '''
        定义员工类的属性
        user_name用户名
        key密码
        name姓名
        identity身份
        '''

    def get_menu(self,date,window):
        #查看菜单
        #需调用B模块
        #返回含菜单的列表
        #参数：date（日期），window（窗口号）
        return(file_operate.get_menu(date,window))      #返回菜单列表
        
        
    def creat_menu(self,date,menu_list,window):
        menu=file_operate.creat_menu(menu_list,date,window)
        return(menu)        #返回菜单
        #创建菜单
        #参数：date（日期），menu_list（含菜单的列表）,window(窗口号）
        #返回一个字典，key为date，value菜单列表，保存新的数据结构

#更改至此
    def change_menu(self,date,old_list,delete_item,add_item):
        new_list=old_list.copy()
        new_list.remove(delete_item)
        new_list.append(add_item)
        new_menu_dict=dict()
        new_menu_dict[date]=new_list
        return(new_menu_dict)
        #更改菜单
        #参数：date（日期），old_list（存放旧菜单的列表），delete_item（要删除的菜品），add_item（要新增的菜品）
        #返回一个字典，key为日期，value为新菜单列表

    def get_order_now(self,date,window_number):
        #查看当前各窗口的预订情况
        #参数：date（日期），window_number（窗口号）
        #返回列表，元素均为字典，key为菜名，value是数量
        #需调用B模块
        pass

#定义管理员类
class admin():
    def __init__(self,user_name,key,name,identity):
        self.user_name=user_name
        self.key=key
        self.name=name
        self.identity=identity
        '''
        管理员类属性初始化
        user_name用户名
        key密码
        name姓名
        identity身份
        '''

    def add_stuaccount(self,user_name,key,name):
        new_stuaccount=student(user_name,key,name)
        return(new_stuaccount)
        #创建学生账户
        #参数：user_name用户名，key密码，name姓名
        #返回一个student类

    def delete_stuaccount(self,user_name):
        #删除学生账户
        #参数：user_name用户名
        #需调用B模块
        pass

    def add_stuffaccount(self,user_name,key,name):
        new_stuffaccount=stuff(user_name,key,name)
        return(new_stuffaccount)
        #创建员工账户
        #参数：user_name用户名，key密码，name姓名
        #返回一个stuff类

    def delete_stuffaccount(self,user_name):
        #删除员工账户
        #参数：user_name用户名
        #需调用B模块
        pass

                        
    


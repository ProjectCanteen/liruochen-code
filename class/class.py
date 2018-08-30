#类模块（class.py）      对学生，员工和管理员的数据建模供主模块调用
#本模块需调用B模块

#定义学生类
class student():
    def __init__(self,user_name,key,name):
        '''
        定义学生类属性
        user_name用户名
        key密码
        name姓名
        '''
        self.user_name=user_name
        self.key=key
        self.user_name=name

    def get_today_menu(self,date):
        #定义获取今日菜单的方法
        #需要调用B模块
        #参数：date（日期）
        pass
        
    def creat_order(self,date,order_list):
        #定义创建订单的方法
        #参数：date(日期），order_list（含订单的列表）
        #返回一个字典，key为日期，value为订单列表
        order_dict=dict()
        order_dict[date]=order_list
        return(order_dict)

    def change_order(self,date,delete_item,add_item,old_order_list):
        #定义更改订单的方法
        #参数：date（日期），delete_item（删除项）,add_item（新增项）,old_order_list（原订单列表）
        #返回一个字典，key为日期，value为新订单列表
        new_order_list=old_order_list.copy()
        new_order_list.remove(delete_item)
        new_order_list.append(add_item)
        new_order_dict=dict()
        new_order_dict[date]=new_order_dict
        return(new_order_dict)

    def delete_order(self,date):
        #定义删除订单的方法
        #参数：date日期
        #需调用B模块
        pass



        
        
        
#定义员工类
class stuff():
    def __init__(self,user_name,key,name):
        self.user_name=user_name
        self.key=key
        self.user_name=name
        '''
        定义员工类的属性
        user_name用户名
        key密码
        name姓名
        '''

    def get_menu(self,date):
        #查看菜单
        #需调用B模块
        #返回含菜单的列表
        #参数：date（日期）
        pass
        
    def creat_menu(self,date,menu_list):
        menu_dict=dict()
        menu_dict[date]=menu_list
        return(menu_dict)
        #创建菜单
        #参数：date（日期），menu_list（含菜单的列表）
        #返回一个字典，key为date，value菜单列表

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
    def __init__(self,user_name,key,name):
        self.user_name=user_name
        self.key=key
        self.name=name
        '''
        管理员类属性初始化
        user_name用户名
        key密码
        name姓名
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

                        
    


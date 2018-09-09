#文件操作模块     主要定义涉及文件IO的函数
import pickle       #导入pickle模块
import os       #导入os模块

#函数login，参数：用户名，密码，用户身份，用户身份必须为'student','stuff','admin'中的一种，访问存放用户登录信息的文件，返回布尔值。

def login(user_name,key,user_identity):
    def check(user_name,key,user_identity):
        try:
            with open('../data/user_info/'+str(user_identity)+'/'+str(user_name)+'.pickle','rb') as f:
                user=pickle.load(f)
            if user.key==key:
                return(True)
            else:
                return(False)
        except IOError:
            return('用户不存在！')        #若文件不存在，则返回错误信息

    response=check(user_name,key,user_identity)
    return(response)        #最终的返回值
   
#函数creat_stumenu，参数：学生订单和日期和窗口号，一个学生类，创建字典，key为学生类，value为订单列表，订单列表第1项是窗口号，用pickle保存在本地，返回新的订单

def creat_stumenu(stu,order_list,date,window):
    #项目的日期格式均为"18-8-31"的格式，便于字符串操作
    try:
        with open('../data/order_info/'+str(window)+'/'+str(date)+'_order.pickle','rb') as f:
            today_stumenu=pickle.load(f)
            #today_stumenu是列表，各元素是字典，key为学生类，value为订单字典
    except IOError as err:
        return(str(err))        #若出错，则将错误信息返回
    order_dict=dict()
    order_list.append(window)       #列表第一项是窗口号
    order_dict[stu]=order_list
    if isinstance(today_stumenu,list):
        today_stumenu.append(order_dict)        #新增数据
    else:
        today_stumenu=[]
        today_stumenu.append(order_dict)
    try:
        with open('../data/order_info/'+str(window)+'/'+str(date)+'_order.pickle','wb') as f:
            pickle.dump(today_stumenu,f)
            #保存更改后的文件
    except IOError as err:
        return(str(err))
    try:
        with open('../data/order_now_info/'+str(window)+'/'+str(date)+'_ordernow.pickle','rb') as f:
            order_now_dict=pickle.load(f)       #字典
        for item in order_list:
            order_now_dict[item]+=1
        with open('../data/order_now_info/'+str(window)+'/'+str(date)+'_ordernow.pickle','wb') as f:
            pickle.dump(order_now_dict,f)       #更新订单状态
    except IOError as err:
        return(str(err))
    return(order_dict)

#函数create_menu，参数：员工创建的菜单列表和日期和窗口号，创建字典，key为日期，value为菜单列表，菜单列表第一项是窗口号，用pickle保存在本地，并返回菜单

def creat_menu(menu_list,date,window):
    menu_list.append(window)        #列表第一项是窗口号
    menu_dict=dict()
    menu_dict[date]=menu_list
    try:
        with open('../data/menu_info/'+str(window)+'/'+str(date)+'_menu.pickle','wb') as f:
            pickle.dump(menu_dict,f)
    except IOError as err:
        return(str(err))        #若出错，则将错误信息返回
    order_now_dict=dict()       #新增订单状态
    for item in menu_list:
        order_now_dict[item]=0
    try:
        with open('../data/order_now_info/'+str(window)+'/'+str(date)+'_ordernow.pickle','wb') as f:
            pickle.dump(order_now_dict,f)       #创建订单状态字典
    except IOError as err:
        return(str(err))
    return(menu_dict)   #返回菜单


#函数get_menu，参数：日期，窗口号，返回存放菜单的列表

def get_menu(date,window):
    try:
        with open('../data/menu_info/'+str(window)+'/'+str(date)+'_menu.pickle','rb') as f:
            menu_file=pickle.load(f)    #menu_list是菜单列表
    except IOError as err:
        return(str(err))        #若出错，则将错误信息返回
    return(menu_file[1:])       #列表第一项是窗口号，因此需进行切片操作

#函数delete_stumenu,参数：日期，用户名，窗口号，删除并返回该学生该日的订单,若该学生该日该窗口无订单，则返回False

def delete_stumenu(date,user_name,window):
    try:
        with open('../data/order_info/'+str(window)+'/'+str(date)+'_order.pickle','rb') as f:
            order_file=pickle.load(f)       #order_file是一个列表，元素是字典，详细内容参上
    except IOError as err:
        return(str(err))        #若出错，则将错误信息返回
    for each_order in order_file:
        key_list=list(each_order.keys())
        key=key_list[0]
        if user_name==key.user_name:
            deleted_menu=each_order
            order_file.remove(deleted_menu)
            i=True
            break
    if i!=True:
        return(False)
    with open('../data/order_info/'+str(window)+'/'+str(date)+'_order.pickle','wb') as f:
        pickle.dump(order_file,f)
    with open('../data/order_now_info/'+str(window)+'/'+str(date)+'_ordernow.pickle','rb') as f:
        order_now_dict=pickle.load(f)
    for item in deleted_menu:
        order_now_dict[item]=order_now_dict[item]-1
    with open('../data/order_now_info/'+str(window)+'/'+str(date)+'_ordernow.pickle','wb') as f:
        pickle.dump(order_now_dict,f)       #更新订单状态
    return(deleted_menu)        #将旧订单返回

#函数delete_menu,参数：日期，窗口号，删除并返回该日该窗口的菜单

def delete_menu(date,window):
    try:
        file='../data/menu_info/'+str(window)+'/'+str(date)+'_menu.pickle'
        deleted_file=pickle.load(file)
        os.remove(file)
        file_1='../data/order_now_info/'+str(window)+'/'+str(date)+'_ordernow.pickle'
        os.remove(file_1)
        return(deleted_file)        #返回删除的菜单
    except:
        return('菜单未创建！')        #若出错，则将错误信息返回

#函数get_order_now
#参数：date（日期），window（窗口号）
def get_order_now(date,window):
    try:
        with open('../data/order_info/'+str(window)+'/'+str(date)+'_order.pickle','rb') as f:
            order_now=pickle.load(f)
    except IOError as err:
        return(str(err))        #若出错则将错误信息返回
    return(order_now)       #返回当前订单状态

#函数creat_newuser,参数：类，向专用文件夹中添加文件

def creat_newuser(class_):
    def creat_newfile(class_,name,identity):
        try:
            with open('../data/user_info/'+str(identity)+'/'+str(name)+'/.pickle','wb') as f:
                pickle.dump(class_,f)
            return(class_)        #若保存成功则返回对象
        except IOError as err:
            return(str(err))        #若出错则将错误信息返回
    creat_newfile(class_,class_.user_name,class_.identity)

#函数delete_user,参数：user_name（用户名），identity（身份）
def delete_user(user_name,identity):
    file='../data/user_info/'+str(identity)+'/'+str(user_name)+'/.pickle'
    try:
        os.remove(file)
        return(True)        #删除成功返回True
    except Exception as e:
        return(str(e))      #出错将错误信息返回

#函数creat_combine,参数：一个数组，一个key，产生菜品的组合以字典形式保存在本地

def creat_combine(menu_list,key):
    menu_dict=dict()
    menu_dict[key]=menu_list
    try:
        with open('../data/menu_combine/'+str(key)+'_combine.pickle','wb') as f:
            pickle.dump(menu_dict,f)
    except IOError as err:
        return(str(err))        #若出错，则将错误信息返回

#函数delete_combine,参数：key，删除该组合

def delete_combine(key):
    try:
        file='../data/menu_combine/'+str(key)+'_combine.pickle'
        os.remove(file)
    except:
        return('文件删除出错！')       #若出错，则将错误信息返回

#函数get_combine,返回菜品组合,参数：key

def get_combine(key):
    try:
        with open('../data/menu_combine/'+str(key)+'_combine.pickle','rb') as f:
            combine=pickle.load(f)
        return(combine)
    except IOError as err:
        return(str(err))        #若出错，则将错误信息返回

#END
    

        


       






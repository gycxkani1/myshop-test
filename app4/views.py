from django.shortcuts import render
from django.http import HttpResponse
import datetime

def add_userinfo(request):
    users = UserInfo()
    try:
        users.username = "zhangsan"
        users.nickname = "张三"
        users.password = "123456"
        users.suoding = 1
        users.status = "5"
        users.memo = "这是备注"
        users.score = "90.5"
        users.save()
        return HttpResponse("数据新增成功")
    except Exception as e:
        return HttpResponse("数据新增失败")

        # users=UserInfo.objects.create(username="zhangsan",nickname="张三",password="123456",)

from app4.models import *
import django.utils.timezone as timezone
def add_depart(request):
    depart=DepartInfo()
    depart.departname="技术部"
    depart.createdate=timezone.now()
    depart.save()

def add_depart1(request):
    d=dict(departname="财务部",createdate=timezone.now())
    depart=DepartInfo.objects.create(**d)

def add_userbaseinfo(request):
    d=dict(username="张三",password='123456',status=1,createdate=timezone.now())
    depart=UserBaseInfo.objects.create(**d)

def add_userbaseinfo1(request):
    depart=UserBaseInfo.objects.create(username="张三",password='123456',status=1,createdate=timezone.now())

def add_userextrainfo(request):
    #添加用户基本表
    d=dict(username="李四",password='123456',status=1,
    createdate=timezone.now())
    userbaseinfo=UserBaseInfo.objects.create(**d)
    #添加用户扩展表
    d=dict(username="李四",truename='李小四',sex=0,salary=6555.88,age=35,
    status=0,createdate=timezone.now(),memo='',user=userbaseinfo)
    userextrainfo=UserExtraInfo.objects.create(**d)

def query_userinfo(request):
    userextrainfo=UserExtraInfo.objects.get(id=1)
    userextrainfo.user.username

    user=UserBaseInfo.objects.get(id=1)
    user.userextrainfo.username #扩展表名称需要小写

    result=UserExtraInfo.objects.get(id=1)
    result.user.username

def add_cardinfo(request):
    #获取用户基本表
    user=UserBaseInfo.objects.get(id=1)
    #添加卡信息表
    card=CardInfo(cardno='1111111111111111',bank='工商银行',user=user)
    card.save()
    card=CardInfo(cardno='2222222222222222222',bank='招商银行',user=user)
    card.save()

def query_cardinfo(request):
    #通过1查询多。获取用户基本表
    user=UserBaseInfo.objects.get(id=1)
    user.cardinfo_set.all()
    #通过多查询1
    card=CardInfo.objects.get(id=1)
    card.user.username

#多对多
def add_userskillinfo(request):
    #获取用户基本表
    user=UserBaseInfo.objects.all()
    #获取某个id=1的技能
    skill=SkillInfo.objects.get(id=1)
    #所有的用户增加id=1的技能
    result=skill.user.add(*user)



    d=dict(username="李四2",password='123456',status=1,
    createdate=timezone.now())
    userbaseinfo=UserBaseInfo.objects.create(**d)
    user=UserBaseInfo.objects.get(id=1)
    skill=SkillInfo.objects.get(id=1)
    result=skill.user.add(userbaseinfo)

def query_userskillinfo(request):
    #通过1查询多。获取用户基本表
    users=UserBaseInfo.objects.get(id=1)
    users.skillinfo_set.all()

    skills=SkillInfo.objects.all()
    for skill in skills:
        result=skill.user.all()
        print(result) 

def modify_userskillinfo(request):
    #获取用户基本表
    user=UserBaseInfo.objects.all()
    #获取某个id=1的技能
    skill=SkillInfo.objects.get(id=1)
    #修改全部用户的id=1的技能
    result=skill.user.set(user)
    #修改部分用户的id=1的技能
    user=[1,2]
    #user=UserBaseInfo.objects.filter(status=1)
    result=skill.user.set(user)

def del_userskillinfo(request):
    #获取用户基本表
    user=UserBaseInfo.objects.get(id=1)
    #获取某个id=1的技能
    skill=SkillInfo.objects.get(id=1)
    #移除指定的用户
    result=skill.user.remove(user)
    result=skill.user.remove(2)
    result=skill.user.clear()

def sel_rel(request):
    cards=CardInfo.objects.all()
    for card in cards:
        print(card.user)
    cards=CardInfo.objects.select_related("user")
    for card in cards:
        print(card.user)

def pre_rel(request):
    skills=SkillInfo.objects.prefetch_related("user")
    for skill in skills:
        print(skill.skillname)
        users=skill.user.all()
        for user in users:
            print(user.username)

from django.db.models import F
def f_func(request):
    users=UserExtraInfo.objects.all()
    for user in users:
        user.salary+=1000
        user.save()
    
    for user in users:
        user.salary=F("salary")+1000
        user.save()
    

    #users.refresh_from_db()
    
    for user in users:
        user.refresh_from_db()
        print(user.salary)

from django.db.models import Q
def q_func(request):
    user=UserExtraInfo.objects.filter(Q(age__gt=30) & Q(salary__gt=5000))
    user

import json
def raw(request):
    users=UserExtraInfo.objects.raw("select * from userbaseinfo4")
    for user in users:
        print(type(user),user)
    
    name="张三"
    sql='''
        select * from userextrainfo where username=%s
    '''
    users=UserExtraInfo.objects.raw(sql,[name])
    for user in users:
        print(user.id,user.username)
    
    sql='''select a.*,b.* from userbaseinfo4 a,userextrainfo4 b where a.id=b.user_id
    '''
    users=UserBaseInfo.objects.raw(sql)
    for user in users:
        print(user.age)

from django.db import connection
import django.utils.timezone as timezone
def cursor_insert(request):
    cursor=connection.cursor()
    insertsql="insert into departinfo(departname,createdate) values (%s,%s)"
    data=['总经办1',timezone.now()]
    cursor.execute(insertsql,data)#单条数据插入
    cursor.close()

def cursor_query(request):
    cursor=connection.cursor()
    cursor.execute("SELECT * from userextrainfo")
    row = cursor.fetchone() #获取某条数据
    print(row)
    cursor.close()

def cursor_update(request):
    cursor=connection.cursor()
    try:
        updatesql='update departinfo set departname=%s where id=%s'
        data=['销售部',2]
        cursor.execute(updatesql,data)
        rowcount=cursor.rowcount #影响的行数
        print(rowcount)
        connection.commit()
    except:
        connection.rollback()

def cursor_del(request):
    cursor=connection.cursor()
    sql="delete from departinfo where departname =%s"
    data=['总经办']
    cursor.execute(sql,data)#数据删除
    cursor.close()

from django.db import transaction
@transaction.atomic
def trans(request):
    #开启事务
    save_id=transaction.savepoint()
    try:
        #代码操作1
        #代码操作2
        transaction.savepoint_commit(save_id)
    except:
        transaction.savepoint_rollback(save_id)
    

def trans_with(request):
    with transaction.atomic():
        #开启事务
        save_id=transaction.savepoint()
        try:
            #代码操作1
            #代码操作2
            transaction.savepoint_commit(save_id)
        except:
            transaction.savepoint_rollback(save_id)

#@transaction.atomic
def userinfo_trans(request):
    #开启事务
    #save_id=transaction.savepoint()
    try:
        #基本信息保存
        d=dict(username="测试12",password='123456',status=1,
        createdate=timezone.now())
        userbaseinfo=UserBaseInfo.objects.create(**d)
        raise #抛出异常
        #扩展信息保存
        d=dict(username="测试12",truename='测试1',sex=0,salary=6555.88,age=35,
        status=0,createdate=timezone.now(),memo='',user=userbaseinfo)
        userextrainfo=UserExtraInfo.objects.create(**d)
        #transaction.savepoint_commit(save_id)
        msg="新增数据成功"
        print(msg)
    except:
        #transaction.savepoint_rollback(save_id)
        msg="新增数据失败"
        print(msg)
    return HttpResponse(msg)

def qs_all(request):
    users=UserExtraInfo.objects.all()
    print(users[0].truename)
    return HttpResponse(users)

def qs_filter(request):
    users=UserExtraInfo.objects.filter(sex=1)
    for user in users:
        print(user.truename)
    return HttpResponse(users)

def qs_get(request):
    try:
        user=UserExtraInfo.objects.filter(id=1)
        print(user,type(user))
    except Exception as e:
        print(e.message)
    return HttpResponse(user)



def qs_exclude(request):
    users=UserExtraInfo.objects.exclude(age__lt=30)
    for user in users:
        print(user.truename)
    return HttpResponse(users)

def qs_distinct(request):
    users=UserExtraInfo.objects.distinct().values("department")
    print(users[0])
    return HttpResponse(users)

def qs_values(request):
    users=UserExtraInfo.objects.values()
    for user in users:
        print(type(user))
    users=UserExtraInfo.objects.values('id','username','truename')
    return HttpResponse(users)

def qs_query(request):
    users=UserExtraInfo.objects.all() #查询全部
    users=UserExtraInfo.objects.filter(id=1) #查询id=1的数据
    users=UserExtraInfo.objects.get(id=1) #查询id=1的数据

def qs_update(request):
    one_user=UserExtraInfo.objects.get(id=1)
    one_user.username='王五'
    one_user.save()
    one_user=UserExtraInfo.objects.filter(id=2).update(username='赵六')

    users=UserExtraInfo.objects.update(status=1)
    users2=UserExtraInfo.objects.filter(age__gt=35).update(salary=F('salary')+1000)

from django.db import connection,transaction
def query_sql(request):
    cursor=connection.cursor()
    cursor.execute("SELECT * from userextrainfo")
    row = cursor.fetchall()
    print(row)
    print(cursor.rowcount)
    cursor.close()

def query_insert(request):
    cursor=connection.cursor()
    insertsql="insert into departinfo(departname,createdate) values (%s,%s)"
    data=('总经办',timezone.now())
    cursor.execute(insertsql,data)#单条数据插入
    connection.commit()
    cursor.close()
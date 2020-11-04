from django.db import connection, connections

def sqlFetchone(sql):
    # 返回tuple, (21,)
    cursor = connection.cursor()
    cursor.execute(sql)
    rst = cursor.fetchone()
    cursor.close()
    return rst 

def sqlFetchall(sql):
    # 返回tuple, ((21,),)
    cursor = connection.cursor()
    cursor.execute(sql)
    rst = cursor.fetchall()
    cursor.close()
    return rst 
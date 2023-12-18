import mysql.connector

def getTaskID():
        
    conn = mysql.connector.connect(user='root', password='root', host='localhost', database='helmetruleviolation')
    cursor = conn.cursor()
    sql = '''SELECT task_id from image_info'''
    cursor.execute(sql)
    tasklist=cursor.fetchall()
    taskid=0
   # tasklist=[1,2,3]
    if(len(tasklist)==0):
        print("Task List zero ")
        taskid=1
        
    else:
        big=0
        for i in range(len(tasklist)):
            ele=tasklist[i]
            m=ele[0]
            intele=int(m)
           # print("ele ",intele)
            if(intele>big):
                big=intele
            
        
        
        print("big ",big)
        taskid=big+1
        
            
    
    conn.close()
    return taskid



if __name__ == '__main__':
    taskid=getTaskID()
    print("taskid ",taskid)
    
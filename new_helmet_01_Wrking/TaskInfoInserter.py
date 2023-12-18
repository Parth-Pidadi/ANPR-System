import mysql.connector

def getTeskInfoInserted(task_id,status):
    sid=1
    flag=False
    try:
        connection=mysql.connector.connect(host='localhost',database='helmetruleviolation',user='root',password='root')
        cursor=connection.cursor()
        sql_insert_blob_query = """ INSERT INTO taskinfo
            (sid,taskid,status) VALUES (%s,%s,%s) """
        insert_blob_tuple = (sid, task_id, status)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        flag=True

        print("Task Id Successfully Inserted With Status ID", result)
    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
    return flag

if __name__ == '__main__':
    getTeskInfoInserted()
    
    
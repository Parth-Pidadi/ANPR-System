import mysql.connector

def getInsertImageInfo(username, file, vehicle_number, datetime_str, task_id):
    
    flag=False
    try:
        connection=mysql.connector.connect(host='localhost',database='helmetruleviolation',user='root',password='root')
        cursor=connection.cursor()

#empPicture = convertToBinaryData(path)
    #file = convertToBinaryData(tempimagepath)
        sql_insert_blob_query = """ INSERT INTO image_info
        (user_name, image, vehicle_number, date_time, task_id) VALUES (%s,%s,%s,%s,%s) """
        insert_blob_tuple = (username, file, vehicle_number, datetime_str, task_id)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        flag=True

        print("Image and file inserted successfully as a BLOB into python_employee table", result)
    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
    return flag

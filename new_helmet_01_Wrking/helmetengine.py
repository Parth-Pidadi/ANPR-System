#import numpy as np
import time
import cv2
import os

from datetime import datetime






def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

while True:
    # Find haar cascade to draw bounding box around face
    print("Visited")
    time.sleep(3)
    imagedirname="C:\Helmet Image"
    filelist=[]
    for path in os.listdir(imagedirname):
        imagepath = os.path.join(imagedirname, path) 
        filelist.append(imagepath)
        filename=os.path.basename(imagepath)
        print("File name is: ",filename)
    totalfiles=len(filelist) 
    print("Total files ",len(filelist))
    if(totalfiles>0):
        print("EEEEEE")
        himagepath=filelist[0]
        flag1=himagepath.endswith("jpg")
        flagmp4=himagepath.endswith("mp4")
        print("flag1 ",flag1)
        print("flagmp4 ",flagmp4)
        if(flag1==True):
            print("flag 1: ",flag1)
            print("Image found at path ",himagepath)
          
            # Here we need to pass the image path to a function to get Vehicle number 
            import VehicleNumber
            vehicle_number=VehicleNumber.getVehicleNUmber(himagepath)
           
            if(len(vehicle_number)>0):
                    status="Found"
                    print("Vehicle number is: ",vehicle_number)
                    img = cv2.imread(himagepath)
                    dim = (100, 100)
                    resized=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
                 
                    tempimagepath="temp.jpg"
                    cv2.imwrite(tempimagepath,resized)
                    
                    
                    
                   
                    st=filename.split('_')
                    username=st[0]
                    print("Uaser Nane is: "+username)
                    
                    now=datetime.now() 
                    datetime_str=now.strftime("%d/%m/%Y %H:%M:%S")
                    print("Date time is: ",datetime_str) 
                    import InfoFecher
                    task_id=InfoFecher.getTaskID()
                    file = convertToBinaryData(tempimagepath)
                    import InsertImageInfo
                    flag2=InsertImageInfo.getInsertImageInfo(username, file, vehicle_number, datetime_str, task_id)
                    print("flag is ",flag2)
                    
                    import TaskInfoInserter
                    flag3=TaskInfoInserter.getTeskInfoInserted(task_id,status)
                    print("flag is: ",flag3)
            else:
                status="Not Found"
                task_id=InfoFecher.getTaskID()
                flag3=TaskInfoInserter.getTeskInfoInserted(task_id,status)
                print("flag is: ",flag3)

            os.remove(himagepath)
        if(flagmp4==True):
            print("flagmp4: ",flagmp4)
            print("video found at path ",himagepath)
            import VideoViolationDetection
            import TaskInfoInserter
            statuslist,task_id_video=VideoViolationDetection.detecthelmetviolatorinVideo(himagepath,filename)
            if(len(statuslist)>0):
                status="Found"
                flag3=TaskInfoInserter.getTeskInfoInserted(task_id_video,status)
                print("flag is: ",flag3)
                task_id=InfoFecher.getTaskID()
                flag3=TaskInfoInserter.getTeskInfoInserted(task_id_video,status)
                print("flag is: ",flag3)
                       
            else:
                status="Not Found"
                task_id=InfoFecher.getTaskID()
                flag3=TaskInfoInserter.getTeskInfoInserted(task_id_video,status)
                print("flag is: ",flag3)

            os.remove(himagepath)
        
            
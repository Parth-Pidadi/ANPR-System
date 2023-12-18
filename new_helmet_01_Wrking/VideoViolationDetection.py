import cv2
from ultralytics import YOLO
import random
import cv2
import matplotlib.pyplot as plt
import easyocr
import numpy as np
import cv2
from ultralytics import YOLO
import random
import InfoFecher
import InsertImageInfo
import TaskInfoInserter
from datetime import datetime

def recognize_text_img(image):
    reader = easyocr.Reader(['en'], gpu=False)
    
    plt.figure(figsize=(10,10))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()
    
    
    results = reader.readtext(image)
    bikenumber=""
    for result in results:
        text = result[1]
        bikenumber=text
        print(text)
    return bikenumber


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData
def detecthelmetviolatorinVideo(videopath,filename):
    print("Inside video Detecton")
    statuslist=[]
    st=filename.split('_')
    username=st[0]
    task_id=InfoFecher.getTaskID()
        
    model = YOLO("data/motorcyclist.pt") 
    class_list = ["RIDER"]
    
    
    model2 = YOLO("data/num_plate.pt") 
    class_list2 = ["NUM_PLATE"]
    
    
    model1 = YOLO("data/helmet_12k.pt") 
    class_list1 = ["WITH","WITH-OUT"]
    st=filename.split('_')
    username=st[0]
    print("Uaser Nane is: "+username)
    
   
    task_id=InfoFecher.getTaskID()
    cap = cv2.VideoCapture(videopath)
    
    


    while True:
        ret, frame = cap.read()

        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

       
        detect_params = model.predict(source=[frame], conf=0.1, save=False)

      
        for box in detect_params[0].boxes:
            clsID = box.cls.numpy()[0]
            conf = box.conf.numpy()[0]
            bb = box.xyxy.numpy()[0]
        
            x1 = int(bb[0])
            x2 = int(bb[2])
            y1 = int(bb[1])
            y2 = int(bb[3])
        
            text = class_list[int(clsID)] + " " + str(round(conf, 3)) + "%"
        
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 0), 3)
        
            font = cv2.FONT_HERSHEY_COMPLEX
        
            cv2.putText(frame, text, (x1, y1), font, 1, (255, 255, 255), 2)
            
            motorcycle_region = frame[y1:y2, x1:x2]
            
            if clsID == 0:
                # Run model1 on the detected rider
                detect_params1 = model1.predict(source=[motorcycle_region], conf=0.1, save=False)
                
                for box1 in detect_params1[0].boxes:
                    clsID1 = box1.cls.numpy()[0]
                    conf1 = box1.conf.numpy()[0]
                    bb1 = box1.xyxy.numpy()[0]
                    
                    x1_1 = int(bb1[0])
                    x2_1 = int(bb1[2])
                    y1_1 = int(bb1[1])
                    y2_1 = int(bb1[3])
                    
                    text1 = class_list1[int(clsID1)] + " " + str(round(conf1, 3)) + "%"
                    
                    cv2.rectangle(motorcycle_region, (x1_1, y1_1), (x2_1, y2_1), (0, 255, 0), 2)
                    cv2.putText(motorcycle_region, text1, (x1_1, y1_1), font, 1, (255, 255, 255), 2)
                    
                    
                    
                # Run model2 on the detected rider
                detect_params2 = model2.predict(source=[motorcycle_region], conf=0.1, save=False)
        
                for box2 in detect_params2[0].boxes:
                    clsID2 = box2.cls.numpy()[0]
                    conf2 = box2.conf.numpy()[0]
                    bb2 = box2.xyxy.numpy()[0]
                    
                    x1_2 = int(bb2[0])
                   
                    x2_2 = int(bb2[2])
                    y1_2 = int(bb2[1])
                    y2_2 = int(bb2[3])
                
    #                 text2 = class_list2[int(clsID2)] + " " + str(round(conf2, 3)) + "%"
                    text2="LP"

                    cv2.rectangle(motorcycle_region, (x1_2, y1_2), (x2_2, y2_2), (0, 0, 255), 2)
                    cv2.putText(motorcycle_region, text2, (x1_2, y1_2), font, 1, (255, 255, 255), 2)

                    if conf2>0.4 and clsID1==1:
                        number_plate = motorcycle_region[y1_2:y2_2,x1_2:x2_2]
    #                     recognize_text_raw(number_plate)
                        vehicle_number= recognize_text_img(number_plate)
                        print("Number plate: ",vehicle_number)
                        if(len(vehicle_number)>0):
                                status="Found"
                                print("Vehicle number is: ",vehicle_number)
                               # img = cv2.imread(himagepath)
                                dim = (100, 100)
                                resized=cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)
                             
                                tempimagepath="temp.jpg"
                                cv2.imwrite(tempimagepath,resized)
                                file = convertToBinaryData(tempimagepath)
                                now=datetime.now() 
                                datetime_str=now.strftime("%d/%m/%Y %H:%M:%S")
                                print("Date time is: ",datetime_str) 
                                flag2=InsertImageInfo.getInsertImageInfo(username, file, vehicle_number, datetime_str, task_id)
                                print("flag is ",flag2)
                                statuslist.append(vehicle_number)
                                
                               
                        
        
    #         cv2.imshow('ObjectDetection', motorcycle_region)

        if cv2.waitKey(1) == ord('q'):
            break
        cv2.imshow('frame', frame)
            

            

    # Release the capture and destroy all windows
    cap.release()
    cv2.destroyAllWindows()
    return statuslist,task_id


if __name__ == '__main__':
    detecthelmetviolatorinVideo()
#!/usr/bin/python3
import cv2
import syslog

import boto3 
from matplotlib import pyplot as plt
import numpy as np
from datetime import datetime
from mem import Memory


import rospy
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from std_msgs.msg import Int8, String
import rospkg

syslog.openlog(logoption=syslog.LOG_PID, facility=syslog.LOG_LOCAL7)

DEBUG = 0
saver_iterator = 0


class FaceDetector:
    def __init__(self):
        self.img_sub = rospy.Subscriber("/beo/camera/raw_image", Image, self.callback, queue_size=1, buff_size=2**24)
        self.shutdown_node = rospy.Subscriber("/beo/presentation/handle_shutdowns", String, self.shutdown_callback, queue_size=1)
        self.detector_pub = rospy.Publisher("/beo/camera/face_detector", Int8, queue_size=1)
        self.bridge = CvBridge()
        # aws client
        self.client = boto3.client('rekognition')
        # memory of expressions found
        self.memory = Memory()


    def callback(self, data):
        try:
            # processing image
            cv_image = self.bridge.imgmsg_to_cv2(data, 'bgr8')
            # cv_image = cv2.resize(cv_image, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_CUBIC) # previously used fx = fy = 0.3
            gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

            # saving image
            if gray.any():
                cv2.imwrite('./temp_img/image.jpg', gray)
            
            if (DEBUG == 1):
                print('- Requesting analysis for image ')

            # requesting analysis
            face_emotion, face_emotion_confidence = self.get_emotions('./temp_img/image.jpg', self.client)
            
            if (DEBUG == 1):   
                print(' - RESULTS', end='\n\n')
                print('\tMost probable emotion: ' + face_emotion)
                print('\tConfidence: ' + str(face_emotion_confidence), end='\n\n')
                
            # saving analysis data
            self.memory.save_expression(face_emotion, face_emotion_confidence, str(datetime.now()))
            
            if saver_iterator % 100 == 0:
                self.save_emotions()

        except CvBridgeError as e:
            syslog.syslog(LOG_ERR, e)

    # requests analysis to aws rekognition and parsers it
    def get_emotions(self, photo, client):
        with open(photo, 'rb') as image:
            response = client.detect_faces(Image={'Bytes': image.read()}, Attributes=['ALL'])
            print(' - Requested face detection and analysis')

        if len(response) > 0:
            print(' - A face was detected')

        for item in response.get('FaceDetails'):
            face_emotion_confidence = 0
            face_emotion = None
            for emotion in item.get('Emotions'):
                if emotion.get('Confidence') >= face_emotion_confidence:
                    face_emotion_confidence = emotion['Confidence']
                    face_emotion = emotion.get('Type')
            return face_emotion, face_emotion_confidence
        return None, None

    def shutdown_callback(self, node):
        if node.data == "face_detector":
            rospy.signal_shutdown("Not initiated by user. Shutting down.")

    def save_emotions(self):
        self.memory.save('test_save')

if __name__ == "__main__":
    rospy.init_node("face_detector", disable_signals=True)

    syslog.syslog(syslog.LOG_DEBUG, "Initializing face detector node")
    try:
        detector = FaceDetector()
        rospy.spin()
    except rospy.ROSInterruptException as e:
        syslog.syslog(syslog.LOG_ERR, e)

    cv2.destroyAllWindows()
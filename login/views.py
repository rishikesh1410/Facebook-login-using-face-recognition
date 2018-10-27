from django.http import HttpResponse
from .models import user
from django.shortcuts import render
import face_recognition
import os
import cv2
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import time
from PIL import Image
from pynput.keyboard import Key, Controller

dict={"rishikeshsahu14@gmail.com":"Rishi@14101998"}
def index(Request) :
    all_users = user.objects.all()
    context = {
    'all_users' : all_users,
    }
    return render(Request,"login/index.html",context)

def details(Request, user_id) :
    return HttpResponse("<p>Details for user id : " + str(user_id) + "</p>")

def tofb(var,pass1):

    kb= Controller()


    kb.press(Key.ctrl)
    kb.press(Key.shift_l)
    kb.press('n')
    kb.release(Key.ctrl)
    kb.release(Key.shift_l)
    kb.release('n')

    time.sleep(1.5)
    fb="https://www.facebook.com/login/"

    for char1 in fb:
        kb.press(char1)
        kb.release(char1)
        time.sleep(0.0001)

    time.sleep(0.001)
    kb.press(Key.enter)
    time.sleep(0.5)
    kb.release(Key.enter)
    kb.press(Key.tab)
    kb.release(Key.tab)

    time.sleep(3)
    for char2 in var:
        kb.press(char2)
        kb.release(char2)
        time.sleep(0.0001)
    kb.press(Key.tab)
    kb.release(Key.tab)

    for char3 in pass1:
        kb.press(char3)
        kb.release(char3)
        time.sleep(0.0001)
    kb.press(Key.tab)
    kb.release(Key.tab)
    kb.press(Key.enter)
    kb.release(Key.enter)

def capture(Request):
    video = cv2.VideoCapture(0)
    while True:
        check, frame = video.read()


        #gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
        cv2.imshow("Capturing", frame)

        key = cv2.waitKey(1)
        #time.sleep(4)
        if key == ord('q'):
            cv2.destroyWindow("Capturing")
            break

    #data = np.asarray(frame)
    #frame = np.array(Image.fromarray(np.roll(data, 1, axis=-1)))
    folder="login/known/"
    cv2.imwrite(("login/unknown/current.jpg"),frame)
    try:
        image = face_recognition.load_image_file("login/unknown/current.jpg")
        encoding = face_recognition.face_encodings(image)[0]
        encoding= np.array(encoding)
        encoding=np.reshape(encoding,(128,1))
        encodings=[]
        names=[]
        print(os.getcwd())
        for filename in os.listdir(folder):
            img=cv2.imread(folder+filename)
            try:

                encode=face_recognition.face_encodings(img)[0]
                encode= np.array(encode)
                encode=np.reshape(encode,(128,1))
                encodings.append(encode)
                names.append(filename)
            except IndexError:
                continue
        encodings= np.array(encodings)
        encode=np.reshape(encode,(128,1))
        encodings=np.squeeze(encodings)
        angle=cosine_similarity(encoding.T,encodings)
        pos=np.argmax(angle)
        var = names[pos]
        pass1 = dict[var]
        tofb(var,pass1)
        return HttpResponse("<p>"+str(var)+"</p>")
    except IndexError:
        return HttpResponse("<p></p>")

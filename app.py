from __future__ import division, print_function
from flask import Flask,render_template,Response,request
from werkzeug.utils import secure_filename
import statistics as st

import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
import matplotlib.pyplot as plt
# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import os 
import shutil
import librosa

app=Flask(__name__)

try:
    shutil.rmtree('songs')
except:
    print("unable to delete previous audio data or no song folder is present")

try: 
    os.mkdir("songs")
except: 
    print("directry is already present")

def extract_mfcc(filename):
    y, sr = librosa.load(filename, duration=3, offset=0.5)
    mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40).T, axis=0)
    return mfcc

def gen_frames(): 
    output = []
    count = 0
    camera = cv2.VideoCapture(0)
    model = tf.keras.models.load_model('face_model.h5')
    speech_model = tf.keras.models.load_model("speech_model.h5")

    face_output = []
    speech_ouput = []


    GR_dict={1:(0,255,0),0:(0,0,255)}

    dict = {0:'Fear',1:'Happiness',2:'Sadness',3:'Neutral'}
    dict1 = {0:'Fear',1:'Happiness',2:'Neutral',3:'Sadness'}
    dict2 = {"Fear":0, "Happiness":1, "Sadness":2, "Neutral":3}

    model = tf.keras.models.load_model('E:\project AI COmmunication\model4.h5')

    while True:
        f1 = open("face_result.txt", "a")
        f2 = open("speech_result.txt", "a")
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            faces = face_cascade.detectMultiScale(frame,1.05,5)
            
            for x,y,w,h in faces:
                face_img = frame[y:y+h,x:x+w ]
        #       resized = np.array(face_img,target_size=(128,128))

                resized = cv2.resize(face_img,(48,48))
                resized = np.array(tf.image.rgb_to_grayscale(resized,name = None)/255)
                reshaped=resized.reshape(1, 48, 48, 1)
                result = model.predict(reshaped)
                a = dict[np.argmax(result)]
                # a=model.predict(X_test[i].reshape(1,48,48,1))
                # print("Predicted:",dict[np.argmax(a)]," Actual:",dict[np.argmax(y_test[i])])
                
        #         label = np.argmax(result,axis=1)[0]
                
                cv2.rectangle(frame,(x,y),(x+w,y+h),GR_dict[1],2)
                cv2.rectangle(frame,(x,y-40),(x+w,y),GR_dict[1],-1)
                cv2.putText(frame, a, (x, y-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
                face_output.append(a)
                f1.write(a)
                f1.write("\n")
                

                # Sampling frequency
                freq = 44100

                # Recording duration
                duration = 1

                # Start recorder with the given values 
                # of duration and sample frequency
                recording = sd.rec(int(duration * freq), 
                                samplerate=freq, channels=1)

                # Record audio for the given number of seconds
                sd.wait()


                # Convert the NumPy array to audio file
                filename = "songs/recording"+str(count)+".wav"
                wv.write(filename, recording, freq, sampwidth=2)
                
                feature = extract_mfcc(filename)
                
                feature = np.array([feature])
                feature = feature.reshape(1, 40, 1)
                
                audio_result = speech_model.predict(feature)
                audio_result = np.argmax(audio_result)
                audio_result = dict1[audio_result]
                speech_ouput.append(audio_result)
                f2.write(audio_result)
                f2.write("\n")
                
                count += 1
                
                cv2.putText(frame, audio_result, (50,50),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,0))

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
           

            key = cv2.waitKey(1)
            if key == 27: 
                break
          
                
                
        yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        f1.close()
        f2.close()
    
    camera.release()
    cv2.destroyAllWindows()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/camera')
def camera():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/predict')
def predict():
    return render_template('index1.html')

@app.route('/result')
def result():
    
    file1 = open("face_result.txt", "r")
    array1 = []
    for i in file1.readlines():
        array1.append(i[:-1])

    file2 = open("speech_result.txt", "r")
    array2 = []
    for i in file2.readlines():
        array2.append(i[:-1])

    report1 = max(array1, key = array1.count)
    report2 = max(array2, key = array2.count)

    return render_template('result.html', report1 = report1, report2 = report2)


if __name__=='__main__':
    app.run(debug=True, port=5000)
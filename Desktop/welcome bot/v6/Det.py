import tkinter as tk
from tkinter import font  as tkfont
import cv2

import RPi.GPIO as GPIO
import os,time,math
from gtts import gTTS
from pygame import mixer
import qrcode
#from New import done
import numpy as np
import cv2
from matplotlib import pyplot as plt
class SampleApp(tk.Tk):

   
    #------------------------------------------------------------------------------#
    def voice(string):
        global inde;
        tts = gTTS(text=string, lang='en')
        tts.save("sound"+str(inde)+".mp3")
        mixer.init()
        mixer.music.load("sound"+str(inde)+".mp3")
        mixer.music.play()
        time.sleep(5)
        inde=inde+1;

    #------------------------------------------------------------------------------#
    #------------------------------------------------------------------------------#

    def pla():
    
        mixer.init()
        mixer.music.load("st1.mp3")
        mixer.music.play()
        time.sleep(5)

    #------------------------------------------------------------------------------#
 
    def __init__(self, *args, **kwargs):


       

        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title_font = tkfont.Font(family='systemfixed', size=24, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(1,minsize=84)
        container.grid_columnconfigure(0,minsize=40, weight=1)
        self.frames = {}
        for F in (Camera, Details):
            page_name = F.__name__
            frame = F(parent=container,controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=3, sticky="nsew")

        self.show_frame("Camera")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Camera(tk.Frame):
##    app1=Tk()
    def __init__(self, parent, controller):

        #------------------------------------------------------------------------------#

         def voice(string):
            global inde;
            tts = gTTS(text=string, lang='en')
            tts.save("sound"+str(inde)+".mp3")
            mixer.init()
            mixer.music.load("sound"+str(inde)+".mp3")
            mixer.music.play()
            time.sleep(5)
            inde=inde+1;

         #------------------------------------------------------------------------------#
         #------------------------------------------------------------------------------#

         def pla():

            mixer.init()
            mixer.music.load("st1.mp3")
            mixer.music.play()
            time.sleep(5)

         #------------------------------------------------------------------------------#


         def show_entry_fields():


                if(e3.get() == "principal" or e3.get()=="director"):


                

                 cap = cv2.VideoCapture(0)
                 file1 = open("details.txt","w");
                 file1.write(str("Name: " + e1.get()) + "\n" + "Phone: " +str(e2.get()))
                 file1.close()
                 #x=done()
                     
                 #pla();
                 while(True):
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    ret,frame = cap.read() 
                    id="saran"
                    img=frame
                    cv2.putText(img,'Click Y to for your image',(20,50), font, 1.3,(0,255,0),2,cv2.LINE_AA)
                    cv2.imshow('img1',img) 
                    if (cv2.waitKey(1) & 0xFF == ord('y')): #save on pressing 'y' 
                        cv2.imwrite('new.jpg',frame)
                        cv2.imshow('frame1',frame);
                        f21=open("buf.txt","w")
                        f21.write(e3.get());
                        f21.close();
                        f212=open("comd.txt","w")
                        f212.write("");
                        f212.close();
                        f=open("buf1.txt","w")
                        f.write("Hello")
                        f.close()
                        cv2.destroyAllWindows()
                        app.bind('<Escape>', lambda e: tk.Frame.destroy(app))

                        tk.Frame.destroy(app)

                        break
                else:
                    print("Please enter valid destination and click finish")
                cap.release()
    ##             qr = qrcode.QRCode(
    ##                version = 1,
    ##                error_correction = qrcode.constants.ERROR_CORRECT_H,
    ##                box_size = 10,
    ##                border = 4,
    ##            )
    ##
    ##            # The data that you want to store
    ##             data = ("Name:"+e1.get()+"Phone:"+e2.get()+"Location:"+e3.get())
    ##
    ##            # Add data
    ##             qr.add_data(data)
    ##             qr.make(fit=True)
    ##
    ##            # Create an image from the QR Code instance
    ##             img = qr.make_image()
    ##
    ##            # Save it somewhere, change the extension as needed:
    ##             img.save("qrcode.png")
                 #cap.release()
                    

         tk.Frame.__init__(self, parent)
         self.controller = controller
         label = tk.Label(self, text="Name", font=controller.title_font)
         label.pack(side="top",padx=2, pady=1)
         e1 = tk.Entry(self,font=controller.title_font)
         e1.pack(side="top",ipady=10,pady=10)
         label = tk.Label(self, text="Mobile", font=controller.title_font)
         label.pack(side="top",padx=2, pady=1)
         e2 = tk.Entry(self,font=controller.title_font)
         e2.pack(side="top", ipady=10,pady=10)
         label = tk.Label(self, text="Where do u want to go", font=controller.title_font)
         label.pack(side="top",padx=2, pady=1)

         e3 = tk.Entry(self,font=controller.title_font)
         e3.pack(side="top",ipady=10,pady=10)

        ##        button1 = tk.Button(self, text="RETAKE",
        ##                            command=lambda: controller.show_frame("PageTwo"))
         

         button21 = tk.Button(self, text="Finish",
                                  command=show_entry_fields)
         button21.pack(side="bottom")


class Details(tk.Frame):

    
    def __init__(self, parent, controller):

        
        #------------------------------------------------------------------------------#
       
        def voice(string):
            global inde;
            tts = gTTS(text=string, lang='en')
            tts.save("sound"+str(inde)+".mp3")
            mixer.init()
            mixer.music.load("sound"+str(inde)+".mp3")
            mixer.music.play()
            time.sleep(5)
            inde=inde+1;

        #------------------------------------------------------------------------------#
        #------------------------------------------------------------------------------#

        def pla():
        
            mixer.init()
            mixer.music.load("st.mp3")
            mixer.music.play()
            time.sleep(5)

        #------------------------------------------------------------------------------#

        

        def show_entry_fields():
           print("First Name: %s\n" % (e1.get()))
           if(int(e1.get())>4):
               print("Sorry for the inconvinience we cannot you tables more than 4")
               
           else:
                print("Come I will take you to your table")
                
        pla();
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="for how many members should i locate a table", font=controller.title_font)
        e1 = tk.Entry(self)
        label.pack(side="top", fill="x", pady=10)
        e1.pack(side="top",padx=2, pady=1)
        button = tk.Button(self, text="next",
                           command=show_entry_fields)
        button.pack()


if __name__ == "__main__":
##        cam = cv2.VideoCapture(0)
##        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
##        cv2.waitKey(0) # If you don'tput this line,thenthe image windowis just a flash. If you put any number other than 0, the same happens.
##        cv2.destroyAllWindows()
##        while True:
##            ret, im =cam.read()
##            gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
##
##            faces = face_cascade.detectMultiScale(gray, 1.1 , 4)
        try:
              GPIO.setmode(GPIO.BOARD)

              PIN_TRIGGER = 18
              PIN_ECHO = 24

              GPIO.setup(PIN_TRIGGER, GPIO.OUT)
              GPIO.setup(PIN_ECHO, GPIO.IN)

              GPIO.output(PIN_TRIGGER, GPIO.LOW)

              print("Waiting for sensor to settle")
              count = 0
              time.sleep(2)
              while 1:
                  print("Calculating distance")

                  GPIO.output(PIN_TRIGGER, GPIO.HIGH)

                  time.sleep(0.00001)

                  GPIO.output(PIN_TRIGGER, GPIO.LOW)

                  while GPIO.input(PIN_ECHO)==0:
                        pulse_start_time = time.time()
                  while GPIO.input(PIN_ECHO)==1:
                        pulse_end_time = time.time()

                  pulse_duration = pulse_end_time - pulse_start_time
                  distance = round(pulse_duration * 17150, 2)
                  print("Distance:",distance,"cm")
                  time.sleep(1)
                  if(distance>33 and distance<120):
                        count = count + 1
                        if(count>2):
                              print('person is detected')
                              break;

        finally:
              GPIO.cleanup()

        f=open("comd.txt","w")
        f.write("Hello")
        f.close()
             
                
           
##        cam.release()
##        cv2.destroyAllWindows()

        app = SampleApp()

        app.mainloop()

        


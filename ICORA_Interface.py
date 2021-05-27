
# hello_psg.py
#inséret imports
#insérer blibliotheque de fonctions de capture
import PySimpleGUI as sg
from datetime import datetime
from picamera import PiCamera
from time import sleep

camera = PiCamera()
imagepath = r'/home/pi/Pictures/P1'
filename = r'/home/pi/Pictures/P1'
image_elem = sg.Image(imagepath)
Preview_Time = 0

def cam_import():
    from picamera import PiCamera
    from time import sleep
    camera = PiCamera()
def preview(time):
    
    camera.start_preview()
    sleep(time)
    camera.stop_preview()
def take_picture(name):
    camera.capture('/home/pi/Pictures/%s.png' % name)



col1=[ [sg.Text("Show a preview during 5 seconds")], 
           [sg.Button("Preview_5")],
           [sg.Text("Show a preview during X seconds (Min 1, Max 60)")], 
           [sg.Input()],
           [sg.Button("Preview_X")],
           [sg.Text("Take a Picture")], 
           [sg.Button("Take")]]
col2=[[image_elem],[sg.Text("P1.png")]]
layout = [[sg.Column(col1, element_justification='l' ), sg.Column(col2, element_justification='c')]]
#
# Create the window
window = sg.Window("Demo", layout, size=(900,600), grab_anywhere=True) #1500,850

# Create an event loop
while True:
    event, values = window.read()
    if values[0] != "":
        Preview_Time = int(values[0])
    # End program if user closes window or
    # presses the OK button
    if event == "Preview_5":
        print("Preview 5")
        #Place function Preview here
        preview(5)
    if event == "Preview_X" and Preview_Time > 0 and Preview_Time <= 60: 
        print('Preview ', Preview_Time)
        #Place function PreviewX here
        preview(Preview_Time)
    if event == "Preview_X" and Preview_Time == 999: 
        print('activate fine controls')
        #Place function Preview here
        #To code : (min - Max)
        #brightness (1-100)
        #Contrast(-100 - 100)
        #Sharpness(-100 - 100)
        #Saturation(-100 - 100)
        #ISO(100 - 800)
        #EV Compensation(-10 - 10)
    if event == "Take": 
        print('Picture taken')
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d-%H:%M:%S")
        name = 'Capture_ICORA_'+ str(current_time)
        print(name)
        #Place function Picture here with name
        take_picture(name)
        #Subfunction to display new image      
        imagepath = name
        sleep(2)
        image_elem.update(r'/home/pi/Pictures/'+name+'.png') #remplacer par imagepath
      
        #To code : (min - Max)
        #brightness (1-100)
        #Contrast(-100 - 100)
        #Sharpness(-100 - 100)
        #Saturation(-100 - 100)
        #ISO(100 - 800)
        #EV Compensation(-10 - 10)
    if event == sg.WIN_CLOSED:
        break

window.close()
from djitellopy import Tello
import KeyPress as kp
import cv2
import speech_recognition as sr

r = sr.Recognizer()

kp.init()
me = Tello()
me.connect()
print(me.get_battery())

def VoiceInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 150

    if kp.getKey("a"):
        lr = -speed
    elif kp.getKey("d"):
        lr = speed

    if kp.getKey("UP"):
        ud = speed
    elif kp.getKey("DOWN"):
        ud = -speed

    if kp.getKey("w"):
        fb = speed
    elif kp.getKey("s"):
        fb = -speed

    if kp.getKey("RIGHT"):
        yv = speed
    elif kp.getKey("LEFT"):
        yv = -speed

    if kp.getKey("r"):
        me.land()
    if kp.getKey("q"):
        me.takeoff()
    if kp.getKey("u"):  # New key for wake up
        me.send_rc_control(0, 0, 0, 0)  # Stop all movement
        me.takeoff()  # This will start the propellers without lifting off

    return [lr, fb, ud, yv]

me.takeoff()
me.streamon()

while True:
    vals = VoiceInput()
    
    # Handle the wake up command separately
    if vals == [0, 0, 0, 0]:
        continue  # Skip sending control commands when wake up is triggered
    
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    img = me.get_frame_read().frame
    img = cv2.resize(img, (400, 400))
    cv2.imshow("Image", img)

    # Break the loop if the 'x' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('x'):
        me.land()
        break

cv2.destroyAllWindows()
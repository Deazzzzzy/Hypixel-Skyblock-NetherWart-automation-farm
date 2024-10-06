import mouse
import keyboard
import time
time.sleep(3)
#Автоматизация процесса фарминга на Hypixel Skyblock 

#Необходимы : Мега ферма или просто 5-уровневая пашня таких культур как: нарост, морковь, пшеница, картофель
def left():
    keyboard.press('a')
    mouse.press('left')
    time.sleep(120)
    keyboard.release('a')
    mouse.release('left')
#движение секунд (засечено) в левую сторону до упора и до выпада в последнего этажа фермы то бишь 120 
def right():
    keyboard.press('d')
    mouse.press('left')
    time.sleep(120)
    keyboard.release('d')
    mouse.release('left') 
# движение 120 секунд (засечено) в правую сторону до упора   a
def fly():
    keyboard.press("space")
    time.sleep(0.05)
    keyboard.release("space")
    time.sleep(0.2)
    keyboard.press("space")
    time.sleep(0.05)
    keyboard.release("space")  
#взлёт с идеей последующего возвращения к началу фермы на первом этаже
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
#часть кода, отвечающая за возвращение на первоначальную точку с последующим приземлением и аккуратным доделыванием (корректировкой)
#положения игрока относительно пашни 
while True:
    left()
    right()
    left()
    right()
    left()
    fly()  
    time.sleep(3)
    back() 

    
    
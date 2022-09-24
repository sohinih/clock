import pygame
import datetime
from win10toast import ToastNotifier

pygame.mixer.init()
toaster = ToastNotifier()
hr = int(input("HOUR : "))
mi = int(input("MINUTE : "))
sec = int(input("SECOND : "))
c = input("AM or PM : ")
print("THE TIME SPECIFIED TO SET THE ALARM IS -> ", hr, ':', mi, ':', sec, c)
if c == 'PM':
    hr = hr + 12

print("ALARM SET SUCCESSFULLY\n")
while True:
    if hr == datetime.datetime.now().hour:
        if mi == datetime.datetime.now().minute:
            if sec == datetime.datetime.now().second:
                toaster.show_toast("ALARM CLOCK", "WAKE UP", duration=10, threaded=True) #load a musicfile fr plybck
                pygame.mixer.music.load("C:\\Users\\Sohini\\Desktop\\clock\\alarm_tune.mpeg") #strt plybck of music stream
                pygame.mixer.music.play()
                break
print("HAVE A GOOD DAY")

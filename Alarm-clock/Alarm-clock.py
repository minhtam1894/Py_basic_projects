from tkinter import *
from tkinter import messagebox
import datetime
import time
import winsound


################################

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print('Bây giờ là: ', now,' ', date)
        if now==set_alarm_timer:
            winsound.PlaySound("TF001.wav",winsound.SND_ASYNC)
            print('Dậy đi!!!')
            messagebox.showinfo('Báo Thức', "Dậy đi!!!!!!!")
            
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)


clock=Tk()
clock.title('Đồng Hồ Báo Thức')
clock.iconbitmap(r"bell.ico")
clock.geometry("400x200")
time_format = Label(clock, text = "Giờ (định dạng 24h)", fg="red", bg = "black", font = "Arial").place(x=60, y=120)
addTime = Label(clock, text = "Giờ Phút Giây", font='60').place(x=110)
setYourAlarm = Label(clock, text = "Khi nào dậy", fg="blue", relief="solid", font = ("Times", 7, "bold")).place(x=0, y=29)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime = Entry(clock, textvariable = hour, bg="pink", width=15).place(x=110, y=30)
minTime = Entry(clock, textvariable = min, bg="pink", width=15).place(x=150, y=30)
secTime = Entry(clock, textvariable = sec, bg="pink", width=15).place(x=190, y=30)
submit = Button(clock, text="Cài báo thức", fg = "red", width=10, command=actual_time).place(x=110, y=70)

clock.mainloop()


from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(25 * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    # how to convert 1500 sec to 25:00 minutes is by using math module
    count_minute = math.floor(count / 60)
    # convert seconds for every minute by using modulo %
    count_second = count % 60
    canvas.itemconfig(timer_text, text = f"{count_minute}:{count_second}")
    if count > 0:
        window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx= 100, pady= 50, bg=YELLOW)

title_label = Label(text="Timer",fg=GREEN, font=(FONT_NAME,30,"bold"), bg=YELLOW)
title_label.grid(row=0, column=1)

button = Button(text="Start", command=start_timer)
button.grid(row = 2, column =0)
button2 = Button(text="Reset")
button2.grid(row =2, column=2)



canvas = Canvas(width = 200,height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 100, image=tomato_img)
timer_text = canvas.create_text(100, 125, text="00:00", fill= "white", font=(FONT_NAME, 20, "bold"))
canvas.grid(column=1, row=1)

check_marks = Label(text ="✔", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)




window.mainloop()
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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    title_label.config(text = "Timer")
    check_marks.config(text = "")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    count_down(1 * 60)

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 ==0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", font=FONT_NAME, fg = RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short Break", font=FONT_NAME, fg = PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", font=FONT_NAME, fg = GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    # how to convert 1500 sec to 25:00 minutes is by using math module
    count_minute = math.floor(count / 60)
    # convert seconds for every minute by using modulo %
    count_second = count % 60
    if count_second == 0:
        count_second = "00"
    elif count_second < 10:
        count_second = "0" + str(count_second)
    canvas.itemconfig(timer_text, text = f"{count_minute}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(count / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx= 100, pady= 50, bg=YELLOW)

title_label = Label(text="Timer",fg=GREEN, font=(FONT_NAME,30,"bold"), bg=YELLOW)
title_label.grid(row=0, column=1)
button = Button(text="Start", command=start_timer)
button.grid(row = 2, column =0)
button2 = Button(text="Reset", command=reset_timer)
button2.grid(row =2, column=2)



canvas = Canvas(width = 200,height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 100, image=tomato_img)
timer_text = canvas.create_text(100, 125, text="00:00", fill= "white", font=(FONT_NAME, 20, "bold"))
canvas.grid(column=1, row=1)

check_marks = Label( fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)




window.mainloop()
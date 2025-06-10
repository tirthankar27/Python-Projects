from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK="✔"
count=0
job_id=""

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global job_id
    global count
    if job_id!="":
        window.after_cancel(job_id)
    canvas.itemconfig(timer_id, text=f"00:00")
    pomodoro_counter_label.config(text="")
    timer_label.config(text="Timer",fg=GREEN)
    count=0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def pomodoro():
    global count
    count+=1
    if count%2!=0:
        timer_label.config(text="Work",fg=GREEN)
        countdown(WORK_MIN,0)
    elif count%2==0 and count%8!=0:
        timer_label.config(text="Rest",fg=PINK)
        countdown(SHORT_BREAK_MIN,0)
        current_text=pomodoro_counter_label.cget("text")
        pomodoro_counter_label.config(text=current_text+CHECK_MARK)
    else:
        timer_label.config(text="Rest",fg=RED)
        countdown(LONG_BREAK_MIN,0)
        current_text = pomodoro_counter_label.cget("text")
        pomodoro_counter_label.config(text=current_text + CHECK_MARK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(minute,second):
    global job_id
    if minute<10 and second<10:
        canvas.itemconfig(timer_id, text=f"0{minute}:0{second}")
    elif second<10:
        canvas.itemconfig(timer_id, text=f"{minute}:0{second}")
    elif minute<10:
        canvas.itemconfig(timer_id, text=f"0{minute}:{second}")
    else:
        canvas.itemconfig(timer_id,text=f"{minute}:{second}")
    if minute==0 and second==0:
        canvas.itemconfig(timer_id, text=f"0{minute}:0{second}")
        pomodoro()
        return
    if second>0:
        second-=1
    else:
        minute-=1
        second=59
    job_id=window.after(1000,countdown,minute,second)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.minsize(width=500,height=500)
window.title("Pomodoro")
window.config(padx=130,pady=80,bg=YELLOW)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_id=canvas.create_text(100,130,text="00:00",font=(FONT_NAME,36,"bold"),fill="white")
canvas.grid(row=1,column=1)

timer_label=Label(text="Timer",bg=YELLOW,font=(FONT_NAME,38,'bold'),fg=GREEN)
timer_label.grid(row=0,column=1)

start=Button(text="Start",command=pomodoro,fg=GREEN,bg=YELLOW,borderwidth=0,font=(FONT_NAME,38))
start.grid(row=2,column=0)

pomodoro_counter_label=Label(text="",bg=YELLOW,font=(FONT_NAME,12,'bold'),fg=GREEN)
pomodoro_counter_label.grid(row=3,column=1)

reset=Button(text="Reset",command=reset_timer,fg=RED,bg=YELLOW,borderwidth=0,font=(FONT_NAME,38))
reset.grid(row=2,column=2)

window.mainloop()

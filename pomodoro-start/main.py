from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.2#25
SHORT_BREAK_MIN = 0.1#5
LONG_BREAK_MIN = 0.2#20
reps = 0
check_mark = "✔"
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    checkmark.config(text="")
    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text,text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps +=1

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global timer
    count_minute = int(count / 60)
    if count_minute < 10:
        count_minute = "0" + str(count_minute)
    else:
        count_minute = str(count_minute)
    count_second = count % 60
    if count_second < 10:
        count_second = "0" + str(count_second)
    else:
        count_second = str(count_second)
    canvas.itemconfig(timer_text,text=f"{count_minute}:{count_second}")
    if count >0:
        timer = window.after(1000,count_down,count-1)
    else:
        mark = ""
        start_timer()
        for _ in range(int(reps/2)):
            mark += check_mark
        checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,133, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label = Label(text="Timer",font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
label.grid(column=1, row=0)

start_button = Button(text="Start",highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset",highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark = Label( font=(FONT_NAME, 10, "bold"), fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)




window.mainloop()
from tkinter import *
import pandas as pd
import generate_words

data=pd.read_csv("data/french_words.csv")
to_learn=data.to_dict(orient='records')

#************************ CONSTANTS AND VARIABLES ************************
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME='Ariel'
word_list=list()
word=""
dictionary=dict()
word_generator=generate_words.GenerateWords()
FRONT="French"
BACK="ENGLISH"
job_id=""

#************************ GAME ************************
def right():
    global word
    global dictionary
    global new_img
    global old_img
    word_list.append(word)
    dictionary=word_generator.generate(to_learn,word_list)
    word=dictionary['French']
    window.after_cancel(job_id)
    change(old_img,new_img,FRONT,BACK)

def wrong():
    global word
    global dictionary
    global new_img
    global old_img
    dictionary = word_generator.generate(to_learn,word_list)
    word = dictionary['French']
    window.after_cancel(job_id)
    change(old_img, new_img, FRONT, BACK)

def change(new_image,old_image,new_text,old_text):
    global word
    global dictionary
    global job_id
    canvas.itemconfig(side_id,image=new_image)
    canvas.itemconfig(lang_id,text=new_text)
    if new_text=="French":
        dictionary = word_generator.generate(to_learn,word_list)
        word = dictionary['French']
        canvas.itemconfig(word_id, text=f"{word}")
    else:
        word=dictionary['English']
        canvas.itemconfig(word_id, text=f"{word}")
    job_id=window.after(3000,change,old_image,new_image,old_text,new_text)

#************************ USER INTERFACE ************************
window=Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)

wrong_img=PhotoImage(file="images/wrong.png")
right_img=PhotoImage(file="images/right.png")
front_img=PhotoImage(file="images/card_front.png")
back_img=PhotoImage(file="images/card_back.png")

old_img=front_img
new_img=back_img

canvas=Canvas(height=526,width=800,bg=BACKGROUND_COLOR,highlightthickness=0,borderwidth=0)
side_id=canvas.create_image(402,265,image=front_img)
lang_id=canvas.create_text(400,120,text=FRONT,font=(FONT_NAME,40,'italic'))
word_id=canvas.create_text(400,250,text="word",font=(FONT_NAME,60,'bold'))
canvas.grid(row=0,column=0,columnspan=2)

wrong_btn=Button(image=wrong_img,highlightthickness=0,borderwidth=0,command=wrong)
wrong_btn.grid(row=1,column=0)
right_btn=Button(image=right_img,highlightthickness=0,borderwidth=0,command=right)
right_btn.grid(row=1,column=1)
change(old_img,new_img,FRONT,BACK)
window.mainloop()

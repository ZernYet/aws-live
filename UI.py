#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pillow


# In[ ]:


import tkinter as tk

root = tk.Tk()
root.geometry()

for e, expand in enumerate([False, True]):
    for f, fill in enumerate([None, tk.X, tk.Y, tk.BOTH]):
        for s, side in enumerate([tk.TOP, tk.LEFT, tk.BOTTOM, tk.RIGHT]):
            position = '+{}+{}'.format(s * 205 + 100 + e * 820, f * 235 + 100)
            win = tk.Toplevel(root)
            win.geometry('200x200'+position)
            text = str("side='{}'\nfill='{}'\nexpand={}".format(side, fill, str(expand)))
            tk.Label(win, text=text, bg=['#FF5555', '#55FF55'][e]).pack(side=side, fill=fill, expand=expand)
                
root.mainloop()


# In[ ]:


import tkinter as tk
import HT as ht
import numpy as np
from tkinter import ttk
from tkinter import * 
from tkinter import messagebox
from PIL import ImageTk,Image


# this is a function to get the selected radio button value
def getRadioButtonValue():
	buttonSelected = rbVariable.get()
	return buttonSelected

def getRadioButtonValueQ1():
	buttonSelected = rbVariableQ1.get()
	return buttonSelected

def getRadioButtonValueQ2():
	buttonSelected = rbVariableQ2.get()
	return buttonSelected

def getRadioButtonValueQ3():
	buttonSelected = rbVariableQ3.get()
	return buttonSelected

def getRadioButtonValueQ4():
	buttonSelected = rbVariableQ4.get()
	return buttonSelected

def getRadioButtonValueQ5():
	buttonSelected = rbVariableQ5.get()
	return buttonSelected

def getRadioButtonValueQ6():
	buttonSelected = rbVariableQ6.get()
	return buttonSelected

def getRadioButtonValueQ7():
	buttonSelected = rbVariableQ7.get()
	return buttonSelected

def getRadioButtonValueQ8():
	buttonSelected = rbVariableQ8.get()
	return buttonSelected

def getRadioButtonValueQ9():
	buttonSelected = rbVariableQ9.get()
	return buttonSelected

def getRadioButtonValueQ10():
	buttonSelected = rbVariableQ10.get()
	return buttonSelected

def getRadioButtonValueQ11():
	buttonSelected = rbVariableQ11.get()
	return buttonSelected

def getRadioButtonValueQ12():
	buttonSelected = rbVariableQ12.get()
	return buttonSelected

def getRadioButtonValueQ13():
	buttonSelected = rbVariableQ13.get()
	return buttonSelected

def getRadioButtonValueQ14():
	buttonSelected = rbVariableQ14.get()
	return buttonSelected

def getRadioButtonValueQ15():
	buttonSelected = rbVariableQ15.get()
	return buttonSelected

def getRadioButtonValueQ16():
	buttonSelected = rbVariableQ16.get()
	return buttonSelected

def getRadioButtonValueQ17():
	buttonSelected = rbVariableQ17.get()
	return buttonSelected

def getRadioButtonValueQ18():
	buttonSelected = rbVariableQ18.get()
	return buttonSelected

def predictButton():

	inputList = [[float(getRadioButtonValueQ1()), float(getRadioButtonValueQ2()), float(getRadioButtonValueQ3()), 
                 float(getRadioButtonValueQ4()), float(getRadioButtonValueQ5()), float(getRadioButtonValueQ6()), 
                 float(getRadioButtonValueQ7()), float(getRadioButtonValueQ8()), float(getRadioButtonValueQ9()), 
                 float(getRadioButtonValueQ10()), float(getRadioButtonValueQ11()), float(getRadioButtonValueQ12()), 
                 float(getRadioButtonValueQ13()), float(getRadioButtonValueQ14()), float(getRadioButtonValueQ15()), 
                 float(getRadioButtonValueQ16()), float(getRadioButtonValueQ17()), float(getRadioButtonValueQ18())]]
	algoForPrediction(inputList, getRadioButtonValue())

    
def algoForPrediction(inputList, algo):
	if algo == '1':
		predicted_grade = ht.SVMLoad(inputList)        
		tk.messagebox.showinfo( "Your prediction was made", "U have chosen SVM algorithm \n\n" + predicted_grade)
	elif algo == '2':
		predicted_grade = ht.RFLoad(inputList) 
		tk.messagebox.showinfo( "Your prediction was made", "U have chosen RF algorithm \n\n" + predicted_grade)
	elif algo == '3': #zernyet part
		predicted_grade = ht.DTLoad(inputList) 
		tk.messagebox.showinfo( "Your prediction was made", "U have chosen DT algorithm \n\n" + predicted_grade)
	elif algo == '4': #zernyet part
		predicted_grade = ht.LRLoad(inputList) 
		tk.messagebox.showinfo( "Your prediction was made", "U have chosen LR algorithm \n\n" + predicted_grade)
	else: 
		messagebox.showwarning("Warning", "Please select one algorithm to perform prediction")


root = Tk()

# This is the section of code which creates the main window
root.geometry('900x700')
root.title('Taruc Student Grade Prediction Demo')
root.configure(background = 'red')
#root.iconbitmap()

#this is the declaration of the variable associated with the radio button group
rbVariable = tk.StringVar()
rbVariableQ1 = tk.StringVar()
rbVariableQ2 = tk.StringVar()
rbVariableQ3 = tk.StringVar()
rbVariableQ4 = tk.StringVar()
rbVariableQ5 = tk.StringVar()
rbVariableQ6 = tk.StringVar()
rbVariableQ7 = tk.StringVar()
rbVariableQ8 = tk.StringVar()
rbVariableQ9 = tk.StringVar()
rbVariableQ10 = tk.StringVar()
rbVariableQ11 = tk.StringVar()
rbVariableQ12 = tk.StringVar()
rbVariableQ13 = tk.StringVar()
rbVariableQ14 = tk.StringVar()
rbVariableQ15 = tk.StringVar()
rbVariableQ16 = tk.StringVar()
rbVariableQ17 = tk.StringVar()
rbVariableQ18 = tk.StringVar()

# Create a frame that cover the canvas
main_canvas_frame = Frame(root)
main_canvas_frame.pack(fill = BOTH, expand = 1)

# Create a canvas
my_canvas = Canvas(main_canvas_frame,bg="green")
my_canvas.pack(side = LEFT, fill = BOTH, expand = 1)

# Add a scrollbar to the canvas
my_scrollbar = ttk.Scrollbar(main_canvas_frame, orient =VERTICAL, command = my_canvas.yview)
my_scrollbar.pack(side = RIGHT, fill = Y)

# Configure the canvas
my_canvas.configure(yscrollcommand = my_scrollbar.set)
my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
# Create another frame inside the canvas
main_frame = Frame(my_canvas, bg='#80558C')

# Add that newframe to window in the canvas
my_canvas.create_window((0,0), window = main_frame, anchor = "nw")

frame_top = Frame(main_frame,padx = 20, pady = 50,bg='#AF7AB3')
frame_top.pack(side = TOP, padx = 30, pady = (5,20), fill=BOTH, expand=1)

frame_middle = Frame(main_frame, padx = 20, pady = 50,bg='#AF7AB3')
frame_middle.pack(side = TOP, fill=BOTH, expand=1)

frame_middle2 = Frame(main_frame, padx = 20, pady = 10,bg='#AF7AB3')
frame_middle2.pack(side = TOP, fill=BOTH, expand=1)

frame_bottom = Frame(main_frame, padx = 30, pady = 20, bg='#AF7AB3')
frame_bottom.pack(side = TOP, fill = BOTH, expand = 1)

frame_bottom_last = Frame(main_frame, padx = 50, pady = 50, bg='#AF7AB3')
frame_bottom_last.pack(side = TOP, fill = BOTH, ipadx = 50, ipady = 50, expand = 1)


# This is the section of code which creates the a label
label1 = Label(frame_top, text='Welcome To Taruc Student Grade Prediction Demo Showcase', bg='#8A2BE2', 
               font=('arial', 20, 'normal'), width=15, wraplength=500)
label1.pack(side = TOP, fill = X)

# This is the section of code which creates the a label
label2 = Label(frame_top, text='In this Demo Showcase, I am going to predict your current CGPA base on the questionnaire you have entered below', 
               bg='#8A2BE2', font=('arial', 13, 'normal'), width=20, wraplength=500)
label2.pack(side = TOP, fill = X)

# First, we create a canvas to put the picture on
SVM_picture= Canvas(frame_middle, height=120, width=120)
# Then, we actually create the image file to use (it has to be a *.gif)
#picture_file = ImageTk.PhotoImage(Image.open(""))  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
# Finally, we create the image on the canvas and then place it onto the main window
#SVM_picture.create_image(120, 0, anchor=NE, image=picture_file)
SVM_picture.pack(side = LEFT, padx = 30, fill="none", expand=True)


# First, we create a canvas to put the picture on
RF_picture= Canvas(frame_middle, height=120, width=120)
# Then, we actually create the image file to use (it has to be a *.gif)
#picture_file = ImageTk.PhotoImage(Image.open("1.png"))  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
# Finally, we create the image on the canvas and then place it onto the main window
#RF_picture.create_image(120, 0, anchor=NE, image=picture_file)
RF_picture.pack(side = LEFT, padx = 30, fill="none", expand=True)


# First, we create a canvas to put the picture on
DecisionTree_picture= Canvas(frame_middle, height=120, width=120)
# Then, we actually create the image file to use (it has to be a *.gif)
#picture_file = ImageTk.PhotoImage(Image.open("1.png"))  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
# Finally, we create the image on the canvas and then place it onto the main window
#DecisionTree_picture.create_image(120, 0, anchor=NE, image=picture_file)
DecisionTree_picture.pack(side = LEFT, padx = 30, fill="none", expand=True)


# First, we create a canvas to put the picture on
LogisticRegression_picture= Canvas(frame_middle, height=120, width=120)
# Then, we actually create the image file to use (it has to be a *.gif)
#picture_file = ImageTk.PhotoImage(Image.open("1.png"))  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
# Finally, we create the image on the canvas and then place it onto the main window
#LogisticRegression_picture.create_image(120, 0, anchor=NE, image=picture_file)
LogisticRegression_picture.pack(side = LEFT, padx = 30, fill="none", expand=True)


# This is the section of code which creates a group of radio buttons
frame=Frame(frame_middle2, width=0, height=0, bg='#BA55D3')
frame.pack(side = BOTTOM)
ARBEES=[
('SVM algorithm', '1'), 
('Random Forest algorithm', '2'), 
('Decision Tree algorithm', '3'), 
('Logistic Regression algorithm', '4'), 
]
for text, mode in ARBEES:
	rbGroupOne=Radiobutton(frame, text=text, 
                           variable=rbVariable, 
                           value=mode, bg='#BA55D3', 
                           font=('arial', 12, 'normal')).pack(side='left', anchor = 'w')


# This is the question and radio buttons for Q1
frame_bottom_question1 = Frame(frame_bottom, padx = 30, pady = 20, bg='#80558C', highlightbackground="#CBA0AE", highlightthickness=2)
frame_bottom_question1.pack(side = TOP, fill = BOTH, expand = 1, pady = 20)

question1 = Label(frame_bottom_question1, text='1) Age (in years)', bg='#E4D192', anchor = W, font=('arial', 16, 'normal'))
question1.pack(side = TOP, fill = X)

question_frame1=Frame(frame_bottom_question1, width=0, height=0, bg='#BA55D3')
question_frame1.pack(side = LEFT)
ARBEES=[
('17 - 21', '1'), 
('22 - 25', '2'), 
('above 26', '3'), 
]
for text, mode in ARBEES:
	rbGroupOne=Radiobutton(question_frame1, text=text, 
                           variable=rbVariableQ1, 
                           value=mode, bg='#BA55D3', 
                           font=('arial', 13, 'normal')).pack(side=TOP, anchor = 'w')


# This is the question and radio buttons for Q2
frame_bottom_question2 = Frame(frame_bottom, padx = 30, pady = 20, bg='#80558C', highlightbackground="#CBA0AE", highlightthickness=2)
frame_bottom_question2.pack(side = TOP, fill = BOTH, expand = 1, pady = 20)

question2 = Label(frame_bottom_question2, text='2) Gender', bg='#E4D192', anchor = W, font=('arial', 16, 'normal'))
question2.pack(side = TOP, fill = X)

question_frame2=Frame(frame_bottom_question2, width=0, height=0, bg='#BA55D3')
question_frame2.pack(side = LEFT)
ARBEES=[
('Male', '1'), 
('Female', '2'), 
]
for text, mode in ARBEES:
	rbGroupOne=Radiobutton(question_frame2, text=text, 
                           variable=rbVariableQ2, 
                           value=mode, bg='#BA55D3', 
                           font=('arial', 13, 'normal')).pack(side=TOP, anchor = 'w')    

    
# This is the question and radio buttons for Q3
frame_bottom_question3 = Frame(frame_bottom, padx = 30, pady = 20, bg='#80558C', highlightbackground="#CBA0AE", highlightthickness=2)
frame_bottom_question3.pack(side = TOP, fill = BOTH, expand = 1, pady = 20)

question3 = Label(frame_bottom_question3, text='3) What is your current faculty of study?', bg='#E4D192', anchor = W, font=('arial', 16, 'normal'))
question3.pack(side = TOP, fill = X)

question_frame3=Frame(frame_bottom_question3, width=0, height=0, bg='#BA55D3')
question_frame3.pack(side = LEFT)
ARBEES=[
('Faculty of Accountancy, Finance And Business (FAFB)', '1'), 
('Faculty of Applied Sciences (FOAS)', '2'), 
('Faculty of Built Environment (FOBE)', '3'), 
('Faculty of Communication And Creative Industries (FCCI)', '4'), 
('Faculty of Computing And Information Technology (FOCS)', '5'), 
('Faculty of Engineering And Technology (FOET)', '6'), 
('Faculty of Social Science And Humanities (FSSH)', '7'), 
]
for text, mode in ARBEES:
	rbGroupOne=Radiobutton(question_frame3, text=text, 
                           variable=rbVariableQ3, 
                           value=mode, bg='#BA55D3', 
                           font=('arial', 13, 'normal')).pack(side=TOP, anchor = 'w')   
    
    
# This is the question and radio buttons for Q4
frame_bottom_question4 = Frame(frame_bottom, padx = 30, pady = 20, bg='#80558C', highlightbackground="#CBA0AE", highlightthickness=2)
frame_bottom_question4.pack(side = TOP, fill = BOTH, expand = 1, pady = 20)

question4 = Label(frame_bottom_question4, text='4) Do You currently have any scholarship support for your education in TARUC?', bg='#E4D192', anchor = W, font=('arial', 16, 'normal'))
question4.pack(side = TOP, fill = X)

question_frame4=Frame(frame_bottom_question4, width=0, height=0, bg='#BA55D3')
question_frame4.pack(side = LEFT)
ARBEES=[
('None', '1'), 
('50% and below', '2'), 
('Full Scholarship', '3'), 
]
for text, mode in ARBEES:
	rbGroupOne=Radiobutton(question_frame4, text=text, 
                           variable=rbVariableQ4, 
                           value=mode, bg='#BA55D3', 
                           font=('arial', 13, 'normal')).pack(side=TOP, anchor = 'w')    

    
# This is the question and radio buttons for Q5
frame_bottom_question5 = Frame(frame_bottom, padx = 30, pady = 20, bg='#80558C', highlightbackground="#CBA0AE", highlightthickness=2)
frame_bottom_question5.pack(side = TOP, fill = BOTH, expand = 1, pady = 20)

question5 = Label(frame_bottom_question5, text='5) Do You currently work as part-timer / full-timer while pursuing your study?', bg='#E4D192', anchor = W, font=('arial', 16, 'normal'))
question5.pack(side = TOP, fill = X)

question_frame5=Frame(frame_bottom_question5, width=0, height=0, bg='#BA55D3')
question_frame5.pack(side = LEFT)
ARBEES=[
('Yes', '1'), 
('No', '2'), 
]
for text, mode in ARBEES:
	rbGroupOne=Radiobutton(question_frame5, text=text, 
                           variable=rbVariableQ5, 
                           value=mode, bg='#BA55D3', 
                           font=('arial', 13, 'normal')).pack(side=TOP, anchor = 'w')      

    
# This is the question and radio buttons for Q6
frame_bottom_question6 = Frame(frame_bottom, padx = 30, pady = 20, bg='#80558C', highlightbackground="#CBA0AE", highlightthickness=2)
frame_bottom_question6.pack(side = TOP, fill = BOTH, expand = 1, pady = 20)

question6 = Label(frame_bottom_question6, text='6) Are you currently in a relationship?', bg='#E4D192', anchor = W, font=('arial', 16, 'normal'))
question6.pack(side = TOP, fill = X)

question_frame6=Frame(frame_bottom_question6, width=0, height=0, bg='#BA55D3')
question_frame6.pack(side = LEFT)
ARBEES=[
('Yes', '1'), 
('No', '2'), 
]
for text, mode in ARBEES:
	rbGroupOne=Radiobutton(question_frame6, text=text, 
                           variable=rbVariableQ6, 
                           value=mode, bg='#BA55D3', 
                           font=('arial', 13, 'normal')).pack(side=TOP, anchor = 'w')  
    

# This is the question and radio buttons for Q7
frame_bottom_question7 = Frame(frame_bottom, padx = 30, pady = 20, bg='#80558C', highlightbackground="#CBA0AE", highlightthickness=2)
frame_bottom_question7.pack(side = TOP, fill = BOTH, expand = 1, pady = 20)

question7 = Label(frame_bottom_question7, text='7) Do you have regular artistic/sport activities?', bg='#E4D192', anchor = W, font=('arial', 16, 'normal'))
question7.pack(side = TOP, fill = X)

question_frame7=Frame(frame_bottom_question7, width=0, height=0, bg='#BA55D3')
question_frame7.pack(side = LEFT)
ARBEES=[
('Yes', '1'), 
('No', '2'),  
]
for text, mode in ARBEES:
	rbGroupOne=Radiobutton(question_frame7, text=text, 
                           variable=rbVariableQ7, 
                           value=mode, bg='#BA55D3', 
                           font=('arial', 13, 'normal')).pack(side=TOP, anchor = 'w')  

    
# This is the question and radio buttons for Q8
frame_bottom_question8 = Frame(frame_bottom, padx = 30, pady = 20, bg='#80558C', highlightbackground="#CBA0AE", highlightthickness=2)
frame_bottom_question8.pack(side = TOP, fill = BOTH, expand = 1, pady = 20)

question8 = Label(frame_bottom_question8, text='8) What is your Mothers education?', bg='#E4D192', anchor = W, font=('arial', 16, 'normal'))
question8.pack(side = TOP, fill = X)

question_frame8=Frame(frame_bottom_question8, width=0, height=0, bg='#BA55D3')
question_frame8.pack(side = LEFT)
ARBEES=[
('Primary School', '1'), 
('Secondary School', '2'), 
('College/University', '3'), 
('Master', '4'), 
('Ph.D', '5'), 
]
for text, mode in ARBEES:
	rbGroupOne=Radiobutton(question_frame8, text=text, 
                           variable=rbVariableQ8, 
                           value=mode, bg='#BA55D3', 
                           font=('arial', 13, 'normal')).pack(side=TOP, anchor = 'w')  
    

    
# This is the question and radio buttons for Q9
frame_bottom_question9 = Frame(frame_bottom, padx = 30, pady = 20, bg='#80558C', highlightbackground="#CBA0AE", highlightthickness=2)
frame_bottom_question9.pack(side = TOP, fill = BOTH, expand = 1, pady = 20)

question9 = Label(frame_bottom_question9, text='9) What is your Mothers education?', bg='#E4D192', anchor = W, font=('arial', 16, 'normal'))
question9.pack(side = TOP, fill = X)

question_frame9=Frame(frame_bottom_question9, width=0, height=0, bg='#BA55D3')
question_frame9.pack(side = LEFT)
ARBEES=[
('Primary School', '1'), 
('Secondary School', '2'), 
('College/University', '3'), 
('Master', '4'), 
('Ph.D', '5'), 
]
for text, mode in ARBEES:
	rbGroupOne=Radiobutton(question_frame9, text=text, 
                           variable=rbVariableQ9, 
                           value=mode, bg='#BA55D3', 
                           font=('arial', 13, 'normal')).pack(side=TOP, anchor = 'w')      
    
    
# This is the question and radio buttons for Q10
frame_bottom_question10 = Frame(frame_bottom, padx = 30, pady = 20, bg='#80558C', highlightbackground="#CBA0AE", highlightthickness=2)
frame_bottom_question10.pack(side = TOP, fill = BOTH, expand = 1, pady = 20)

question10 = Label(frame_bottom_question10, text='10) Number of sister/brother in the family', bg='#E4D192', anchor = W, font=('arial', 16, 'normal'))
question10.pack(side = TOP, fill = X)

question_frame10=Frame(frame_bottom_question10, width=0, height=0, bg='#BA55D3')
question_frame10.pack(side = LEFT)
ARBEES=[
('Only child', '1'), 
('1', '2'), 
('2', '3'), 
('3', '4'), 
('4 and above', '5'), 
]
for text, mode in ARBEES:
	rbGroupOne=Radiobutton(question_frame10, text=text, 
                           variable=rbVariableQ10, 
                           value=mode, bg='#BA55D3', 
                           font=('arial', 13, 'normal')).pack(side=TOP, anchor = 'w')      

    
# This is the question and radio buttons for Q11
frame_bottom_question11 = Frame(frame_bottom, padx = 30, pady = 20, bg='#80558C', highlightbackground="#CBA0AE", highlightthickness=2)
frame_bottom_question11.pack(side = TOP, fill = BOTH, expand = 1, pady = 20)

question11 = Label(frame_bottom_question11, text='11) Daily Studying Hours', bg='#E4D192', anchor = W, font=('arial', 16, 'normal'))
question11.pack(side = TOP, fill = X)

question_frame11=Frame(frame_bottom_question11, width=0, height=0, bg='#BA55D3')
question_frame11.pack(side = LEFT)
ARBEES=[
('1 hour and below', '1'), 
('1 - 2 hour', '2'), 
('3 - 4 hour', '3'), 
('4 hour and above', '4'), 
]
for text, mode in ARBEES:
	rbGroupOne=Radiobutton(question_frame11, text=text, 
                           variable=rbVariableQ11, 
                           value=mode, bg='#BA55D3', 
                           font=('arial', 13, 'normal')).pack(side=TOP, anchor = 'w')  
    
  
# This is the question and radio buttons for Q12
frame_bottom_question12 = Frame(frame_bottom, padx = 30, pady = 20, bg='#80558C', highlightbackground="#CBA0AE", highlightthickness=2)
frame_bottom_question12.pack(side = TOP, fill = BOTH, expand = 1, pady = 20)

question12 = Label(frame_bottom_question12, text='12) How long do you spend in additional reading materials(excluding own field of study) per day?', bg='#E4D192', anchor = W, font=('arial', 16, 'normal'))
question12.pack(side = TOP, fill = X)

question_frame12=Frame(frame_bottom_question12, width=0, height=0, bg='#BA55D3')
question_frame12.pack(side = LEFT)
ARBEES=[
('None', '1'), 
('30 minutes and below', '2'), 
('30 minutes to 1 hour', '3'), 
('1 hour and above', '4'), 
]
for text, mode in ARBEES:
	rbGroupOne=Radiobutton(question_frame12, text=text, 
                           variable=rbVariableQ12, 
                           value=mode, bg='#BA55D3', 
                           font=('arial', 13, 'normal')).pack(side=TOP, anchor = 'w')  


# This is the question and radio buttons for Q13
frame_bottom_question13 = Frame(frame_bottom, padx = 30, pady = 20, bg='#80558C', highlightbackground="#CBA0AE", highlightthickness=2)
frame_bottom_question13.pack(side = TOP, fill = BOTH, expand = 1, pady = 20)

question13 = Label(frame_bottom_question13, text='13) Who do you mostly did your preparation to midterm/final assessment?', bg='#E4D192', anchor = W, font=('arial', 16, 'normal'))
question13.pack(side = TOP, fill = X)

question_frame13=Frame(frame_bottom_question13, width=0, height=0, bg='#BA55D3')
question_frame13.pack(side = LEFT)
ARBEES=[
('Alone', '1'), 
('With Friends/Tutor', '2'), 
]
for text, mode in ARBEES:
	rbGroupOne=Radiobutton(question_frame13, text=text, 
                           variable=rbVariableQ13, 
                           value=mode, bg='#BA55D3', 
                           font=('arial', 13, 'normal')).pack(side=TOP, anchor = 'w')  


# This is the question and radio buttons for Q14
frame_bottom_question14 = Frame(frame_bottom, padx = 30, pady = 20, bg='#80558C', highlightbackground="#CBA0AE", highlightthickness=2)
frame_bottom_question14.pack(side = TOP, fill = BOTH, expand = 1, pady = 20)

question14 = Label(frame_bottom_question14, text='14) Do you take past year exam paper as preparation for the midterm/final assessment?', bg='#E4D192', anchor = W, font=('arial', 16, 'normal'))
question14.pack(side = TOP, fill = X)

question_frame14=Frame(frame_bottom_question14, width=0, height=0, bg='#BA55D3')
question_frame14.pack(side = LEFT)
ARBEES=[
('None', '1'), 
('1 to 2', '2'), 
('3 to 4', '3'), 
('5 above', '4'), 
]
for text, mode in ARBEES:
	rbGroupOne=Radiobutton(question_frame14, text=text, 
                           variable=rbVariableQ14, 
                           value=mode, bg='#BA55D3', 
                           font=('arial', 13, 'normal')).pack(side=TOP, anchor = 'w')  

    

# This is the question and radio buttons for Q15
frame_bottom_question15 = Frame(frame_bottom, padx = 30, pady = 20, bg='#80558C', highlightbackground="#CBA0AE", highlightthickness=2)
frame_bottom_question15.pack(side = TOP, fill = BOTH, expand = 1, pady = 20)

question15 = Label(frame_bottom_question15, text='15) When exactly that you did your preparation to midterm', bg='#E4D192', anchor = W, font=('arial', 16, 'normal'))
question15.pack(side = TOP, fill = X)

question_frame15=Frame(frame_bottom_question15, width=0, height=0, bg='#BA55D3')
question_frame15.pack(side = LEFT)
ARBEES=[
('Closest date to the exam', '1'), 
('Regularyly during the semester', '2'), 
('Never', '3'), 
]
for text, mode in ARBEES:
	rbGroupOne=Radiobutton(question_frame15, text=text, 
                           variable=rbVariableQ15, 
                           value=mode, bg='#BA55D3', 
                           font=('arial', 13, 'normal')).pack(side=TOP, anchor = 'w')  
    
    
# This is the question and radio buttons for Q16
frame_bottom_question16 = Frame(frame_bottom, padx = 30, pady = 20, bg='#80558C', highlightbackground="#CBA0AE", highlightthickness=2)
frame_bottom_question16.pack(side = TOP, fill = BOTH, expand = 1, pady = 20)

question16 = Label(frame_bottom_question16, text='16) Paying attention in Lecture Classes', bg='#E4D192', anchor = W, font=('arial', 16, 'normal'))
question16.pack(side = TOP, fill = X)

question_frame16=Frame(frame_bottom_question16, width=0, height=0, bg='#BA55D3')
question_frame16.pack(side = LEFT)
ARBEES=[
('Seldom, but self revision after class', '1'), 
('Sometimes', '2'), 
('Most of the time', '3'), 
]
for text, mode in ARBEES:
	rbGroupOne=Radiobutton(question_frame16, text=text, 
                           variable=rbVariableQ16, 
                           value=mode, bg='#BA55D3', 
                           font=('arial', 13, 'normal')).pack(side=TOP, anchor = 'w')  
    
    
# This is the question and radio buttons for Q17
frame_bottom_question17 = Frame(frame_bottom, padx = 30, pady = 20, bg='#80558C', highlightbackground="#CBA0AE", highlightthickness=2)
frame_bottom_question17.pack(side = TOP, fill = BOTH, expand = 1, pady = 20)

question17 = Label(frame_bottom_question17, text='17) Taking notes in classes', bg='#E4D192', anchor = W, font=('arial', 16, 'normal'))
question17 .pack(side = TOP, fill = X)

question_frame17=Frame(frame_bottom_question17, width=0, height=0, bg='#BA55D3')
question_frame17.pack(side = LEFT)
ARBEES=[
('Rarely', '1'), 
('For Particular Chapter Only', '2'), 
('Most of the Chapter', '3'), 
]
for text, mode in ARBEES:
	rbGroupOne=Radiobutton(question_frame17, text=text, 
                           variable=rbVariableQ17, 
                           value=mode, bg='#BA55D3', 
                           font=('arial', 13, 'normal')).pack(side=TOP, anchor = 'w')  
    
    
# This is the question and radio buttons for Q18
frame_bottom_question18 = Frame(frame_bottom, padx = 30, pady = 20, bg='#80558C', highlightbackground="#CBA0AE", highlightthickness=2)
frame_bottom_question18.pack(side = TOP, fill = BOTH, expand = 1, pady = 20)

question18 = Label(frame_bottom_question18, text='18) What is your grade point average(GPA) in the last semester', bg='#E4D192', anchor = W, font=('arial', 16, 'normal'))
question18.pack(side = TOP, fill = X)

question_frame18=Frame(frame_bottom_question18, width=0, height=0, bg='#BA55D3')
question_frame18.pack(side = LEFT)
ARBEES=[
('< 2.00', '1'), 
('2.00 - 2.75', '2'), 
('2.75 - 3.75', '3'), 
('3.75 and above', '4'), 
]
for text, mode in ARBEES:
	rbGroupOne=Radiobutton(question_frame18, text=text, 
                           variable=rbVariableQ18, 
                           value=mode, bg='#BA55D3', 
                           font=('arial', 13, 'normal')).pack(side=TOP, anchor = 'w')  
    
    
    
B = tk.Button(frame_bottom_last, text ="Make Prediction", bg = '#E4D192', font = "20", command = predictButton, padx = 15, pady = 15)
B.pack(anchor = W)



root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





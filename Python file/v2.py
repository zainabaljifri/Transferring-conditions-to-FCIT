import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from PIL import Image, ImageTk  # PIL is pillow external library

# lists are not needed in this version
# # create a list to store girls section students
# g_list = []
# # create a list to store boys section students
# b_list = []

# grade tuple (0-100)
grade_list = (0,)  # first value
for i in range(1, 101):  # range (start, end) where end is excluded
    grade_list = grade_list + (i,)

# GPA tuple (0.0-5.0)
gpa_list = (0.0,)  # first value
point = 0.01  # incremental value
for i in range(1, 501):  # range (start, end) where end is excluded
    gpa_list = gpa_list + (point,)
    point = round(point + 0.01, 2)  # rounding the gpa values to 2 decimal points


# class student is not needed in this version
# # create a student class, each instance has: name, ID, weighted average attributes
# class Student:
#     def __init__(self, stu_name, stu_id, weighted_avg):
#         self.stu_name = stu_name
#         self.stu_id = stu_id
#         self.weighted_avg = weighted_avg


# CPIT-110 grade checker
def cpit_checker(_):
    stu_grade = int(cpit_grade.get())
    if stu_grade < 80:  # if the grade is below 80
        messagebox.showerror('Condition Is Not Satisfied', 'Sorry! your CPIT 110 grade is below 80 which violates the '
                                                           'condition.\n\nA make-up course should be '
                                                           'taken with score of at least 75.\n\nAvailable make-up '
                                                           'courses:\n(1) CPCS 202\n(2) CPCS 203')
        lbl_imgt1.config(state=tk.DISABLED)  # tick image is set to DISABLED
        lbl_imgx1.config(state=tk.NORMAL)  # cross image is set to NORMAL
    else:  # if the grade is 80 or higher
        lbl_imgt1.config(state=tk.NORMAL)   # tick image is set to NORMAL
        lbl_imgx1.config(state=tk.DISABLED)  # cross image is set to DISABLED


# MATH-110 grade checker
def math_checker(_):
    stu_grade = int(math_grade.get())
    if stu_grade < 85:  # if the grade is below 85
        messagebox.showerror('Condition Is Not Satisfied', 'Sorry! your MATH 110 grade is below 85 which violates the '
                                                           'condition.\n\nA make-up course should be '
                                                           'taken with score of at least 75.\n\nAvailable make-up '
                                                           'courses:\n(1) CPCS 202\n(2) CPCS 203')
        lbl_imgt2.config(state=tk.DISABLED)  # tick image is set to DISABLED
        lbl_imgx2.config(state=tk.NORMAL)  # cross image is set to NORMAL
    else:  # if the grade is 85 or higher
        lbl_imgt2.config(state=tk.NORMAL)  # tick image is set to NORMAL
        lbl_imgx2.config(state=tk.DISABLED)  # cross image is set to DISABLED


# ELI-104 grade checker
def eli_checker(_):
    if eli_grade.get() != 'TR':  # if ELI-104 is not "transferred"
        stu_grade = int(eli_grade.get())
        if stu_grade < 85:  # if the grade is below 85
            messagebox.showerror('Condition Is Not Satisfied', 'Sorry! your ELI 104 grade is below 85 which violates '
                                                               'the condition.\n\nA make-up course should be '
                                                               'taken with score of at least 80.\n\nAvailable make-up '
                                                               'courses:\n(1) CPIT 201\n(2) CPIT 221')
            lbl_imgt3.config(state=tk.DISABLED)  # tick image is set to DISABLED
            lbl_imgx3.config(state=tk.NORMAL)  # cross image is set to NORMAL
        else:  # if the grade is 85 or higher
            lbl_imgt3.config(state=tk.NORMAL)  # tick image is set to NORMAL
            lbl_imgx3.config(state=tk.DISABLED)  # cross image is set to DISABLED
    else:  # if ELI-104 is "transferred"
        lbl_imgt3.config(state=tk.NORMAL)  # tick image is set to NORMAL
        lbl_imgx3.config(state=tk.DISABLED)  # cross image is set to DISABLED


# if CPIT-110 or MATH-110 make-up course
def make_up1():
    if chk_box_mkup1.get() == 1:  # whenever the box checked = make-up course 1 was taken
        # set make-up course 1 related widgets to NORMAL
        lbl_mkup1.config(state=NORMAL)
        mkup1_1.config(state=NORMAL)
        mkup1_2.config(state=NORMAL)
        mkup1_grade.config(state='readonly')  # to avoid unexpected input
        mkup1_grade.config(foreground='black')
        gpa.config(state='readonly')  # gpa is required in case of make-up courses
        gpa.config(foreground='black')
        # set CPIT-110& MATH-110 related widgets to DISABLED
        # since they are in the same path,
        # we are concerned about the last course which is the make-up course 1 in this case
        lbl_cpit.config(state=DISABLED)
        cpit_grade.config(state=DISABLED)
        cpit_grade.config(foreground='SystemButtonFace')
        lbl_math.config(state=DISABLED)
        math_grade.config(state=DISABLED)
        math_grade.config(foreground='SystemButtonFace')

    else:  # whenever unchecked = make-up course 1 was not taken
        # set make-up course 1 related widgets to DISABLED
        lbl_mkup1.config(state=DISABLED)
        mkup1_1.config(state=DISABLED)
        mkup1_2.config(state=DISABLED)
        mkup1_grade.config(state=DISABLED)
        mkup1_grade.config(foreground='SystemButtonFace')
        if chk_box_mkup2.get() == 0:  # gpa is DISABLED ONLY if no make-up course was taken
            gpa.config(state=DISABLED)
            gpa.config(foreground='SystemButtonFace')
        # set CPIT-110& MATH-110 related widgets to NORMAL
        lbl_cpit.config(state=NORMAL)
        cpit_grade.config(state='readonly')  # to avoid unexpected input
        cpit_grade.config(foreground='black')
        lbl_math.config(state=NORMAL)
        math_grade.config(state='readonly')  # to avoid unexpected input
        math_grade.config(foreground='black')


# CPIT-110/MATH-110 make-up course grade checker
def mkup1_checker(_):
    stu_grade = int(mkup1_grade.get())
    if stu_grade < 75:  # if the grade is below 75
        messagebox.showerror('Condition Is Not Satisfied', 'Sorry! your grade in the make-up course is below 75 '
                                                           'which violates the condition.')


# if ELI-104 make-up course
def make_up2():
    if chk_box_mkup2.get() == 1:  # whenever the box checked = make-up course 2 was taken
        # set make-up course 2 related widgets to NORMAL
        lbl_mkup2.config(state=NORMAL)
        mkup2_1.config(state=NORMAL)
        mkup2_2.config(state=NORMAL)
        mkup2_grade.config(state='readonly')  # to avoid unexpected input
        mkup2_grade.config(foreground='black')
        gpa.config(state='readonly')  # gpa is required in case of make-up courses
        gpa.config(foreground='black')
        # set ELI-104 related widgets to DISABLED
        # since they are in the same path,
        # we are concerned about the last course which is the make-up course 2 in this case
        lbl_eli.config(state=DISABLED)
        eli_grade.config(state=DISABLED)
        eli_grade.config(foreground='SystemButtonFace')

    else:  # whenever unchecked = make-up course 2 was not taken
        # set make-up course 2 related widgets to DISABLED
        lbl_mkup2.config(state=DISABLED)
        mkup2_1.config(state=DISABLED)
        mkup2_2.config(state=DISABLED)
        mkup2_grade.config(state=DISABLED)
        mkup2_grade.config(foreground='SystemButtonFace')
        if chk_box_mkup1.get() == 0:  # gpa is DISABLED ONLY if no make-up course was taken
            gpa.config(state=DISABLED)
            gpa.config(foreground='SystemButtonFace')
        # set ELI-104 related widgets to NORMAL
        lbl_eli.config(state=NORMAL)
        eli_grade.config(state='readonly')  # to avoid unexpected input
        eli_grade.config(foreground='black')


# ELI-104 make-up course grade checker
def mkup2_checker(_):
    stu_grade = int(mkup2_grade.get())
    if stu_grade < 80:  # if the grade is below 80
        messagebox.showerror('Condition Is Not Satisfied', 'Sorry! your grade in the make-up course is below 80 '
                                                           'which violates the condition.')


# GPA checker
def gpa_checker(_):
    stu_gpa = float(gpa.get())
    if stu_gpa < 3.75:  # if the GPA is below 3.75
        messagebox.showerror('Condition Is Not Satisfied', 'Sorry! your GPA is below 3.75 which violates the condition.'
                                                           '\nCheck with the faculty educational affairs.')


# check button
def check():
    # note: the entered name & ID are not checked for validity since the college database is unavailable
    # although it is known that the ID is 7 digits long but still the entered ID can be wrong

    # show warning message if there was an empty entry(name/ID) or combobox(grades)
    if ent_name.get() == '' or ent_id.get() == '':  # if student info is incomplete
        messagebox.showwarning('Checking Can Not Be Done', 'Your information is incomplete.')
        canv.yview_moveto('0.0')  # the scrollbar is moved to the top
        ent_name.focus() if ent_name.get() == '' else ent_id.focus()  # focus is set to the empty entry

    elif chk_box_mkup1.get() == 0 and (cpit_grade.get() == '' or math_grade.get() == ''):
        if cpit_grade.get() == '':
            messagebox.showwarning('Checking Can Not Be Done', 'Your CPIT 110 grade is required.')
            canv.yview_moveto('0.2')  # scrollbar is moved to the specified location
            cpit_grade.focus()
        else:
            messagebox.showwarning('Checking Can Not Be Done', 'Your MATH 110 grade is required.')
            canv.yview_moveto('0.2')  # scrollbar is moved to the specified location
            math_grade.focus()

    elif chk_box_mkup2.get() == 0 and eli_grade.get() == '':
        messagebox.showwarning('Checking Can Not Be Done', 'Your ELI 104 grade is required.')
        canv.yview_moveto('0.2')  # scrollbar is moved to the specified location
        eli_grade.focus()

    elif chk_box_mkup1.get() == 1 and mkup1_grade.get() == '':
        chosen_mkup1 = 'CPCS 202' if mkup1.get() == 1 else 'CPCS 203'
        messagebox.showwarning('Checking Can Not Be Done', 'Your ' + chosen_mkup1 + ' grade is required.')
        canv.yview_moveto('1.0')  # scrollbar is moved to the bottom
        mkup1_grade.focus()

    elif chk_box_mkup2.get() == 1 and mkup2_grade.get() == '':
        chosen_mkup2 = 'CPIT 201' if mkup2.get() == 1 else 'CPIT 221'
        messagebox.showwarning('Checking Can Not Be Done', 'Your ' + chosen_mkup2 + ' grade is required.')
        canv.yview_moveto('1.0')  # scrollbar is moved to the bottom
        mkup2_grade.focus()

    elif (chk_box_mkup1.get() == 1 or chk_box_mkup2.get() == 1) and gpa.get() == '':
        messagebox.showwarning('Checking Can Not Be Done', 'Your GPA is required.')
        canv.yview_moveto('1.0')  # scrollbar is moved to the bottom
        gpa.focus()

    # if all required data is entered completely
    else:
        # if (CPIT-110 and MATH-110 grades are accepted) or (make-up course 1 grade and GPA are accepted)
        if (chk_box_mkup1.get() == 0 and int(cpit_grade.get()) >= 80 and int(math_grade.get()) >= 85) \
                or (chk_box_mkup1.get() == 1 and int(mkup1_grade.get()) >= 75 and float(gpa.get()) >= 3.75):

            # if (ELI-110 grade is accepted) or (make-up course 2 grade and GPA are accepted)
            if (chk_box_mkup2.get() == 0 and (eli_grade.get() == 'TR' or int(eli_grade.get()) >= 85)) \
                    or (chk_box_mkup2.get() == 1 and (int(mkup2_grade.get()) >= 80) and float(gpa.get()) >= 3.75):
                # conditions are entirely satisfied
                verified()

            else:  # if conditions are not satisfied
                messagebox.showerror('Not Verified', 'Sorry! transfer could not be done due to violation ' +
                                     'of condition(s).')
                canv.yview_moveto('1.0')

        else:  # if conditions are not satisfied
            messagebox.showerror('Not Verified', 'Sorry! transfer could not be done due to violation ' +
                                 'of condition(s).')
            canv.yview_moveto('1.0')


# calculations
def verified():
    credit = 3  # most credit courses are 3
    # first path grades
    if chk_box_mkup1.get() == 0:  # CPIT-110& MATH-110 grades are considered
        # (credit * grade) for both courses
        path1 = (int(cpit_grade.get()) * credit + int(math_grade.get()) * credit)
        weight = credit + credit  # weight of path 1
    else:  # CPIT-110/ MATH-110 make-up course grade is considered
        path1 = (int(mkup1_grade.get()) * credit)
        weight = credit  # weight of path 1

    # second path grades
    if chk_box_mkup2.get() == 0:  # ELI-104 grade is considered
        if eli_grade.get() == 'TR':
            credit = 0
            path2 = 0
        else:
            credit = 2  # ELI-104 credit is 2
            path2 = (int(eli_grade.get()) * credit)
    else:  # ELI-104 make-up course is considered
        if mkup2.get() == 2:  # if choice is CPIT-221 whose credit is 2
            credit = 2
        path2 = (int(mkup2_grade.get()) * credit)

    weight = weight + credit  # weight of path 2

    # calculate weighted average of the two paths
    w_a = (path1 + path2) / weight

    # lines 279-284 are not needed in this version
    # student = Student(ent_name.get(), ent_id.get(), w_a)  # student object (instance)
    # # append a new student to the list
    # if section.get() == 1:  # girls section students list
    #     g_list.append(student)
    # else:  # boys section students list
    #     b_list.append(student)
    retry = messagebox.askquestion('Verified', 'Good job ' + ent_name.get().split()[0] +
                                   '!\nAll conditions are satisfied and you are eligible to transfer.'
                                   '\nYour weighted average is ' +
                                   str(rounding(w_a, 2)) + '\n\nDo you want to reset data?')
    if retry == 'yes':
        reset_data()


# lines 294-327 are not needed in this version
# display accepted transferring requests
# def display():
#     if section.get() == 1:  # girls section students list
#         stu_list = g_list
#         chosen_sec = 'Girls Section'
#     else:  # boys section students list
#         stu_list = b_list
#         chosen_sec = 'Boys Section'
#
#     if stu_list:  # if list is not empty
#         # sort the student list based on their weighted average and store the data in a new list
#         sorted_list = sorted(stu_list, key=lambda x: x.weighted_avg, reverse=True) #lambda is used for a shortcut fun.
#
#         # create an empty string to store students names& IDs only
#         accepted_list = ''
#         counter = 0
#         max_students = 15  # maximum number of accepted students
#         while counter < len(sorted_list) and counter < max_students:  # loop is repeated to store the top 15 student
#             accepted_list = accepted_list + '\n' + sorted_list[counter].stu_name + ', ' + sorted_list[counter].stu_id
#             counter += 1
#
#         # store the least accepted weighted average
#         least_wa = sorted_list[counter-1].weighted_avg
#
#         # print the accepted students list
#         messagebox.showinfo('Accepted Students in the ' + chosen_sec,
#                             'The names and IDs of the students whose requests for transferring were accepted based on'
#                             ' their weighted average are:\n' + accepted_list +
#                             '\n\n*Note: If your name and ID were not listed, we are sorry to inform'
#                             ' you that your weighted average is less than (' + str(rounding(least_wa, 2)) +
#                             ') the least accepted weighted average')
#
#     else:  # if list is empty
#         messagebox.showinfo('No Requests Accepted in the ' + chosen_sec, 'There are no requests accepted yet.\t')


# reset the widgets data
def reset_data():
    ent_name.focus()
    ent_name.delete(0, END)
    ent_id.delete(0, END)
    section.set(1)
    cpit_grade.set('')
    lbl_imgt1.config(state=tk.DISABLED)
    lbl_imgx1.config(state=tk.DISABLED)
    math_grade.set('')
    lbl_imgt2.config(state=tk.DISABLED)
    lbl_imgx2.config(state=tk.DISABLED)
    eli_grade.set('')
    lbl_imgt3.config(state=tk.DISABLED)
    lbl_imgx3.config(state=tk.DISABLED)
    chk_box_mkup1.set(0)
    mkup1.set(1)
    mkup1_grade.set('')
    chk_box_mkup2.set(0)
    mkup2.set(1)
    mkup2_grade.set('')
    make_up1()
    make_up2()
    gpa.set('')
    canv.yview_moveto('0.0')


# close the window using exit button
def exit_window():
    window.destroy()


# since the built-in round() function does not work properly
# recreated a rounding function
def rounding(num, digits):
    return round(num+10**(-len(str(num))-1), digits)


############################################################################################
# -------------------------------- GUI STARTS HERE --------------------------------------- #
############################################################################################


# create the window (a simple GUI)
window = tk.Tk()
window.geometry('702x620')  # dimensions (size) of the window
window.title('Transferring to FCIT')  # title of the window

# comment out the old logo code
# window.tk.call('wm', 'iconphoto', window.w, PhotoImage(file='logo.png'))  # logo of the window & any other pop message

# new logo code
window.iconphoto(False, PhotoImage(file='logo.png'))  # logo of the window & any other pop message
#######################################################################

# create a scrollbar using Canvas class
canv = tk.Canvas(window, bg='white', highlightthickness=0)  # canvas instance with white background and 0 highlight ring
scrollbar = Scrollbar(window, orient="vertical", command=canv.yview)  # create a scrollbar & set its direction
scrollable_frame = tk.Frame(canv, bg='white') # main frame which contains all frames& widgets (except the buttons frame)
scrollable_frame.bind("<Configure>", lambda e: canv.configure(scrollregion=canv.bbox("all")))  # bind the frame
canv.create_window((0, 0), window=scrollable_frame, anchor="nw")  # set the position
canv.configure(yscrollcommand=scrollbar.set)  # when the canvas y-position changes, the scrollbar moves

#######################################################################

# frame 1 (the one lies on the top) holds the opening sentences
frm1 = tk.Frame(scrollable_frame, relief=RAISED, borderwidth=3, bg='#211F1F')  # bg = background
frm1.pack(fill=tk.BOTH, side=tk.TOP, ipadx=5, ipady=10) # fill the frame in the top of the window with specified padding

# welcoming label placed in frame 1
lbl_wlc = tk.Label(frm1, text='Welcome to Faculty of Computing and Information Technology! ',
                   font=('Arial Rounded MT Bold', 15), bg='#211F1F', fg='white')  # fg = foreground (i.e. text color)
lbl_wlc.pack(ipady=10)

# description label placed in frame 1
lbl_des = tk.Label(frm1,
                   text='The following conditions are required to transfer to FCIT\nKing Abdulaziz University - Jeddah,'
                        ' Saudi Arabia',
                   font=('Arial', 10), bg='#211F1F', fg='white')
lbl_des.pack()

#######################################################################

# frame 2 (the one lies under frame 1) holds the student name& id
frm2 = tk.Frame(scrollable_frame, relief=RIDGE, borderwidth=1, bg='#FFDD6D')
frm2.pack(fill=tk.BOTH, ipadx=5, ipady=5)

# student name label& entry placed in frame 2
lbl_name = tk.Label(frm2, text='Student Name: ', bg='#FFDD6D', font=('Arial Rounded MT Bold', 10), fg='navy')
lbl_name.pack(side=tk.LEFT)
ent_name = tk.Entry(frm2, width=30, highlightthickness=1, highlightbackground='#FFDD6D')
ent_name.pack(side=tk.LEFT)


# student id label& entry placed in frame 2
lbl_id = tk.Label(frm2, text='   Student ID: ', bg='#FFDD6D', font=('Arial Rounded MT Bold', 10),
                  fg='navy')
lbl_id.pack(side=tk.LEFT)
ent_id = tk.Entry(frm2, highlightthickness=1, highlightbackground='#FFDD6D')
ent_id.pack(side=tk.LEFT)

#######################################################################

# frame 3 (the one lies on the bottom) holds the buttons horizontally
frm3 = tk.Frame(window, relief=FLAT, borderwidth=1, padx=2)  # not included in the scrollable_frame
frm3.pack(fill=tk.BOTH, side=tk.BOTTOM, ipady=10)

# check button placed in frame 3
image_check = Image.open('checking.png')  # set an icon to the button
image_check = image_check.resize((25, 25), Image.ANTIALIAS)  # resize the image to fit in the button
photo_check = ImageTk.PhotoImage(image_check)
btn_check = tk.Button(frm3, text='Check Conditions', image=photo_check, compound='left', bg='white',
                      font=('Arial Rounded MT Bold', 10), command=check)
btn_check.pack(side=tk.LEFT, padx=6)  # placed on the left

# reset button placed in frame 3
image_reset = Image.open('reset.png')  # set an icon to the button
image_reset = image_reset.resize((25, 25), Image.ANTIALIAS)  # resize the image to fit in the button
photo_reset = ImageTk.PhotoImage(image_reset)
btn_reset = tk.Button(frm3, text=' Reset', image=photo_reset, compound='left',  bg='white',
                      font=('Arial Rounded MT Bold', 10), command=reset_data)
btn_reset.pack(side=tk.LEFT, padx=6)  # placed on the left

# exit button placed in frame 3
image_exit = Image.open('exit.png')  # set an icon to the button
image_exit = image_exit.resize((25, 25), Image.ANTIALIAS)  # resize the image to fit in the button
photo_exit = ImageTk.PhotoImage(image_exit)
btn_exit = tk.Button(frm3, text='', image=photo_exit, compound='left', bg='white', font=('Arial Rounded MT Bold', 10),
                     command=exit_window)
btn_exit.pack(side=tk.RIGHT, padx=20, ipadx=2)  # placed on the right

#######################################################################

# frame 4 holds the faculty sections info
frm4 = tk.Frame(scrollable_frame, bg='white')
frm4.pack(fill=tk.BOTH)

# label frame holds the sections widgets placed in frame 4
lbl_frm_sec = tk.LabelFrame(frm4, text=' Choose your section ', width=200, height=20, bg='white',
                            font=('Arial Rounded MT Bold', 10), borderwidth=2)
lbl_frm_sec.pack(pady=20, ipady=7)

# set a white background for the bellow radio buttons using Style class
sec_style = Style(lbl_frm_sec)
sec_style.configure('sec.TRadiobutton', background='white')
# choosing the student section (radio button widget placed in the label frame)
section = IntVar()
section.set(1)  # the first section is the default choice
# faculty sections: girls - boys
# girls section
g_sec = Radiobutton(lbl_frm_sec, variable=section, text="Girls section", value=1, style='sec.TRadiobutton')
g_sec.pack(side=tk.LEFT, padx=20)
# boys section
b_sec = Radiobutton(lbl_frm_sec, variable=section, text="Boys section", value=2, style='sec.TRadiobutton')
b_sec.pack(side=tk.RIGHT, padx=20)

#######################################################################

# set an image (group of students)
image1 = Image.open('students1.png')
# resize the image to fit in the window
image1 = image1.resize((680, 290), Image.ANTIALIAS)  # (width, height) = (680, 290)
photo1 = ImageTk.PhotoImage(image1)
# create a label to display the image
tk.Label(scrollable_frame, image=photo1, bg='white').pack(pady=3)

#######################################################################

# label clarifies the purpose of the next widgets
tk.Label(scrollable_frame, text='Required foundation year courses:', bg='white',
         font=('Arial Rounded MT Bold', 13)).pack()

#######################################################################

# frame 5 holds the CPIT-110 info
frm5 = tk.Frame(scrollable_frame, bg='white')
frm5.pack(fill=tk.X)  # the frame fills the scrollable_frame horizontally

# sub-frame 5_1 (to set the widgets in the center besides each other)
frm5_1 = tk.Frame(frm5, bg='#20B2AA')
frm5_1.pack(padx=10, pady=10)

# CPIT-110 condition label placed in the sub-frame 5_1
lbl_cpit = tk.Label(frm5_1, text='1. Your CPIT 110 grade  ', font=('Arial Rounded MT Bold', 10))
lbl_cpit.pack(side=tk.LEFT, ipady=10, ipadx=10)

# choosing CPIT-110 grade (combobox widget placed in sup-frame 5_1)
cpit_grade = Combobox(frm5_1, values=grade_list, width=3, state='readonly')
cpit_grade.bind('<<ComboboxSelected>>', cpit_checker)  # action is taken if grade is below 80
cpit_grade.pack(side=tk.LEFT, padx=10)

# ------------------

# set a small image (tick image tells if the grade is accepted)
image_tick = Image.open('tick.png')
# resize the image
image_tick = image_tick.resize((21, 21), Image.ANTIALIAS)
photot1 = ImageTk.PhotoImage(image_tick)
# create a label to display the image
lbl_imgt1 = tk.Label(frm5_1, image=photot1, bg='white')
lbl_imgt1.config(state=tk.DISABLED)  # DISABLED is the default state (before choosing the grade)
lbl_imgt1.pack(ipadx=5, ipady=8, side=tk.LEFT)

# ------------------

# set a small image (cross image tells if the grade is rejected)
image_x = Image.open('close.png')
# resize the image
image_x = image_x.resize((21, 21), Image.ANTIALIAS)
photox1 = ImageTk.PhotoImage(image_x)
# create a label to display the image
lbl_imgx1 = tk.Label(frm5_1, image=photox1, bg='white')
lbl_imgx1.config(state=tk.DISABLED)   # DISABLED is the default state (before choosing the grade)
lbl_imgx1.pack(ipadx=5, ipady=8, side=tk.LEFT)

#######################################################################

# frame 6 holds the MATH-110 info
frm6 = tk.Frame(scrollable_frame, bg='white')
frm6.pack(fill=tk.X)

# sub-frame 6_1 (to set the widgets in the center besides each other)
frm6_1 = tk.Frame(frm6, bg='#4169E1')
frm6_1.pack(padx=10, pady=10)

# MATH-110 condition label placed in the sub-frame 6_1
lbl_math = tk.Label(frm6_1, text='2. Your MATH 110 grade', font=('Arial Rounded MT Bold', 10))
lbl_math.pack(side=tk.LEFT, ipady=10, ipadx=10)

# choosing MATH-110 grade (combobox widget placed in sup-frame 6_1)
math_grade = Combobox(frm6_1, values=grade_list, width=3, state='readonly')
math_grade.bind('<<ComboboxSelected>>', math_checker)  # action is taken if grade is below 85
math_grade.pack(side=tk.LEFT, padx=10)

# ------------------

# set a small image (tick image tells if the grade is accepted)
photot2 = ImageTk.PhotoImage(image_tick)
# create a label to display the image
lbl_imgt2 = tk.Label(frm6_1, image=photot2, bg='white')
lbl_imgt2.config(state=tk.DISABLED)  # DISABLED is the default state (before choosing the grade)
lbl_imgt2.pack(ipadx=5, ipady=8, side=tk.LEFT)

# ------------------

# set an image (cross image tells if the grade is rejected)
photox2 = ImageTk.PhotoImage(image_x)
# create a label to display the image
lbl_imgx2 = tk.Label(frm6_1, image=photox2, bg='white')
lbl_imgx2.config(state=tk.DISABLED)  # DISABLED is the default state (before choosing the grade)
lbl_imgx2.pack(ipadx=5, ipady=8, side=tk.LEFT)

#######################################################################

# frame 7 holds the ELI-104 info
frm7 = tk.Frame(scrollable_frame, bg='white')
frm7.pack(fill=tk.BOTH)

# sub-frame 7_1 (to set the widgets in the center besides each other)
frm7_1 = tk.Frame(frm7, bg='#FFC800')
frm7_1.pack(padx=10, pady=10)

# ELI-104 condition label placed in the sub-frame 7_1
lbl_eli = tk.Label(frm7_1, text='3. Your ELI 104 grade      ', font=('Arial Rounded MT Bold', 10))
lbl_eli.pack(side=tk.LEFT, ipady=10, ipadx=10)

# adding "TR" into ELI-104 grades
grade_eli = ('TR',) + grade_list

# choosing ELI-104 grade (combobox widget placed in sup-frame 7_1)
eli_grade = Combobox(frm7_1, values=grade_eli, width=3, state='readonly')
eli_grade.bind('<<ComboboxSelected>>', eli_checker)  # action is taken if grade is below 85
eli_grade.pack(side=tk.LEFT, padx=10)

# ------------------

# set a small image (tick image tells if the grade is accepted)
photot3 = ImageTk.PhotoImage(image_tick)
# create a label to display the image
lbl_imgt3 = tk.Label(frm7_1, image=photot3, bg='white')
lbl_imgt3.config(state=tk.DISABLED)  # DISABLED is the default state (before choosing the grade)
lbl_imgt3.pack(ipadx=5, ipady=8, side=tk.LEFT)

# ------------------

# set a small image (cross image tells if the grade is rejected)
photox3 = ImageTk.PhotoImage(image_x)
# create a label contains the image
lbl_imgx3 = tk.Label(frm7_1, image=photox3, bg='white')
lbl_imgx3.config(state=tk.DISABLED)  # DISABLED is the default state (before choosing the grade)
lbl_imgx3.pack(ipadx=5, ipady=8, side=tk.LEFT)

#######################################################################

# set an image (2 students)
image2 = Image.open('students2.png')
# resize the image
image2 = image2.resize((300, 200), Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(image2)
# create a label to display the image
tk.Label(scrollable_frame, image=photo2, bg='white').pack(pady=10)

#######################################################################

# label
tk.Label(scrollable_frame, text='\nDidn\'t score well in any of the above courses?', bg='white',
         font=('Arial Rounded MT Bold', 14)).pack()

#######################################################################

# set an image (paper airplane)
photo3 = ImageTk.PhotoImage(Image.open('paper_airplane.png').resize((200, 100), Image.ANTIALIAS))
tk.Label(scrollable_frame, image=photo3, bg='white').pack(pady=6)

#######################################################################

# clarifying label
tk.Label(scrollable_frame, text='Don\'t worry! The following courses are offered if a course grade did not '
                                'satisfy the condition.', bg='white', font=('Arial Rounded MT Bold', 10)).pack()

#######################################################################

# frame 8 holds the make-up courses info (for both paths)
frm8 = tk.Frame(scrollable_frame)
frm8.pack(fill=tk.BOTH)

# sub-frame 8_1 holds make-up course 1 info
# (if CPIT-110,MATH-110 or both conditions are not satisfied)
frm8_1 = tk.Frame(frm8, bg='#ADD8E6')
frm8_1.pack(fill=tk.BOTH, side=tk.LEFT, ipadx=26)

# make-up course 1 checkbox placed in the sub-frame 8_1
chk_box_mkup1 = IntVar()
chk_stmt1 = tk.Checkbutton(frm8_1, text='CPIT 110 or MATH 110 make-up course was taken', var=chk_box_mkup1,
                           bg='#ADD8E6', activebackground='#ADD8E6', command=make_up1)
chk_stmt1.pack()

# choosing CPIT-110/MATH-110 make-up course
# available make-up courses: CPCS-202 or CPCS-203
# note: the program is only interested in the last make-up course if both were taken

# make-up course 1 name label placed in the sub-frame 8_1
lbl_mkup1 = tk.Label(frm8_1, text='Choose the make-up course\n(or the last one if both were taken) and its grade:',
                     bg='#ADD8E6')
lbl_mkup1.config(state=tk.DISABLED)
lbl_mkup1.pack()

# set a colored background for the bellow radio buttons using Style class
mkup1_style = Style(frm8_1)
mkup1_style.configure('mkup1.TRadiobutton', background='#ADD8E6')
# choosing make-up course 1 (radio button widget placed in the sub-frame 8_1)
mkup1 = IntVar()
mkup1.set(1)  # the first course is the default choice
# CPCS-202
mkup1_1 = Radiobutton(frm8_1, variable=mkup1, text="CPCS 202", value=1, style='mkup1.TRadiobutton')
mkup1_1.config(state=DISABLED)  # DISABLED is the default state
mkup1_1.pack()
# CPCS-203
mkup1_2 = Radiobutton(frm8_1, variable=mkup1, text="CPCS 203", value=2, style='mkup1.TRadiobutton')
mkup1_2.config(state=DISABLED)  # DISABLED is the default state
mkup1_2.pack()

# label frame holds the grade widget placed in the sub-frame 8_1
lbl_mkup1_grade = tk.LabelFrame(frm8_1, text=' Grade ', bg='#ADD8E6')
lbl_mkup1_grade.pack(ipadx=10, padx=5, pady=5)

# choosing make-up course 1 grade (combobox widget placed in the label frame)
mkup1_grade = Combobox(lbl_mkup1_grade, values=grade_list, width=3, state='readonly')
mkup1_grade.bind('<<ComboboxSelected>>', mkup1_checker)  # action is taken if grade is below 75
mkup1_grade.pack(pady=5)
mkup1_grade.config(state=DISABLED)  # DISABLED is the default state

# ------------------

# sub-frame 8_2 holds make-up course 2 info
# (if ELI-104 condition is not satisfied)
frm8_2 = tk.Frame(frm8)
frm8_2.pack(fill=tk.BOTH, side=tk.LEFT, ipadx=26)

# make-up course 2 checkbox placed in the sub-frame 8_2
chk_box_mkup2 = IntVar()
chk_stmt2 = tk.Checkbutton(frm8_2, text='ELI 104 make-up course was taken', var=chk_box_mkup2, command=make_up2)
chk_stmt2.pack()

# choosing ELI-104 make-up course
# available make-up courses: CPIT-201 or CPIT-221
# note: the program is only interested in the last make-up course if both were taken

# make-up course 2 name label placed in the sub-frame 8_2
lbl_mkup2 = tk.Label(frm8_2, text='Choose the make-up course\n(or the last one if both were taken) and its grade:')
lbl_mkup2.config(state=tk.DISABLED)
lbl_mkup2.pack()

# choosing make-up course 2 (radio button widget placed in the sub-frame 8_1)
mkup2 = IntVar()
mkup2.set(1)  # the first course is the default choice
# CPIT 201
mkup2_1 = Radiobutton(frm8_2, variable=mkup2, text="CPIT 201", value=1)
mkup2_1.config(state=DISABLED)  # DISABLED is the default state
mkup2_1.pack()
# CPIT 221
mkup2_2 = Radiobutton(frm8_2, variable=mkup2, text="CPIT 221", value=2)
mkup2_2.config(state=DISABLED)  # DISABLED is the default state
mkup2_2.pack()


# label frame holds the grade widget placed in the sub-frame 8_2
lbl_mkup2_grade = tk.LabelFrame(frm8_2, text=' Grade ')
lbl_mkup2_grade.pack(ipadx=10, padx=5, pady=5)

# choosing make-up course 2 grade (combobox widget placed in the label frame)
mkup2_grade = Combobox(lbl_mkup2_grade, values=grade_list, width=3, state='readonly')
mkup2_grade.bind('<<ComboboxSelected>>', mkup2_checker)  # action is taken if grade is below 80
mkup2_grade.pack(pady=5)
mkup2_grade.config(state=DISABLED)  # DISABLED is the default state


#####################################

# set in image (half circle which indicates that both paths lead to the GPA)
photo4 = ImageTk.PhotoImage(Image.open('half_circle.png'))
tk.Label(scrollable_frame, image=photo4, bg='white').pack()

#####################################

# frame 9 holds the GPA info
frm9 = tk.Frame(scrollable_frame, bg='white')
frm9.pack()

# clarifying statement
tk.Label(frm9, text='Your GPA is only required\nif any make-up course was taken!', bg='white',
         font=('Arial Rounded MT Bold', 13)).pack(side=tk.TOP, fill=tk.X, padx=30)

# lable frame holds the GPA widget placed in frame 9
lbl_gpa = tk.LabelFrame(frm9, text=' GPA ', bg='white')
lbl_gpa.pack(ipadx=10, padx=5, pady=5)

# choosing GPA (combobox widget placed in the label frame)
gpa = Combobox(lbl_gpa, values=gpa_list, width=4, state='readonly')
gpa.bind('<<ComboboxSelected>>', gpa_checker)  # action is taken if the GPA is below 3.75
gpa.pack(pady=5)
gpa.config(state=DISABLED)  # DISABLED is the default state

canv.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
window.mainloop()

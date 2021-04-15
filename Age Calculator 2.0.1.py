from tkinter import *
from tkinter.ttk import *
from tkcalendar import DateEntry
from tkinter import ttk
from datetime import date, timedelta

# creating root of the window
root = Tk()

# name of the app
root.title("Age Calculator")
root.geometry("300x500")
root.config(background='#FEFFFA')

# creating the first frame of the app
cal_area = LabelFrame(root, text="Welcome")
cal_area.pack(fill='x', expand=False, padx=6, pady=10)

# for changing the color of the cal_area
s = ttk.Style()
s.configure('Red.TLabelframe.label', background='#42D1A7')
# cal_area.config(background='#447EFF')

# the date selector for selecting the dates
Label(cal_area, text='Birth Date:', font=('Comic Sans MS', 14)).grid(column=0, row=0, padx=(5, 10), sticky='w',
                                                                     columnspan=2)
b_date = DateEntry(cal_area, locale='en_IN', date_pattern='dd/mm/y')  # b_date = birth_date
b_date.grid(column=3, row=0, sticky='news', padx=(50, 5), pady=10)

# current birthdate, it is changeable as well
Label(cal_area, text='Today:', font=('Comic Sans MS', 14)).grid(column=0, row=1, padx=(5, 10), sticky='w', columnspan=2)
c_date = DateEntry(cal_area, locale='en_IN', date_pattern='dd/mm/y')
c_date.grid(column=3, row=1, sticky='news', padx=(50, 5), pady=10)


# this method is called when button is clicked
def age():
	# all the calculation part goes here
	current = c_date.get_date()
	user = b_date.get_date()
	total_days = (current - user).days
	years = int(total_days / 365.25)
	months = int((total_days % 365.25) / 30.41)
	days = current.day - user.day
	total_weeks = int(total_days / 7)
	b_day_month, b_day_daydiff, b_day_name = birth_day()

	# display updated information on canvas
	c1.itemconfig(box_age, text=years)
	c1.itemconfig(box_b_day, text=f"{months} months | {days} days")
	c1.itemconfig(box_day, text=b_day_name)
	c1.itemconfig(box_b_day_time, text=f"{b_day_month} months | {b_day_daydiff} days")
	c1.itemconfig(box_month, text=f"{int(total_days / 30.41)}")
	c1.itemconfig(box_age_day, text=total_days)
	c1.itemconfig(box_weeks, text=total_weeks)


def birth_day():
	b_dates = b_date.get_date()
	b_day = date(int(c_date.get_date().year), int(b_dates.month), int(b_dates.day))
	if b_day <= c_date.get_date():
		b_day += timedelta(days=365.25)
	no_of_days = (b_day - c_date.get_date()).days
	months = int((no_of_days % 365.25) / 30.41)
	day_diff = c_date.get_date().day - b_day.day
	day_name = b_day.strftime('%A')
	return months, day_diff, day_name


b = Button(root, text='GET', command=age)
b.pack()
# frame containing the button
frame3 = Frame(root)
frame3.pack(fill='x', expand=False, padx=5, pady=5)

# drawing canvas
c1 = Canvas(frame3, height=280, width=288)
c1.pack(fill='x', expand=False)
# c1.grid(column=0, row=1, columnspan=4, sticky=(N, W, E, S), padx=10)

# base rectange
c1.create_rectangle(2, 2, 288, 260, fill='#4C515D', outline='#18191D', width=2)

# vertical divider line
c1.create_line(144, 0, 144, 150, fill="#18191D", width=2, smooth=1)

# horizontal divider line
c1.create_line(1, 150, 288, 150, fill="#18191D", width=2, smooth=1)

# 1st box Age text
c1.create_text(72, 10, text='Age', font=('Comic Sans MS', 15),
               anchor='n',
               fill='#FF6D00')

# 1st box age in numbers
box_age = c1.create_text(42, 45, text='00', font=('Comic Sans MS', 32, 'bold'),
                         anchor='n',
                         fill='White')

# 1st box bottom year text
c1.create_text(109, 65, text='years', font=('Comic Sans MS', 14, 'bold'),
               anchor='n',
               fill='white')

# 1st box bottom text
box_b_day = c1.create_text(72, 128, text='12 months | 12 days',
                           font=('Comic Sans MS', 10),
                           anchor='n',
                           fill='#BFBFC1')

# 2nd box heading
c1.create_text(180, 10, text='Next Birthday',
               font=('Comic Sans MS', 10, 'bold'),
               anchor='nw',
               fill='#FF6D00')

# 2nd box supposed to be and image here
c1.create_text(215, 30, text='🎂', font=('Helvetica', 36), anchor='n', fill='white')

# 2nd box day
box_day = c1.create_text(215, 90, text='----', font=('Helvetica', 12, 'bold'),
                         anchor='n',
                         fill='white')

# 2nd box bottom text
box_b_day_time = c1.create_text(215, 128, text='12 months | 12 days',
                                font=('Comic Sans MS', 10),
                                anchor='n',
                                fill='#BFBFC1')

# this_image = PhotoImage(file='cake.png')
# c1.create_image(215, 50, image=this_image)

# 3rd box summary
c1.create_text(144, 155, text='Summary', font=('Comic Sans MS', 12),
               anchor='n',
               fill='#FF6D00')

# 3rd box first category
c1.create_text(45, 185, text='Months', font=('Comic Sans MS', 11),
               anchor='n',
               fill='#BFBFC1')

# 3rd box first category number
box_month = c1.create_text(40, 210, text='12', font=('Comic Sans MS', 14),
                           anchor='n',
                           fill='white')

# 3rd box second category
c1.create_text(144, 185, text='Days', font=('Comic Sans MS', 11),
               anchor='n',
               fill='#BFBFC1')

# 3rd box second category numbers
box_age_day = c1.create_text(144, 210, text='27', font=('Comic Sans MS', 14),
                             anchor='n',
                             fill='white')

# 3rd box third category
c1.create_text(245, 185, text='Weeks', font=('Comic Sans MS', 11),
               anchor='n',
               fill='#BFBFC1')

# 3rd box third category number
box_weeks = c1.create_text(245, 210, text='5000', font=('Comic Sans MS', 14),
                           anchor='n',
                           fill='white')

# credit
c1.create_text(144, 260, text='Created by - Prianshu Rai', font=('Comic Sans MS', 8),
               anchor='n',
               fill='#BFBFC1')
# running the app
root.mainloop()

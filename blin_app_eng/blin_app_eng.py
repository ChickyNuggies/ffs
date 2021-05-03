from tkinter import *

root = Tk()
root.title("blin calculator 2.0")
root.config(background = '#444444')
root.iconbitmap('blin.ico')



#entry
e = Entry(root, width = 10, borderwidth = 2, bg = '#444444', foreground = 'white')

#variables
ingredients = []

#label
global label
label = Label(root, padx = 10, pady = 15, bg = '#444444', foreground = 'white', text = "How much milk do you have: ")

#functions
def enter_eggs():
	label.configure(text = "How many eggs do you have: ")


def enter_flour():
	label.configure(text = "How much flour do you have: ")


def enter_portions():
	label.configure(text = "Number of portions: ")


def button_click(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0,str(current) + str(number))

def main(num_ing):
	milk = num_ing[0]
	eggs = num_ing[1]
	flour = num_ing[2]
	portions = int(num_ing[3])

	global milk_needed
	global eggs_needed
	global flour_needed

	if portions == 1:
		milk_needed = 100
		eggs_needed = 0.5
		flour_needed = 50

	elif portions == 2:

		milk_needed = 200
		eggs_needed = 1
		flour_needed = 100

	elif portions == 3:

		milk_needed = 300
		eggs_needed = 1.5
		flour_needed = 150

	elif portions == 4:

		milk_needed = 400
		eggs_needed = 2
		flour_needed = 200

	elif portions == 5:

		milk_needed = 500
		eggs_needed = 2.5
		flour_needed = 250

	elif portions == 6:

		milk_needed = 600
		eggs_needed = 3
		flour_needed = 300

	elif portions == 7:

		milk_needed = 700
		eggs_needed = 3.5
		flour_needed = 350

	elif portions == 8:

		milk_needed = 800
		eggs_needed = 4
		flour_needed = 400

	elif portions == 9:

		milk_needed = 900
		eggs_needed = 4.5
		flour_needed = 450

	elif portions == 10:

		milk_needed = 1000
		eggs_needed = 5
		flour_needed = 500

	label.config(text = portions)

	def main_calculations():
		global more_milk
		global more_eggs
		global more_flour

		more_milk = int(milk_needed) - int(milk)
		more_eggs = int(eggs_needed) - int(eggs)
		more_flour = int(flour_needed) - int(flour)
		label.config(text = f"You still need {more_milk} ml of milk, {more_eggs} eggs and {more_flour} g of flour.")

	main_calculations()

def enter(num_ing):
	if len(num_ing) == 0:
		global milk

		milk = e.get()
		ingredients.append(milk)
		e.delete(0, END)
		enter_eggs()

	elif len(num_ing) == 1:
		global eggs

		eggs = e.get()
		ingredients.append(eggs)
		e.delete(0, END)
		enter_flour()

	elif len(num_ing) == 2:
		global flour

		flour = e.get()
		ingredients.append(flour)
		e.delete(0, END)
		enter_portions()

	elif len(num_ing) == 3:
		global portions

		portions = e.get()
		ingredients.append(portions)
		e.delete(0, END)
		main(ingredients)

def clear():
	e.delete(0, END)


#if statements


#buttons
button1 = Button(root, text = "1" ,padx = 40, pady = 45, bg = '#333333', foreground = 'white', command = lambda: button_click(1))
button2 = Button(root, text = "2" ,padx = 40, pady = 45, bg = '#333333', foreground = 'white', command = lambda: button_click(2))
button3 = Button(root, text = "3" ,padx = 40, pady = 45, bg = '#333333', foreground = 'white', command = lambda: button_click(3))

button4 = Button(root, text = "4" ,padx = 40, pady = 45, bg = '#333333', foreground = 'white', command = lambda: button_click(4))
button5 = Button(root, text = "5" ,padx = 40, pady = 45, bg = '#333333', foreground = 'white', command = lambda: button_click(5))
button6 = Button(root, text = "6" ,padx = 40, pady = 45, bg = '#333333', foreground = 'white', command = lambda: button_click(6))

button7 = Button(root, text = "7" ,padx = 40, pady = 45, bg = '#333333', foreground = 'white', command = lambda: button_click(7))
button8 = Button(root, text = "8" ,padx = 40, pady = 45, bg = '#333333', foreground = 'white', command = lambda: button_click(8))
button9 = Button(root, text = "9" ,padx = 40, pady = 45, bg = '#333333', foreground = 'white', command = lambda: button_click(9))

button0 = Button(root, text = "0" ,padx = 40, pady = 45, bg = '#333333', foreground = 'white', command = lambda: button_click(0))

button_enter = Button(root, text = "ENTER", padx = 40, pady = 20 ,bg = '#333333', foreground = 'white', command = lambda: enter(ingredients))

button_clear = Button(root, text = "CLEAR", padx = 40, pady = 20, bg = '#333333', foreground = 'white', command = clear)




#placemant
button1.grid(row = 1 ,column = 0)
button2.grid(row = 1 ,column = 1)
button3.grid(row = 1 ,column = 2)

button4.grid(row = 2,column = 0)
button5.grid(row = 2,column = 1)
button6.grid(row = 2,column = 2)

button7.grid(row = 3,column = 0)
button8.grid(row = 3,column = 1)
button9.grid(row = 3,column = 2)

button0.grid(row = 4,column = 1)

button_enter.grid(row = 4, column = 2)
button_clear.grid(row = 4, column=0)

label.grid(row=0, column=0, columnspan=2)
e.grid(row=0, column=1, columnspan=3, padx = 2, pady = 5)

#ending loop
root.mainloop()
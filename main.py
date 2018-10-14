
from ezprint import *
from tkinter import *
import os
#00FFFF голубой
#FFFF00 желтый

root = None


def go_up(event):
	try:
		os.chdir(os.path.normpath(os.getcwd() + os.sep + os.pardir))
	except:
		pass
	print_directory()

def print_directory():
	dir = os.getcwd()
	root.title(dir)


def print_dots():
	label = Label(root, text = '...', bg='#000080', fg='#FFFF00')
	label.config(font = ('Arial', 10 , 'bold'))
	label.place(x=40, y=30)
	label.bind("<Button-1>", go_up)


def start_gui():
	global root

	root = Tk()

	root.title('File Manager')

	root.resizable(0, 0)
	root.geometry('600x600')

	root.config(bg = '#000080')
	root.config()
	#(a+b)*2
	y = 0
	for x in range(1, 285, 15):
		label = Label(root, text = '▦', bg='#000080', fg='#FFFF00')
		label.config(font = ('Arial', 25 , 'bold'))
		label.place(x=(x+y)*2, y=0)
	for x in range(1, 285, 15):
		label = Label(root, text = '▦', bg='#000080', fg='#FFFF00')
		label.config(font = ('Arial', 25 , 'bold'))
		label.place(x=(x+y)*2, y=550)
	x = 0
	for y in range(1, 285, 15):
		label = Label(root, text = '▦', bg='#000080', fg='#FFFF00')
		label.config(font = ('Arial', 25 , 'bold'))
		label.place(x=x, y=(x+y)*2)
	for y in range(1, 285, 15):
		label = Label(root, text = '▦', bg='#000080', fg='#FFFF00')
		label.config(font = ('Arial', 25 , 'bold'))
		label.place(x=575, y=(x+y)*2)

	print_directory()
	print_dots()
	root.mainloop()


def main():
	os.system('color 1e')
	start_gui()
	# commands()


def commands():
	command = input('>>>')
	if command == 'start':
		start_gui()

if __name__ == '__main__':
	main()

from ezprint import *
from tkinter import *
import os
#00FFFF голубой
#FFFF00 желтый



def start_gui():
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
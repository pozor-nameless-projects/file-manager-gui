
from ezprint import *
from tkinter import *
import threading
from time import *
import os
#00FFFF голубой
#FFFF00 желтый
# ண

root = None
time_tread = None
isWork = True
files = os.listdir(os.getcwd())


def go_file(file):
	isDir = False
	if os.path.isdir(file):
		isDir = True

	if isDir:
		os.chdir(file)
		print_directory()
		print_files()
	else:
		os.system('start ' + file)


def draw_borded():
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


def go_up(event):
	try:
		os.chdir(os.path.normpath(os.getcwd() + os.sep + os.pardir))
	except:
		pass
	print_directory()
	print_files()


def print_directory():
	dir = os.getcwd()
	root.title(dir)


def print_dots():
	label = Label(root, text = '...', bg='#000080', fg='#FFFF00')
	label.config(font = ('Arial', 10 , 'bold'))
	label.place(x=40, y=30)
	label.bind("<Button-1>", go_up)


def time_update():
	while isWork:
		t = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		label = Label(root, text = t, bg='#000080', fg='#FFFF00')
		label.config(font = ('Arial', 15 , 'bold'))
		label.place(x=20, y=557)
		sleep(1)


def print_files():
	global files
	
	y = 50
	for i in range(len(files)):
		label = Label(root, text = files[i], bg='#000080', fg='#000080')
		label.config(font = ('Arial', 10 , 'bold'))
		label.place(x=40, y=y)
		y+= 20
		label.bind("<Button-1>", go_up)

	files = os.listdir(os.getcwd())
	types = []
	sizes = []

	for file in files:
		fs = os.path.getsize(file)
		p = 'B'
		if fs > 1024:
			fs = round(fs/1024)
			p = 'KB'
		if fs > 1024:
			fs = round(fs/1024)
			p = 'MB'
		if fs > 1024:
			fs = round(fs/1024)
			p = 'GB'
		if os.path.isdir(file):
			types.append('Directory')
		else:
			types.append('File')

		sizes.append(str(fs) + ' ' + p)

	y = 50
	for i in range(len(files)):
		label = Label(root, text = files[i], bg='#000080', fg='#FFFF00')
		label.config(font = ('Arial', 10 , 'bold'))
		label.place(x=40, y=y)
		y+= 20
		# label.bind("<Button-1>", go_up)
		label.bind("<Button-1>",lambda e,file=files[i]:go_file(file))


def on_closing():
	isWork = False
	# time_tread.join()
	root.destroy()


def start_gui():
	global root
	global time_tread

	root = Tk()

	root.title('File Manager')

	root.resizable(0, 0)
	root.geometry('600x600')

	root.config(bg = '#000080')
	root.config()
	draw_borded()

	print_directory()
	print_dots()
	
	time_tread = threading.Thread(target=time_update)
	time_tread.start()

	print_files()

	root.protocol("WM_DELETE_WINDOW", on_closing)

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
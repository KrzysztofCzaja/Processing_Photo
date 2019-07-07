from tkinter import *

from PIL import Image
from os import listdir
from os.path import isfile, join


def edit_image():
	if convert.get() == 1:
		status['text'] = "Done!"
		ConvertingImages()
	elif convert.get() == 2:
		status['text'] = "Done!"
		BorderingImage()
	else:
		status['text'] = "Choose an option"

def ConnectingImages(first,second,No):
	rawImages = []

	rawImages.append(Image.open('source/'+str(first)))
	if second is not None:
		rawImages.append(Image.open('source/'+str(second)))
	else:
		rawImages[0].save('product/'+str(No)+'.jpg')
		return

	for i in range (0,2):
		w, h =rawImages[i].size
		if w > h:
			rawImages[i] = rawImages[i].transpose(Image.ROTATE_270)

	rawWidths,rawHeights = zip(*(i.size for i in rawImages))

	baseheight = min(rawHeights)
	for i in range (0,2):
		hpercent = (baseheight/float(rawImages[i].size[1]))
		wsize = int((float(rawImages[i].size[0]) * float(hpercent)))
		rawImages[i] = rawImages[i].resize((wsize, baseheight), Image.ANTIALIAS)
		rawImages[i].save('temp/temp'+str(i)+'.png')

	# # print(rawImages[1].size)
	images = map(Image.open, ['temp/temp0.png','temp/temp1.png'])#,'temp/temp2.png'])

	widths, heights = zip(*(i.size for i in images))


	total_width = sum(widths)
	max_height = max(heights)

	new_im = Image.new('RGB', (total_width, max_height))

	x_offset = 0
	images = map(Image.open, ['temp/temp0.png','temp/temp1.png'])#,'temp/temp2.png'])

	for im in images:
		new_im.paste(im, (x_offset,0))
		x_offset += im.size[0]

	new_im.save('product/'+str(No)+'.jpg')

def CollectingImages(first,second):
	onlyfiles = [f for f in listdir('source') if isfile(join('source', f))]
	len = onlyfiles.__len__()
	return onlyfiles[first],(onlyfiles[second] if second< len else None)

def ConvertingImages():
	onlyfiles = [f for f in listdir('source') if isfile(join('source', f))]
	len = onlyfiles.__len__()

	i=0
	No = 1
	while i<len:
		firstImage, secondImage = CollectingImages(i,i+1)
		ConnectingImages(firstImage,secondImage,No)
		# print(str(No)+'/'+str(int(len)/2))
		# Tkinter.status['text'] = 'Converted '+str(No)+'/'+str(int(len)/2)+' photos.'
		i+=2
		No+=1

def BorderingImage():
	onlyfiles = [f for f in listdir('source') if isfile(join('source', f))]
	len = onlyfiles.__len__()

	i=0
	No = 1
	while i<len:
		firstImage, secondImage = CollectingImages(i,i+1)
		Border(firstImage, No)
		# print(str(No)+'/'+str(int(len)))
		# Tkinter.status['text'] = 'Converted ' + str(No) + '/' + str(int(len)) + ' photos.'
		i+=1
		No+=1


def Border(first, No):
	image = Image.open('source/'+str(first))
	print(image.size)

	width, height = image.size
	print(width,height)
	new_im = Image.new('RGB', (image.size[0], image.size[1]), (255, 255, 255))
	image = image.resize(((int(image.size[0]-image.size[0]/15)), (int(image.size[1]-image.size[1]/10))), Image.ANTIALIAS)
	print(image.size)

	new_im.paste(image, (((int(image.size[0]/30)), (int(image.size[1]/20)))))
	new_im.save('product/Frame'+str(No)+'.png')



root = Tk()
root.title("Image Tool")
root.wm_iconbitmap('camera.ico')
root.geometry("300x100")
frame = Frame(root)
frame.pack()
# BUTTONs
button_1 = Button(frame, text="START", command=edit_image, justify= CENTER ,width= 10, height= 3, bd=5)
button_1.pack(side=LEFT)
quit_button = Button(frame, text="EXIT", command=frame.quit, justify= CENTER ,width= 10, height= 3, bd=5)
quit_button.pack(side=LEFT)

# STATUS BAR
status = Label(root, text="Do something...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

# RADIOBUTTON in MENU BAR
menu = Menu(root)
root.config(menu=menu)
submenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Options", menu=submenu)

convert = IntVar()
submenu.add_radiobutton(label="Connecting Picture", value=1, variable=convert)
submenu.add_radiobutton(label="Bordering Picture", value=2, variable=convert)

root.mainloop()
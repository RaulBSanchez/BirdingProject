import requests
import json 
import pprint
from tkinter import *
import tkintermapview





#initialize window, set size, don't let size change
root = Tk()
root.maxsize(900,  600)
#root.resizable(0,0)
root.title("Bird App - ebird")



def birdCall(code):


	location = code

	url = 'https://api.ebird.org/v2/data/obs/' + location + '/recent'
	#print("This is the url ", url)
	headers = {'X-eBirdApiToken': 'jkpggffi2t7n'}

	request = requests.get(url, headers = headers)

	request_list = request.json()

	bird_dict = {item['comName']:item for item in request_list}

	commonBirds = list(bird_dict.keys())


	#print(commonBirds)

	entry.delete(0, END)
	entry.insert(0, commonBirds)




def bird(location):
	loc = location 
	if loc == "Wissahickon Valley Park":
		birdCall("L775182")

	elif loc == "Wissahickon Valley Park--Clifford Park":
		birdCall("L13019184")

	elif loc == "Wissahickon Valley Park--Blue Bell Area":
		birdCall("L3636277")

	elif loc == "Wissahickon Valley Park--Lavender Trail":
		birdCall("L2142520")

	elif loc == "Wissahickon Valley Park--South End":
		birdCall("L4018014")


# top frame 
#top_frame = Frame(root,width = 410)
#top_frame.grid(row = 0, column = 0)

#bottom_frame = Frame(root, width = 410)
#bottom_frame.grid(row = 1, column = 0)

#try layout with left and right frame to make it look better
left_frame  =  Frame(root,  width=200,  height=  400,  bg='grey')
left_frame.grid(row=0,  column=0,  padx=10,  pady=5)

right_frame  =  Frame(root,  width=650,  height=400,  bg='grey')
right_frame.grid(row=0,  column=1,  padx=10,  pady=5)



#set coordinates to Wissahickon PA
dropdown_options = ["Wissahickon Valley Park", "Wissahickon Valley Park--Clifford Park", "Wissahickon Valley Park--Blue Bell Area", 
"Wissahickon Valley Park--Lavender Trail", "Wissahickon Valley Park--South End"]
first = StringVar()
first.set(dropdown_options[0])

dropdown = OptionMenu(left_frame, first, *dropdown_options)
dropdown.grid(row = 1, column = 1)

entry = Entry(left_frame)
entry.insert(0, "Birds Spotting")
entry.grid(row = 1, column = 3)

location = Label(left_frame, text= "Location"  )
location.grid(row=1, column = 0)

bird_fetch = Button(left_frame, text ="Check Bird Sitings", command = lambda: bird(first.get()))
bird_fetch.grid(row = 2, column = 0, sticky='w'+'e'+'n'+'s')

map_widget = tkintermapview.TkinterMapView(right_frame, width = 600, height = 350, corner_radius = 0)
#set coordinates to Wissahickon PA
map_widget.set_position(40.056211, -75.217331)

map_widget.set_zoom(12)

map_widget.pack()



#location



root.mainloop()


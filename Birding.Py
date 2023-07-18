import requests
import json 
import pprint
from tkinter import *
import tkintermapview


'''
# url and header
url = 'https://api.ebird.org/v2/data/obs/L1145863/recent'
headers = {'X-eBirdApiToken': ''}


# request for the information 
request = requests.get(url, headers = headers)

#variable to hold information
request_list = request.json()

print('print the reuqests')
pprint.pprint(request_list)
#create new dictionary to convert lists of dictionraries from json to 
bird_dict = {item['comName']:item for item in request_list}
print('now pringint bird dictionary')
pprint.pprint(bird_dict)
'''





#initialize window, set size, don't let size change
root = Tk()
root.geometry("450x400")
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


# front of GUI

#loc_name = Label(window, text = "Wissahickon", font = 'Arial 12 bold').pack(pady=10)
#Button(window, command = BirdCall, text = "Bird Call", font = "Arial 10 ", bg = 'lightblue', fg = 'black', activebackground='teal', padx=5, pady = 5).pack(pady=20)

#birds_now = Label(window, text = "Most Recent Birds are ", font = 'Arial 12 bold').pack(pady=10)

#tfield = Text(window, width = 46, height = 10)
#tfield.pack()


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
top_frame = Frame(root,width = 410)
top_frame.grid(row = 0, column = 0)

bottom_frame = Frame(root, width = 410)
bottom_frame.grid(row = 1, column = 0)

#set coordinates to Wissahickon PA
dropdown_options = ["Wissahickon Valley Park", "Wissahickon Valley Park--Clifford Park", "Wissahickon Valley Park--Blue Bell Area", 
"Wissahickon Valley Park--Lavender Trail", "Wissahickon Valley Park--South End"]
first = StringVar()
first.set(dropdown_options[0])

dropdown = OptionMenu(bottom_frame, first, *dropdown_options)
dropdown.grid(row = 1, column = 1)

entry = Entry(bottom_frame)
entry.insert(0, "Birds Spotting")
entry.grid(row = 1, column = 3)

location = Label(bottom_frame, text= "Location",  anchor = "w")
location.grid(row=1, column = 0)

bird_fetch = Button(bottom_frame, text ="Check Bird Sitings",  command = lambda: bird(first.get()))
bird_fetch.grid(row = 2, column = 0)

map_widget = tkintermapview.TkinterMapView(top_frame, width = 400, height = 200, corner_radius = 0)
#set coordinates to Wissahickon PA
map_widget.set_position(40.056211, -75.217331)

map_widget.set_zoom(12)

map_widget.pack()



#location



root.mainloop()


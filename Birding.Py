import requests
import json 
import pprint
from tkinter import *


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
window = Tk()
window.geometry("400x400")
window.resizable(0,0)
window.title("Bird App - ebird")



def BirdCall():

	url = 'https://api.ebird.org/v2/data/obs/L1145863/recent'
	headers = {'X-eBirdApiToken': ''}

	request = requests.get(url, headers = headers)

	request_list = request.json()

	bird_dict = {item['comName']:item for item in request_list}

	tfield.insert(INSERT, bird_dict)


# front of GUI

loc_name = Label(window, text = "Wissahickon", font = 'Arial 12 bold').pack(pady=10)
Button(window, command = BirdCall, text = "Bird Call", font = "Arial 10 ", bg = 'lightblue', fg = 'black', activebackground='teal', padx=5, pady = 5).pack(pady=20)

birds_now = Label(window, text = "Most Recent Birds are ", font = 'Arial 12 bold').pack(pady=10)

tfield = Text(window, width = 46, height = 10)
tfield.pack()

window.mainloop()


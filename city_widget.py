import requests
import json
from tkinter import *

root = Tk()
root.geometry("400x400")
#root.overrideredirect(True)
root.configure(background="gold")

city_name_label = Label(root, text="City Information", font=("Helvetica", 18,'bold'), bg="gold")
city_name_label.place(relx=0.5, rely=0.05, anchor=CENTER)

city_entry = Entry(root)
city_entry.place(relx=0.5, rely=0.25, anchor=CENTER)

label_name = Label(root, text="Name: ", font=("bold", 10), bg="gold")
label_name.place(relx=0.1, rely=0.35, anchor=CENTER)

label_language = Label(root, text="Language: ", font=("bold", 10), bg="gold")
label_language.place(relx=0.12, rely=0.45, anchor=CENTER)

label_population = Label(root, text="Population: ", font=("bold", 10), bg="gold")
label_population.place(relx=0.12, rely=0.55, anchor=CENTER)

label_area = Label(root, text="Area: ", font=("bold", 10), bg="gold")
label_area.place(relx=0.1, rely=0.65, anchor=CENTER)

def city_details():
    api_request = requests.get("https://restcountries.com/v2/capital/" + city_entry.get())
    api_output_json = json.loads(api_request.content)

root.mainloop()
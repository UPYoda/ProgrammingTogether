#Setup and Import tkinter
from tkinter import * #The (*) means everything is imported from tkinter module which is included in base python
from tkinter import ttk  #Explicitly requiring the ttk prefix faclitates context switching between tkinter and ttk


#Create a program to calculate Feet to Meters and back

#define a way to calculate from feet into meters

def calculate_meters(*args): #Dont really know what try or pass or ValueError is doing here
    try:
        value = float(feet.get()) #This is defined later as the feet passing in
        meters_result.set((0.3048*value)) #This is calculation feet to meters
    except ValueError: #this throws an exception and quits if wrong type of argument is passed
        meters_result.set("Invalid Argument") #CUSTOM: Added a response when a user does not use the correct type of input variable
        pass

def calculate_feet(*args):
    try:
        value = float(meters.get())
        feet_result.set((3.28084*value))
    except ValueError:
        feet_result.set("Invalid Argument")
        pass

#Change incoming numbers to prettier numbers with commas


#Setup the base of the canvas

root = Tk() #This sets up the class tk and lets us augment it after declaring it root
root.title("Feet to Meters and Vice Versa") #This labels the top of the window

#create some space for padding the buttons and labelers

mainframe = ttk.Frame(root, padding=(6, 6, 12, 12)) #Originally I haod this as ttk.Button, ttk.Frame makes more sense...
mainframe.grid(column=0, row=0, sticky=(N,W,E,S)) #Make a background for all the UI
root.columnconfigure(0, weight=1) #not sure what this does
root.rowconfigure(0, weight=1) #not sure what this does

#Create a visual separation between the two converters for ease of use WIP

top = ttk.Style()
bot = ttk.Style()
top.configure('Feet.Meter', background='blue', borderwidth=3, relief='raised')
bot.configure('Meter.Feet', background='yellow', borderwidth=3)



#Define the input variably so we can augement and send it to calculate_feet

feet = StringVar() #Construct a string variable named feet
feet_result = StringVar()
feet_entry = ttk.Entry(mainframe, width=20, textvariable=feet) #Needs to be a textvariable for this.
feet_entry.grid(column=2, row=1, sticky=(W, E)) # this aligns it on a left right but not N,S; also sticks it in the middle column top row
ttk.Label(mainframe, font=25, textvariable=feet_result).grid(column=2, row=5, sticky=(W,E)) #This outputs the result of the feet program



#Define meters for input variability and sending and send it to our defined function

meters = StringVar() #To be passed in the definition for calculating feet
meters_result = StringVar() #Construct a string variable to be passed out of the conversion
meters_entry = ttk.Entry(mainframe, width = 20, textvariable=meters)
meters_entry.grid(column=2, row=4, sticky=(W, E))
ttk.Label(mainframe, font = 25, textvariable=meters_result).grid(column=2, row=2, sticky=(W,E))  #This will output the result of the meters to the correct postion

#Create an event driven button to execute our waiting definition and put it in the bottom right

ttk.Button(mainframe, text="Calculate", command=calculate_meters).grid(column=3, row=3, sticky=W)
ttk.Button(mainframe, text="Calculate", command=calculate_feet).grid(column=3, row=6, sticky=W)

#Construct the labels that come hardcoded after each input box and output box

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W) #Puts feet after input box as it is in the first row
ttk.Label(mainframe, text="meters").grid(column=3, row=4, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=5, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="feet").grid(column=3, row=5, sticky=W)





for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate_meters)


root.mainloop()
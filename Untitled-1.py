from tkinter import *


def callbackFunc():
    resultString.set("{} - {}".format(landString.get(),
                                      cityString.get()))
     
app = Tk() 
app.geometry('200x100')

labelLand = Label(app,
                    text = "Country")
labelLand.grid(column=0, row=0, sticky=W)
labelCity = Label(app,
                    text = "City")
labelCity.grid(column=0, row=1, sticky=W)

landString = StringVar()
cityString = Entry(app, width=20, textvariable=landString)
entryCity = Entry(app, width=20, textvariable=cityString)

entryLand.grid(column=1, row=0, padx=10)
entryCity.grid(column=1, row=1, padx=10)


resultButton =Button(app, text = 'Get Result',
                         command=callbackFunc)

resultButton.grid(column=0, row=2, pady=10, sticky=W)

resultString=StringVar()
resultLabel = Label(app, textvariable=resultString)
resultLabel.grid(column=1, row=2, padx=10, sticky=W)

app.mainloop()

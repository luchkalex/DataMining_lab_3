from tkinter import *
import matplotlib.pyplot as plt
import numpy as np


def graph():
    prices = np.random.normal(20000, 1000, 5000)
    plt.hist(prices, 50)
    plt.show()


root = Tk()
root.title = "Title"
mainLabel = Label(root, text="MyLabel", font=("Times New Roman", 14, 'bold'))
mainLabel.pack()
graphButton = Button(root, text="Show", command=graph)
graphButton.pack()
root.mainloop()




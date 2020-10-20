from tkinter import *
from constants import *
from data_processor import *
from services import *
from ui.drawer import graph

root = Tk()
root.title = "Title"
cluster_quantity = StringVar()
main_label_text = StringVar()
main_label = Label(root, textvariable=main_label_text, font=("Times New Roman", 13, 'bold'))
cluster_field = Entry(textvariable=cluster_quantity)
graph_button = Button(root, text="Build", command=lambda: {build()})

r_var = IntVar()
r_var.set(0)
radio_button1 = Radiobutton(text=file_name_cases[1], variable=r_var, value=1)
radio_button2 = Radiobutton(text=file_name_cases[2], variable=r_var, value=2)
radio_button3 = Radiobutton(text=file_name_cases[3], variable=r_var, value=3)
radio_button4 = Radiobutton(text=file_name_cases[4], variable=r_var, value=4)


def show_main_form():
    radio_button1.pack()
    radio_button2.pack()
    radio_button3.pack()
    radio_button4.pack()

    cluster_field.pack()
    main_label.pack()
    graph_button.pack()

    root.mainloop()


def build():
    if validate_input():
        string_list = get_list_of_lines_from_file(SOURCE_DIR + "/" + file_name_cases[r_var.get()])
        points = get_points_from_string_list(string_list)
        clusters = get_clusters(cluster_quantity.get(), points)
        distribute_points(clusters, points)
        graph(clusters)

    else:
        cluster_quantity.set("")
        main_label_text.set("Invalid value")


def validate_input():
    try:
        get_clusters_quantity()
        return True
    except ValueError:
        return False


def get_clusters_quantity():
    string = cluster_quantity.get()
    if string:
        return cluster_quantity
    else:
        raise ValueError

from tkinter import *
from tkinter import ttk
# import random
# from random import choices
from Algo_visualization_module import bubble_start, linear_search_start,binary_start


# import partial


class AlgoVisualize(Tk):
    def __init__(self):
        super().__init__()
        # root.geometry('900x600')
        self.title("ALGO_VISUALIZATION")
        self.maxsize(900, 600)
        self.config(bg="#2C3539")
        # Variables
        selected_algo = StringVar()

        self.frame_1 = Frame(self, width=600, height=200, bg="#4863A0")
        self.frame_1.grid(row=0, column=0, padx=10, pady=5)

        self.canvas = Canvas(self, width=600, height=300, bg="#FFFFFF")
        self.canvas.grid(row=1, column=0, padx=10, pady=5)

        # UI
        self.label_1 = Label(self.frame_1, text="Algorithm", bg="#413839", fg="white")
        self.label_1.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.algo_menue = ttk.Combobox(self.frame_1, textvariable=selected_algo,
                                       values=['Bubble Sort', 'Insertion Sort', 'Quick Sort', 'Linear Search','Binary Search'])
        self.algo_menue.grid(row=0, column=1, padx=5, pady=5, columnspan=1)
        self.algo_menue.current(0)

        self.button_1 = Button(self.frame_1, text='RUN IT!!',
                               command=lambda: self.algo_group(self.algo_menue.get(), int(self.win_width_sliders.get()),int(self.win_height_sliders.get()),int(self.win_speed_sliders.get()),int(self.win_width_bar_sliders.get())))
        self.button_1.grid(row=0, column=2, padx=5, pady=5)

        self.label_2 = Label(self.frame_1, text='Window Width')
        self.label_2.grid(row=1, column=0)

        self.win_width_sliders = Scale(self.frame_1, from_=100, to=1000, length=200, resolution=2, orient=HORIZONTAL)
        self.win_width_sliders.grid(row=2, column=0, padx=5)

        self.label_3 = Label(self.frame_1, text='Window Height')
        self.label_3.grid(row=1, column=1)

        self.win_height_sliders = Scale(self.frame_1, from_=100, to=1000, length=200, resolution=2, orient=HORIZONTAL)
        self.win_height_sliders.grid(row=2, column=1, padx=5)

        self.label_3 = Label(self.frame_1, text='Speed of Algo Execution')
        self.label_3.grid(row=1, column=2)

        self.win_speed_sliders = Scale(self.frame_1, from_=1, to=500, length=200, resolution=2, orient=HORIZONTAL)
        self.win_speed_sliders.grid(row=2, column=2, padx=5)

        self.label_3 = Label(self.frame_1, text='Width of Each Bar')
        self.label_3.grid(row=3, column=0)

        self.win_width_bar_sliders = Scale(self.frame_1, from_=1, to=50, length=200, resolution=2, orient=HORIZONTAL)
        self.win_width_bar_sliders.grid(row=4, column=0, padx=5)

    def algo_group(self, id, win_width, win_height, algo_speed, wid_bar):
        if id == 'Bubble Sort':
            bubble_start(window_width=win_width, window_height=win_height, width_of_bars=wid_bar, speed_of_sorting=algo_speed)

        if id == 'Linear Search':
            linear_search_start(window_width=win_width, window_height=win_height, width_of_bars=wid_bar,
                                speed_of_sorting=algo_speed)

        if id == 'Binary Search':
            binary_start(window_width=win_width, window_height=win_height, width_of_bars=wid_bar,
                         speed_of_sorting=algo_speed)




if __name__ == '__main__':
    mainwin_2 = AlgoVisualize()
    print(type(mainwin_2.win_speed_sliders))
    print(mainwin_2.win_speed_sliders)
    mainwin_2.mainloop()

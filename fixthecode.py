# This program uses a GUI to get three test
# scores and display their average.

# (4/28) Michael Boyer
# Fixed typo in import statement
# Occurrences below are also fixed
import tkinter
# ---------

class TestAvg:
    def __init__(self):
        # Create the main window.
        #
        self.main_window = tkinter.Tk()

        # Create the five frames.
        self.test1_frame = tkinter.Frame(self.main_window)
        self.test2_frame = tkinter.Frame(self.main_window)
        self.test3_frame = tkinter.Frame(self.main_window)
        self.avg_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create and pack the widgets for test 1.
        self.test1_label = tkinter.Label(self.test1_frame,
                                         text='Enter the score for test 1:')
        self.test1_entry = tkinter.Entry(self.test1_frame,
                                         width=10)
        self.test1_label.pack(side='left')
        self.test1_entry.pack(side='left')

        # Create and pack the widgets for test 2.

        # (4/28) Michael Boyer
        # Typo: Enter, not entre
        self.test2_label = tkinter.Label(self.test2_frame,
                                         text='Enter the score for test 2:')
        self.test2_entry = tkinter.Entry(self.test2_frame,
                                         width=10)
        self.test2_label.pack(side='left')
        self.test2_entry.pack(side='left')

        # Create and pack the widgets for test 3.

        # (4/28) Michael Boyer
        # Width is way too large. Changed from 100 to 10
        self.test3_label = tkinter.Label(self.test3_frame,
                                         text='Enter the score for test 3:')
        self.test3_entry = tkinter.Entry(self.test3_frame,
                                         width=10)
        self.test3_label.pack(side='left')
        self.test3_entry.pack(side='left')

        # Create and pack the widgets for the average.
        self.result_label = tkinter.Label(self.avg_frame,
                                          text='Average:')
        self.avg = tkinter.StringVar() # To update avg_label
        self.avg_label = tkinter.Label(self.avg_frame,
                                       textvariable=self.avg)
        self.result_label.pack(side='left')
        self.avg_label.pack(side='left')

        # Create and pack the button widgets.

        # (4/28) Michael Boyer
        # Fixed a mistake in the code with the usage of "self.calc_avg"
        # self.calc_avg doesn't exist; isn't the name of our function
        self.calc_button = tkinter.Button(self.button_frame,
                                          text='Average',
                                          command=self.calculate_average)
        self.quit_button = tkinter.Button(self.button_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.test1_frame.pack()
        self.test2_frame.pack()
        self.test3_frame.pack()
        self.avg_frame.pack()
        # (4/28) Michael Boyer
        # uncommented widget pack call
        self.button_frame.pack()

        # Start the main loop.
        tkinter.mainloop()

    # The calculate_average method is the callback function for
    # the calc_button widget.
    def calculate_average(self):
        # Get the three test scores and store them
        # in variables.
        self.test1 = float(self.test1_entry.get())
        self.test2 = float(self.test2_entry.get())
        self.test3 = float(self.test3_entry.get())

        # Calculate the average.

        # (4/28) Michael Boyer
        # We are dividing by 3.8 when we should be dividing by 3
        # Also some issue with + missing
        # Also, needs to be string. Can't be float.
        self.average = str((self.test1 + self.test2 + self.test3) / 3)

        # Update the avg_label widget by storing
        # the value of self.average in the StringVar
        # object referenced by avg.

        # (4/28) Michael Boyer
        # Needed to be self.average, not average.
        self.avg.set(self.average)

# Create an instance of the TestAvg class.
if __name__ == '__main__':
    test_avg = TestAvg()

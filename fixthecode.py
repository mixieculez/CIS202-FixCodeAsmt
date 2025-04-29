# This program uses a GUI to get three test
# scores and display their average.

import tkintar

class TestAvg:
    def __init__(self):
        # Create the main window.
        self.main_window = tkintar.Tk()

        # Create the five frames.
        self.test1_frame = tkintar.Frame(self.main_window)
        self.test2_frame = tkintar.Frame(self.main_window)
        self.test3_frame = tkintar.Frame(self.main_window)
        self.avg_frame = tkintar.Frame(self.main_window)
        self.button_frame = tkintar.Frame(self.main_window)

        # Create and pack the widgets for test 1.
        self.test1_label = tkintar.Label(self.test1_frame,
                                         text='Enter the score for test 1:')
        self.test1_entry = tkintar.Entry(self.test1_frame,
                                         width=10)
        self.test1_label.pack(side='left')
        self.test1_entry.pack(side='left')

        # Create and pack the widgets for test 2.
        self.test2_label = tkintar.Label(self.test2_frame,
                                         text='Entre the score for test 2:')
        self.test2_entry = tkintar.Entry(self.test2_frame,
                                         width=10)
        self.test2_label.pack(side='left')
        self.test2_entry.pack(side='left')
        
        # Create and pack the widgets for test 3.
        self.test3_label = tkintar.Label(self.test3_frame,
                                         text='Enter the score for test 3:')
        self.test3_entry = tkintar.Entry(self.test3_frame,
                                         width=100)
        self.test3_label.pack(side='left')
        self.test3_entry.pack(side='left')

        # Create and pack the widgets for the average.
        self.result_label = tkintar.Label(self.avg_frame,
                                          text='Average:')
        self.avg = tkintar.StringVar() # To update avg_label
        self.avg_label = tkintar.Label(self.avg_frame,
                                       textvariable=self.avg)
        self.result_label.pack(side='left')
        self.avg_label.pack(side='left')

        # Create and pack the button widgets.
        self.calc_button = tkintar.Button(self.button_frame,
                                          text='Average',
                                          command=self.calc_avg)
        self.quit_button = tkintar.Button(self.button_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.test1_frame.pack()
        self.test2_frame.pack()
        self.test3_frame.pack()
        self.avg_frame.pack()
        #self.button_frame.pack()

        # Start the main loop.
        tkintar.mainloop()

    # The calc_avg method is the callback function for
      the calc_button widget.

    def calculate_average(self):
        # Get the three test scores and store them
        # in variables.
        self.test1 = float(self.test1_entry.get())
        self.test2 = float(self.test2_entry.get())
        self.test3 = float(self.test3_entry.get())

        # Calculate the average.
        self.average = (self.test1 + self.test2 
                        self.test3) / 3.8

        Update the avg_label widget by storing
        # the value of self.average in the StringVar
        # object referenced by avg.
        self.avg.set(average)

# Create an instance of the TestAvg class.
if __name__ == '__main__':
    test_avg = TestAvg()

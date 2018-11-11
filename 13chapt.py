"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""
import tkinter

# TODO 13.2 Using the tkinter Module
# Write the code from program 13-2 to display an empty window, no need
# to re-import tkinter
class MyGUI:
    def __int__(self):
        self.main_window = tkinter.Tk()

# TODO 13.3 Adding a label widget
# add a label that prints your first and last name
        self.label = tkinter.Label(self.main_window, text='RYan Le')

# pack the label
        self.label.pack()
# enter the main loop
        tkinter.mainloop()
# create an instance of MyGUI2
my_gui2 = MyGUI()
# TODO 13.4 Organizing Widgets with Frames
# Create a window in the MyGUI3 class that has two frames
# In the top Frame add a labels with your name and major
# In the bottom frame add labels with the classes you are taking this semester
class MyGUI3(MyGUI):
        def __int__(self):
            self.main_window = tkinter.Tk()
            self.top_frame = tkinter.Frame(self.main_window)
            self.bottom_frame = tkinter.Frame(self.main_window)

            self.label1 = tkinter.Label(self.top_frame, text = 'Ryan Le')
            self.label2 = tkinter.Label(self.top_frame, text = 'Digital Media')
            self.label1.pack(side='top')
            self.label2.pack(side='top')

            self.label3 = tkinter.Label(self.bottom_frame, text = 'Graphic Design')
            self.label4 = tkinter.Label(self.bottom_frame, text = 'Adobe Design Suite')
            self.label5 = tkinter.Label(self.bottom_frame, text = 'English Compossition')
            self.label3.pack(side='left')
            self.label4.pack(side='left')
            self.label5.pack(sode='left')

            self.top_frame.pack()
            self.bottom_frame.pack()
            tkinter.mainloop()
my_gui3 = MyGUI3
# TODO 13.5 Button Widgets and info Dialog Boxes
# Tell a joke with a button to show the punch line, which should appear in a dialog box
class MyGUI4(MyGUI):
    def __int__(self):
        self.main_window = tkinter.Tk()
        self.label1 = tkinter.Label(self.top_frame, text = 'What do you call something that wasnt worth the money?')
        self.label = tkinter.Label(self.main_window, text='I dont know')
# TODO 13.6 getting input / 13.7 Using Labels as output fields
# Using the program in 13.10 kilo converter as a sample, create a program
# to convert inches to centimeters
inches = int(input("input a number of inches to be converted to centimeters "))
centimeters = inches * 12
print("you converted ", inches, "to ", centimeters, " centimeters")

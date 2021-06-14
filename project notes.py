#NOTES:

#SMS******************************************************************************************************
# Definition and Usage
# The requests module allows you to send HTTP requests using Python.

# The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).



# JSON is a syntax for storing and exchanging data.

# JSON is text, written with JavaScript object notation.

# JSON in Python
# Python has a built-in package called json, which can be used to work with JSON data.
# Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.
# Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

# response.json() returns a JSON object of the result (if the result was written in JSON format, 
# if not it raises an error). Python requests are generally used to fetch the content from a 
# particular resource URI. Whenever we make a request to a specified URI through Python, it returns a response object. Now, 
# this response object would be used to access certain features such as content, headers, etc. 
#******************************************************************************************************************************


#GUI:*******************************************************************************************************
#Python offers multiple options for developing GUI (Graphical User Interface).
#  Out of all the GUI methods, tkinter is the most commonly used method. It is a standard Python interface to the Tk GUI 
# toolkit shipped with Python. Python with tkinter is the fastest and easiest way to create the GUI applications. Creating a GUI using tkinter is an easy task.

# To create a tkinter app:
# Importing the module – tkinter
# Create the main window (container)
# Add any number of widgets to the main window
# Apply the event Trigger on the widgets.
# Importing tkinter is same as importing any other module in the Python code. Note that the name of the module in Python 
# 2.x is ‘Tkinter’ and in Python 3.x it is ‘tkinter’.

# import tkinter
# There are two main methods used which the user needs to remember while creating the Python application with GUI.

# Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1): To create a main window, tkinter offers a method ‘Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1)’. To change the name of the window, you can change the className to the desired one. The basic code used to create the main window of the application is:
# m=tkinter.Tk() where m is the name of the main window object
# mainloop(): There is a method known by the name mainloop() is used when your application is ready to run. mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed.
# m.mainloop()
# import tkinter
# m = tkinter.Tk()
# '''
# widgets are added here
# '''
# m.mainloop()
# tkinter also offers access to the geometric configuration of the widgets which can organize the widgets in the parent windows. There are mainly three geometry manager classes class.

# pack() method:It organizes the widgets in blocks before placing in the parent widget.
# grid() method:It organizes the widgets in grid (table-like structure) before placing in the parent widget.
# place() method:It organizes the widgets by placing them on specific positions directed by the programmer.
#*************************************************************************************************************************
import tkinter
import random

#Creates the main window
root = tkinter.Tk()
root.title("Idea Generator")

#Sets the height and width of the window
rootCanvas = tkinter.Canvas(root, width = 200, height = 10)

#Creates two tkinter labels and sets them to blank values
firstWord = [line.strip() for line in open("dictionary.txt")]
wordOne = tkinter.Label(root, text = " ")

secondWord = [line.strip() for line in open("operations.txt")]
wordTwo = tkinter.Label(root, text = " ")

#Sets the strings to random words from the text files
def generate():
	global firstWord
	global wordOne
	global secondWord
	global wordTwo
	wordOne.config(text = random.choice(firstWord))
	wordTwo.config(text = random.choice(secondWord))

#Creates the button and sets it's command to the generate function
generateIdea = tkinter.Button(root, text = "Generate Idea", command = generate)

#Packs all the tkinter objects
generateIdea.pack()
wordOne.pack()
wordTwo.pack()
rootCanvas.pack()

#Runs the window
root.mainloop()
import tkinter
import random

root = tkinter.Tk()
root.title("Idea Generator")

rootCanvas = tkinter.Canvas(root, width = 200, height = 10)

firstWord = [line.strip() for line in open("dictionary.txt")]
wordOne = tkinter.Label(root, text = " ")

secondWord = [line.strip() for line in open("operations.txt")]
wordTwo = tkinter.Label(root, text = " ")

def generate():
    global firstWord
	global wordOne
	global secondWord
	global wordTwo
	wordOne.config(text = random.choice(firstWord))
	wordTwo.config(text = random.choice(secondWord))

generateIdea = tkinter.Button(root, text = "Generate Idea", command = generate)

generateIdea.pack()
wordOne.pack()
wordTwo.pack()
rootCanvas.pack()

root.mainloop()
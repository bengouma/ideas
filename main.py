import tkinter
import random

root = tkinter.Tk()
root.title("Idea Generator")

rootCanvas = tkinter.Canvas(root, width = 200, height = 10)

def generate():
    firstWord = [line.strip() for line in open("dictionary.txt")]
    wordOne = tkinter.Label(root, text = random.choice(firstWord))

    secondWord = [line.strip() for line in open("operations.txt")]
    wordTwo = tkinter.Label(root, text = " " + random.choice(secondWord))

    wordOne.pack()
    wordTwo.pack()

generateIdea = tkinter.Button(root, text = "Generate Idea", command = generate)

generateIdea.pack()
rootCanvas.pack()

root.mainloop()
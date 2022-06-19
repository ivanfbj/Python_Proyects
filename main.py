"""
source:
https://data-flair.training/blogs/python-mad-libs-generator-game/#:~:text=Mad%20libs%20generator%20is%20a,stories%20after%20filling%20the%20blanks.
Python Mad Libs Generator
The objective of this project is to develop a Mad Libs Generator python project. In this project,
the user first has to pick a story by the title of the story. Then the user has to enter specific words like a noun,
adverb, verb, food, adjective, etc, according to the requirements. And then the story will be generated.

This is a python project for absolute beginners and is developed using the basic concept of python and tkinter.
"""
from tkinter import Label, Tk, Button


# Define Function
def madlib1():
    animals = input('Enter a animal name : ')
    profession = input('Enter a profession name: ')
    cloth = input('Enter a piece of cloth name: ')
    things = input('Enter a thing name: ')
    name = input('Enter a name: ')
    place = input('Enter a place name: ')
    verb = input('Enter a verb in ing form: ')
    food = input('Food name: ')
    print(
        'say ' + food + ', the photographer said as the camera flashed! ' + name + ' and I had gone to ' + place
        + ' to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as '
        + animals + ' pretending to be a ' + profession
        + '. when we saw the second photo, it was exactly what I wanted. We both looked like '
        + things + ' wearing ' + cloth + ' and ' + verb + ' --exactly what I had in mind')


def madlib2():
    adjective = input('Enter adjective : ')
    color = input('Enter a color name : ')
    thing = input('Enter a thing name :')
    place = input('Enter a place name : ')
    person = input('Enter a person name : ')
    adjective1 = input('Enter a adjective : ')
    insect = input('Enter a insect name : ')
    food = input('Enter a food name : ')
    verb = input('Enter a verb name : ')
    print(
        'Last night I dreamed I was a ' + adjective + ' butterfly with ' + color + ' splocthes that looked like '
        + thing + ' .I flew to ' + place + ' with my bestfriend and ' + person + ' who was a ' + adjective1 + ' '
        + insect + ' .We ate some ' + food + ' when we got there and then decided to '
        + verb + ' and the dream ended when I said-- lets ' + verb + '.')


def madlib3():
    person = input('Enter person name: ')
    color = input('Enter color : ')
    foods = input('Enter food name : ')
    adjective = input('Enter aa adjective name: ')
    thing = input('Enter a thing name : ')
    place = input('Enter place : ')
    verb = input('Enter verb : ')
    adverb = input('Enter adverb : ')
    food = input('Enter food name: ')
    things = input('Enter a thing name : ')

    print(
        'Today we picked apple from ' + person
        + "'s Orchard. I had no idea there were so many different varieties of apples. I ate "
        + color + ' apples straight off the tree that tested like ' + foods + '. Then there was a ' + adjective
        + ' apple that looked like a ' + thing + '.When our bag were full, we went on a free hay ride to ' + place
        + ' and back. It ended at a hay pile where we got to ' + verb + ' ' + adverb
        + '. I can hardly wait to get home and cook with the apples. We are going to make appple '
        + food + ' and ' + things + ' pies!.')


if __name__ == "__main__":
    # Create a Display Window
    root = Tk()  # Tk() initialized tkinter which means window created
    root.geometry('300x300')  # geometry() used when we want to set the width and height of the window
    root.title('DataFlair-Mad Libs Generator')  # title() used to give the title of the window
    Label(root, text='Mad Libs Generator \n Have Fun!',
          font='arial 20 bold').pack()  # Label() widget use to display text that users can’t able to modify
    Label(root, text='Click Any One :', font='arial 15 bold').place(x=40, y=80)

    Button(root, text='The Photographer', font='arial 15', command=madlib1, bg='ghost white').place(x=60, y=120)
    Button(root, text='apple and apple', font='arial 15', command=madlib3, bg='ghost white').place(x=70, y=180)
    Button(root, text='The Butterfly', font='arial 15', command=madlib2, bg='ghost white').place(x=80, y=240)

    root.mainloop()

"""
Summary
We have successfully developed the mad libs generator python project. We used tkinter library for rendering graphics
on a display window and learn how to create buttons widget and pass the function to the button. In this way,
we build this python project.
"""

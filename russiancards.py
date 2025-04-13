import os
import sys
import PySimpleGUI as sg

engVocabFile = open("engvocab.txt", "r")
rusVocabFile = open("rusvocab.txt", "r")

engVocabList = [line.rstrip() for line in engVocabFile]
rusVocabList = [line.rstrip() for line in rusVocabFile]

engVocabFile.close()
rusVocabFile.close()

currentNumber = 0

layout = [ [sg.Text(f'English: {engVocabList[currentNumber]}', key='-ENGLISH-')],
          [sg.Text(f'Russian: ', key='-RUSSIAN-')],
          [sg.Button('Previous'), sg.Button('Russian'), sg.Button('Next')]
]

window = sg.Window("Flashcards", layout)

def showEnglish():
    print(f"EN: {engVocabList[currentNumber]}")
    window["-ENGLISH-"].update(f"English: {engVocabList[currentNumber]}")

def showRussian():
    window["-RUSSIAN-"].update(f"Russian: {rusVocabList[currentNumber]}")

def nextCard():
    global currentNumber
    currentNumber += 1

def prevCard():
    global currentNumber
    currentNumber -= 1

running = True

while running:
    event, values = window.read()

    if event in (None, 'Exit'):
        break

    if event == 'Next':
        nextCard()
        showEnglish()
        window["-RUSSIAN-"].update("Russian: ")
    if event == 'Previous':
        prevCard()
        showEnglish()
    if event == 'Russian':
        showRussian()

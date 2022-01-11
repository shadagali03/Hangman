from os import write
import pygame
from pygame.display import set_caption
from pygame.image import load
from pygame.locals import *
import csv
import random

class Button:
    def __init__(self,text,pos,color,size=[25,25],fontSize=16):
        self.x, self.y = pos
        self.font = pygame.font.Font('freesansbold.ttf',fontSize)
        self.text = text
        self.color = color
        self.rect = pygame.Rect(self.x,self.y,size[0],size[1])
        self.isClicked = False
        self.size = size
    def show(self):
        if self.isClicked:
            pygame.draw.rect(screen,self.color,self.rect)
        else:
            pygame.draw.rect(screen,(0,128,0),self.rect)
        writeText = self.font.render(self.text,True,(0,0,0))
        myRect = writeText.get_rect()
        myRect.center = (self.x+(self.size[0]//2),self.y+(self.size[1]//2))
        screen.blit(writeText,myRect)
    def click(self):
        x, y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(x, y):
                self.isClicked = True
                return self.text
            else:
                return ''
        else:
            return ''

pygame.init()
screen = pygame.display.set_mode((800,600))
running = True
pygame.display.set_caption("Hangman")

def fileToList(path,col):
    file = open(path)
    reader = csv.reader(file)
    rows = []
    for row in reader:
        rows.append(row[col])
    return rows
def getNetflixShows(path):
    file = open(path)
    reader = csv.reader(file)
    shows = []
    for row in reader:
        if row[0] != 'Movie':
            shows.append(row[2])
    return shows

def loadingScreen():
    font = pygame.font.Font('freesansbold.ttf',64)
    font1 = pygame.font.Font('freesansbold.ttf',32)
    Movies = Button('Disney Movies',(425,200),(133,22,190),[300,75],32)
    movieList = fileToList('/Users/sarang_hadagali/Code/Personal_Projects/Python/Pygame/Hangman/disney_movies.csv',0)
    Sports = Button('Sports',(75,200),(1,254,0),[300,75],32)
    file = open('/Users/sarang_hadagali/Code/Personal_Projects/Python/Pygame/Hangman/sports.txt','r')
    sportsList = []
    for row in file:
        row = row[:-1]
        sportsList.append(row)
    tvShow = Button('Netflix TV Shows',(75,300),(1,254,0),[300,75],32)
    netflixList = getNetflixShows('/Users/sarang_hadagali/Code/Personal_Projects/Python/Pygame/Hangman/netflix_titles.csv')
    Countries = Button('Countries',(75,400),(1,254,0),[300,75],32)
    file = open('/Users/sarang_hadagali/Code/Personal_Projects/Python/Pygame/Hangman/Countries.txt','r')
    countriesList = []
    for row in file:
        country = ''
        for letter in row:
            if letter != ',':
                country += letter
        countriesList.append(country)
    Presidents = Button('Presidents',(425,300),(1,254,0),[300,75],32)
    presidentList = fileToList('/Users/sarang_hadagali/Code/Personal_Projects/Python/Pygame/Hangman/us_presidents.csv',4)
    Mix = Button('Mix All',(425,400),(1,254,0),[300,75],32)
    mixList = movieList + sportsList + netflixList + countriesList + presidentList


    Welcome = font.render("Hangman",True,(40,40,40))
    category = font1.render('Choose A Category',True,(56,89,32))
    running = True
    while running:
        screen.fill((0,204,204))
        screen.blit(Welcome,(250,50))
        screen.blit(category,(250,130))
        Movies.show()
        Sports.show()
        tvShow.show()
        Countries.show()
        Presidents.show()
        Mix.show()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                Movies.click()
                Presidents.click()
                Sports.click()
                tvShow.click()
                Countries.click()
                Mix.click()
                if Movies.isClicked:
                    number = random.randint(1,len(movieList))
                    word = movieList[number]
                    gameLoop(word)
                if Presidents.isClicked:
                    number = random.randint(0,len(presidentList))
                    word = presidentList[number]
                    gameLoop(word)
                if Sports.isClicked:
                    number = random.randint(0,len(sportsList))
                    word = sportsList[number]
                    gameLoop(word)
                if tvShow.isClicked:
                    number = random.randint(0,len(netflixList))
                    word = netflixList[number]
                    gameLoop(word)
                if Countries.isClicked:
                    number = random.randint(0,len(countriesList))
                    word = countriesList[number]
                    gameLoop(word)
                if Mix.isClicked:
                    number = random.randint(0,len(mixList))
                    word = mixList[number]
                    gameLoop(word)

                    
        pygame.display.update()

x_pos = 500
y_pos = 150
myList = []
ButtonA = Button('A',(x_pos,y_pos),(255,0,0))
myList.append(ButtonA)
ButtonB = Button('B',(x_pos+30,y_pos),(255,0,0))
myList.append(ButtonB)
ButtonC = Button('C',(x_pos+60,y_pos),(255,0,0))
myList.append(ButtonC)
ButtonD = Button('D',(x_pos+90,y_pos),(255,0,0))
myList.append(ButtonD)
ButtonE = Button('E',(x_pos+120,y_pos),(255,0,0))
myList.append(ButtonE)
ButtonF = Button('F',(x_pos+150,y_pos),(255,0,0))
myList.append(ButtonF)
ButtonG = Button('G',(x_pos+180,y_pos),(255,0,0))
myList.append(ButtonG)
ButtonH = Button('H',(x_pos+210,y_pos),(255,0,0))
myList.append(ButtonH)
ButtonI = Button('I',(x_pos+240,y_pos),(255,0,0))
myList.append(ButtonI)
ButtonJ = Button('J',(x_pos,y_pos+40),(255,0,0))
myList.append(ButtonJ)
ButtonK = Button('K',(x_pos+30,y_pos+40),(255,0,0))
myList.append(ButtonK)
ButtonL = Button('L',(x_pos+60,y_pos+40),(255,0,0))
myList.append(ButtonL)
ButtonM = Button('M',(x_pos+90,y_pos+40),(255,0,0))
myList.append(ButtonM)
ButtonN = Button('N',(x_pos+120,y_pos+40),(255,0,0))
myList.append(ButtonN)
ButtonO = Button('O',(x_pos+150,y_pos+40),(255,0,0))
myList.append(ButtonO)
ButtonP = Button('P',(x_pos+180,y_pos+40),(255,0,0))
myList.append(ButtonP)
ButtonQ = Button('Q',(x_pos+210,y_pos+40),(255,0,0))
myList.append(ButtonQ)
ButtonR = Button('R',(x_pos+240,y_pos+40),(255,0,0))
myList.append(ButtonR)
ButtonS = Button('S',(x_pos,y_pos+80),(255,0,0))
myList.append(ButtonS)
ButtonT = Button('T',(x_pos+30,y_pos+80),(255,0,0))
myList.append(ButtonT)
ButtonU = Button('U',(x_pos+60,y_pos+80),(255,0,0))
myList.append(ButtonU)
ButtonV = Button('V',(x_pos+90,y_pos+80),(255,0,0))
myList.append(ButtonV)
ButtonW = Button('W',(x_pos+120,y_pos+80),(255,0,0))
myList.append(ButtonW)
ButtonX = Button('X',(x_pos+150,y_pos+80),(255,0,0))
myList.append(ButtonX)
ButtonY = Button('Y',(x_pos+180,y_pos+80),(255,0,0))
myList.append(ButtonY)
ButtonZ = Button('Z',(x_pos+210,y_pos+80),(255,0,0))
myList.append(ButtonZ)

def drawLines(inputWord):
    y = 0
    for x in range(len(inputWord)):
        y+=40
        z = 200//len(inputWord)
        if inputWord[x] != ' ':
            pygame.draw.line(screen,(0,0,0),(50+y,500),(70+y,500))
def startStop():
        playAgain = Button('Play Again?',(300,300),(0,233,0),[100,50])
        playAgain.show()
        playAgain.click()
        if playAgain.isClicked:
            for btn in myList:
                if btn.isClicked:
                    btn.isClicked = False
            loadingScreen()
        GameOver = Button('Exit',(300,400),(255,0,0),[100,50])
        GameOver.show()
        GameOver.click()
        if GameOver.isClicked:
            pygame.quit()
def checkCase(inputWord,allLetters):
    noDuplicates = sorted(list(set(inputWord)))
    compare = sorted(allLetters)
    if noDuplicates == compare:
        startStop()
def drawLetters(inputWord,allLetters):
    allLetters = allLetters[1:]
    y = 0
    z = 200//len(inputWord)
    font = pygame.font.Font('freesansbold.ttf',32)
    checkCase(inputWord,allLetters)
    for letter in allLetters:
        y = 0
        for value in inputWord:
            y+=40
            if letter == value:
                w = font.render(letter,True,(0,0,0))
                rect = w.get_rect()
                rect.center = (115//2+y,485)
                screen.blit(w,rect)
def showWrong(wrongCount,inputWord):
    if wrongCount == 0:
        h1 = pygame.image.load('/Users/sarang_hadagali/Code/Personal_Projects/Python/Pygame/Hangman/HangmanStand.png')
    if wrongCount == 1:
        h1 = pygame.image.load('/Users/sarang_hadagali/Code/Personal_Projects/Python/Pygame/Hangman/HangmanStand1.png')
    elif wrongCount == 2:
        h1 = pygame.image.load('/Users/sarang_hadagali/Code/Personal_Projects/Python/Pygame/Hangman/HangmanStand2.png')
    elif wrongCount == 3:
        h1 = pygame.image.load('/Users/sarang_hadagali/Code/Personal_Projects/Python/Pygame/Hangman/HangmanStand3.png')
    elif wrongCount == 4:
        h1 = pygame.image.load('/Users/sarang_hadagali/Code/Personal_Projects/Python/Pygame/Hangman/HangmanStand4.png')
    elif wrongCount == 5:
        h1 = pygame.image.load('/Users/sarang_hadagali/Code/Personal_Projects/Python/Pygame/Hangman/HangmanStand5.png')
    elif wrongCount == 6:
        h1 = pygame.image.load('/Users/sarang_hadagali/Code/Personal_Projects/Python/Pygame/Hangman/HangmanStand6.png')
        string = inputWord
        correct = Button(string,(400,50),(0,255,255),[0,0],32)
        correct.show()
        startStop()
    screen.blit(h1,(-200,-50))

def showButtons():
    for btn in myList:
        btn.show()

def gameLoop(input):
    running = True
    wordBank = ''
    correct = []
    wrong = []
    wrongCounter = 0
    while running:
        screen.fill((0,255,255))
        input = input.upper()
        showButtons()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if wordBank == '':
                    wordBank = ButtonA.click()
                if wordBank == '':
                    wordBank = ButtonB.click()
                if wordBank == '':
                    wordBank = ButtonC.click()
                if wordBank == '':
                    wordBank = ButtonD.click()
                if wordBank == '':
                    wordBank = ButtonE.click()
                if wordBank == '':
                    wordBank = ButtonF.click()
                if wordBank == '':
                    wordBank = ButtonG.click()
                if wordBank == '':
                    wordBank = ButtonH.click()
                if wordBank == '':
                    wordBank = ButtonI.click()
                if wordBank == '':
                    wordBank = ButtonJ.click()
                if wordBank == '':
                    wordBank = ButtonK.click()
                if wordBank == '':
                    wordBank = ButtonL.click()
                if wordBank == '':
                    wordBank = ButtonM.click()
                if wordBank == '':
                    wordBank = ButtonN.click()
                if wordBank == '':
                    wordBank = ButtonO.click()
                if wordBank == '':
                    wordBank = ButtonP.click()
                if wordBank == '':
                    wordBank = ButtonQ.click()
                if wordBank == '':
                    wordBank = ButtonR.click()
                if wordBank == '':
                    wordBank = ButtonS.click()
                if wordBank == '':
                    wordBank = ButtonT.click()
                if wordBank == '':
                    wordBank = ButtonU.click()
                if wordBank == '':
                    wordBank = ButtonV.click()
                if wordBank == '':
                    wordBank = ButtonW.click()
                if wordBank == '':
                    wordBank = ButtonX.click()
                if wordBank == '':
                    wordBank = ButtonY.click()
                if wordBank == '':
                    wordBank = ButtonZ.click()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    wordBank = 'a'
                    ButtonA.isClicked = True
                if event.key == pygame.K_b:
                    wordBank = 'b'
                if event.key == pygame.K_c:
                    wordBank = 'c'
                if event.key == pygame.K_d:
                    wordBank = 'd'
                if event.key == pygame.K_e:
                    wordBank = 'e'
                if event.key == pygame.K_f:
                    wordBank = 'f'
                if event.key == pygame.K_g:
                    wordBank = 'g'
                if event.key == pygame.K_h:
                    wordBank = 'h'
                if event.key == pygame.K_i:
                    wordBank = 'i'
                if event.key == pygame.K_j:
                    wordBank = 'j'
                if event.key == pygame.K_k:
                    wordBank = 'k'
                if event.key == pygame.K_l:
                    wordBank = 'l'
                if event.key == pygame.K_m:
                    wordBank = 'm'
                if event.key == pygame.K_n:
                    wordBank = 'n'
                if event.key == pygame.K_o:
                    wordBank = 'o'
                if event.key == pygame.K_p:
                    wordBank = 'p'
                if event.key == pygame.K_q:
                    wordBank = 'q'
                if event.key == pygame.K_r:
                    wordBank = 'r'
                if event.key == pygame.K_s:
                    wordBank = 's'
                if event.key == pygame.K_t:
                    wordBank = 't'
                if event.key == pygame.K_u:
                    wordBank = 'u'
                if event.key == pygame.K_v:
                    wordBank = 'v'
                if event.key == pygame.K_w:
                    wordBank = 'w'
                if event.key == pygame.K_x:
                    wordBank = 'x'
                if event.key == pygame.K_y:
                    wordBank = 'y'
                if event.key == pygame.K_z:
                    wordBank = 'z'
            wordBank = wordBank.upper()
            if wordBank in input and wordBank not in correct:
                correct.append(wordBank)
            elif wordBank not in input and wordBank not in wrong:
                wrong.append(wordBank)
                wrongCounter += 1
        drawLetters(input,correct)
        drawLines(input)
        showWrong(wrongCounter,input)
        wordBank = ''
        pygame.display.update()
loadingScreen()
    


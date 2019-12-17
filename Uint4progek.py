Points = 0
import random#this is to radomises all of the qustiond
List = [0,1,2,3,4,5,6,7,8,9]
random.shuffle(List)
Userinput = input("What Catagory 1 Memes or 2 Pop Culter")
if Userinput == "1":
    file = open('set1.txt', "r+")
    file2 = open('set1answers.txt', "r")
else: #This is beacuse if it not one then it 2 so you will open other file
     file = open('Set2.txt', "r+")#this opens the file so it reads out the text from the file
     file2 = open('set2answers.txt', "r")
Memes = file.readlines()
Memesanswers = file2.readlines()#this is to read the lines
for m in List:
    usersinput = input(Memes[m])
    if usersinput.lower() == Memesanswers[m].strip().lower():#this is just a point system to set up points
        print("Corect")
        Points = Points +1
    else:
        print("Wrong")
print("You got this many right:")
print(Points)
file = open("highscore.txt", "r")
data = int(file.read().strip())
file.close()
if Points > data:
    file = open("highscore.txt", "w")#this is so it writes out your new high score 
    file.write (str(Points))
    print("new high score")












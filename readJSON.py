from cgitb import small
import pandas as pd # library for data analysis
import requests # library to handle requests
from bs4 import BeautifulSoup # library to parse HTML documents
import wikipedia
import lxml
import re
import os
import json
from googleapiclient.discovery import build
from copy import deepcopy
import webbrowser


os.chdir("E:/Semester/2022W/SI 507/HW/Final Project")

yes_list=["yes","yup","y","sure"]

id=['Labrador_Retriever','German_Shepherd','Golden_Retriever','French_Bulldog','Poodles',
    'Beagles','Rottweilers','Dachshunds','Yorkshire_Terrier','Boxers','Australian_Shepherd',
    'Siberian_Husky','Cavalier_King_Charles_Spaniel','Great_Dane','Miniature_Schnauzer',
    'Doberman_Pincher','Shih_Tzu','Afghan_Hound', 'Affenpinscher', 'Pomeranian_dog', 'Papillon_dog',
    'Saluki', 'Vizsla','Tazy','Toy_Fox_Terrier',"Leonberger",'Maltese_dog']

name=['Labrador Retriever','German Shepherd','Golden Retriever','French Bulldog','Poodles',
    'Beagles','Rottweilers','Dachshunds','Yorkshire Terrier','Boxers','Australian Shepherd',
    'Siberian Husky','Cavalier King Charles Spaniel','Great Dane','Miniature Schnauzer',
    'Doberman Pincher','Shih Tzu','Afghan Hound', 'Affenpinscher', 'Pomeranian', 'Papillon',
    'Saluki', 'Vizsla', 'Tazy','Toy Fox Terrier','Leonberger','Maltese']

size=["big", "big", "big", "small", "small",
   "small","big","small","small","small","small","big",
    "small","big","small","big","small", "big", "small", "small", "small",
    "big", "big", "big", "small", "big",'small']

# Read dogsInfo JSON file to dict
with open('tree.json') as json_file:
    dogsInfo = json.load(json_file)


class Dogs:
    """
    Create class structure
    """
    def __init__(self, json):
        self.name=json["name"]
        self.summary=json["summary"]
        self.origin=json["origin"]
        self.weight=json["weight"]
        self.height=json["height"]
        self.colour=json["colour"]
        self.lifeSpan=json["lifeSpan"]
        self.size=json["size"]
        self.urls=json["urls"]
        self.titles=json["titles"]
        self.descriptions=json["descriptions"]
        self.question=None

dogsClass=[]
for k in dogsInfo.keys():
    dogsClass.append(Dogs(dogsInfo[k]))


# Divide Dogs Class Data According to Tree Structure in Next Step

bigDogs=[]
EUbigDogs=[]
NonEUbigDogs=[]

smallDogs=[]
EUsmallDogs=[]
NonEUsmallDogs=[]

def bigDog(dogs,listA,listB):
    """
    Divide list of dogs class objects into big dogs and small dogs according to their size attribute.
    dogs: full list of class objects
    listA: Big dogs list of class objects
    listB: Small dogs list of class objects
    """
    new_dogs=deepcopy(dogs)
    for x in range(len(new_dogs)):
        new_dogs[x].question = "Do you prefer big dogs than small dogs?"
        if new_dogs[x].size == "big":
            listA.append(new_dogs[x])
            x += 1
        else: 
            listB.append(new_dogs[x])
            x += 1

def EuropeDog(dogs,listA,listB):
    """
    Divide list of dogs class objects into European dogs and Non-European dogs according to their origin attribute.
    dogs: full list of class objects
    listA: European dogs list of class objects
    listB: Non-European dogs list of class objects
    """
    new_dogs=deepcopy(dogs)
    for x in range(len(new_dogs)):
        new_dogs[x].question = "Do you prefer dogs originated from Europe?"
        if "Germany" in dogs[x].origin or "France" in dogs[x].origin:
            listA.append(new_dogs[x])
            x += 1
        else: 
            listB.append(new_dogs[x])
            x += 1


bigDog(dogsClass,bigDogs,smallDogs)
EuropeDog(bigDogs,EUbigDogs,NonEUbigDogs)
EuropeDog(smallDogs,EUsmallDogs,NonEUsmallDogs)

# Create Tree Structure and Insert Data
class Node:
    """
    Create tree structure
    """
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert_left(self, child):
        if self.left == None:
            self.left = child
        else:
            child.left = self.left
            self.left = child

    def insert_right(self, child):
        if self.right == None:
            self.right = child
        else:
            child.right = self.right
            self.right = child

    def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print(self.data)
      if self.right:
         self.right.PrintTree()

root = Node(None)
BigDogs=Node(bigDogs)
SmallDogs=Node(smallDogs)

root.insert_left(BigDogs)
BigDogs.insert_left(Node(EUbigDogs))
BigDogs.insert_right(Node(NonEUbigDogs))

root.insert_right(SmallDogs)
SmallDogs.insert_left(Node(EUsmallDogs))
SmallDogs.insert_right(Node(NonEUsmallDogs))

#len(dogsInfo)
#len(BigDogs.val)
#len(SmallDogs.val)


# Program

def printNodes(tree):
    """
    Print the recommended dogs breed names
    tree: binary search result, tree structure
    """
    print("I select several dogs breeds for you: ")
    for i in range(len(tree.val)):
        print(i+1, tree.val[i].name)
        i += 1

def chooseOneDog(tree):
    """
    From the recommended dogs list, choose one to look at details and videos.
    tree: binary search result, tree structure
    """
    q = input("Please choose a dog with more specific information by typing the index: ")
    q = int(q)-1
    print("The dog you selected is: ", tree.val[q].name, ", and a summary is as below")
    print(tree.val[q].summary)
    print("The other information about this dog are as below: ", tree.val[q].weight, tree.val[q].height, tree.val[q].colour, tree.val[q].size, tree.val[q].lifeSpan, tree.val[q].origin)
    p = input("Do you want to see related videos on YouTube?")
    if p in yes_list:
        print("The videos are sorted by popularity: ")
        for i in range(len(tree.val[q].urls)):
            print(i, tree.val[q].titles[i],tree.val[q].urls[i])
        d = input("Type an index to see description of the video. Or type 'No' to leave")

        if d == "No": pass
        else: 
            d = int(d)
            print(tree.val[q].descriptions[i])
            k = input("Do you want to open the video in browser?")
            if k in yes_list:
                webbrowser.open(tree.val[q].urls[d])
            else:pass

    else: pass

def search(tree):
    """
    Binary search in the dogs data.
    tree: dogs data of class objects, tree structure
    """
    while tree.left != None:
        answer=input(tree.left.val[0].question)
        if answer in yes_list:
            return search(tree.left)
        else: return search(tree.right)

    else: 
        printNodes(tree)
        chooseOneDog(tree)

def play(tree):
    """
    Take the quiz to find recommended dogs, look at more detailed information and videos.
    tree: dogs data of class objects, tree structure
    """
    search(tree)
    replay = input("Do you want to find a new dog?")
    if replay in yes_list:
        play(tree)
    else: print("Bye!")



def main():
    play(root)



if __name__ == '__main__':
    main()



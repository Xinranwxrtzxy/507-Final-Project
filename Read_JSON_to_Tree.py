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
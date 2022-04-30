# 507-Final-Project
Binary Search Tree: Find Your Ideal Dog

## Required Packages
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

## How to Obtain YouTube API Key
Refered to Pedro Hernández(https://medium.com/mcd-unison/youtube-data-api-v3-in-python-tutorial-with-examples-e829a25d2ebd)
API Documentation: https://developers.google.com/youtube/v3/getting-started?hl=en_US 

First of all, you need to have a Google account. If you do not have it, you can register at https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp.
Once you have signed up, you need to go to Google Cloud Platform at https://cloud.google.com/.

Then, you must create a new project. Click on Select a project tab near the upper left corner, and then click on NEW PROJECT.
You will be redirected to the New Project page. Name your project, for example as YouTube Data Extraction and click on CREATE.
After that, you will be redirected to the project’s dashboard. Note the Select a project tab now has the project name written on it, than means you have the YouTube Data Extraction project selected. In case you have more projects, you can select them from this tab.

Now, you need to enable the API in this project. Click on Explore and enable APIs option within Getting Started card in the lower left corner of the dashboard.
After that, you will be redirected to APIs & Services page. Here, click on + ENABLE APIS AND SERVICES at the top of the page.
Then, you will be redirected to the API Library. Scroll down a little bit the options and you will find YouTube’s APIs. For the purposes of this article, you only need the one named YouTube Data API v3, so click on it.
Next, you will be redirected to the API Overview page. At the top you will see the message “To use this API, you may need credentials. Click ‘Create credentials’ to get started”. Click on CREATE CREDENTIALS at the top right corner of the page.
The Create credentials form will be shown. Select YouTube Data API v3 in the Select an API dropdown menu and check the Public data radio button, then click on NEXT.

Finally, your API key will be displayed. This key is mandatory in order to use the API in your programs.
You can always check the key from the Credentials screen. You can access this screen from the hamburger menu at the top left corner of the Google Cloud Platform interface.

## How to install Google API Python Client Library

To perform this installation you just need to type a single instruction in the command line:

    pip install google-api-python-client  
  
## How to use api key

After getting the api key, you need to change the value of **api_key** in **Final_project_full.py** to your key value.

    api_key = "your_key_value"
    
## Data Structure

The variables **id**, **name**, and **size** are set by users. 
**id** refers to the strings after "https://www.youtube.com/watch?v=" in Wikipedia page of a dog.
**name** refers to the name of a dog breed.
**size** refers to the size of dog.
You can add name, id and size of a dog to these three lists to include the new dog in the data.

The data are stored as class objects in a binary tree structure in **tree.json** file.
The class structure named Dogs has 12 attributes: **name, summary, origin, height, weight, lifeSpan, color, size, urls, titles, descriptions, question**. 
The first eight attributes are used to store data collected from Wikipedia.
Each class object has 25 elements for urls, title, description and each one is information about one video of that class object using YouTube API. 
Another attribute question is used to store question that will ask the user to choose between two leaves of a node in next step. 
The first node divides 27 dog breeds into 12 big dogs (left leaf) and 15 small dogs (right leaf). 
The big dog’s node has 5 dogs from Europe as left leaf and 7 dogs from other places as right leaf. 
The small dogs’ node has 7 dogs from Europe as left leaf and 5 dogs from other places as right leaf. 

## Program and Data File

To read json file into tree structure and run the program, run **readJSON.py** with data file **tree.json**.

To access the data using YouTube and Wikipedia API, create data strcture, and run the program, run **Final_project_full.py**

## How to Interact with the Program

1.	The program helps user to find out what breed of dog fit them well by answering several questions. There are two questions in sequence: “Do you prefer big dogs than small dogs?” and “Do you prefer dogs originally from Europe or other places?” User can type yes or no to answer the question.
2.	After typing the answer to both questions, the user will be provided with names of dog breeds recommended for them.
3.	They will be able to explore more detailed information of a specific dog breed among these dogs. They can type index to choose a dog and view the summary, body size statistics, origin, colour, and life span. 
4.	Then the system asks if they want to see videos of this dog on YouTube. If yes, they will be provided with a list of titles of popular dog videos of this breed at first. Then they can type the index of video to see descriptions and urls. They are able to further choose to open the url in browser. 
5.	After that, the users are asked if they want to choose a new dog by answering the two questions again. If no, the program will end.

**Demo Video Link: https://youtu.be/TOo-ll4ITec**

import pandas as pd # library for data analysis
import requests # library to handle requests
from bs4 import BeautifulSoup # library to parse HTML documents
import wikipedia
import lxml
import re
import os
import json
from googleapiclient.discovery import build

os.chdir("E:/Semester/2022W/SI 507/HW/Final Project")

id=['Labrador_Retriever','German_Shepherd','Golden_Retriever','French_Bulldog','Poodles',
    'Beagles','Rottweilers','Dachshunds','Yorkshire_Terrier','Boxers','Australian_Shepherd',
    'Siberian_Husky','Cavalier_King_Charles_Spaniel','Great_Dane','Miniature_Schnauzer',
    'Doberman_Pincher','Shih_Tzu']

name=['Labrador Retriever','German Shepherd','Golden Retriever','French Bulldog','Poodles',
    'Beagles','Rottweilers','Dachshunds','Yorkshire Terrier','Boxers','Australian Shepherd',
    'Siberian Husky','Cavalier King Charles Spaniel','Great Dane','Miniature Schnauzer',
    'Doberman Pincher','Shih Tzu']

# size=["big", "big", "big", "small", "small",
#   "small","big","small","small","small","small","big",
#    "small","big","small","big","small"]

# Access videos information using Youtube api v3
api_key = "AIzaSyDQq1dTXTknBa8dgolJgtF45F_CY_gBVCQ"
youtube = build('youtube','v3',developerKey=api_key)
YTB_lists=[]
all_YTBurls=[]
def getYTB(name):
    for n in name:
        req = youtube.search().list(q=n,part='snippet',type="video",maxResults=25, order="viewCount")
        res = req.execute()
        YTB_lists.append(res["items"])

getYTB(name)

# Write urls to JSON file
json_string = json.dumps(YTB_lists)
with open("YTBurls.json", "w") as outfile:
    outfile.write(json_string)

# Extract useful infomation from YTB data

def getYTBurls(name):
    for n in name:
        req = youtube.search().list(q=n,part='snippet',type="video",maxResults=25, order="viewCount")
        res = req.execute()
        video_url_list=[]
        for i in range(len(res["items"])):
            id=res["items"][i]["id"]['videoId']
            video_url="https://www.youtube.com/watch?v="+ id
            video_url_list.append(video_url)
        all_YTBurls.append(video_url_list)

        

# Get Information of wikipages using API and Web scraping
url=[]
summary=[]
def getUrlSummary(id_list):
    """
    Get Summary and url of wikipage using Wiki API
    """
    for i in id_list:
        wikiurl="https://en.wikipedia.org/wiki/"+ i
        summary.append(wikipedia.summary(i,auto_suggest=False))
        url.append(wikiurl)
getUrlSummary(id)

summary_dict = {name[i]: summary[i] for i in range(len(name))}
url_dict= {name[i]: url[i] for i in range(len(name))}

origin=[]
height=[]
weight=[]
colour=[]
lifespan=[]

def getInfo(url_dict):
    """
    Get Specific Informations from Wiki using Web Scraping
    """
    for key in url_dict:
        response=requests.get(url_dict[key])
        soup=BeautifulSoup(response.content,"html.parser")
        indiatable=soup.find('table',{'class':"infobox"})
        df=pd.read_html(str(indiatable))
        # convert list to dataframe
        df=pd.DataFrame(df[0])
        
        df_o=df[df.iloc[:,0]=="Origin"]
        df_h=df[df.iloc[:,0]=="Height"]
        df_w=df[df.iloc[:,0]=="Weight"]
        df_c=df[df.iloc[:,0]=="Colour"]
        df_l=df[df.iloc[:,0]=='Life\xa0span']

        df_o=pd.Series.to_string(df_o.iloc[:,1])
        df_h=pd.Series.to_string(df_h.iloc[:,1])
        df_w=pd.Series.to_string(df_w.iloc[:,1])
        df_c=pd.Series.to_string(df_c.iloc[:,1])
        df_l=pd.Series.to_string(df_l.iloc[:,1])
        
        origin.append(df_o)
        height.append(df_h)
        weight.append(df_w)
        colour.append(df_c)
        lifespan.append(df_l)

getInfo(url_dict)

# Clean data

def cleanData(data,newdata):   
    for i in data:
        x = re.sub("^\d.+(Dogs)","",i)
        x = re.sub("(Series).+","",x)
        x = re.sub("\d+\s\s+" , "", x)
        newdata.append(x)

newweight=[]
newheight=[]
newcolour=[]
newlifespan=[]
cleanData(weight,newweight)
cleanData(height,newheight)
cleanData(colour,newcolour)
cleanData(lifespan,newlifespan)

origin_dict= {name[i]: origin[i] for i in range(len(name))}
weight_dict= {name[i]: newweight[i] for i in range(len(name))}
height_dict= {name[i]: newheight[i] for i in range(len(name))}
colour_dict= {name[i]: newcolour[i] for i in range(len(name))}
lifeSpan_dict={name[i]: newlifespan[i] for i in range(len(name))}

# Create Tree structure

class Node:

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
      print( self.data),
      if self.right:
         self.right.PrintTree()

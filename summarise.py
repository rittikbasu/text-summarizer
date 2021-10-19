import bs4
import urllib.request as url
import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk import sent_tokenize
from nltk.corpus import stopwords
from nltk import word_tokenize
stop_word = stopwords.words('english')
import string
import heapq

def geturl(url_name,numofsentences):
  web = url.urlopen(url_name)
  try:
    page = bs4.BeautifulSoup(web,'html.parser')
    elements = page.find_all('p')
    if len(elements)==0:
      summary = "Sorry this site couldn't be summarised."
      return summary
    else:
      article = ''
      for i in elements:
        article+= (i.text)
      summary = process(article,numofsentences)
      return summary
  except:
      summary = "Please enter a valid Url"

def process(article,numofsentences):
  processed = article.replace(r'^\s+|\s+?$','')
  processed = processed.replace('\n',' ')

  processed = processed.replace("\\",'')
  processed = processed.replace(",",'')
  processed = processed.replace('"','')
  processed = re.sub(r'\[[0-9]*\]','',processed)

  sentences = sent_tokenize(processed)
  
  frequency = {}

  processed1 = processed.lower()

  for word in word_tokenize(processed1):

    if word not in stop_word and word not in string.punctuation:

        if word not in frequency.keys():

            frequency[word]=1

        else:

            frequency[word]+=1

  max_fre = max(frequency.values())
  
  for word in frequency.keys():

    frequency[word]=(frequency[word]/max_fre)

  frequency
  sentence_score = {}


  for sent in sentences:

    for word in word_tokenize(sent):

      if word in frequency.keys():

        if len(sent.split(' '))<30:

            if sent not in sentence_score.keys():

              sentence_score[sent] = frequency[word]

            else:
              sentence_score[sent]+=frequency[word]
  sentence_score

  summary = heapq.nlargest(numofsentences,sentence_score,key = sentence_score.get)

  summary = ' '.join(summary)

  return summary
S

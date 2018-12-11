# Copyright 2016 Xinyi Wang All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import math, os, pickle, re

class Bayes_Classifier:

   def __init__(self, trainDirectory = "movie_reviews/"):
      '''This method initializes and trains the Naive Bayes Sentiment Classifier.  If a 
      cache of a trained classifier has been stored, it loads this cache.  Otherwise, 
      the system will proceed through training.  After running this method, the classifier 
      is ready to classify input text.'''
      self.p_word = {}
      self.n_word = {}
      p_file = "/Users/wangxinyi/Desktop/artificial intelligence/bayes/positive.txt"
      n_file = "/Users/wangxinyi/Desktop/artificial intelligence/bayes/negative.txt"
      if os.path.exists(p_file) and os.path.exists(n_file):
          self.p_word = self.load(p_file)
          self.n_word = self.load(n_file)
      else:
          self.train()

   def train(self):   
      '''Trains the Naive Bayes Sentiment Classifier.'''
      lFileList = []
      for fFileObj in os.walk("/Users/wangxinyi/Desktop/artificial intelligence/bayes/movies_reviews/"):
          lFileList = fFileObj[2]
          break

      strlist=[]
      p_label=[]
      n_label=[]
      for i in range(len(lFileList)):
          strlist.append(lFileList[i].split('-'))
          if strlist[i][1] == '1':
              n_label.append(lFileList[i])
          if strlist[i][1] == '5':
              p_label.append(lFileList[i])
                    
      p_word = {}
      n_word = {}

      for i in lFileList:
          content = bc.loadFile("/Users/wangxinyi/Desktop/artificial intelligence/bayes/movies_reviews/"+i)
          word = self.tokenize(content)
          if i in p_label:
              for j in word:
                  if j in p_word.keys():
                      p_word[j] += 1
                  else: 
                      p_word[j] = 1
                    
              
                      
          if i in n_label:
          #    n_sum += len(word)
              for j in word:
                  if j in n_word.keys():
                      n_word[j] += 1 
                  else: 
                      n_word[j] = 1
      self.save(p_word,"/Users/wangxinyi/Desktop/artificial intelligence/bayes/positive.txt")
      self.save(n_word,"/Users/wangxinyi/Desktop/artificial intelligence/bayes/negative.txt")
       

    
   def classify(self, sText):
      '''Given a target string sText, this function returns the most likely document
      class to which the target string belongs. This function should return one of three
      strings: "positive", "negative" or "neutral".
      '''
     # self.__init__()
      lFileList = []
      for fFileObj in os.walk("/Users/wangxinyi/Desktop/artificial intelligence/bayes/movies_reviews/"):
          lFileList = fFileObj[2]
          break
      
      strlist=[]
      p_num = 0
      n_num = 0
      for i in range(len(lFileList)):
          strlist.append(lFileList[i].split('-'))
          if strlist[i][1] == '1':
              n_num += 1
          if strlist[i][1] == '5':
              p_num += 1
      
      p_p = p_num/len(lFileList) 
      p_n = n_num/len(lFileList)       
      
      word = self.tokenize(sText)
      prior_p = 1
      prior_n = 1
      
      
      p_all = 0
      n_all = 0
      for i in self.p_word.keys():
          p_all += self.p_word[i]
      for i in self.n_word.keys():
          n_all += self.n_word[i]
          
          
      a = 0
      b = 0
      num_notin_p = 0
      num_notin_n = 0

      
      for i in word:
          if i not in self.p_word.keys():
              num_notin_p += 1
          if i not in self.n_word.keys():
              num_notin_n += 1
      
      for i in word:
          if i in self.p_word.keys():
              a = self.p_word[i]
          else:
              a = 0
          prior_p += math.log((a+1)/(p_all + len(self.p_word) +num_notin_p))
          
          
          if i in self.n_word.keys():
              b = self.n_word[i]
          else:
              b = 0
          prior_n += math.log((b+1)/(n_all + len(self.n_word) +num_notin_n))
 
              
      pos_p = math.log(p_p) + prior_p
      pos_n = math.log(p_n) + prior_n
     
      if pos_p > pos_n:
          return "positive"
      elif pos_p < pos_n:
          return 'negative'
      elif pos_p == pos_n:
          return 'neutral'
      
   def loadFile(self, sFilename):
      '''Given a file name, return the contents of the file as a string.'''

      f = open(sFilename, "r")
      sTxt = f.read()
      f.close()
      return sTxt
   
   def save(self, dObj, sFilename):
      '''Given an object and a file name, write the object to the file using pickle.'''

      f = open(sFilename, "wb")
      p = pickle.Pickler(f)
      p.dump(dObj)
      f.close()
   
   def load(self, sFilename):
      '''Given a file name, load and return the object stored in the file.'''

      f = open(sFilename, "rb")
      u = pickle.Unpickler(f)
      dObj = u.load()
      f.close()
      return dObj

   def tokenize(self, sText): 
      '''Given a string of text sText, returns a list of the individual tokens that 
      occur in that string (in order).'''

      lTokens = []
      sToken = ""
      for c in sText:
         if re.match("[a-zA-Z0-9]", str(c)) != None or c == "\'" or c == "_" or c == '-':
            sToken += c
         else:
            if sToken != "":
               lTokens.append(sToken)
               sToken = ""
            if c.strip() != "":
               lTokens.append(str(c.strip()))
               
      if sToken != "":
         lTokens.append(sToken)

      return lTokens


bc=Bayes_Classifier()
path="/Users/wangxinyi/Desktop/artificial intelligence/bayes/movies_reviews/movies-1-102.txt"
a=bc.loadFile(path)
b=bc.tokenize(a)
#print(b)
bc.train()
bc.classify("I love my AI class!")




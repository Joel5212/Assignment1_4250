#-------------------------------------------------------------------------
# AUTHOR: Joel Joshy
# FILENAME: Assignment1
# SPECIFICATION: Building term matrix of 3 documents
# FOR: CS 4250- Assignment #1
# TIME SPENT: 90 minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#Importing some Python libraries
import csv

import math

documents = []

#Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0])

#Conducting stopword removal. Hint: use a set to define your stopwords.
#--> add your Python code here
stopWords = {"I", "and", "She", "her", "They", "their"}
documentsAfterStopWordRemoval = []

for doc in documents:
    newDocument = ""
    for word in doc.split():
        if word not in stopWords:
            newDocument = newDocument + " " + word
    documentsAfterStopWordRemoval.append(newDocument.strip())

print("Documents After Stop Word Removal:")            
print(documentsAfterStopWordRemoval) 
print("")       

#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
#--> add your Python code here
stemming = {
    "loves": "love",
    "cats": "cat",
    "dogs": "dog"
}
documentsAfterStemming = []

for doc in documentsAfterStopWordRemoval:
    newDocument = ""
    for word in doc.split():
        if word in stemming:
            newDocument = newDocument + " " + stemming.get(word)
        else:
            newDocument = newDocument + " " + word
    documentsAfterStemming.append(newDocument.strip())

print("Documents After Stemming:")
print(documentsAfterStemming)   
print()


#Identifying the index terms.
#--> add your Python code here
terms = []

for doc in documentsAfterStemming:
    for word in doc.split():
        if word not in terms:
          terms.append(word)
 
print("Index Terms:")
print(terms)   
print()

#Building the document-term matrix by using the tf-idf weights.
#--> add your Python code here
docTermMatrix = []

for doc in documentsAfterStemming:
  wordsInDocument = doc.split()
  docTermMatrixRow = []
  for term in terms:
      tf = doc.count(term) / len(wordsInDocument)
      df = sum(1 for doc in documents if term in doc)
      idf = math.log10(len(documents)/df)
      tfidf = tf*idf
      docTermMatrixRow.append(tfidf)
  docTermMatrix.append(docTermMatrixRow)

#Printing the document-term matrix.
#--> add your Python code here
print("Document Term Matrix: ")
print(docTermMatrix)

# The Unredactor
we will try to predict the redacted names in the document

Whenever sensitive information is shared with the public, the data must go through a redaction process. That is, all sensitive names, places, and other sensitive information must be hidden. Documents such as police reports, court transcripts, and hospital records all containing sensitive information. Redacting this information is often expensive and time consuming. I have already done the redaction phrase in my previous project, you can check that before going through this project of unredaction.

As part of phase 2, we will be creating the Unredactor. The unredactor will take a redacted document and the redaction flag as input, in return it will give the most likely candidates to fill in the redacted location. In this project my unredactor only unredacts names, you may extend it to other entities. To predict the name we will have to solve the Entity Resolution problem.

As you can guess, discovering names is not easy. To discover the best names, we will have to train a model to help us predict missing words. For this assignment, we will use the Large Movie Review Data Set.
link for the dataset: http://ai.stanford.edu/~amaas/data/sentiment/ 
This is a data set of movie reviews from IMDB containing. The initial goal of the data set is to discover the sentiment of each review. For this project, we will only use the reviews for their textual content.

----
Project Source can viewed from  https://oudalab.github.io/textanalytics/projects/project2
----
-------------
Author 
---
**Venkata Subbaraju Sagi**

All known Bugs and fixes can be sent to subbaraju.v@ou.edu

Packages required for the project : nltk, DictVectorizer, numpy, sent_tokenize, word_tokenize,ne_chunk

-------
Platform used
---
I have used Sypder IDE for running the python code, you will have to change the location of the files, which you would like to train and test upon,  I will explain the function shortly.


---

Description of Functions Used
---
I have divided the complete code into three sections, first section takes all text files from test folder and trains our model,
Second section is for getting the names from the test folder.
Third section redacts the test folder data, and we predict the names that are redacted using the model from first section.

Functions

Section 1:


1 . **doextraction(glob_text):**

The function doextraction(glob_text), uses glob to extract all the text files present in the given folder. It takes the folder location as input.once a file is extracted we open it read mode and pass that file to get_entity(text) funcion. we call get_entity function inside this function which return us complete dictonary of features.


 2 .  **get_entity(text)**

The function get_entity(text) takes the texted file that is open in read mode. once the text file is passed, we tokenize the text and try to get all the the 'Person' entities from this text file.

our main intention is to train our model using the dataset, so we need to extract features that we will be using to train our classification model.

I have extracted following features:
```
i) total names in the document
ii)Length of each name
iii)spaces beween names
iv)total word count in the document
```

one we extract all the features, I have created a list of dictonaries, where each dictonary has all features along with the name associate with it, and the list containes dictonaries of the names we extract from the text files.
we return these entites


3 . **createdb()*

Note, all the columns correspond directly to the columns in the arrest pdfs. The arrest address contains information from the arrestee address, city, state, and zip code. 


4 . **populatedb**
The function populatedb(db, incidents) function takes the rows created in the extractincidents() function and adds it to the normanpd.db database.


5 . **status(db)**

The status(db) function prints to standard out, a random row from the database

----
How To run this 
--


---

List of external links that I used for help
--


-------
**Assumptions/Bugs**
--

```
I have assumed that the page have only 12 columns, out of which the data is missing only from columns 7,8,9. If there is a missing value in different column or number of columns are more than 12 the code might not give desired results.

To clean the data and to get desired formatting, you will see me using hard coding in some cases, like combing multi lined string values and removing space in between them, and adding some special characters and split the text using that character. So the code can handle only those cases.

The code requires manual input from the user, failing to give that might not give you any output, so I assume you know that condition.
```
------

***   Thankyou for checking ,Hope this help you in your work!***


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

The function doextraction(glob_text), uses glob to extract all the text files present in the given folder. It takes the folder location as input.once a file is extracted we open it read mode and pass that file to get_entity(text) function. We call get_entity function inside this function which return us complete dictonary of features.


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

one we extract all the features, I have created a list of dictionaries, where each dictionary has all features along with the name associate with it, and the list containes dictonaries of the names we extract from the text files.
We return these entites and actual names from this function.

Once we have these functions ready, we seperate our entities in to feature vector and target vector, to make it ready for training.

Since my feature vector is a dictionary, I have used DictVecorizer package to convert this into vectors.

```
DV = DictVectorizer(sparse = False)  
    
feature_array = DV.fit_transform(feature_array
```
After the conversion, I have trained the dataset with GuassianNaivebaise classifier, 
```

from sklearn.naive_bayes import GaussianNB
classifier2 = GaussianNB()
classifier2.fit(feature_array, target_variable)

```
This classification model will be used while we try to predict the names in the redacted document.

I have combined the redaction of names in the document and extracting features from the redacted document in the same function, which covers our section two and three.

Section 2 and Section 3

3 . **doextraction_test(glob_text):**
It is similar to the doextraction(glob_text) function, it does similar function.



4 . **get_entity_test(text):**
The function is caled inside doextraction_test(glob_text), we pass each text file into it. once we pass firstly the person names are redacted in the documnet, and we use regex to extract the redacted names. Once we have these names we try to get features from these redacted names. Main point here is to check that you extract the same features which you used for training. Once features are extracted we return these features.

we call the function by passing test data text files, which gives us features associated with the test data.

so now we have the features from our test set, we use DictVectorization again on this and pass that feature matrix into our model and predict the names.


```
predicted_names = loaded_model.predict(feature_array_test)
```
List of external links that I used for help
--

https://www.digitalocean.com/community/tutorials/how-to-handle-plain-text-files-in-python-3 # understanding the basics of text file
https://stackoverflow.com/questions/35672809/how-to-read-a-list-of-txt-files-in-a-folder-in-python #used for taking all text files in the current folder
https://docs.python.org/2/library/logging.html
https://medium.com/@acrosson/extracting-names-emails-and-phone-numbers-5d576354baa #extracting the data and facing issues for installing required packages
https://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7da
https://stackoverflow.com/questions/31088509/identifying-dates-in-strings-using-nltk
https://stackoverflow.com/questions/3868753/find-phone-numbers-in-python-script?utm_source=zapier.com&utm_medium=referral&utm_campaign=zapier # for finding phone numbers
https://www.geeksforgeeks.org/get-synonymsantonyms-nltk-wordnet-python/

-------
**Assumptions/Bugs**
--

```
1) while extracting the redacted names I have used following regex, 

\█+\s?\██\s?\█+\D█+

which could not to extract all the redacted names.

Due to this non extraction:
The total names are different than the extracted redacted names, which will make it difficult to compare the predicted results with actual results.This is a bug in the code I have provided.

2)I have assumed that 4 features which I have discussed earlier gives us better results.
So I have choosen only those 4 features but we can always add other features.

3)I am assuming you will be running the program in your local machine.
I assume that you will can give the text file location directly.

4) Predicted names are too far from the actual names, But since my idea is to check the model working I convinced myself on it.

5)I am not saving the redacted files in any location, I have shown the process in my previous project, you can check that if you desire to save your redacted files.

```

***   Thankyou for checking ,Hope this help you in your work!***


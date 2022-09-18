# Voice-analysis-for-emotion-recognition-using-deep-learning-and-machine-learning
Emotion recognition system ( voice) and export api
This project presents a deep learning classifier able to predict the emotions of a human speaker encoded in an audio file. The classifier is trained using 2 different datasets, RAVDESS and TESS, and has an overall F1 score of 83% on 8 classes (neutral, calm, happy, sad, angry, fearful, disgust and surprised).

*gathering datasets*dataset**
- the [Ryerson Audio-Visual Database of Emotional Speech and Song (RAVDESS) dataset](https://zenodo.org/record/1188976#.XsAXemgzaUk) 
- the [Toronto emotional speech set (TESS) dataset](https://tspace.library.utoronto.ca/handle/1807/24487) 

The samples include: 

- 1440 speech files and 1012 Song files from **RAVDESS**. This dataset includes recordings of 24 professional actors (12 female, 12 male), vocalizing two lexically-matched statements in a neutral North American accent. Speech includes calm, happy, sad, angry, fearful, surprise, and disgust expressions, and song contains calm, happy, sad, angry, and fearful emotions. Each file was rated 10 times on emotional validity, intensity, and genuineness. Ratings were provided by 247 individuals who were characteristic of untrained adult research participants from North America. A further set of 72 participants provided test-retest data. High levels of emotional validity, interrater reliability, and test-retest intrarater reliability were reported. Validation data is open-access,

- 2800 files from **TESS**. A set of 200 target words were spoken in the carrier phrase "Say the word _____' by two actresses (aged 26 and 64 years) and recordings were made of the set portraying each of seven emotions (anger, disgust, fear, happiness, pleasant surprise, sadness, and neutral). There are 2800 stimuli in total. Two actresses were recruited from the Toronto area. Both actresses speak English as their first language, are university educated, and have musical training. Audiometric testing indicated that both actresses have thresholds within the normal range.

The classes the model wants to predict are the following: (0 = neutral, 1 = calm, 2 = happy, 3 = sad, 4 = angry, 5 = fearful, 6 = disgust, 7 = surprised)



**data preparation**
In the first dataset, we have selected audios from 44.1 kHz video files, which have been removed.
In order to prevent the occurrence of conflicting files with a frequency of 48khz, after deletion, we got the number of votes
Final of the first data set is
1440 speech files and 1012 songs files
The first set of data, we already have 2800 files, so we got a total of 5052 files that are ready
Feelings of anger, sadness, disgust, surprise, calmness, naturalness, happiness and fear.
But we have a problem is that the file naming syntax in the dataset

It is as follows 03-01-01-01-01-01-03.wav where the third digit indicates the number of the feeling.
The file naming format in TESS is as follows: OAF_back_fear.wav
In this case, we will have a problem in processing the outputs from the training, so we will standardize the formulas
Label the two base files to appear in one format and one naming format.
We have for files  For TESS files.
OAF_back_fear.wav The next file and the rest of the files are the same, so we will try by writing
Instructions for converting the name of the feeling in the form of its naming and matching it with the number corresponding to the name of the feeling in files
ravdess seven separate numbered digits we will put random numbers in each so that it becomes the same formula
The boxes except for the third digit, which represents the number of the feeling corresponding to its name in the following form
01(random) 01(emotion=02) 01(random) 01(random) 01(random)
01(random)
For required folders that are formatted with the same name as the first rule and their formats are files
In both bases it is ready for processing and extracting the required features
**Data processing**
Our final goal before starting the training is to get the features from the audio files and convert the file format
The acoustic frequencies of the human voice are another form of mfcc, which is the frequency slope coefficients.
We divide the file into forty time segments and each segment we represent as an mfc, we will find the slope coefficients
Frequency for each coil The ray will represent the frequency slope coefficients for each input matrix coil x or data, and . represents
The corresponding feeling for each file is an array y (label), we will save the data and labels in two files from
X.jobliby.joblib  format
**Modeling**
The goal of this step is to build a machine or deep learning model through neural networks for data analysis
Using different analytical techniques and reviewing the result. Using the prepared data, we evaluate the model and the questions
We have is the identification of feelings according to the named data on which the model has been trained in advance, it belongs to a category
Supervised learning, which is a classification question. We will build models with the data we extracted and adopt the results
The most accurate is through training using machine learning algorithms from classification algorithms, which are
1.Knn
2. decision tree
3.random forest
4.svm
And CNN 1D
![Link to loss](https://github.com/abdulhameednabhan/Voice-analysis-for-emotion-recognition-using-deep-learning-and-machine-learning/blob/main/cnn_structure.PNG) 
![Link to stract](https://github.com/abdulhameednabhan/Voice-analysis-for-emotion-recognition-using-deep-learning-and-machine-learning/blob/main/cnn.PNG)

**model select**
Obtain 87% accuracy in test data, 97% in training data, svm, and algorithm
The overfitting ratio is quite clear
For the convolutional network, we were able to obtain an accuracy of 86% in the training data and 83% in
This test indicates the almost absence of an overfitting state, while in machine learning algorithms, it indicates
The overfitting is simple.
The difference between training and testing remains about 7%, which is a good percentage, the results of the network have been approved
Neuroscience as a final model and this is a comparison in the results of the networks and the result of each feeling
In the f1-score it is noted that the feeling of calm is the lowest accuracy and this is something logical because it is difficult to distinguish
And mixing it with many other feelings even for a human being
![Link to stract](https://github.com/abdulhameednabhan/Voice-analysis-for-emotion-recognition-using-deep-learning-and-machine-learning/blob/main/eval.PNG)

**model deployment**
We created an api to test files and create a simple web application from the framework Flask
In the prediction function, we receive a file and then extract the frequency slope coefficients for it and change the dimensions of the matrices
The result is to match the neural network, then download the model, test the file on it, and return the result
Digitally and then interview the resulting number with the corresponding feeling
We receive the file that we want to process in the application, apply the prediction function to it, and then return, to make it easier
Process it and deal with it in web pages or android json application
We run the application through




# Voice-analysis-for-emotion-recognition-using-deep-learning-and-machine-learning
Emotion recognition system ( voice) and export api
This project presents a deep learning classifier able to predict the emotions of a human speaker encoded in an audio file. The classifier is trained using 2 different datasets, RAVDESS and TESS, and has an overall F1 score of 80% on 8 classes (neutral, calm, happy, sad, angry, fearful, disgust and surprised).

**Feature set information**

For this task, the dataset is built using 5252 samples from:

- the [Ryerson Audio-Visual Database of Emotional Speech and Song (RAVDESS) dataset](https://zenodo.org/record/1188976#.XsAXemgzaUk) 
- the [Toronto emotional speech set (TESS) dataset](https://tspace.library.utoronto.ca/handle/1807/24487) 

The samples include: 

- 1440 speech files and 1012 Song files from **RAVDESS**. This dataset includes recordings of 24 professional actors (12 female, 12 male), vocalizing two lexically-matched statements in a neutral North American accent. Speech includes calm, happy, sad, angry, fearful, surprise, and disgust expressions, and song contains calm, happy, sad, angry, and fearful emotions. Each file was rated 10 times on emotional validity, intensity, and genuineness. Ratings were provided by 247 individuals who were characteristic of untrained adult research participants from North America. A further set of 72 participants provided test-retest data. High levels of emotional validity, interrater reliability, and test-retest intrarater reliability were reported. Validation data is open-access, and can be downloaded along with our paper from [PLoS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0196391).

- 2800 files from **TESS**. A set of 200 target words were spoken in the carrier phrase "Say the word _____' by two actresses (aged 26 and 64 years) and recordings were made of the set portraying each of seven emotions (anger, disgust, fear, happiness, pleasant surprise, sadness, and neutral). There are 2800 stimuli in total. Two actresses were recruited from the Toronto area. Both actresses speak English as their first language, are university educated, and have musical training. Audiometric testing indicated that both actresses have thresholds within the normal range.

The classes the model wants to predict are the following: (0 = neutral, 1 = calm, 2 = happy, 3 = sad, 4 = angry, 5 = fearful, 6 = disgust, 7 = surprised). This dataset is skewed as there is not a calm class in TESS, hence there are less data for that particular class and this is evident when observing the classification report.

Please note that previous versions of this work was developed using only the RAVDESS dataset and TESS has been added recently. Also, the previous versions of this work used audio features extracted from the videos of the RAVDESS dataset. This particular part of the pipeline has been removed because it was shuffling very similar files in the training and test sets, boosting accuracy of the model as a consequence (overfitting). Take a look at [this issue](https://github.com/marcogdepinto/Emotion-Classification-Ravdess/issues/11) to understand more. The old data exploration codebase, including the above mentioned pipeline, is stored in the ```legacy_code``` folder.



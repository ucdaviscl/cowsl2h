# COWSL2H
## The UC Davis Corpus of Written Spanish, L2 and Heritage Speakers

The UC Davis Corpus of Written Spanish, L2 and Heritage Speakers (COWSL2H) consists of short essays collected from students enrolled in university-level Spanish courses. Courses SPA 1-24 are L2 Learner courses. Course SPA 31-33 are Heritage Learner courses.

All essays, annotations, and corrections are available both as individual text files as well as comma-separated value (csv) files.

Essays are divided based on the prompts used to collect the data-

- famous: Write a text in Spanish about the following subject: "a famous person"

- vacation: Write a text in Spanish about the following subject: "your perfect vacation plan"

- special: Write a text in Spanish about the following subject: "a special person in your life"

- terrible: Write a text about the following subject: "a terrible story"

- yourself: Write a text describing yourself.

- beautiful: Write a text in Spanish about the following subject: "a beautiful story"

- place_you_disike: Write a text in Spanish about the following subject: "a place you dislike"

- Chaplin: Watch a brief clip from Chaplin's 'The Kid'. Write a text in Spanish describing the scene.

Each essay prompt is further divided by the quarter in which the data was collected.

Please see our recent [OpenReview paper submission](https://openreview.net/pdf?id=h6577g6KoMi) for a more detailed description of the corpus and motivations for its development.

#### Longitudinal data:

We include a CSV file, `longitudinal_essay_data.csv`, that lists all essays submitted by students who participated in the project for three or more academic terms. This data allows researchers to study individual language acquisition patterns, as well as to study the development of a cohort of students.

#### Study Abroad (SA) data:

This is the subset of the COWS corpus consisting of longitudinal data from English-dominant students participating in immersive study abroad (SA) programs in Spanish-speaking contexts. The prompts were designed as emails in which students completed the speech act of making a request. The SA data, and more information about its collection, can be found in the '[SA folder]([url](https://github.com/ucdaviscl/cowsl2h/tree/master/SA)).' 

#### Annotations: 

The first round of annotations consists of annotations of a subset of essays for gender/number agreement or attribution and usage of "a personal." These annotation targets were chosen based on specific research questions. Our second round of annotations added the following targets:

1.	Presence or absence of subject pronouns or articles.
2.	Confusion of preposition usage or of the usage of the verbs 'ser' and 'estar'.
3.	Adjective placement errors.

Many essays have been annotated for the same target by two (or in some cases more) anntotators to ensure annotation reliability. Essays that have been multi-annotated will include a second copy of the annotated file with a ' (1)' appended to the filename. Similarly, many annotated files have been annotated for different error targets - those which are targeting verb errors (specifically the use of 'ser' and 'estar') have "_verbs" appended to the filename. Please see the version 2.0 annotation guidelines for a more detailed description.

Note that all essays listed in the `longitudinal_essay_data.csv` file have been annotated following the version 2.0 annotation guidelines.

A more detailed description of these error types and the annotations procedure can be found in the version 2.0 annotation and correction documentation included in the repository (in Spanish).

We encourage fellow researchers to add to our annotations. Please see the included annotation scheme for further information.

#### Corrections: 

The corpus includes holistic corrections (corrected by graduate-level Spanish instructors) for a large portion of the collected essays. As with the annotated data, all essays in the `longitudinal_essay_data.csv` file have been corrected by at least one instructor.

A portion of the essays have been corrected by two instructors to measure correction consistency and to provide multiple correction referecens for grammatical error correction (GEC) model evaluation. Those essays which have two corrections will have a duplicate of the target file with a ' (1)' appended to the filename.

#### Metadata:
Metadata files consist of the following data items separated by "|||":
1) Course enrolled
2) Age
3) Gender
4) L1 language
5) Other L1 language(s)
6) Language(s) spoken at home
7) Language(s) studied
8) listening comprehension *
9) reading comprehension *
10) speaking ability **
11) writing ability **
12) Have you ever lived in a Spanish-speaking country?

NOTE: Metadata questions updated for for W21 and S21 data. See below.

\* Comprehension is self-described on the following scale:
* 1 (not confident at all)
* 2 (not extremely confident, but I am sometimes able to understand)
* 3 (somewhat confident but it depends a lot on the context and on my degree of focus on the task)
* 4 (quite confident: I understand written messages most of the time)
* 5 (extremely confident: I can understand any written message in Spanish)

** Speaking/writing ability is self-described on the following scale:
* 1 (not confident at all)
* 2 (not extremely confident)
* 3 (somewhat confident)
* 4 (quite confident)
* 5 (extremely confident)

Metadata format for S21 and W21:
1) Course enrolled
2) Age
3) Gender
4) How many years of Spanish courses had you taken before arriving to UC Davis?
5) What was the first Spanish course you took at UC Davis? 
6) How many previous Spanish upper division courses have you been enrolled in?
7) Which language(s) do you consider to be your mother tongue(s)?
8) Did you grow up in a Spanish-speaking household?
9) How many languages can you communicate in (including your mother tongue)?
10) Have you ever spent more than 1 month in a Spanish-speaking country?
11) Where did you attend elementary school?
12) Where did you attend High School?
13) Did you ever attend a bilingual (Spanish-English) school during K-12?
14) On a normal day, how much exposure (radio, papers, movies, people talking to you, etc.) to the Spanish language do you get outside of your Spanish language class?
15) Why do you study Spanish?
16) I feel [1] understanding my instructor when they speak Spanish in class.
17) feel [2] understanding a Spanish-speaking movie without subtitles.
18) feel [3] understanding the readings in the Spanish textbook or other classroom materials.
19) feel [4] understanding a newspaper article in Spanish.
20) feel [5] speaking Spanish in class.
21) feel [6] speaking Spanish outside of class.
22) feel [7] writing assignments for my Spanish course.
23) feel [8] writing a blog post in Spanish. 
24) [1]  that I will get a good grade for my current Spanish course.
25) I feel [2] about my current Spanish class. 
26) I feel that my Spanish course is [3].

## CSV Data Format

In addition to the raw text and corresponding annotations, corrections, and metadata files for individual essays, we have provided all of the currently available COWS-L2H data in a more user-friendly CSV format. To access these files, you can download the entire COWS-L2H repository, as described in the guide [How to use the COWS-L2H Corpus](https://docs.google.com/document/d/1vdEGCx2LSg_-sI2lGDwPGfbhJF_wzGDLvW9o95wp6wY/edit?usp=sharing). Alternatively, if you wish to view and download individual CSV files, do the following:

1) Browse to "csv" directory, which lists all available CSV files by topic and quarter.
2) Click on the desired CSV file, such as "famous.F17.csv"
3) If the contents of the file do not display automatically, click on the "View raw" option.
4) The raw text format of the data should now be visible in your browser window.
5) Click "File" then "Save Page As" or the equivalent on your browser menu.
6) Select the desired save location and save the file.

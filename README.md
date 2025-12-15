# Final Project Overview
The project I choose to complete to illustrate and apply my understanding of coding in python language is titled the priming facial categorization and intensity task. 
This task examines the function of emotion processing after a priming experience. Hypothetically, in this within-subjects design participants complete both a negative and neutral prime condition. 
In these conditions, participants watch a short video and then complete a face task that is composed of 32-trials. 
There are two priming videos, the negative prime video consists of a chicken farm (I don't recommend you select the negative prime condition when going through the experimental component, the video is disturbing), while the neutral prime consists of a step-by-step cooking video. 
The face task consists of 32 images pulled from the Nimstim data base, selected are four face identities, two males and two females. There are 8 images per-identity, within these images consists of four emotions (happy,sad,fear,angry), there are two images per-emotion, one image consists of an open-mouth expression, while the other consists of a closed-mouth expression. 
Participants are asked to indicate using the keyboard which emotion expression they believed each face stim to be illustrating. During this task, each stim image is considered one trial, a face will appear at random (without repeats), the stim will remain on the screen until the participant responds. 
After a response, a new prompt will appear asking the participant to record how intense they felt that emotional expression to be using a 1-5 point scale. There are several outcome variables collected from this task; response key to face stim, accuracy of response, RT of response, intensity rating, and intensity rating RT. 
# Project Components
This project consists of two and a half components. 
1. Experiment - Designing and coding the prime face task in psychopy. The code runs as an individual person-to-person experiment, this would be an ideal code to use in a real life experiment. The code runs through, simulating the prime videos and face task. It collects various components of data in a csv file (one file for each participant/session).
2. Data simulation - Using the same hypothetical design of my experiment, but re-coding it in a way that allows for data simulation. The code runs and computes hypothetical data based on normal distributions and the number of participants inputted. It computes and saves various components of simulated data into a csv file (one file for multiple participants/sessions)
3. Data figures - I wanted to try and make some graphs based on the simulated data. I used the simulated data and made multiple figures (bar graphs/line graphs) that show how emotion/prime condition differed on each outcome variable. 
# Key Folder and File 
* Please navigate to the FinalProject folder, this folder contains all the material needed and used in this project
* In this folder, please refer to the file named FinalProjectNotes. This file is a keymap to each step taken throughout this entire project. It consists of each step during my code process when creating the experiment, data simulation and data figures. It also acts as a map, in which it will guide you which files to open and look at to understand each coding step. 
# Key Files for Each Project Component 
The faces and primes folders consist of the face stim and prime videos used in this project. The file FinalProjectLoad.csv contains image paths and detail on pre-trial information. This was preloaded in my project to help with the coding procedure.
1. Experiment - Code is found in the file FinalProjectCode.py. An example output csv file is found in file 00_session1_neutral_faceTask.csv.
2. Data simulation - Code is found in the file FinalProjectCodeDataSim.py. An example output csv file is found in file Simulated_FaceTask_Data.csv. 
3. Data figures - Code is found in FinalProjectDescriptiveDataFigs.ipynb. I used the code from the data simulation section and then coded figures, these additional code segments and figures are found in this file.



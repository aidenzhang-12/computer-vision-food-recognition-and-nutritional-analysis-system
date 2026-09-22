# Computer Vision Food Health/Calorie Checker


## Table of Contents
- [Overview](#Overview)
- [Motivation & Background](#Motivation-&-Background)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [How it works](#how-it-works)
- [Example Output](#example-output)
- [Installations](#installations)
- [Sources](#Sources)





**Overview**
---

This personal project is a computer vision-based food health checker and sorting tool that classifies everyday food items (e.g. eggs, chocolate, bread, pizza, apples) and evaluates whether they are healthy or unhealthy. In addition to classification, it also displays key nutritional information per 100 grams, including calories, protein, carbohydrates, and fat. 

This project integrates text-to-speech (TTS) functionality so that whenever a new food item is detected, the system not only displays its nutritional details but also reads them aloud in real-time. For example, the tool will announce: “Detected: Apple. Health status: Healthy. Calories per 100 grams: 61. Fat: 0.15 grams. Carbohydrates: 14.8 grams. Protein: 0.13 grams.” This ensures users can receive instant auditory feedback while keeping their focus on the food item or camera feed, which can potentially help visually impaired individuals. 

By using a pre-trained teachable machine ([https://teachablemachine.withgoogle.com/train/image](url)) and live webcam input, the program analyzes the food item in real-time and delivers both visual and auditory feedback on the classification result, health assessment, and macros. This project demonstrates how AI can support health-conscious decision-making and raise awareness about everyday food choices.


**Motivation & Background**
---

Obesity, poor diet, and diet-related diseases are growing public health challenges in Canada and the United States. According to Statistics Canada, in Canada, about 30% of adults are estimated to have obesity as of 2022, a rise over the past decades (9% in 1981 to 27.2% in 2018, and now 30%)

After the COVID-19 pandemic, obesity rates in Canada continued to accelerate: from 25% in 2009 to 30% in 2022, an increase of about 8 percentage points, with it gaining each year. 

These trends highlight the urgent need for better public awareness about food quality, daily calorie intake, and nutrition. Many people consume foods without fully understanding their nutrient composition, making it harder to make healthier choices in everyday life. 

This project aims to address part of that gap by providing a real-time food identifier + nutrition insight tool. By recognizing common food items (e.g. eggs, chocolate, bread, pizza, apples) and showing their calories and macronutrients per 100g, this system could be a starting point, with more foods and drinks being expanded into the data set. This system could also help users
- Become more aware of what they are eating
- Quickly judge if the food is relatively healthy
- Use the data to guide better diet decisions

To sum it up, this project uses computer vision and machine learning for nutritional education, with the hope of contributing (small-scale) to better health awareness in our communities.


**Features**
---

- Live food item detection using the webcam and computer vision
  
- Classifies between: Eggs, Chocolate, Bread, Pizza, and Apples (More can be added)
  
- Evaluates whether each item is healthy or unhealthy
  
- Displays macronutrient breakdown per 100g:
  
      - Calories
      - Fat (g)
      - Carbohydrates (g)
      - Protein (g)

- Built using deep learning, OpenCV, and TensorFlow for real-time classification
  
- New food or potentially drink items can be added or retrained using Teachable Machine


**Tech Stack**
---

- Python

  
- TensorFlow & Teachable Machine: Deep learning & machine learning

  
- OpenCV: Real-time computer vision and webcam usage

  
- NumPy: numerical operations

  
- Pandas: Food categorization

  
- h5py: model storage

- pyttsx3: Text-to-speech (TTS) engine for reading out classification results and nutritional information in real-time

- Threading & Queue: Enable non-blocking text-to-speech so the webcam feed continues running smoothly while speech is processed in parallel

**Project Structure**
---
foodhealthchecker.py # Python File with full workflow

keras_model.h5 # pre-trained keras classification model (from teachable machine)

labels.txt # Food category labels

README.md # project documentation and summary

Results # Screenshot of outputs and video 

**NOTE keras_model.h5 and labels.txt should be in a folder called converted_keras_food when running code, unzip the ZIP file (The ZIP file)**

**How it Works**
---
Model Loading
- A keras .h5 model is loaded

Label Processing
- labels.txt provides class indices and food labels (e.g. "Eggs", "Pizza")
- Each food is mapped to a health classification and nutritional data via a Pandas DataFrame

Nutrition Data (CSV)
- A lookup table includes:

      - Food Name
      - Calories per 100g
      - Fat (g) per 100g
      - Carbs (g) per 100g
      - Fat(g)
      - Health Status: Healthy or Unhealthy

Live Classification 
- Captures webcam frames
- Runs predictions through the model
- Display classifications results and disposal instructions on screen



**Example Output**
---
Detected: Eggs

Health Status: Healthy


Per 100g
- Calories: 155 cal
- Fat: 10.0
- Carbs: 1.1
- Protein: 13.0

**Table of Macros**
---


**Installations**
---
Install packages before running the program

```bash
pip install opencv-contrib-python numpy requests tensorflow pandas h5py pyttsx3 

```


**Sources**
---
Research for Motivations & Background: [https://www150.statcan.gc.ca/n1/pub/82-003-x/2025002/article/00002-eng.htm](url)

Calories & Macros for each Food: [https://fdc.nal.usda.gov/](url)



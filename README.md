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

This personal project is a computer vision-based food health checker and sorting tool that classifies everyday food items (e.g. eggs, chocolate, bread, pizza, oranges) and evaluates whether they are healthy or unhealthy. In addition to classification, it also displays key nutritional information per 100 grams, including calories, protein, carbohydrates, and fat. 

This project uses a pre-trained teachable machine ([https://teachablemachine.withgoogle.com/train/image](url)) and live webcam input, the program analyzes the food item in real-time and displays the classification result, health assesment, and macros. This project demonstrates how AI can support health-conscious decision-making and make awareness about everyday food choices.


**Motivation & Background**
---

Obseity, poor diet, and diet-related diseases are growing public health challenges in Canada and the United States. According to Statistics Canada, in Canada about 30% of adults are estimated to have obseity as of 2022, a rise over the past decades (9% in 1981 to 27.2% in 2018, and now 30%)

After the COVID-19 pandemic, obsesity rates in Canada continued to accelerate from


**Features**
---

- Live food item detection using webcam and and computer vision
  
- Classifies between: Eggs, Chocolate, Bread, Pizza, and Oranges (More can be added)
  
- Evalutes whether each item is healthy or unhealthy
  
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

  
- Pandas: Waste categorization

  
- h5py: model storage

**Project Structure**
---
food_classifier.py # Python File with full workflow

keras_model.h5 # pre-trained keras classification model (from teachable machine)

labels.txt # Waste category labels

README.md # project documentation and summary

Results # Screenshot of outputs and video 


**How it Works**
---
Model Loading
- A keras .h5 model is loaded

Label Processing
- labels.txt provides class indicies and food labels (e.g. "Eggs", "Pizza")
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
- Runs predictions through model
- Display classifications results and disposal instructions on screen



**Example Output**
---
Detected: Eggs

Health Status: Healthy
Per 100g
- Calories
- Fat:
- Carbs:
- Protein:




**Installations**
---
Install packages before running the program

```bash
pip install opencv-contrib-python numpy requests tensorflow pandas h5py

```


**Sources**
---
[https://www150.statcan.gc.ca/n1/pub/82-003-x/2025002/article/00002-eng.htm](url)

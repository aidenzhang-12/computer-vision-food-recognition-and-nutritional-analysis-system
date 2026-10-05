# Computer Vision Food Health/Nutritional Analysis System


## Table of Contents

- [Overview](#overview)
- [Demo / Example Output](#demo--example-output)
- [Features](#features)
- [How It Works](#how-it-works)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Nutrition Data](#nutrition-data)
- [Motivation & Background](#motivation--background)
- [Future Improvements](#future-improvements)
- [Sources](#sources)





**Overview**
---

This personal project is a computer vision-based food health checker and sorting tool that classifies everyday food items (e.g. eggs, chocolate, bread, pizza, apples) and evaluates whether they are healthy or unhealthy. In addition to classification, it also displays key nutritional information per 100 grams, including calories, protein, carbohydrates, and fat. 

This project integrates text-to-speech (TTS) functionality so that whenever a new food item is detected, the system not only displays its nutritional details but also reads them aloud in real-time. For example, the tool will announce: “Detected: Apple. Health status: Healthy. Calories per 100 grams: 61. Fat: 0.15 grams. Carbohydrates: 14.8 grams. Protein: 0.13 grams.” This ensures users can receive instant auditory feedback while keeping their focus on the food item or camera feed, which can potentially help visually impaired individuals. 

By using a pre-trained teachable machine ([https://teachablemachine.withgoogle.com/train/image](url)) and live webcam input, the program analyzes the food item in real-time and delivers both visual and auditory feedback on the classification result, health assessment, and macros. This project demonstrates how AI can support health-conscious decision-making and raise awareness about everyday food choices.


**Demo / Example Output**
---
Detected: Eggs

Health Status: Healthy


Per 100g
- Calories: 155 cal
- Fat: 10.0
- Carbs: 1.1
- Protein: 13.0


## Installations

### Requirements

- **Python 3.11**
- Webcam
- Teachable Machine Keras model (`keras_model.h5`)
- Food classification labels (`labels.txt`)

This project uses a Teachable Machine `.h5` model. **Python 3.11 with TensorFlow 2.15.1 and Keras 2.15.0** is recommended for compatibility with the exported model.

### 1. Clone the Repository

```bash
git clone https://github.com/aidenzhang-12/computer-vision-food-recognition-and-nutritional-analysis-system.git
cd computer-vision-food-recognition-and-nutritional-analysis-system
```

### 2. Create a Virtual Environment

Create a Python 3.11 virtual environment:

```powershell
py -3.11 -m venv .venv
```

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

When activated, the terminal should display:

```text
(.venv)
```

> **Note:** The virtual environment only needs to be created once. However, it must be activated again whenever a new terminal is opened.

### 3. Install Dependencies

Upgrade `pip`:

```powershell
python -m pip install --upgrade pip
```

Install TensorFlow and Keras:

```powershell
python -m pip install tensorflow==2.15.1 keras==2.15.0
```

Install the remaining dependencies:

```powershell
python -m pip install opencv-contrib-python numpy pandas h5py pyttsx3
```

### 4. Configure Model Files

The program requires the following Teachable Machine files:

```text
keras_model.h5
labels.txt
```

Create a folder named:

```text
converted_keras_food
```

Place both files inside the folder:

```text
converted_keras_food/
├── keras_model.h5
└── labels.txt
```

The Python program currently expects the files at:

```text
C:\converted_keras_food\keras_model.h5
C:\converted_keras_food\labels.txt
```

If your model files are stored somewhere else, update the corresponding file paths in `foodhealthchecker.py`.

### 5. Run the Program

Make sure the virtual environment is activated:

```powershell
.\.venv\Scripts\Activate.ps1
```

Then run:

```powershell
python foodhealthchecker.py
```

The program will:

1. Load the trained Teachable Machine model
2. Open the webcam
3. Classify the detected food item
4. Display its health status and nutritional information
5. Read the nutritional information aloud using text-to-speech

Press `Esc` while the webcam window is selected to close the program.



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


**Tech Stack**
---

- Python 3.11: Main programming language 

  
- TensorFlow 2.15.1 / Keras 2.15.0 — Deep learning model inference


- Google Teachable Machine — Image classification model training


- OpenCV: Real-time webcam capture and computer vision 

  
- NumPy: Image and numerical processing

  
- Pandas: Food categorization and nutritional data management 

  
- h5py: Keras `.h5` model file handling


- pyttsx3: Offline text-to-speech for classification and nutritional feedback


- Threading & Queue: Non-blocking text-to-speech so the webcam feed continues running while speech is processed

**Project Structure**
---
foodhealthchecker.py # Python File with full workflow

keras_model.h5 # pre-trained keras classification model (from teachable machine)

labels.txt # Food category labels

README.md # project documentation and summary

Results # Screenshot of outputs and video 

**NOTE keras_model.h5 and labels.txt should be in a folder called converted_keras_food when running code, unzip the ZIP file (The ZIP file)**


## Nutrition Data

The system maps each recognized food item to nutritional information per 100 grams. The current prototype includes the following foods:

| Food | Health Status | Calories (kcal) | Fat (g) | Carbohydrates (g) | Protein (g) |
|---|---|---:|---:|---:|---:|
| Eggs | Healthy | 155 | 11.0 | 1.1 | 13.0 |
| Chocolate | Unhealthy | 598 | 42.6 | 46.4 | 7.8 |
| Bread | Neutral | 265 | 3.2 | 49.0 | 9.0 |
| Pizza | Unhealthy | 266 | 10.0 | 33.0 | 11.0 |
| Apples | Healthy | 61 | 0.15 | 14.8 | 0.13 |

> **Note:** Nutritional values are approximate and are expressed per 100 grams. Values can vary depending on the specific product, recipe, or preparation method.


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

**Future Improvements**

- Expand the model to recognize more food and drink categories
- Improve classification accuracy using a larger and more diverse dataset
- Add confidence scores for each prediction
- Store nutritional information in an external CSV or database
- Estimate serving sizes instead of displaying only per-100g values
- Add a graphical user interface
- Explore accessibility improvements for visually impaired users

**Sources**
---
Research for Motivations & Background: [https://www150.statcan.gc.ca/n1/pub/82-003-x/2025002/article/00002-eng.htm](url)

Calories & Macros for each Food: [https://fdc.nal.usda.gov/](url)



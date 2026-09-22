# install libraries required for this classifier (opencv-contrib-python, numpy, requests, tensorflow, pandas, pyttsx3, threading, queue)

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import cv2
import sys
from keras.models import load_model  # tensorflow is required for Keras to work
import cv2  
import h5py # for reading HDF5 files
import numpy as np # for numerical operations
import pandas as pd # for data manipulation
import pyttsx3 # for tts
import threading, queue

# Initialize TTS engine once
tts_engine = pyttsx3.init()

_speech_q = queue.Queue()

def _tts_worker():
    while True:
        text = _speech_q.get()
        if text is None:  # shutdown signal
            break
        try:
            tts_engine.say(text)
            tts_engine.runAndWait()
        except Exception as e:
            print("TTS error:", e)
        finally:
            _speech_q.task_done()

_tts_thread = threading.Thread(target=_tts_worker, daemon=True)
_tts_thread.start()


# disabling scientific notation
np.set_printoptions(suppress=True)


# Developed a computer vision system for waste stations. 
# The system uses an cameras to identify waste type and suggest correct disposal. 
# Built a prototype machine learning model for testing on sample waste images trained on [Teachable Machine](https://teachablemachine.withgoogle.com/train/image) model using photos of different types of waste.

f = h5py.File(r"C:\converted_keras_food\keras_model.h5", mode="r+") # this is the path of the HDF5 file

model_config_string = f.attrs.get("model_config") 

# Model Training

# Used Teachable Machine to train an image classification model on labeled food images.
# Collected varied images for each class.
# Trained with default settings.
# Tested accuracy using new images.


if model_config_string.find('"groups": 1,') != -1: 
    model_config_string = model_config_string.replace('"groups": 1,', '') 

f.attrs.modify('model_config', model_config_string) 
f.flush() 

model_config_string = f.attrs.get("model_config") 

assert model_config_string.find('"groups": 1,') == -1 

# Load the trained keras model from the specified file path
# 'compile=False' is used here because we only need the model for inference (making predictions) not for further training. This speeds up loading and avoids loading optimizer state.
model = load_model(r"C:\converted_keras_food\keras_model.h5", compile=False) 


model.summary()  # Display a detailed summary of the model architectureincluding each layer's name, output shape, and number of parameters.


# Load the list of class labels from the specified text file.
# Each line in this file corresponds to a class index and its name (e.g., "0 Cardboard").
# Using readlines() returns all lines as a list, which can be used for mapping model predictions to human-readable names.
class_names = open(r"C:\converted_keras_food\labels.txt", "r").readlines()
# Display the loaded class labels
class_names


# Define text style for OpenCV image overlay
font = cv2.FONT_HERSHEY_SIMPLEX  # Font type
fontScale = 1 # size of the text
color = (0, 153, 0) # text colour in BGR format (green here)
thickness = 2 # Thickness of the text


class_list = [] # Create an empty list to store cleaned class names
# Loop through each label in class_names
for x in class_names:
    # Split each entry on the first space to separate the index and the name
    # Take the second part [1], strip leading/trailing spaces
    clean_name = x.split(' ', 1)[1].strip()

    # Append the cleaned name to the new list
    class_list.append(clean_name.lstrip())

# Display the class names
class_list 

food_categorization = pd.DataFrame(class_list, columns= ['Classification']) # Create a DataFrame from class_list with a single column named "Classification"
 
# Display the DataFrame
food_categorization

food_categorization = food_categorization.set_index('Classification') # Set "Classification" as the index for easier row access


food_categorization # Display updated DataFrame

food_categorization['Health Status'] = "Unknown"
food_categorization['Calories (100g)'] = 0
food_categorization['Fat (g)'] = 0.0
food_categorization['Carbs (g)'] = 0.0
food_categorization['Protein (g)'] = 0.0



# Assign realistic macros and health status per 100g of food
# Format: [Health Status, Calories, Fat, Carbs, Protein]
food_categorization.loc['Eggs'] = ['Healthy', 155, 11.0, 1.1, 13.0]
food_categorization.loc['Chocolate'] = ['Unhealthy', 598, 42.6, 46.4, 7.8]
food_categorization.loc['Bread'] = ['Neutral', 265, 3.2, 49.0, 9.0]
food_categorization.loc['Pizza'] = ['Unhealthy', 266, 10.0, 33.0, 11.0]
food_categorization.loc['Apples'] = ['Healthy', 61, 0.15, 14.8, 0.13]

# Set clean index
food_categorization.index = food_categorization.index.str.strip()

food_categorization # Display the updated DataFrame

# Predict using the trained model
def predict_model(model, prediction_image):
    # Make a copy to avoid altering the original image
    image = prediction_image.copy()
    
    # Resize the image to match the model's expected input size (224x224 pixels)
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    
    # Convert to numpy array, cast to float32, and reshape for the model
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
    
    # Normalize pixel values to the range [-1, 1]
    image = (image / 127.5) - 1.0
    
     # Make prediction
    prediction = model.predict(image)
    
    # Get the index of the highest probability class
    index = np.argmax(prediction)
    
    # Retrieve the class name and confidence score
    class_name = class_names[index].strip()  # Removing extra characters
    if " " in class_name:
        class_name = class_name.split(" ", 1)[1]  # drop the leading number
    
    return class_name

def get_nutrition_info(food_categorization, class_name):
    
    default_output = {
        "Health Status": "Unknown",
        "Calories (100g)": 0,
        "Protein (g)": 0.0,
        "Carbs (g)": 0.0,
        "Fat (g)": 0.0
    }
    try:
        info = food_categorization.loc[class_name]
        return {
            "Health Status": info['Health Status'],
            "Calories (100g)": info['Calories (100g)'],
            "Fat (g)": info['Fat (g)'],
            "Carbs (g)": info['Carbs (g)'],
            "Protein (g)": info['Protein (g)']
        }
    except KeyError:
        print("DEBUG: label not found ->", repr(class_name))
        return default_output

def speak_nutrition (class_name, info):
    text = (
        f"{class_name}. "
        f"Health status: {info['Health Status']}. "
        f"Calories per 100 grams: {info['Calories (100g)']} kilocalories. "
        f"Fat: {info['Fat (g)']} grams. "
        f"Carbohydrates: {info['Carbs (g)']} grams. "
        f"Protein: {info['Protein (g)']} grams."
    )

    # keep only the latest message so we don't queue old ones
    while not _speech_q.empty():
        try:
            _speech_q.get_nowait()
            _speech_q.task_done()
        except queue.Empty:
            break

    
    _speech_q.put(text)
    

def add_text_to_image(image, class_name, food_categorization):
    """
    Output food classification + nutrition info on the fram.

    Parameters:
        image (ndarray): The image to annotate.
        class_name (str): Predicted food name.
        nutrition_info(dict): Must contain keys:
        'Health Status', 'Calories (100g)', 'Fat (g)', 'Carbs (g)', 'Protein (g)'

    Returns:
        ndarray: Annotated frame.
    """
    
    info = get_nutrition_info (food_categorization, class_name)


     # ---- messages ----
    msg0 = "Show food item to classify"
    msg1 = f"Detected: {class_name}"
    msg2 = f"Health: {info['Health Status']}"
    msg3 = f"Calories (100g): {info['Calories (100g)']} kcal"
    msg4 = (f"Fat: {info['Fat (g)']}g   "
            f"Carbs: {info['Carbs (g)']}g")
            
    msg5 = (f"Protein: {info['Protein (g)']}g")

    # Text positions
    org_instructions = (25, 50)
    org_class = (25, 350)
    org_conf = (25, 400)
    org_bin = (25, 450)

    line_h = 40 # adjust spacing between phrase
    # Draw text on image
    x, y0 = 25, 45
    cv2.putText(image, msg0, (x, y0), font, fontScale, color, thickness)
    cv2.putText(image, msg1, (x, y0 + 1*line_h), font, fontScale, color, thickness)
    cv2.putText(image, msg2, (x, y0 + 2*line_h), font, fontScale, color, thickness)
    cv2.putText(image, msg3, (x, y0 + 3*line_h), font, fontScale, color, thickness)
    cv2.putText(image, msg4, (x, y0 + 4*line_h), font, fontScale, color, thickness)
    cv2.putText(image, msg5, (x, y0 + 5*line_h), font, fontScale, color, thickness)
    
    return image



camera = cv2.VideoCapture(0)  
if not camera.isOpened():
    print("Could not open webcam. Please check camera connection or index")
    sys.exit()

last_spoken = None # keep track of the last spoken class



while True:
    # Capture frame from webcam
    ret, image = camera.read()
    if not ret:
        break

    # Resize frame for display
    image = cv2.resize(image, (640, 480), interpolation=cv2.INTER_AREA)

    # Get prediction
    class_name = predict_model(model, image)

    # Print results to console
    print("Detected: ", class_name)

    # only speak if its a new object
    
    if class_name != last_spoken:
        info = get_nutrition_info(food_categorization, class_name)
        speak_nutrition(class_name, info)      
        last_spoken = class_name

    
    
    image = add_text_to_image(image, class_name, food_categorization)


    # Display annotated frame
    cv2.imshow("Food Nutrition Classification Tool", image)

    # Exit on ESC key
    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()

# stop TTS worker thread cleanly
_speech_q.put(None)
_tts_thread.join(timeout=2)

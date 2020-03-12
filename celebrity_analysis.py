"""
@author: PrithviSriram
"""

import requests
import matplotlib.pyplot as plt
import json
from PIL import Image
from io import BytesIO
import numpy as np
import sys
import os
import time
from lime import lime_image
from skimage.segmentation import mark_boundaries

def predict_fn(images):
    # to return classifier_fn: classifier prediction probability function, which takes a numpy array and outputs prediction probabilities.
    # return session.run(probabilities, feed_dict={processed_images: images})
    # It returns a 2d array of probabilities. Therefore only the probability of caption should be fine.
    probabilities = np.empty(shape = (len(images),1))
    i=0
    for image in images:
        if(type(image)!= "JpegImageFile"):
            im = Image.fromarray(image)
            im.save(image_path_2)
            image_data = open(image_path_2, "rb").read()
            response = requests.post(analyze_url, headers=headers, params=params, data=image_data)
            response.raise_for_status()
            analysis = response.json()
            probabilities[i,0] = 0
            try:
                all_celebs = analysis["categories"][0]["detail"]["celebrities"]
                if(all_celebs is not None or len(all_celebs)>0):
                    for tag_i in all_celebs:
                        if(tag_i["name"] == actual_celebrity):
                            probabilities[i,0] = tag_i["confidence"] 
            except:
                probabilities[i,0] = 0
            i = i+1
        else:
            image_data = open(image_path_2, "rb").read()
            response = requests.post(analyze_url, headers=headers, params=params, data=image_data)
            response.raise_for_status()
            analysis = response.json()
            probabilities[i,0] = 0
            try:
                all_celebs = analysis["categories"][0]["detail"]["celebrities"]
                if(all_celebs is not None or len(all_celebs)>0):
                    for tag_i in all_celebs:
                        if(tag_i["name"] == actual_celebrity):
                            probabilities[i,0] = tag_i["confidence"] 
            except:
                probabilities[i,0] = 0
            i = i+1
    time.sleep(1)
    return(probabilities)

def predict_fn_one_time(images):
    # Check if API call works.
    # to return classifier_fn: classifier prediction probability function, which takes a numpy array and outputs prediction probabilities.
    # return session.run(probabilities, feed_dict={processed_images: images})
    probabilities = np.empty(shape = (len(images),1))
    i=0
    for image in images:
        print("Checking to ensure API call works . . .")
        image_data = open(image_path, "rb").read()
        response = requests.post(analyze_url, headers=headers, params=params, data=image_data)
        response.raise_for_status()
        analysis = response.json()
        probabilities[i,0] = 0
        all_celebs = analysis["categories"][0]["detail"]["celebrities"]
        if(all_celebs is not None or len(all_celebs)>0):
            for tag_i in all_celebs:
                print(tag_i)
                if(tag_i["name"] == actual_celebrity):
                    probabilities[i,0] = tag_i["confidence"] 
        celeb_tag = actual_celebrity
        probabilities[i,0] = analysis["categories"][0]["detail"]["celebrities"][0]['confidence']
        i = i+1
    time.sleep(1)
    return(probabilities, celeb_tag)

def load_image( infilename ) :
    img = Image.open( infilename )
    img.load()
    data = np.asarray( img, dtype="uint8" )
    return data

if __name__ == "__main__":
    subscription_key = sys.argv[1]
    endpoint = sys.argv[2]
    image_path = sys.argv[3]
    image_path_2 = sys.argv[4]
    actual_celebrity = sys.argv[5]
    number_samples = int(sys.argv[6])

    analyze_url = endpoint + "vision/v2.1/analyze"
    image_data_init = open(image_path, "rb").read()
    headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
    params = {'details': 'celebrities'}

    images = []
    # Convert to Numpy Array
    image = load_image(image_path)
    # print(image.shape)
    images.append(image)
    probabilities, celeb_tag = predict_fn_one_time(images)
    print("API Call works")
    
    plt.imshow(image)
    plt.axis("off")
    _ = plt.title(celeb_tag, size="x-large", y=-0.1)

    explainer = lime_image.LimeImageExplainer()
    tmp = time.time()
    # Hide color is the color for a superpixel turned OFF. Alternatively, if it is NONE, the superpixel will be replaced by the average of its pixels
    explanation = explainer.explain_instance(image, predict_fn, top_labels=1, hide_color=0, num_samples=number_samples)
    print (time.time() - tmp)
    temp, mask = explanation.get_image_and_mask(0, positive_only=False, num_features=10, hide_rest=False)
    plt.imshow(mark_boundaries(temp, mask))
    plt.show()
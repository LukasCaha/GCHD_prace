from keras.models import load_model
from keras.preprocessing import image

# Load model
classifier = load_model('classifierNEW')

import glob, os, numpy as np
#move to predict dir
counter = 0
for file in glob.glob("dataset/single_prediction/*.jpg"):
    counter = counter+1
    #print(file)
    test_image = image.load_img(file, target_size = (64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = classifier.predict(test_image)
    if result[0][0] == 1:
        prediction = 'dog'
    else:
        prediction = 'cat'
       
    # Rename
    """for filename in os.listdir("dataset/single_prediction/"):
        if filename.startswith(file[26:]):
            os.rename('dataset/single_prediction/'+filename, 'dataset/single_prediction/'+prediction+''+str(counter)+'.jpg')"""
    # Change directory
    for filename in os.listdir("dataset/single_prediction/"):
        if filename.startswith(file[26:]):
            os.rename('dataset/single_prediction/'+filename, 'dataset/single_prediction/'+prediction+'/'+prediction+''+str(counter)+'.jpg')
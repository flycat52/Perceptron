# COMP307 - Assignment1 - part3
# 300434790 - Yalian

import random as rd
import numpy as np
import os
import os.path
import argparse

class Feature:
    def __init__(self, row, col, sgn):
        self._row = row
        self._col = col
        self._sgn = sgn
    def get_row(self): return self._row
    def get_col(self): return self._col
    def get_sgn(self): return self._sgn
    def __str__(self):
        return "row = {0}, col = {1}, sgn = {2}".format(self._row, self._col, self._sgn)   

def get_feature_list(f):
    feature_list = []
    print('The random features are:')
    f.write('The random features are: \n')
    for k in range(60):
        row, col, sgn = ([] for i in range(3))
        for i in range(4):
            row.append(rd.randint(0,9))
            col.append(rd.randint(0,9))
            sgn.append(rd.randint(0,1))
        feature = Feature(row, col, sgn)
        print(feature.__str__())
        f.write(feature.__str__() + '\n')
        feature_list.append(feature)
    return feature_list

def get_original_image_list(img_file):
    with open(img_file, 'r') as f:
        data = f.read().split('P1\n')[1:]
        #print(data)
        image_list = []
        for img in data:
            img = img.split('\n') 
            img_class = img[0]
            img_val = list(img[2] + img[3])
            #split img_val into 10 arrays
            img_val = [img_val[i:i + 10] for i in range(0, len(img_val), 10)]
            image_list.append((img_val, img_class))
    #print(image_list)
    return image_list

def get_image_feature_value_list(image_list, feature_list):
    #image_list = get_original_image_list(img_file)
    
    image_feature_value_list = []
    for i in range(len(image_list)):
        image = image_list[i][0] #array of 0,1
        image_class = image_list[i][1]
        image_feature_value = []
        image_feature_value.append(1) #dummy 
        for f in feature_list:
            sum = 0
            for j in range(4):
                if(image[f.get_row()[j]][f.get_col()[j]] == str(f.get_sgn()[j])):
                    sum += 1
            image_feature_value.append(1 if sum>=3 else 0)
        image_feature_value_list.append((image_feature_value, image_class))
    
    return image_feature_value_list

def get_initial_weight():
    weight = []
    for i in range(61):
        weight.append(rd.uniform(0, 1))
    return weight

def finalize_weights(image_list, feature_list, f):
    weight = get_initial_weight()
    img_feature_value = get_image_feature_value_list(image_list, feature_list)

    k = 0
    hits = 0
    while hits < 100 or k < 500:
        hits = 0
        for feature_val in img_feature_value:
            predit = np.dot(weight, feature_val[0])
            if predit > 0: predit_class = '#X'
            else: predit_class = '#O'
            if feature_val[1] == predit_class: hits += 1
            else:
                output = 1 if feature_val[1]=='#X' else 0
                predict = 1 if predit_class == '#X' else 0
                for i in range(61):
                    weight[i] += (output - predict) * feature_val[0][i]
        if hits == 100: break
        k += 1 
    print('The final set of weights are: ')       
    print(str(weight))
    print('After ' + str(k) + ' times training cycles, ' + str(hits) + ' images are classified correctly. \n' )

    f.write('The final set of weights are: \n')       
    f.write(str(weight) + '\n')
    f.write('After ' + str(k) + ' times training cycles, ' + str(hits) + ' images are classified correctly. \n' )
    return weight

def Main():
    output_file = 'sampleoutput.txt'
    if os.path.exists(output_file):
        os.remove(output_file)

    parser = argparse.ArgumentParser()
    parser.add_argument('trainingset', help='Choose a training data set')
    args = parser.parse_args()

    with open(output_file,'a') as f:
        image_list = get_original_image_list(args.trainingset)
        feature_list = get_feature_list(f)
        weights = finalize_weights(image_list, feature_list, f)

        test_image_list = get_original_image_list('test.data')
        test_image_feature_value = get_image_feature_value_list(test_image_list, feature_list)

        f.write('\nEvaluate perceptron on the test set: \n')
        i = 1
        correct = 0
        for feature_val in test_image_feature_value:
            predit = np.dot(weights, feature_val[0])
            if predit > 0: predit_class = '#X'
            else: predit_class = '#O'
            if feature_val[1] == predit_class:
                correct += 1
                print('Class of image ' + str(i) +' is correct.')
                f.write('Class of image ' + str(i) +' is correct.\n')
            else:
                print('Class of image ' + str(i) +' is incorrect.')
                f.write('Class of image ' + str(i) +' is correct.\n')
            i += 1
        accuracy = round(correct/len(test_image_list) * 100, 2)
        print('The accuracy of test image set is: ' + str(accuracy) + '%. \n')
        f.write('The accuracy of test image set is: ' + str(accuracy) + '%. \n')

Main()


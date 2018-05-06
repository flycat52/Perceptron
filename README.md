# Perceptron

This part of the assignment involves writing a program that implement a perceptron with “random” features that learns to distinguish between two classes of black and white images (X’s and O’s).

## Data Set
The file image.data consists of 100 image files, concatenated together. Each image file is in PBM format, with exactly one comment line.
- The first line contains P1;
- The second line contains a comment (starting with #) that contains the class of the image (such as X and O),
- The third line contains the image width and height (number of columns and rows)
- The remaining lines contain 1’s and 0’s representing the pixels in the image, with ’1’ representing black, and ’0’ representing white. The line breaks are ignored.

## Features
The program should construct a perceptron that uses at least 50 “random” features. Each feature should be connected to 4 randomly chosen pixels. Each connection should be randomly marked as true or false, and the feature should return 1 if at least three of the connections match the image pixel, and return 0 otherwise. For example, if the Feature class has fields:
```
class feature {
  int[] row;
  int[] col;
  boolean[] sgn;
}
```
then a feature with positive connections to pixels (5,2), and (2,9), and negative connections to (6,5) and (9,1) could be represented using three arrays of length 4:
```
f.row = { 5, 2, 6, 9};
f.col = { 2, 9, 5, 1};
f.sgn = { true, true, false, false};
```
and the value of the feature for the given image (represented by a 2D boolean array) could be computed by:
```
int sum=0;
for(int i=0; i < 4; i++)
  if (image[f.row[i], f.col[i]]==f.sgn[i])
    sum++;
return (sum>=3)?1:0;
```
You may find it convenient to calculate the values of the features on each image as a preprocessing step, before you start learning the perceptron weights. This means that each image can be represented by an array of feature values. Don’t forget to include the “dummy” feature whose value is always 1.


## Prerequisite
- Python 3.6 or higher
- Please keep all the related data files in the same folder (i.e.part3).


## Running Steps
1. Open Terminal console
2. Go to the project part3 directory
3. Run command: python perceptron.py image.data
4. An output file (sampleoutput.txt) will be generated in the same project folder. Check it for the result.
(Note: the output result might be different from that in the assignment report. Because the initial weights and features are generated randomly.)




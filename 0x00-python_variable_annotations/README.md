# 0x00. Python - Variable Annotations 

## Table of content

| Title | Project File |
|:-----|:-----|
|task 0|[0-add.py](https://github.com/inderitu/alx-backend-python/blob/main/0x00-python_variable_annotations/0-add.py)|
|task 1|[1-concat.py](https://github.com/inderitu/alx-backend-python/blob/main/0x00-python_variable_annotations/1-concat.py)|
|task 2|[2-floor.py](https://github.com/inderitu/alx-backend-python/blob/main/0x00-python_variable_annotations/2-floor.py)|
|task 3|[3-to_str.py](https://github.com/inderitu/alx-backend-python/blob/main/0x00-python_variable_annotations/3-to_str.py)|
|task 4|[4-define_variables.py](https://github.com/inderitu/alx-backend-python/blob/main/0x00-python_variable_annotations/4-define_variables.py)|
|task 5|[5-sum_list.py](https://github.com/inderitu/alx-backend-python/blob/main/0x00-python_variable_annotations/5-sum_list.py)|
|task 6|[6-sum_mixed_list.py](https://github.com/inderitu/alx-backend-python/blob/main/0x00-python_variable_annotations/6-sum_mixed_list.py)|
|task 7|[7-to_kv.py](https://github.com/inderitu/alx-backend-python/blob/main/0x00-python_variable_annotations/7-to_kv.py)|
|task 8|[8-make_multiplier.py](https://github.com/inderitu/alx-backend-python/blob/main/0x00-python_variable_annotations/8-make_multiplier.py)|
|task 9|[9-element_length.py](https://github.com/inderitu/alx-backend-python/blob/main/0x00-python_variable_annotations/9-element_length.py)|

### 0. Basic annotations - add 

 
 
 
Write a type-annotated function add that takes a float a and a float b as arguments and returns their sum as a float. 

### 1. Basic annotations - concat 

 
 
 
Write a type-annotated function concat that takes a string str1 and a string str2 as arguments and returns a concatenated string 

### 2. Basic annotations - floor 

 
 
 
Write a type-annotated function floor which takes a float n as argument and returns the floor of the float. 

### 3. Basic annotations - to string 

 
 
 
Write a type-annotated function to_str that takes a float n as argument and returns the string representation of the float. 

### 4. Define variables 

 
 
 
Define and annotate the following variables with the specified values: 
 
a, an integer with a value of 1
pi, a float with a value of 3.14
i_understand_annotations, a boolean with a value of True
school, a string with a value of “Holberton” 

### 5. Complex types - list of floats 

 
 
 
Write a type-annotated function sum_list which takes a list input_list of floats as argument and returns their sum as a float. 

### 6. Complex types - mixed list 

 
 
 
Write a type-annotated function sum_mixed_list which takes a list mxd_lst of integers and floats and returns their sum as a float. 

### 7. Complex types - string and int/float to tuple 

 
 
 
Write a type-annotated function to_kv that takes a string k and an int OR float v as arguments and returns a tuple. The first element of the tuple is the string k. The second element is the square of the int/float v and should be annotated as a float. 

### 8. Complex types - functions 

 
 
 
Write a type-annotated function make_multiplier that takes a float multiplier as argument and returns a function that multiplies a float by multiplier. 

### 9. Let's duck type an iterable object 

 
 
 
Annotate the below function’s parameters and return values with the appropriate types 
 
def element_length(lst):
    return [(i, len(i)) for i in lst] 

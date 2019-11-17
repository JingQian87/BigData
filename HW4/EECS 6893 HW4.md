## EECS 6893 HW4

#### Jing Qian (jq2282)

### Problem 1

###### 1. Answer these questions in simple words.

**1.1 ** 

SVG Coordinate Space and Mathematical/Graph Coordinate are both 2-dimensional flat space. They work in the same way except following:

* The (0, 0) coordinates of Mathematical Coordinate Space fall on the bottom left while those of SVG Coordinate Space on the top left.

* The Mathematical Coordinate Space has Y coordinate growing from bottom to top while SVG Coordinate Space has Y coordinate growing from top to bottom. 

  

**1.2**

In d3.js, enter() and exit() are operations that used in joining an array of data to a D3 selection. If the array is longer than the selection, we use enter() to represent the missing elements. If the array is shorter than the selection, we use exit() to represent elements that need to be removed.



**1.3**

In SVG, transform functions are used for geometric manipulations on the SVG elements, including translation (movement), rotation, scale, and skew (shear). 

A translation moves all the points of an element in the same direction and by the same amount. Translation preserves parallelism, angles and distances.



**1.4**

The anonymous function a.map(function(d,i){return i+5}) here equals to the following command in Python: [i+5 for i in range(len(a))]. So the return value of the anonymous function is: [5, 6, 7, 8, 9]. 需要描述anonymous function或者map吗？对于定义还是有点迷茫。



###### 2. Modify the sample code to get desired figure.

The screenshots of codes and the output bar-chart are as following:

![Q1-1](/Users/mac/Desktop/BigData/HW4/Q1-1.png)

![Q1-2](/Users/mac/Desktop/BigData/HW4/Q1-2.png)

![Q1-3](/Users/mac/Desktop/BigData/HW4/Q1-3.png)



### Problem 2
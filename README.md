### Convolution

Convolves an image with a kernel. It uses zero-padding to account for edges of the photo.

**Results:**

*Convolve 1* (with addition): 18.4720001221s

*Convolve 2* (dot product): 15.8229999542s

*Scipy Convolve*: 0.0549998283386s

Using the image:

![alt text](https://github.com/birdievera/Convolution/cat.jpg "Cat")

Our convolved image is:

![alt text](https://github.com/birdievera/Convolution/example.jpg "Convolved ")


**Further improvements**

* Convert the two for loops into a generator
* Convert the two for loops into map and lambda functions

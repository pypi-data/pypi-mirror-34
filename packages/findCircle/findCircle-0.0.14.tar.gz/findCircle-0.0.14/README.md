Note this uses python3.

# Setup
To install the package use the following command in terminal:

    pip install findCircle

To import the package, put at the top of your python script:

    from findCircle.findCircle import *
or

    from findCircle.findCircle import intercept

# Quickstart
Once imported you can use the following function:

    intercept([(x_0,y_0,r_0),(x_1,y_1,r_1),(x_2,y_2,r_2)])

Where `(x_0,y_0,r_0)` is a tuple representing a circles, vertex and radius.

The function `intercept()` returns a tuple of the form `((x_a,y_a),duplicates)`,
Where `(x_a,y_a)` is a tuple representing the intersection point, and `duplicates` is an integer representing the number of overlapping circles at that point.

There is also the function `plotIntercept` that works the same way but will plot circles using `matplotlib`, you can define the boundaries of the figure by using the input parameter `xlim` and `ylim` which take in tuples of the form `(minValue,maxValue)` where `minValue` and `maxValue` are floats/doubles.

# Example

    from findCircle import findCircle
    points=findCircle.intercept([(0,0,4),(8,0,4),(4,4,4)])
    findCircle.plotIntercept([(0,0,4),(8,0,4),(4,4,4)],xlim=(-20,20),ylim=(-20,20))

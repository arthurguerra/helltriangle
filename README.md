# Hell Triangle

Given a triangle of numbers, find the maximum total from top to bottom

Example:
    6
   3 5
  9 7 1
 4 6 8 4

In this triangle the maximum total is: 6 + 5 + 7 + 8 = 26.

An element can only be summed with one of the two nearest elements in the next row.
For example: The element 3 in the 2nd row can only be summed with 9 and 7, but not with
1

Your code will receive an (multidimensional) array as input.
The triangle from above would be:
example = [[6],[3,5],[9,7,1],[4,6,8,4]]

## Algorithm

* The idea is to pass each element in the triangle only once
* The hell triangle looks like a binary tree (with some specialties) and we can find the maximum sum
  with an algorithm similar to DFS.
1) In order to get the max sum of an element in the triangle, we need to know the maximum sum we
  can get from the left child as well as the max sum from the right child. So, the max sum of the
  current element will be whatever the current element value is plus the max sum between my left and
  right children.
2) Based on (1), instead of going from the top to bottom, we go from bottom to top. By doing that, we
   avoid computing the max sum for the same element twice. So, first we compute the max sum for all "leaves"
   (last row of my triangle), then we compute the max sum for the row above, and so on until we reach the
   top.
   * The operation of finding the max sum is done in-place, so we are using the input array to store
     the value for the max sum until the current element.
3) Once the top of the triangle is reached, we will have the max sum for the whole triangle right at
   the top element, so we just return it.
   
## Run Unit Tests

Before you run the tests, make sure you have Python 3 installed on your system.

Once you have clone the hell triangle repository, do:

    $ cd helltriangle
    $ python -m unittest discover

The `python -m unittest discover` command will find the `tests` package inside the project directory and execute all the tests.

## Why Python?

As you can see, this code challenge was implemented in Python 3. The reason to use Python is because its simplicity. The sintax
is clean, not verbose, and you can do many things with a single line of code. Also, to run the application it is not 
necesssary to compile anything, just execute the script. The code is there available for you to take a look at.

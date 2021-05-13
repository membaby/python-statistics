# Solving Statistics Problems with Python
Includes solutions to tasks related to real life problems.

Task (1): [PYTHON CODE](docs/circles_bounded_area_in_square.py)
**Problem:** We have a square ABCD with side lengths 4.0 cm. An area is bounded by two circles centered at corners B and D. 
**Required:** Estimate the area of the bounded part.
**Given:**
https://i.imgur.com/ZzVIq6o.png

**Solution:**
Area of square = 4 * 4 = 16.0 cm2.
Radius of each circle is 4.0 cm.

* Create 2 functions f(x,y) and g(x,y) to test the existance of x and y points in a certain circle.
* Send 10,000 checks to coordinates [X: 0->4, Y: 0->4].
* For each check, if X, Y exist in both circles then it is a part of the shaded area.
* Find the probability and get the area of the bounded shape.



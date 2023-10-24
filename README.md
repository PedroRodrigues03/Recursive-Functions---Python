# Recursive-Functions---Python


## Developers

* Pedro Lopes Rodrigues


## What are Recursive Functions?

They are functions that call themselves whthin their own scope.
They are usefull to divide big problems into small ones.
Every recursive function must have:
+ A problem that can be divided into small ones;
+ A recursive case that resolve the small problem;
+ A base case that stop the recursivity.

NOTE 1: Recursive Functions are similiar to repeat loops, such as for and while.
NOTE 2: Usually when we got a for loop or while loop too big, USUALLY, we can turn them into a recursive function.


## Why avoid them in Python when we got a large number of recursions?
We must have attention when bulding recursive functions, mainly in Python. When we creat a recursive function we are exposed to the risk of creat a state of Stack Overflow. This is the name of what happens when we overpass the maximum limit of recursivity inside the call stack. It will raise us an Exception called RecursionError, that is the Python warning us that's something wrong in our code and if he continues to execute the code, he may "blow" our computer up (the computer's memory). That's why our base case to stop the recursivity is so important.
Now that we understand what happens under the covers, we must pay attention cause we may break our code even though it's right! Why can it happens? The Python (VS Code) has a recursivity limit in the call back, that is 1000 recursions. When we surpass this limit the code breaks and we have the same exception (RecursionError).

NOTE 3: Personally, i would not recomend build a recursive function when you got more than 500~600 recursions, preferring the for loops and while loops, but, there is a manner that we can bypass the limit situation (again, it's not a recomandation, avoid this approach) importing the module sys. See below:
+ import sys
+ sys.setrecursionlimit(new_limit)
+ The "new_limit" is a int number that define a new limit of recursions, you can set, for example a new limit of 2000 recursions.


## Examples of Recursive Functions

<li><a href="/src/"> Code</a></li>


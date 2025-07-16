# Week 4: Libraries
# Using Packages
# import cowsay
# import sys

# if len(sys.argv) == 2:
#     # cowsay.cow("hello, " + sys.argv[1])
#     cowsay.trex("hello, " + sys.argv[1])


# Using my own library
import sys
from sayings import hello

# only call the function when arg provided
if len(sys.argv) == 2:
    hello(sys.argv[1])

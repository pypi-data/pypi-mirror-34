###############################################################################
    Sheldon

    Sheldon Cooper ALWAYS points out what [he thinks] is wrong with people and
    their work.

      by

    Pablo Ordorica <pablo.ordorica@nablazerolabs.com>
###############################################################################

This package provides a tool to find all the divisions in Python source code in
order to facilitate updating Python 2 code to Python 3. (Specify the Python 
source code extensions in the sheldon module)

It is known that divisions in Python 3 always result in a float unlike divi-
sions in Python 2 that result in an int. Therefore, it's imperative to point 
out where divisions are being executed when updating Python code.

####
# To run Sheldon, run the leonard.py script with Python 3. The package contains
# a Pipfile & Pipfile.lock for the virtualenv of Sheldon.
####

The package contains a tests/ folder with python source files to test Sheldon

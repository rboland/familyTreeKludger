Family Tree Kludger
===================

The given string has pipe delimited nodes that represent family members in a family tree. Each node is a CSV with the values being "parent_id, node_id, node_name". Write a method that takes an input string and return a single result that represents the data as a hierarchy (root, children, siblings, etc).
Sample input: "null,0,grandpa|0,1,son|0,2,daugther|1,3,grandkid|1,4,grandkid|2,5,grandkid|5,6,greatgrandkid"
• Solve it in any language that you prefer
• Display the hierarchical result any way you prefer (as long as the parent/child connections are clear)

I chose Python.

Main Python file
----------------

https://github.com/rboland/familyTreeKludger/blob/master/venv/ftk.py

Pytest Unit Test file
---------------------
https://github.com/rboland/familyTreeKludger/blob/master/venv/testFtk.py

Repository Notes:
-----------------
The repo contains an entire PyCharm project, with a virtual environment, 
and PyTest included.  To activate the virtual environment, cd into the venv/
directory and run the appropriate "bin/activate" script.  In Linux, run:
    source bin/activate

When usage is completed, run the command "deactivate".

The only external package used is pytest, so if you already have pytest
installed, using venv may not be necessary.

Usage
-----
    python3 ftk.py "input string"  #Be sure an use the quotes.
If the "input string" argument is not included, the code will use the string 
supplied in the problem statement by default.

Run Tests
---------
    pytest testftk.py #Needs pytest installed, or venv activated.
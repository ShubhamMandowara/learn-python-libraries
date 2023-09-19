- What is pylint : Is python library to help us to list error, enforce coding standards, looks for code smell, give suggestion of code imporvement
- Usage and problem it solves: Its hard to understand the code of any repository so pylint help us to rescue from the problem by checking score of the code before commint

- How to install : pip install pylint
- Use it on code : 

        # without docstring
        
        def function(a, b):
            return a + b
        function()

        # with doc string

        def function(a, b):
            '''funciton to sum the values"""
            return a + b
        function()
- command to run : 
 `pylint fileName.py`




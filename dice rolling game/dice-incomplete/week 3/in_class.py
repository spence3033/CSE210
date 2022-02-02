class Base:

    def __init__(self):
        self._helper()

    def _helper(self):
        print("Helper function")

    def __helper2(self):
        print("Helper 2 function")
    
x = Base()

print("Trying to call subfunction")

x._helper()

# This won't work because __helper2() is private.
# But the code below the comment is possible as a side door so to speak.
# x.__helper2()

x._Base__helper2()
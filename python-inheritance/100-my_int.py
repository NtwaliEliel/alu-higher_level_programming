#!/usr/bin/python3


"""No module imported"""


class MyInt(int):

    """Inherits from int"""
    
    def __eq__(self, other):
        """Inverts eq"""
        return super(MyInt, self).__ne__(other)

    def __ne__(self, other):
        """Inverts ne"""
        return super(MyInt, self).__eq__(other)

class Tree:
    '''
    This is realization of a tree for exact project
    '''
    def __init__(self, data):
        '''
        obj, str -> None
        This method initializes an object
        '''
        self.data = data
        self._left = None
        self._right = None

    def set_left(self, value):
        '''
        obj, str -> None
        This puts needed value on the left
        '''
        self._left = value

    def get_left(self):
        '''
        obj, str -> None
        This returns needed value on the left
        '''
        return self._left

    left = property(fset=set_left, fget=get_left)

    def set_right(self, value):
        '''
        obj, str -> None
        This puts needed value on the right
        '''
        self._right = value

    def get_right(self):
        '''
        obj, str -> None
        This returns needed value on the right
        '''
        return self._right

    def __repr__(self):
        '''
        obj -> str
        This method represents object
        '''
        return f"{self.data}"


    right = property(fset=set_right, fget=get_right)

    def is_empty(self):
        '''
        obj -> bool
        This method checks whether tree is empty
        '''
        return self._left is None and self._right is None
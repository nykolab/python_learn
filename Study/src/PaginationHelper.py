     
    
class PaginationHelper(object):
    '''
    The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page. 
    The types of values contained within the collection/array are not relevant. Examples:
    
    >>> helper = PaginationHelper(['a','b','c','d','e','f'], 4)
    >>> print helper.page_count()
    2
    >>> print helper.item_count()
    6

    helper.pages(0) # ['a', 'b', 'c', 'd']
    helper.pages(100) # []
    
    helper.page_item_count(0)  # should == 4
    helper.page_item_count(1) # last page - should == 2
    helper.page_item_count(2) # should == -1 since the page is invalid# 
    
    # page_index takes an item index and returns the page that it belongs on
    helper.page_index(5) # should == 1 (zero based index)
    helper.page_index(2) # should == 0
    helper.page_index(20) # should == -1
    helper.page_index(-10) # should == -1 because negative indexes are invalid
    
    '''
        
    def __init__(self, items, pages):
        if hasattr(items, "__iter__"):
            self.items = items
        if isinstance(pages, int):
            self.pages = pages

    def page_count(self):
        return (len(self.items) / self.pages)+1
    
    def item_count(self):
        return len(self.items)
    
    def pages(self):
        
        pass
        
# ===============================================

if __name__ == '__main__':
    import doctest
    doctest.testmod()
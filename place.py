# Create your Place class in this file

class Place:
    '''define the class place，add property of name，country, priority, is_visited to the class'''
    def __init__(self, name='', country='', priority=0, is_visited=False):
        self.name = name
        self.country = country
        self.priority = priority
        self.is_visited = is_visited

    def __str__(self):
        string = 'Name: ' + self.name
        string += ', Country: ' + self.country
        string += ', Priority: ' + str(self.priority)
        if self.is_visited:
            string += ', Visited.'
        else:
            string += ', Not visited.'
        return string

    def mark_visited(self):
        self.is_visited = True

    def mark_unvisited(self):
        self.is_visited = False

    def is_important(self):
        if self.priority <= 2:
            return True
        else:
            return False

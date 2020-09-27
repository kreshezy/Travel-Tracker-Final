"""..."""
import pandas as pd
from place import Place

# Create your PlaceCollection class in this file

class PlaceCollection:
    '''set up place collection'''
    def __init__(self):
        self.places = []

    def load_places(self, filename):
        '''read places from file'''
        data = pd.read_csv(filename, header=None)
        for value in data.values:
            value = value.tolist()
            is_visited = value[-1] == 'visited'
            self.places.append(
                Place(value[0], value[1], int(value[2]), is_visited))

    def add_place(self, place):
        self.places.append(place)

    def save_place(self, filename):
        f = open(filename, 'w')
        for place in self.places:
            '''write every single places to the file'''
            result = place.name + "," + \
                place.country + ',' + str(place.priority)
            if place.is_visited:
                result += ',v'
            else:
                result += ',n'
            f.write(result + '\n')
        f.close()

    def get_unvisited_number(self):
        '''get all unvisited numbers of places'''
        count = 0
        for place in self.places:
            if not place.is_visited:
                count += 1
        return count

    def sort(self, key, ascending=True):
        '''sort the cities in a custom order by priority'''
        reverse = not ascending
        if key == 'name':
            self.places = sorted(self.places, key=lambda x: [
                x.name, x.priority], reverse=reverse)
        if key == 'country':
            self.places = sorted(self.places, key=lambda x: [
                x.country, x.priority], reverse=reverse)
        if key == 'priority':
            self.places = sorted(self.places, key=lambda x: [
                x.priority, x.priority], reverse=reverse)
        if key == 'visited':
            self.places = sorted(self.places, key=lambda x: [
                x.is_visited, x.priority], reverse=reverse)

    def __str__(self):
        string = 'There are {0} places, and {1} unvisited places.\n'\
            .format(len(self.places), self.get_unvisited_number())
        for i in range(len(self.places)):
            string += str(i+1) + ': ' + str(self.places[i]) + '\n'
        return string

"""
Name:Shizheng Li
Date:Sep.26
Brief Project Description:This project is the hardest one I had even done since I learned programming. The first part of this project is asked students
                                            to use Class subject to improve their codes of assignment 1. The second part is GUI program, and I consider that two parts are
                                            challengeable. Fortunately, in this project, there are some sources provided to students, and its quite useful. By referring
                                            to these sources, and the codes in previous practicals，and few ideas from internet. I finished this project difficultly,
                                            and tried my best to avoid making the same mistakes in my assignment 1. Now, after several times of testing, I personally
                                            think that all the parts are working without any mistakes. On the other hand, this project also helped me significantly
                                            improved my logic, knowledge, and experience of programming. Overall, it is a very valuable and challengeable assignment for me.
                                                                                                                                    
GitHub URL:
"""
# Create your main program in this file, using the TravelTrackerApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from kivy.properties import ListProperty

from place import Place
from placecollection import PlaceCollection

SORT_FIELD = {'Visited': 'visited', 'Priority': 'priority', 'Country': 'country', 'Name': 'name'}
FILE_PATH = "places.csv"


def placeBtnStyle(place, btn):
    '''Set the text and background color of the buttons according to the place object'''
    if place.is_visited:
        btn.text = '{} in {},priority {} (visited)'.format(place.name, place.country, place.priority)
    else:
        btn.text = '{} in {},priority {}'.format(place.name, place.country, place.priority)
        btn.background_color = [0.2, 0.6, 1, 1]


def getUnvisitedHighPriority(place_collection):
    '''Get high priority in unvisited places'''
    priority = 0
    for place in place_collection.places:
        if place.is_visited:
            continue
        if place.priority > priority:
            priority = place.priority
    return priority


class TravelTrackerApp(App):
    '''A kivy demo'''
    current_sort = StringProperty()
    sort_by = ListProperty()

    def build(self):
        '''build Kivy app from the kv file'''
        self.title = "TravelTracker"
        self.root = Builder.load_file('app.kv')
        self.sort_by = SORT_FIELD.keys()
        self.current_sort = self.sort_by[0]

        self.place_collection = PlaceCollection()
        self.place_collection.load_places(FILE_PATH)
        self.place_collection.sort(list(SORT_FIELD.values())[0])
        self.updateUnvisitedInfo()
        self.setupBtns()

        return self.root

    def on_stop(self):
        '''Called before kivy window destroyed'''
        self.place_collection.save_place(FILE_PATH)

    def updateUnvisitedInfo(self):
        '''update unvisited info show in top bar'''
        self.root.ids.bar_top.text = 'Places to visit:{}'.format(self.place_collection.get_unvisited_number())

    def setupBtns(self):
        '''Set the buttons according to place in place_collection'''
        self.root.ids.btns_container.clear_widgets()
        for place in self.place_collection.places:
            btn = Button()
            placeBtnStyle(place, btn)
            btn.place = place
            btn.bind(on_press=self.btnPressed)
            self.root.ids.btns_container.add_widget(btn)

    def btnPressed(self, btn):
        '''Handle place button pressed'''
        btn.place.is_visited = not btn.place.is_visited
        priority = getUnvisitedHighPriority(self.place_collection)
        if btn.place.is_visited:
            if btn.place.priority >= priority:
                s = 'You visited {}. Great travelling!'
            else:
                s = 'You visited {}.'
        else:
            if btn.place.priority >= priority:
                s = 'You need to visit {}. Get going!'
            else:
                s = 'You need to visit {}.'
        self.root.ids.bar_bottom.text = s.format(btn.place.name)
        self.place_collection.save_place(FILE_PATH)
        self.updateUnvisitedInfo()
        self.setupBtns()

    def change_sort(self, text):
        '''Handle sort field changed'''
        if not hasattr(self, 'place_collection'):
            return
        self.place_collection.sort(SORT_FIELD[text])
        self.current_sort = text
        self.setupBtns()

    def handle_add(self):
        '''Handle add new place button pressed'''
        name = self.root.ids.input_name.text
        country = self.root.ids.input_country.text
        priority = self.root.ids.input_priority.text
        if '' in [name, country, priority]:
            self.root.ids.bar_bottom.text = 'All fields must be completed'
            return
        if not priority.isdigit():
            self.root.ids.bar_bottom.text = 'Please enter a valid number'
            return
        priority = int(priority)
        if priority < 1:
            self.root.ids.bar_bottom.text = 'Priority must be > 0'
            return
        self.place_collection.add_place(Place(name, country, priority, False))
        self.place_collection.save_place(FILE_PATH)
        self.updateUnvisitedInfo()
        self.setupBtns()
        self.handle_clear()
        self.root.ids.bar_bottom.text = '{} in {},priority {} added'.format(name, country, priority)

    def handle_clear(self):
        '''Handle clear button pressed'''
        self.root.ids.input_name.text = ''
        self.root.ids.input_country.text = ''
        self.root.ids.input_priority.text = ''
        self.root.ids.bar_bottom.text = ''

if __name__ == '__main__':
    TravelTrackerApp().run()

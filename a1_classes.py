"""..."""
# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class

from place import Place
import pandas as pd
from placecollection import PlaceCollection

def display(df):
    df.sort('visited')
    print(str(df))
    if df.get_unvisited_number() == 0:
        print('{} places. No places left to visit. Why not add a new place?'.format(
            format(len(df.places))))
    else:
        print('{} places. You still want to visit {} places.'.format(
            len(df.places), df.get_unvisited_number()))
    return df.get_unvisited_number(), len(df.places) - df.get_unvisited_number()

def add(df):
    while True:
        name = input('Name: ')
        if name == '':
            print('Input can not be blank')
            continue
        break
    while True:
        country = input('Country: ')
        if country == '':
            print('Input can not be blank')
            continue
        break
    while True:
        priority = input('Priority: ')
        if priority.isdigit():
            priority = eval(priority)
            if priority <= 0:
                print('Number must be > 0')
                continue
        else:
            print('Invalid input; enter a valid number')
            continue
        break
    
    df.add_place(Place(name, country, priority, False))
    print(name+' in '+country+' (priority', priority, ') added to Travel Tracker')

def mark(df):
    n, v = display(df)
    if n == 0:
        print('No unvisited places')
        return
    while True:
        m = input('Enter the number of a place to mark as visited\n')
        if m.isdigit():
            m = eval(m)
            if m <= 0:
                print('Number must be > 0')
                continue
            elif n < m <= n+v:
                print('That place is already visited')
                continue
            elif m > n+v:
                print('Invalid place number')
                continue
            else:
                print("{} in {} visited!".format(
                    df.places[m-1].name, df.places[m-1].country))
                df.places[m-1].mark_visited()
        else:
            print('Invalid input; enter a valid number')
            continue
        break

def save(df):
    df.save_place('places.csv')
    print('{} places saved to places.csv'.format(len(df.places)))
    print('Have a nice day :)')

def main():
    print('Travel Tracker 1.0 - by Shizheng Li')
    place_collection = PlaceCollection()
    place_collection.load_places("places.csv")
    rows = len(place_collection.places)
    print('{} places loaded from place.csv'.format(rows))

    while True:
        print('Menu:')
        print('L - List places')
        print('A - Add new place')
        print('M - Mark a place as visited')
        print('Q - Quit')
        choice = input().lower()
        if choice == 'l':
            display(place_collection)
        elif choice == 'a':
            add(place_collection)
        elif choice == 'm':
            mark(place_collection)
        elif choice == 'q':
            save(place_collection)
            return
        else:
            print('Invalid menu choice')

main()

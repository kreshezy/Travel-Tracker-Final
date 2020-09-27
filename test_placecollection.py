from placecollection import PlaceCollection
from place import Place

def run_tests():
    """Test PlaceCollection class."""

    # Test empty PlaceCollection (defaults)
    print("Test empty PlaceCollection:")
    place_collection = PlaceCollection()
    print(place_collection)
    assert not place_collection.places  # an empty list is considered False

    # Test loading places
    print("Test loading places:")
    place_collection.load_places('places.csv')
    print(place_collection)
    # assuming CSV file is non-empty, non-empty list is considered True
    assert place_collection.places

    # Test adding a new Place with values
    print("Test adding new place:")
    place_collection.add_place(Place("Smithfield", "Australia", 5, False))
    print(place_collection)

    # Test sorting places
    print("Test sorting - priority:")
    place_collection.sort("priority")
    print(place_collection)

    # TODO: Add more sorting tests
    print('Test sorting - is visited:')
    place_collection.sort('visited')
    print(place_collection)
    
    # TODO: Test saving places (check CSV file manually to see results)
    place_collection.save_place('place.csv')
    
    # TODO: Add more tests, as appropriate, for each method 
    print('Test get_unvisited_number:')
    place_collection.add_place(Place())
    assert place_collection.get_unvisited_number() == 6

run_tests()

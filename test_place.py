from place import Place

def run_tests():
    """Test Place class."""
    print("Test empty place:")
    default_place = Place()
    print(default_place)
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.is_visited

    # Test initial-value place
    print("Test initial-value place:")
    new_place = Place("Malagar", "Spain", 1, False)
    # TODO: Write tests to show this initialisation works
    assert new_place.name == 'Malagar'
    assert new_place.country == 'Spain'
    assert new_place.priority == 1
    assert not new_place.is_visited

    # TODO: Add more tests, as appropriate, for each method
    new_place.mark_visited()
    assert new_place.is_visited
    assert new_place.is_important()
    print(str(new_place))
    assert str(new_place) == 'Name: Malagar, Country: Spain, Priority: 1, Visited.'

run_tests()

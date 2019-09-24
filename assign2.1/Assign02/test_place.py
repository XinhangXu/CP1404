"""(Incomplete) Tests for Movie class."""
from Assign02.place import Place


def run_tests():
    """Test Place class."""

    # Test empty movie (defaults)
    print("Test empty place:")
    default_place = Place()
    print(default_place)
    assert default_place.title == ""
    assert default_place.category == ""
    assert default_place.year == 0
    assert not default_place.is_watched

    # Test initial-value movie
    initial_movie = Place("Thor: Ragnarok", 2017, "Comedy", True)
    # TODO: Write tests to show this initialisation works

    # TODO: Add more tests, as appropriate, for each method


run_tests()

"""
(incomplete) Tests for BookList class
"""
from assign2.placelist import PlaceList
from assign2.place import Place

# test empty BookList
place_list = PlaceList()

assert len(place_list.placelists) == 0

# test loading books
place_list.placelists()

assert len(place_list.placelists) > 0  # assuming CSV file is not empty

print(place_list)
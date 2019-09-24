"""
(incomplete) Tests for Book class
"""
from assign2.place import Place

place = Place()
print(place)
assert place.city == ""
assert place.country == ""
assert place.priority == 0

place2 = Place("aaa", "aaaa", 2, 'n')

print(place2)
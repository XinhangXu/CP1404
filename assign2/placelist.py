from assign2.place import Place
from operator import attrgetter

class PlaceList:

    def __init__(self):
        # initialize
        placelists = [] #created an open list
        self.placelists = placelists

    def __getitem__(self, item):
        return self.placelists[item]

    def __str__(self):
        # for testing test_placelist"""
        return self.placelists

    def add_place(self,city,country,priority):
        # to add a new place
        placebook = Place(city,country,priority,'n')
        self.placelists.append(placebook)

    def listplace(self):
        # read the csv file
        f_read = open("places_copy.csv", 'r')
        for index, data in enumerate(f_read.readlines()):
            data = data.strip()
            divide = data.split(",")
            list_place = Place(divide[0],divide[1],divide[2], divide[3])
            self.placelists.append(list_place)
        f_read.close()
        return self.placelists

    def sort_place(self):
        # sorting based priority
        sort = self.placelists.sort(key=attrgetter('priority'))
        return sort

    def save_place(self):
        # saves into csv file from placelists"""
        f_write = open("places.csv", "w")
        for each in range(len(self.placelists)):
            item = self.placelists[each]
            each = "{},{},{},{}\n" .format(item.city,item.country,item.priority,item.status)
            f_write.write(each)
        f_write.close()

    def visited_place(self):
        # to count number of place visited
        visited_places = 0
        for i in range(len(self.placelists)):
            if self.placelists[i].status == 'v':
                visited_places = visited_places + 1
        total_visited_places = "Total visited places: {}" .format(visited_places)
        return total_visited_places

    """def extraPages(self,pages):
        to check for extra pages, more than 500 or so
        if int(pages) > 500:
            return True
        else:
            return False"""



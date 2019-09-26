from place import Place


class PlacesCollection:
    def __init__(self):
        # create a list called place_list, to store data from .csv file
        self.place_list = []

# read data from .csv file
    def load_places(self):
        f_reader = open("places.csv", "r")
        for place in f_reader.readlines():
            file = place.split(",")
            self.place_list.append([Place(file[0], file[1], int(file[2]), file[3].strip())])
        f_reader.close()

# function add place to place_list[]
    def add_place(self, name, country, priority):
        self.place_list.append([Place(name, country, priority, 'n')])
        self.write_csv()

# sort data in 3 ways: by city, country, priority
    def sort(self, sort_method):
        if sort_method == "Name":
            self.place_list.sort(key=lambda sort: (sort[0].name, sort[0].country))
        elif sort_method == "Country":
            self.place_list.sort(key=lambda sort: sort[0].country)
        elif sort_method == "Priority":
            self.place_list.sort(key=lambda sort: (sort[0].priority, sort[0].country))
        else:
            self.place_list.sort(key=lambda i: (i[0].status, i[0].country))

# count unvisited place
    def unvisited_places_count(self):
        unvisited_places = 0
        for place in self.place_list:
            if place[0].status == 'n':
                unvisited_places += 1
        return unvisited_places

# count visited place
    def visited_places_count(self):
        visited_places = 0
        for place in self.place_list:
            if place[0].status == 'v':
                visited_places += 1
        return visited_places

# for getting place, if true, return place name
    def get_place(self, place):
        for pname in self.place_list:
            if pname[0].name == place:
                return pname[0]

# Write csv file after finishing
        # import place_list to .csv file
    def write_csv(self):
        f_writer = open('places.csv', 'w')
        for item in self.place_list:
            f_writer.write(
                item[0].name + "," + item[0].country + "," + str(item[0].priority) + "," + item[0].status + "\n")
        f_writer.close()

    def __str__(self):
        return self.place_list

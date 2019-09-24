# Create PlaceCollection class in this file

from Assign02.place import Place
from operator import attrgetter

class PlaceCollection:

    def __init__(self):
        """initializing the program"""
        # built an array [][]
        data_list = []
        for i in range(200):
            data_list.append([0] * 5)
            # [0] place, [1] country, [2] priority, [3] 'v' or 'n'
        self.data_list = data_list

    def __getitem__(self, item):
        return self.data_list[item]

    def __str__(self):
        """used for testing test_placecollection"""
        return self.data_list

    # fuction for sort list by priority
    def takeThird(val):
        return int(val[2])

    def list_place(self,city,country,priority,status):
        data_list.sort(key=takeThird())  # sort by priority, no: descending -> reverse = True
        n = 1  # the order number of unvisited place
        # print unvisited places first, add * and order number
        for line in data_list:
            if line[3] == 'n':
                print("*{}. ".format(n), end="")
                print("{:12} in  {:16} priority {:>4}".format(line[0], line[1], line[2]))
                n = n + 1
        # print visited places, add order number
        for line_x in data_list:
            if line_x[3] == 'v':
                print(" {}. ".format(n), end="")
                print("{:12} in  {:16} priority {:>4}".format(line_x[0], line_x[1], line_x[2]))
                n = n + 1
        # show the number of total places and unvisited places
        place_total = 0
        unvisited_place = 0
        for line_n in data_list:
            if line_n[3] == 'n' or line_n[3] == 'v':
                place_total = place_total + 1
            if line_n[3] == 'n':
                unvisited_place = unvisited_place + 1
        print("{} places. You still want to visit {} places.".format(int(place_total), int(unvisited_place)))

    def add_place(self,city,country,priority,status):
        city = str(input(" Name: "))
        while city == "":
            print("Input can not be blank")
            name = str(input(" Name: "))
        else:
            country = str(input(" Country: "))
            while country == "":
                print("Input can not be blank")
                country = str(input(" Country: "))
            else:
                index = 0
                priority = input(" Priority: ")
                while index == 0:
                    if priority == "":  # none
                        print("Input can not be blank")
                        index == 0
                        priority = input(" Priority: ")
                    else:  # not none
                        if priority.isdigit():  # is number
                            index = 1
                            data_list.append([name, country, priority, 'n', ''])
                            print("{} in {} (priority {}) added to Travel Tracker".format(name, country, priority))
                            show_menu()
                            command = input(">>> ").lower()
                        elif priority.startswith('-') and priority[1:].isdigit():  # it < 0
                            print("Number must be > 0")
                            index == 0
                            priority = input(" Priority: ")
                        else:
                            print("Invalid input; enter a valid number")
                            index == 0
                            priority = input(" Priority: ")

    def mark_place(self):
        # show place list as command'l'
        data_list.sort(key=takeThird)  # sort by priority, no: descending -> reverse = True
        n = 1  # the order number of unvisited place
        # print unvisited places first, add * and order number
        for line in data_list:
            if line[3] == 'n':
                print("*{}. ".format(n), end="")
                print("{:12} in {:12} priority {:12}".format(line[0], line[1], line[2]))
                line[4] = n
                n = n + 1
        # print visited places, add order number
        for line_x in data_list:
            if line_x[3] == 'v':
                print(" {}. ".format(n), end="")
                print("{:12} in {:12} priority {:12}".format(line_x[0], line_x[1], line_x[2]))
                line_x[4] = n
                n = n + 1
        # show the number of total places and unvisited places
        place_total = 0
        unvisited_place = 0
        for line_n in data_list:
            if line_n[3] == 'n' or line_n[3] == 'v':
                place_total = place_total + 1
            if line_n[3] == 'n':
                unvisited_place = unvisited_place + 1
        print("{} places. You still want to visit {} places.".format(int(place_total), int(unvisited_place)))
        # ask for entering place would like to mark
        print("Enter the number of a place to mark as visited")
        mark_in = input(">>> ")
        index = 0
        while index == 0:
            if mark_in == "":  # none
                print("Input can not be blank")
                index == 0
                mark_in = input(">>> ")
            else:  # not none
                if mark_in.isdigit():  # is a vaild number
                    mark_num = int(mark_in)
                    for line in data_list:
                        if line[4] == mark_num:  # when number_in(the num shows on displaying list) == order number
                            # check the place is 'v' or 'n'
                            if line[3] == 'n':
                                index = 1
                                line[3] = 'v'
                                print("{} in {} visited!".format(line[0], line[1]))
                                show_menu()
                                command = input(">>> ").lower()
                            else:
                                index = 0
                                print("That place is already visited")
                                mark_in = input(">>> ")
                elif mark_in.startswith('-') and mark_in[1:].isdigit():  # it < 0
                    print("Number must be > 0")
                    index == 0
                    mark_in = input(">>> ")
                else:
                    print("Invalid input; enter a valid number")
                    index == 0
                    mark_in = input(">>> ")
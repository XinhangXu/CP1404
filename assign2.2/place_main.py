
"""
Name: Xu Xinhang
Date: 26/09/2019
Brief Project Description: An functional GUI based on assignment_01
GitHub URL: https://github.com/XinhangXu/CP1404
Tips: The final submission of assignment_02 will be named "XinhangXu_13757132_A2"
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from place_collection import PlacesCollection

# Main class of this program, provide some methods called by other classes
# Kivy with task for button label


class TravelTracker(App):

    def __init__(self):
        super().__init__()
        self.place_list = PlacesCollection()
        self.sort_label = Label(text="Sort by:")

        # sort by country, priority and visited
        self.spinner = Spinner(text="Name", values=( "Country", "Priority", "Visited"))

        # adding a new place
        self.add_label = Label(text="New Place:")

        # input the name
        self.name_label = Label(text="Name: ")
        self.name_input = TextInput(write_tab=False, multiline=False)

        # input the country
        self.country_label = Label(text="Country: ")
        self.country_input = TextInput(write_tab=False, multiline=False)

        # input the priority
        self.priority_label = Label(text="Priority: ")
        self.priority_input = TextInput(write_tab=False, multiline=False)

        # add button for 'add place' and 'clear fields
        self.add_button = Button(text="Add place")
        self.top_label = Label(id="count_place_label")
        self.clear_button = Button(text="Clear Fields")

    def build(self):

        # Build GUI by using kivy and performs tasks on boot.
        # Loads items as a list of lists, into items as lists

        self.title = "TravelTracker 2.0 by Xu Xinhang"
        self.root = Builder.load_file('app.kv')
        self.place_list.load_places()
        self.build_widgets_left_col()
        # input on the left side
        self.build_widgets_right_col()
        # output on the right side
        return self.root

    def build_widgets_left_col(self):

        # input and choose type
        # including the city , country, priority,  add button and clear button.

        self.root.ids.left_layout.add_widget(self.sort_label)
        self.root.ids.left_layout.add_widget(self.spinner)
        self.root.ids.left_layout.add_widget(self.add_label)
        self.root.ids.left_layout.add_widget(self.name_label)
        self.root.ids.left_layout.add_widget(self.name_input)
        self.root.ids.left_layout.add_widget(self.country_label)
        self.root.ids.left_layout.add_widget(self.country_input)
        self.root.ids.left_layout.add_widget(self.priority_label)
        self.root.ids.left_layout.add_widget(self.priority_input)
        self.root.ids.left_layout.add_widget(self.add_button)
        self.root.ids.left_layout.add_widget(self.clear_button)
        self.root.ids.top_layout.add_widget(self.top_label)

        self.add_button.bind(on_release=self.control_add_place)
        self.clear_button.bind(on_release=self.clear_fields)
        self.spinner.bind(text=self.places_sort)

    def places_sort(self, *args):
        self.place_list.sort(self.spinner.text)
        self.root.ids.right_layout.clear_widgets()
        self.build_widgets_right_col()

    def control_add_place(self, *args):
        if str(self.name_input.text).strip() == '' or str(self.country_input.text).strip() == '' or str(self.priority_input.text).strip() == '':
            self.root.ids.bottom_layout.text = "All the fields must be filled !!"
        else:
            try:
                if int(self.priority_input.text) <= 0:
                    self.root.ids.bottom_layout.text = "ERROR: Priority must > 0"
                else:
                    self.place_list.add_place(self.name_input.text, self.country_input.text, int(self.priority_input.text))
                    self.place_list.sort(self.spinner.text)
                    self.clear_fields()
                    self.root.ids.right_layout.clear_widgets()
                    self.build_widgets_right_col()
            except ValueError:
                self.root.ids.bottom_layout.text = "Enter a number in the priority field"

    def build_widgets_right_col(self):

        # display the top column, show how many place left for visit, give color

        self.top_label.text = "Visited: {} places. Remain{} places unvisited.".format(
            str(self.place_list.visited_places_count()), self.place_list.unvisited_places_count())
        for place in self.place_list.place_list:
            if place[0].status == "v":
                travel_display_button = Button \
                    (text="'{}' in  {} ({}) visited".format(place[0].place, place[0].country, place[0].priority),
                                               id=place[0].place)
                travel_display_button.background_color = [88, 88, 0.65, 0.4]

            else:
                travel_display_button = Button \
                    (text="'{}' in  {} ({}) unvisited".format(place[0].place, place[0].country, place[0].priority), id=place[0].place)
                travel_display_button.background_color = [83, 88, 0.3, 0.3]
            travel_display_button.bind(on_release=self.visit_Places)
            self.root.ids.right_layout.add_widget(travel_display_button)

    # for user to add a new place including name, country and priority

    def clear_fields(self, *args):
        # clean all the field
        self.name_input.text = ""
        self.country_input.text = ""
        self.priority_input.text = ""
        self.root.ids.bottom_layout.text = ""

    # visit_places using to def the 'n' and 'v' and tell the user what
    # they need or the place that they visit or unvisited.

    def visit_Places(self, button):
        # convert unvisited to visited
        if self.place_list.get_place(button.id).status == 'n':
            self.place_list.get_place(button.id).status = 'v'
            self.root.ids.bottom_layout.text = "You need to visit {}".format \
                (str(self.place_list.get_place(button.id).place))

        else:# convert visited to unvisited
            self.place_list.get_place(button.id).status = 'n'
            self.root.ids.bottom_layout.text = "You visited {}".format(str(self.place_list.get_place(button.id).place))
        self.places_sort()
        self.root.ids.right_layout.clear_widgets()
        self.build_widgets_right_col()

if __name__ == '__main__':
    app = TravelTracker()
    app.run()


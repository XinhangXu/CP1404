"""
Name: Xu Xinhang 13757132
Date: Begin at 20.09.2019
Brief Project Description: Places Recorder
GitHub URL:
"""
# Create main program, using the PlaceToMarkApp class

from kivy.app import App
from kivy.app import Builder
from assign2.place import Place
from assign2.placelist import PlaceList
from kivy.uix.button import Button

class ReadingListApp(App):
    def __init__(self, **kwargs):
        "declaring variables for class place and placelist"
        super(ReadingListApp, self).__init__(**kwargs)
        place_lists = PlaceList()
        place_items = Place()
        self.place_lists = place_lists
        self.place_items = place_items
        self.place_lists.listplace()

    def build(self):
        """loading kv file"""
        self.title = "Travel Tracker 2.0 by Xinhang Xu "
        self.root = Builder.load_file("app.kv")
        return self.root

    def on_start(self):
        """initiates the program"""
        self.place_button(way='req')
        self.root.ids.required_place_button.state = 'down'
        self.root.ids.completed_place_button.state = 'normal'

    def on_stop(self):
        "runs after program ends"
        self.place_lists.save_places()

    def add_places(self, text_city, text_country, text_priority):
        """kivy code for add places function"""
        try:
            place_priority = int(text_priority)
            if text_city=="" or text_country=="" or text_priority=="":
                self.root.ids.description.text = " WARNING: All the fields must be filled !!"
            elif place_priority <= 0:
                self.root.ids.description.text = "ERROR: Priority must > 0"
                self.root.ids.text_priority.text = ""
                self.root.ids.text_priority.value = ""
            else:
                self.place_lists.add_place(text_city, text_country, text_priority)
                self.clear_text()
                self.place_lists.sort_place()
                self.on_start()
                self.root.ids.description.text = "{} in {}, priority {} is added".format(text_city, text_country, text_priority)
        except ValueError:
            if text_city=="" or text_country=="" or text_priority=="":
                self.root.ids.description.text = " WARNING: All the fields must be filled !! "
            else:
                self.root.ids.description.text = "Please enter a valid number"
                self.root.ids.text_priority.text = ""
                self.root.ids.text_priority.value = ""

    def required_places(self, instance):
        city = instance.text
        for each in self.place_lists.placelists:
            if each.city == city:
                marking = self.place_items.mark_as_complete(each.status)
                if marking == True:
                    each.status = 'v'
                self.on_start()
                self.root.ids.description.text = "{} marked as completed".format(each.city)

    def completed_places(self,instance):
        city = instance.text
        for each in self.place_lists.placelists:
            if each.city == city:
                self.root.ids.description.text = "{} (completed)".format(each)

    def place_button(self, way):
        """book button for widget box"""
        self.clear_places()
        if way == "req":#button for required books
            for each in range(len(self.place_lists.placelists)):
                if self.place_lists[each].status == 'v':

                    temp_button = Button(text=self.place_lists[each].city)
                    temp_button.bind(on_release=self.required_places)

                #    property_check = self.place_lists.extraPages(self.book_lists[each].pages)
                    #checking length of pages
                #   if page_check == True:
                    #        temp_button.background_color = 1, 2, 1, 1
                    #    else:
                    #        temp_button.background_color = 0, 0.8, 10, 1

                    self.root.ids.box.add_widget(temp_button)

            #total_required_priority = self.place_lists.requiredplaces_priority()
            self.root.ids.place_priority.text = total_required_priority
            self.root.ids.description.text = "Click place to mark them as completed"

        elif way == "com":#button for completed books
            for each in range(len(self.place_lists.placelists)):
                if self.place_lists[each].status == 'u':
                    temp_button = Button(text=self.place_lists[each].city)
                    temp_button.bind(on_release=self.completed_places)
                    temp_button.background_color = 0,1.37,1.37,1
                    self.root.ids.box.add_widget(temp_button)
            total_completed_priority = self.place_lists.completedplaces_priority()
            self.root.ids.description.text = "Click place to show the description"
            self.root.ids.place_priority.text = total_completed_priority

    def select_required_places(self):
        """runs after list required is selected"""
        self.place_button(way='req')
        self.root.ids.required_place_button.state = 'down'
        self.root.ids.completed_place_button.state = 'normal'

    def select_completed_places(self):
        """runs after list completed in selected"""
        self.place_button(way='com')
        self.root.ids.required_place_button.state = 'normal'
        self.root.ids.completed_place_button.state = 'down'

    def clear_places(self):
        """clears button"""
        self.root.ids.box.clear_widgets()

    def clear_text(self):
        """clears text in the add book fields"""
        self.root.ids.text_city.text = ""
        self.root.ids.text_country.text = ""
        self.root.ids.text_priority.text = ""


ReadingListApp().run()

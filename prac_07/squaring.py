from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class SquareNumberApp(App):

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (200, 100)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        result = value ** 2
        self.root.ids.output_label.text = str(result)


SquareNumberApp().run()

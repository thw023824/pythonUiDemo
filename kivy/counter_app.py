import kivy
kivy.require('2.3.1') # Ensure this matches your Kivy version

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import NumericProperty

class CounterLayout(BoxLayout):
    counter = NumericProperty(0)

    def __init__(self, **kwargs):
        super(CounterLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 10

        self.counter_label = Label(text=str(self.counter), font_size='40sp')
        self.bind(counter=self.update_label_text)
        self.add_widget(self.counter_label)

        buttons_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height='50dp')
        
        increment_button = Button(text='Increment', on_press=self.increment)
        buttons_layout.add_widget(increment_button)

        decrement_button = Button(text='Decrement', on_press=self.decrement)
        buttons_layout.add_widget(decrement_button)

        self.add_widget(buttons_layout)

    def increment(self, instance):
        self.counter += 1

    def decrement(self, instance):
        self.counter -= 1
    
    def update_label_text(self, instance, value):
        self.counter_label.text = str(value)

class CounterApp(App):
    def build(self):
        return CounterLayout()

if __name__ == '__main__':
    CounterApp().run()

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        layout.add_widget(Label(
            text='📋 Dashboard',
            font_size='24sp',
            size_hint=(1, 0.2)
        ))

        layout.add_widget(Button(text='➕ Add Medicine', size_hint=(1, 0.15)))
        layout.add_widget(Button(text='⏰ Set Reminder', size_hint=(1, 0.15)))
        layout.add_widget(Button(text='📅 Missed Logs', size_hint=(1, 0.15)))
        layout.add_widget(Button(text='👤 Profile', size_hint=(1, 0.15)))

        self.add_widget(layout)


from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        layout.add_widget(Label(
            text='Medicine Reminder App',
            font_size='24sp',
            size_hint=(1, 0.2)
        ))

        layout.add_widget(Label(
            text='Welcome! Stay healthy by never missing your medicine.',
            font_size='16sp',
            size_hint=(1, 0.2)
        ))

        btn = Button(
            text='Go to Dashboard',
            size_hint=(1, 0.2)
        )
        btn.bind(on_press=self.go_to_dashboard)
        layout.add_widget(btn)

        self.add_widget(layout)

    def go_to_dashboard(self, instance):
        self.manager.current = 'dashboard'




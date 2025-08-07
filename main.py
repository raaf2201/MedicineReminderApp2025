from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from welcome_screen import WelcomeScreen
from dashboard_screen import DashboardScreen

class MedicineReminderApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        return sm

if __name__ == '__main__':
    MedicineReminderApp().run()




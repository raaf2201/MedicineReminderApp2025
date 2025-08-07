from kivy.app import App
from kivy.uix.label import Label

class MedicineReminderApp(App):
    def build(self):
        return Label(text="Hello! This is the Medicine Reminder App")

if __name__ == "__main__":
    MedicineReminderApp().run()

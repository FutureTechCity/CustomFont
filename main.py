from kivy.app import App
from kivy.uix.widget import Widget

class CustomFontScreen(Widget):
    pass

class CustomFontApp(App):
    def build(self):
        return CustomFontScreen()


if __name__ == '__main__':
    CustomFontApp().run()

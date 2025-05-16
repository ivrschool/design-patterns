# factories/theme_factory.py
class LightTheme:
    def background(self): return "white"
    def font(self): return "black"

class DarkTheme:
    def background(self): return "black"
    def font(self): return "white"

class ThemeFactory:
    @staticmethod
    def get_theme(theme_name):
        if theme_name == "light":
            return LightTheme()
        elif theme_name == "dark":
            return DarkTheme()
        else:
            raise ValueError("Unknown theme")

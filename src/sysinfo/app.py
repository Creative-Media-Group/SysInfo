"""
An application for reading systeminfo.
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import psutil
import platform


class SysInfo(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        uname = platform.uname()
        main_box = toga.Box()
        main_box.style.direction = "column"
        
        # Widgets
        system = toga.Label(text=f"System: {uname.system}")

        # add
        main_box.add(system)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return SysInfo()

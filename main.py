# -*- coding: utf-8 -*-

import sys, os

# Set up PATH
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, "lib"))
sys.path.append(os.path.join(parent_folder_path, "plugin"))

# Imports
from flowlauncher import FlowLauncher
import webbrowser


# Plugin extends FlowLauncher class
class Komorebi(FlowLauncher):

    # FlowLauncher provides query with the users's text
    def query(self, param: str = ""):
        """
        When a user activates our plugin, we can retrieve their query by providing a query method.
        Flow Launcher provides the argument query with the users text.
        This method must be part of your plugin class.

        To send a response back, we need to return a list of dictionaries.
        The JsonRPCAction dict allows you to provide a method that will be called by Flow Launcher
        with the parameters you provided.
        """
        return [
            {
                "Title": "Hello World, this is where title goes. {}".format(
                    ("Your query is: " + param, param)[param == ""]
                ),
                "SubTitle": "This is where your subtitle goes, press enter to open Flow's url",
                "IcoPath": "Images/app.png",
                "JsonRPCAction": {
                    "method": "open_url",
                    "parameters": ["https://github.com/Flow-Launcher/Flow.Launcher"],
                },
            }
        ]

    """
    The context menu is activated when the user uses Shift+Enter or right-clicks on a result.
    The context menu is similar to the query method except it does not receive a query argument
    but a data argument with a list of values from the result selected.
    """

    def context_menu(self, data):
        return [
            {
                "Title": "Hello World Python's Context menu",
                "SubTitle": "Press enter to open Flow the plugin's repo in GitHub",
                "IcoPath": "Images/app.png",
                "JsonRPCAction": {
                    "method": "open_url",
                    "parameters": [
                        "https://github.com/Flow-Launcher/Flow.Launcher.Plugin.HelloWorldPython"
                    ],
                },
            }
        ]

    def open_url(self, url):
        webbrowser.open(url)


if __name__ == "__main__":
    Komorebi()

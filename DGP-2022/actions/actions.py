# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
import random
import requests
import datetime as dt 
from typing import Any, Text, Dict, List
# import os

# from oauth2client.service_account import ServiceAccountCredentials
# from googleapiclient.discovery import build

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# Tmaterials_SPREADSHEET_ID = '1rCMJJ2I4wrEYK7kRNI8LNRJrChu-92tc2h0B8YQgNHk'
# classesHours_SPREADSHEET_ID = '1uNnriEN44iDqDMRunvhAcTXs5wqujoUtz4TJnDRxs1Y'

# key_file_location = os.path.join(os.path.expanduser('~'), 'rasa2022dgp-2ef451d6a1cf.json')
# api_key = os.environ['GKEY']
# creds = ServiceAccountCredentials.from_json_keyfile_name(key_file_location, SCOPES)
# service = build('sheets', 'v4', credentials=creds, developerKey=api_key)

# sheet = service.spreadsheets()

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        url = "http://worldtimeapi.org/api/timezone/America/Sao_Paulo";
        json_data = requests. get(url) .json();
        __TIME = dt.datetime.fromtimestamp(json_data["unixtime"]).strftime("%a, %d %b %Y %H:%M:%S");
        # __TIME = dt.now().strftime("%a, %d %b %Y %H:%M:%S");
        dispatcher.utter_message(text=f"A data é {__TIME}")

        return []
        
class ActionGetName(Action):

    def name(self) -> Text:
        return "action_get_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name =  tracker.get_slot('name');
        dispatcher.utter_message(response = "utter_greet_by_name", name = name)

        return []

class ActionGetName(Action):

    def name(self) -> Text:
        return "action_get_ClassesHours"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # result = sheet.values().get(spreadsheetId=classesHours_SPREADSHEET_ID,range="A1").execute()
        # values = result.get('values', [])

        name =  tracker.get_slot('name');
        dispatcher.utter_message(response = "utter_askingAbtClassesHours", name = name)

        return []

class ActionGetName(Action):

    def name(self) -> Text:
        return "action_get_TeacherMaterial"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # result = sheet.values().get(spreadsheetId=Tmaterials_SPREADSHEET_ID,range="A:A").execute()
        # values = result.get('values', [])
        # val=random.choice(list(set(values)))

        name =  tracker.get_slot('Teacher');
        dispatcher.utter_message(response = "utter_askingForTeacherName", Teacher = val)

        return []

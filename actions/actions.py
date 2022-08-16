from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import pandas as pd

df = pd.read_csv("/home/haseeb/Desktop/NLU/CB/files/chatbot_menu - Sheet1.csv")
order = pd.read_csv("/home/haseeb/Desktop/NLU/CB/files/user_menu - Sheet1.csv")

class ActionCheckAvail(Action):

    def name(self) -> Text:
        return "action_check_avail" 

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        item = next(tracker.get_latest_entity_values("item"), None)
        
        avail = False
        list = []
        for index in df.index:
            if item == df["item"][index]:
                list.append(df["item"][index])
                list.append(df["price"][index])
                length = len(order)
                order.loc[length] = list
                avail = True
    
        if avail == True:
            dispatcher.utter_message(f"{item} is added to the menu")
        else:
            dispatcher.utter_message("Item is unavailable")

        return []

class ActionRecommend(Action):

    def name(self) -> Text:
        return "action_recommend" 

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        section = next(tracker.get_latest_entity_values("section"), None)
        avail = False
        
        for index in df.index:
            if section == df["preference"][index] or section == df["type"][index]:
                dispatcher.utter_message(df["item"][index])
                avail = True
                
        if avail == False:
            dispatcher.utter_message("Sorry, We dont serve this type of cuisine.")
            
        return []
    
class ActionViewMenu(Action):

    def name(self) -> Text:
        return "action_view_menu" 

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("Here is the menu: ")
        for index in df.index:
            dispatcher.utter_message(df["item"][index])

        return []

class ActionViewOrder(Action):

    def name(self) -> Text:
        return "action_view_order" 

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        total = 0
        
        dispatcher.utter_message("Here is the order so far: ")
        for index in order.index:
            dispatcher.utter_message(order["item"][index])
            total+=order["price"][index]
        dispatcher.utter_message(f"Total is {total} rupees.")
        dispatcher.utter_message("Shall i confirm?")

        return []
  
class ActionCancelOrder(Action):

    def name(self) -> Text:
        return "action_cancel_order" 

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        order = order[0:0]
        dispatcher.utter_message("Order is Cancelled. ")

        return []  
    

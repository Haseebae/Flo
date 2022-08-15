from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

menu_db = {
    'pizza':1,
    'soup':2,
    'biriyani':3,
    'noodles':4,
    'burger':5,
    'pepsi':6,
    'thumbs up':7,
    'limca':8,
    'appy fizz':9,
}

class ActionCheckAvail(Action):

    def name(self) -> Text:
        return "action_check_avail" #this name is referred in the yml files

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        current_item = next(tracker.get_latest_entity_values("item"), None)
        tz_string = menu_db.get(current_item, None)
        
        if not tz_string:
            msg = f"{current_item} is not available."
            dispatcher.utter_message(text=msg)
            return[]
        
        msg = f"{current_item} is available"
        dispatcher.utter_message(text=msg)

        return []

# class FormDataCollect(FormAction):
#     def item(self) -> Text:
#         return "Form_info"
    
#     @staticmethod
#     def required_slots(tracker: "Tracker") -> List[Text]:
#         return ["item","quantity"]
    
#     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
#         return {
#             "item":[self.from_entity(entity="item")],
#             "quantity":[self.from_entity(entity="quantity")]
#             }
        
#     def submit(
#         self,
#         dispatcher: "CollectingDispatcher",
#         tracker: "Tracker",
#         domain: Dict[Text, Any],
#     ) -> List[EventType]:
        
#         return []
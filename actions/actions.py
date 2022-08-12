
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

class FormDataCollect(FormAction):
    def item(self) -> Text:
        return "Form_info"
    
    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        return ["item","quantity"]
    
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
        return {
            "item":[self.from_entity(entity="item")],
            "quantity":[self.from_entity(entity="quantity")]
            }
        
    def submit(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        
        return []
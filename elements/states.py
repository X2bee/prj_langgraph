from typing import Annotated, Optional
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from selenium import webdriver

class OverallState(TypedDict):
    user_input: str
    messages: Annotated[list, add_messages]
    character_persona_dict: dict

class InputState(TypedDict):
    start_input: str
    
class PersonaState(TypedDict):
    user_input: str
    messages: Annotated[list, add_messages]
    character_persona_dict: dict
    retrieve_check: bool
    retrieval_msg: str
    rewrite_query: str
    tools_call_switch: Annotated[bool, True]

class SearchQueryState(TypedDict):
    messages: Annotated[list, add_messages]
    character_persona_dict: dict
    query_list: list
    selected_query: str
    previous_query: list
    is_revise: bool
    selected_item: str
    select_reason: str
    item_information_origin: list
    item_information_list: list
    item_index: int
    chrome_driver: webdriver.Chrome
    
class EndState(TypedDict):
    messages: Annotated[list, add_messages]
    query_list: list

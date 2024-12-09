from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):

    def __init__(self, **properties):
      self.init_components(**properties)

    def my_first_button_click(self, **event_args):
      """This method is called when the button is clicked"""
      my_message = 'You just cvlicked the button!'
      alert(my_message)


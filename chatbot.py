import random
import re


class Suppporbot:

 negative_res =("no","nope","not a chance","sorry")
 exit_commands = ("quite","pause","exist","goodbye","bye","farewell")

def __init__(self):
   self.support_responses = {
      'ask_about_product': r'.*\s*product.*',
      'technical_support': r'.*technical.*support.*',
       'about_retures': r'.*\s*returnpolicy.*',
       'general_query': r'.*how.*help.*'
   }

def greet(self):
   self.name = input("Hello!Welcome to our customer support.What's your name?\n")
   will_help = input(f"Hi {self.name}, how can I assist you today?\n")
   if will_help in self.negative_res:
      print("Alright have a greate day!")
      return
   self.chat()

def make_exist(self,reply):
   for command in self.exist_commands:
      if command in reply:
         print("Thanks for reaching out. Have a great day!")
         return True
      return False
   

def  chat(self):
      reply = input("Please tell me your query:").lower()
      while not self.make_exist(reply):
         reply = input(self.match_reply(reply))

def match_reply(self,reply):
   for intent , regex_pattern in self.support_responses.items():
      found_match = re.search(regex_pattern,reply)
      if found_match and intent =='ask_about_product':
         return self.ask_about_product()
      elif found_match and intent =='technical_support':
          return self.technical_support()
      elif found_match and intent =='about_returns':
             return self.about_returns()
      elif found_match and intent =='general_query':
              return self.general_query()
   return self.no_match_intent()


def ask_about_product(self):
   responses =("Our product is top-notch and has excellent reviews!\n",
                "You can find all product details on our website.\n")
   return random.choice(responses)
   
def technical_support(self):
   responses=("Please visit our technical support page for detailed assistance.\n",
              "You can also call our tech support helpline for immediate help.\n")
   return random.choice(responses)

def about_reterns(self):
   responses=("We have a 30-day return policy.\n",
              "Please ensure the product is in its original conditions when returning.\n")
   return random.choice(responses)

def general_query(self):
   responses = ("How can I assist you further?\n",
                "Is there anything else you'd like to know?\n")
   return random.choice(responses)

def no_match_intent(self):
   responses = ("I'm sorry, I didn't quite understand that. Can you please rephrase?\n"
                "My apologies, can you provide more details?\n")
   return random.choice(responses)
   
bot = Suppporbot()
bot.greet()
      
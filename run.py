from main import GenericAssistant
import sys

def function_for_greetings():
    print("You triggered the greetings intent!")
    
def function_for_goodbye():
    print("You triggered the goodbye intent!")
    done = False
    while not done:
        response = input("Are you sure you want to leave? (Y/N): ")
        if response.lower() == "y":
            assistant.request_goodbye()
            sys.exit()
        elif response.lower() == "n":
            done = True
        else:
            print("Not a valid response, I'll ask again.")

def function_for_thanks():
    print("You triggered the thanks intent!")

mappings = {
    'greeting' : function_for_greetings, 
    'goodbye' : function_for_goodbye,
    'thanks' : function_for_thanks
}

assistant = GenericAssistant('intents.json', intent_methods=mappings, model_name="test_model")
assistant.train_model()
assistant.save_model()
#assistant.load_model()

done = False

while not done:
    message = input("Enter a message: ")
    
    if message.lower() == "stop":
        done = True
    else:
        assistant.request_response(message)
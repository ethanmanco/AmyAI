from main import GenericAssistant
import sys
import argparse

# Usage
# Training:
# python run.py --model train
# Testing:
# python run.py

def function_for_goodbye():
    done = False
    while not done:
        response = input("Are you sure you want to leave? ")
        if assistant.request_answer(response) == "yes":
            assistant.request_goodbye()
            sys.exit()
        elif assistant.request_answer(response) == "no":
            done = True
        else:
            print("Not a valid response, I'll ask again.")

def function_for_shortcut():
    if phoneType == "Android":
        print("1. Navigate to the application you want to make a shortcut for.")
        print("2. Press and hold the application and drag it upwards.")
        print("3. Let go of the application in the spot of your choice.")
    else:
        print("iPhones do not have shortcuts.")
        print("You should be able to find every application on the home screen.")

def function_for_brightness():
    if phoneType == "Android":
        print("Swipe your finger down from the top of the screen twice to change the brightness slider.")
        print("Thats it!")
    else:
        print("Swipe down from the top right corner of your phone to change the brightness slider.")
        print("Thats it!")



mappings = {
    'goodbye' : function_for_goodbye,
    'shortcut' : function_for_shortcut,
    'brightness' : function_for_brightness
}

argScan = argparse.ArgumentParser()
argScan.add_argument("--model", required=False)
args = argScan.parse_args()
modelAction = args.model

assistant = GenericAssistant('intents.json', intent_methods=mappings, model_name="test_model")

if (modelAction == 'train'):
    assistant.train_model()
    assistant.save_model()
else:
    assistant.load_model()

done = False

while not done:
    response = input("Are you using an iPhone or Android? ")
    
    if assistant.request_answer(response) == "iPhone":
        phoneType = "iPhone"
        print("(Troubleshooting iPhone)")
        done = True
    elif assistant.request_answer(response) == "Android":
        phoneType = "Android"
        print("(Troubleshooting Android)")
        done = True
    else:
        print("Not a valid response, I'll ask again.")


assistant.request_greeting()

done = False

while not done:
    message = input("Enter a message: ")
    
    if message.lower() == "stop":
        done = True
    else:
        assistant.request_response(message)
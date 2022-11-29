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

def printing():
    if phoneType == "Android":
        print("1. Open the app you want to print from.")
        print("2. Tap the three dots at the top right of the screen, or swipe upwards on your image.")
        print("3. Swipe right on the top part of the menu until the 'Print' option is shown.")
        print("4. Tap the 'Print' button.")
        print("5. Choose your printer on the dropdown menu at the top.")
        print("6. Choose nuumber of copies and options")
        print("7. Tap the print icon at the top right.")
    else:
        print("1. Open the app that you want to print from.")
        print("2. To find the print option, tap the app’s share icon or tap the three dots.")
        print("3. Scroll down and tap the print icon or text.")
        print("4. Tap 'Select Printer' and choose an AirPrint printer")
        print("5. Choose nuumber of copies and options")
        print("6. Tap 'Print' in the top right corner.")

def wifi():
    if phoneType == "Android":
        print("1. From your Home screen, go to Settings > Network & internet.")
        print("2. Tap the Internet section.")
        print("3. Turn on Wi-Fi, your device should automatically search for Wi-Fi networks.")
        print("4. Tap the name of the Wi-Fi network that you want to join.")
        print("5. You may have to enter a password or agree to terms and conditions.")
        print("6. You should see the Wi-Fi icon on the top right of your phone, next to the battery icon.")
    else:
        print("1. From your Home screen, go to Settings > Wi-Fi.")
        print("2. Turn on Wi-Fi, your device should automatically search for Wi-Fi networks.")
        print("3. Tap the name of the Wi-Fi network that you want to join.")
        print("4. You may have to enter a password or agree to terms and conditions.")
        print("5. You should see the Wi-Fi icon on the top right of your phone, next to the battery icon.")

def app_search():
    if phoneType == "Android":
        print("1. Go to the home screen (swipe up from the very bottom).")
        print("2. Swipe up from the middle of the screen.")
        print("3. Tap the search field at the top of the screen.")
        print("4. Enter the name of the app or scroll up and down to browse the list.")
        print("5. To open an app, tap it.")
    else:
        print("1. Go to the home screen (swipe up from the very bottom).")
        print("2. Swipe left past all Home Screen pages to get to your App Library.")
        print("3. Tap the search field at the top of the screen.")
        print("4. Enter the name of the app or scroll up and down to browse the list.")
        print("5. To open an app, tap it.")


mappings = {
    'goodbye' : function_for_goodbye,
    'shortcut' : function_for_shortcut,
    'brightness' : function_for_brightness,
    'printing' : printing,
    'wifi' : wifi,
    'app_search' : app_search
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
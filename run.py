from main import GenericAssistant
import sys

def function_for_goodbye():
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

def function_for_shortcut():
    done = False
    while not done:
        response = input("Are you using a computer? ")
        if assistant.request_answer(response) == "yes":
            print("1. Navigate to the item or application you want to make a shortcut for.")
            print("2. Right-click it.")
            print("3. Select 'Create shortcut.'")
            print("Done! Your shortcut will appear on your desktop.")
            done = True
        elif assistant.request_answer(response) == "no":
            response = input("Are you using a mobile device? ")
            if assistant.request_answer(response) == "yes":
                response = input("Are you using an Android? ")
                if assistant.request_answer(response) == "yes":
                    print("1. Navigate to the application you want to make a shortcut for.")
                    print("2. Press and hold the application and drag it upwards.")
                    print("3. Let go of the application in the spot of your choice.")
                    done = True
                elif assistant.request_answer(response) == "no":
                    print("iPhones do not have shortcuts.")
                    print("You should be able to find every application on the home screen.")
                    done = True
                else:
                    print("Not a valid response, I'll ask again.")
        else:
            print("Not a valid response, I'll ask again.")

def function_for_brightness():
    done = False
    while not done:
        response = input("Are you using a computer? ")
        if assistant.request_answer(response) == "yes":
            response = input("Are you using a laptop? ")
            if assistant.request_answer(response) == "yes":
                print("1. Find the function (fn) key and your brightness (*) keys on your keyboard.")
                print("2. While holding the function key down, select the up brightness key.")
                done = True
            elif assistant.request_answer(response) == "no":
                response = input("Is this a Mac? ")
                if assistant.request_answer(response) == "yes":
                    print("1. Choose the apple menu at the top left of your screen.")
                    print("2. Select 'System Settings.'")
                    print("3. Click 'Displays.'")
                    print("4. Drag the brightness slider to your preference.")
                    print("Done!")
                    done = True
                elif assistant.request_answer(response) == "no":
                    print("1. Search for buttons on your monitor.")
                    print("2. Select the menu button and navigate to brightness.")
                    print("3. Use the up and down buttons to increase/decrease brightness.")
                    print("Done!")
                    done = True
                else:
                    print("Not a valid response, I'll ask again.")
            else:
                print("Not a valid response, I'll ask again.")
        elif assistant.request_answer(response) == "no":
            response = input("Are you using a mobile device? ")
            if assistant.request_answer(response) == "yes":
                response = input("Are you using an Android? ")
                if assistant.request_answer(response) == "yes":
                    print("Swipe your finger down from the top of the screen twice to change the brightness slider.")
                    print("Thats it!")
                    done = True
                elif assistant.request_answer(response) == "no":
                    print("Swipe down from the top right corner of your phone to change the brightness slider.")
                    print("Thats it!")
                    done = True
                else:
                    print("Not a valid response, I'll ask again.")
        else:
            print("Not a valid response, I'll ask again.")

mappings = {
    'goodbye' : function_for_goodbye,
    'shortcut' : function_for_shortcut,
    'brightness' : function_for_brightness
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
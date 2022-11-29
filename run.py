from main import GenericAssistant
import sys
import argparse

# Usage
# Training:
# python run.py --model train
# Testing:
# python run.py

def goodbye():
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

def shortcut():
    if phoneType == "Android":
        print("1. Navigate to the application you want to make a shortcut for.")
        print("2. Press and hold the application and drag it upwards.")
        print("3. Let go of the application in the spot of your choice.")
    else:
        print("iPhones do not have shortcuts.")
        print("You should be able to find every application on the home screen.")

def brightness():
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

def bookmarks():
    if phoneType == "Android":
        print("1. On your Android phone or tablet, open the Chrome app.")
        print("2. Go to a site you want to visit again in the future.")
        print("3. To the right of the address bar, tap More (three vertical dots icon) and then Star icon.")
        print("Thats it!")
    else:
        print("1. On your device, open the Safari app.")
        print("3. Navigate to the website you wish to bookmark.")
        print("2. Touch and hold the Show Bookmarks button(book icon), then tap Add Bookmark.")
        print("Thats it!")

def fontsize():
    if phoneType == "Android":
        print("1. On your device, open the Settings app.")
        print("2. Search and select Font size.")
        print("3. To change your preferred font size, move the slider left or right.")
        print("Thats it!")
    else:
        print("1. Go to Settings > Display & Brightness, then select Text Size.")
        print("2. Drag the slider to select the font size you want.")
        print("If you want to make the font even bigger follow these steps:")
        print("1. Go to Settings > Accessibility, then select Display & Text Size.")
        print("2. Tap Larger Text for larger font options.")
        print("3. Drag the slider to select the font size you want.")
        print("Thats it!")

def emailspam():
    if phoneType == "Android":
        print("To block the sender you can follow the following steps:")
        print("1. On your Android phone or tablet, open the Gmail app.")
        print("2. Open the message.")
        print("3. In the top right of the message, tap More (three vertical dots icon).")
        print("4. Tap Block [sender].")

        print("To remove the spam email use the following steps:")
        print("1. On your Android phone or tablet, open the Gmail app.")
        print("2. Tap the letter or photo to the left of the message, or open the message.")
        print("3. In the top right, tap More (three vertical dots icon).")
        print("4. Tap Report Spam.")
        print("Thats it!")
    else:
        print("1. Open the iCloud app.")
        print("2. Find the email you wish to mark as spam.")
        print("3. Swipe left on the message, tap More, then tap Move to Junk.")
        print("Thats it!")

def screenorientation():
    if phoneType == "Android":
        print("1. Open your device's Settings app.")
        print("2. Select Accessibility.")
        print("3. Select Auto-rotate screen.")
        print("Thats it!")
    else:
        print("1. Swipe down from the top-right corner of your screen to open Control Center.")
        print("2. Tap the Portrait Orientation Lock button (a directional circle with a lock inside icon) to make sure that it's off.")
        print("Thats it!")

def resetpassword():
    if phoneType == "Android":
        print("1. On your Android phone or tablet, open your device's Settings app and then Google and then Manage your Google Account.")
        print("2. At the top, tap Security.")
        print("3. Under 'Signing in to Google,' tap Password. You might need to sign in.")
        print("4. Enter your new password, then tap Change Password.")
        print("Tip: When you enter your password on mobile, the first letter isn't case sensitive.")
        print("Thats it!")
    else:
        print("1. Tap Settings > your name > Password & Security.")
        print("2. Tap Change Password.")
        print("3. Enter your current password or device passcode, then enter a new password and confirm the new password. Forgot your password?")
        print("4. Tap Change or Change Password.")
        print("Thats it!")

mappings = {
    'goodbye' : goodbye,
    'shortcut' : shortcut,
    'brightness' : brightness,
    'printing' : printing,
    'wifi' : wifi,
    'app_search' : app_search,
    'bookmarks' : bookmarks,
    'fontsize'  : fontsize,
    'emailspam' : emailspam,
    'screenorientation' : screenorientation,
    'resetpassword' : resetpassword
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
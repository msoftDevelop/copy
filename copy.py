import pyautogui
import time

# Wait for 5 seconds to give the user time to switch to the Chrome window
time.sleep(5)

# Copy the selected text from the active window
pyautogui.hotkey('ctrl', 'c')

# Get the text from the clipboard
text = pyautogui.paste()

# Print the text to the console
print(text)

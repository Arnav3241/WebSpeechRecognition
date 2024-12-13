from WebSpeechRecognition import SpeechRecognition

### Example Code

# Path to Chrome WebDriver
driver_path = "path_to_your_chrome_webdriver"

# Create a SpeechRecognition object with language code
recognizer = SpeechRecognition(driver_path, "en-IN")

# Start the WebDriver
recognizer.Init()

# Listen for speech and print results
while True:
  print(recognizer.Listen(print_allowed=True))
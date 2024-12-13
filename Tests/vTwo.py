from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import importlib.resources as resources
from selenium import webdriver
from os import path, getcwd
import warnings

warnings.simplefilter("ignore")

class SpeechRecognition:
  """
  Main class for SpeechRecognition.
  Handles initializing the driver, listening to speech input, and cleanup.
  """
  
  def __init__(self, driver_path, website_file):
    """
    Initialize the SpeechRecognition class with a path to ChromeDriver and locate the website file.

    Args:
    - driver_path (str): Path to ChromeDriver executable.
    - website_file (str): Path to the script or main HTML to locate the `web.html`.
    """
    
    
    self.driver_path = driver_path
    # Dynamically resolve web.html's location
    with resources.path("WebSpeechRecognition", "web.html") as web_path:
      self.website = str(web_path)
    self.driver = None

  def init(self):
    """
    Initializes the Chrome WebDriver with custom options for running Selenium.
    Prepares the ChromeDriver to start a simulated web session.
    """
    service = Service(self.driver_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--use-fake-ui-for-media-stream")
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--allow-insecure-localhost")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--disable-features=IsolateOrigins,site-per-process")
    chrome_options.add_argument("--use-fake-device-for-media-stream")
    chrome_options.add_argument("--use-file-for-fake-audio-capture=/path/to/audio.wav")
    chrome_options.add_argument("--log-level=3")  # Suppress warnings and errors
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--silent")

    self.driver = webdriver.Chrome(service=service, options=chrome_options)

  def listen(self, print_allowed=False):
    """
    Simulates listening for speech on the web interface and returns recognized text.

    Args:
    - print_allowed (bool): Whether to print debug information during listening.

    Returns:
    - str: The text recognized from the user's speech input.
    """
    if not self.driver:
      raise Exception("Driver not initialized. Call init() first.")

    self.driver.get(self.website)
    self.driver.find_element(by=By.ID, value='start').click()

    if print_allowed:
      print("Listening ...")

    while True:
      text = self.driver.find_element(by=By.ID, value='output').text
      if text:
        if print_allowed:
          print(f"You: {text}")
        self.driver.find_element(by=By.ID, value='end').click()
        return text

  def quit_driver(self):
    """
    Properly quits and cleans up the WebDriver after usage.
    Ensures all browser resources are released.
    """
    if self.driver:
      self.driver.quit()

if __name__ == "__main__":
  driver_path = path.join(getcwd(), "Drivers", "chromedriver.exe")
  Recognizer = SpeechRecognition(driver_path, __file__)
  
  try:
    Recognizer.init()
    while True:
      print(Recognizer.listen(print_allowed=True))
  except KeyboardInterrupt:
    print("Exiting...")
  finally:
    Recognizer.quit_driver()

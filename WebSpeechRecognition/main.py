from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from os import path
import warnings

warnings.simplefilter("ignore")

class SpeechRecognition:
  """
  Main class for SpeechRecognition.
  Handles initializing the driver, listening to speech input, and cleanup.
  """
  
  def __init__(self, driver_path, language="en-US"):
    """
    Initialize the SpeechRecognition class with a path to ChromeDriver and select your desired language.

    Args:
    - driver_path (str): Path to ChromeDriver executable.
    - language (str): Select your language from the following options: "en-US", "en-GB", "en-AU", "en-CA", "en-IN", "hi-IN", "fr-FR", "fr-CA", "es-ES", "es-MX", "pt-BR", "pt-PT", "de-DE", "it-IT", "ar-SA", "ar-EG", "ja-JP", "ko-KR", "zh-CN", "zh-TW", "ru-RU", "nl-NL", "da-DK", "sv-SE", "no-NO", "fi-FI", "tr-TR", "id-ID", "ms-MY", "ta-IN", "te-IN", "ml-IN".
    """
    
    self.driver_path = driver_path
    self.website = path.join(path.dirname(__file__), "web.html")
    self.driver = None
    self.language = language  # Set the default language (editable)

  def Init(self):
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

  def Listen(self, print_allowed=False):
    """
    Simulates listening for speech on the web interface and returns recognized text.

    Args:
    - print_allowed (bool): Whether to print debug information during listening.

    Returns:
    - str: The text recognized from the user's speech input.
    """
    if not self.driver:
      raise Exception("Driver not initialized. Call Init() first.")

    # Pass language to the web page dynamically
    self.driver.get(self.website + f"?lang={self.language}")
    self.driver.find_element(by=By.ID, value='start').click()

    if print_allowed: print("Listening ...")

    while True:
      text = self.driver.find_element(by=By.ID, value='output').text
      if text:
        if print_allowed: print(f"You: {text}")
        self.driver.find_element(by=By.ID, value='end').click()
        return text

  def Quit(self):
    """
    Properly quits and cleans up the WebDriver after usage.
    Ensures all browser resources are released.
    """
    if self.driver:
      self.driver.quit()

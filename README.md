# WebSpeechRecognition Library

## Introduction

WebSpeechRecognition is a Python library that helps turn speech into text in real time. It uses the Selenium WebDriver and the HTML5 Web Speech API. This tool is built to work with Chrome WebDriver and is easy to use for speech recognition tasks.



## Installation

To install WebSpeechRecognition, you can use pip:

```bash
pip install WebSpeechRecognition
```

## Features

- **Works in Many Languages:** You can set the language you want using simple codes like "en-US" for English.
- **Change Language Easily:** You can pick a language at any time while using it.
- **Simple Functions:** It has easy-to-understand methods to start and stop speech recognition.

## Usage

### Initialization

To start using WebSpeechRecognition, initialize the `SpeechRecognition` class with the path to your ChromeDriver executable and the language code:

```python
from WebSpeechRecognition import SpeechRecognition

recognizer = SpeechRecognition("path/to/chromedriver", language="en-US")
recognizer.Init()
```

### Speech Recognition

To start listening and transcribing speech, use the `Listen` method. This method returns the transcribed text:

```python
text = recognizer.Listen(print_allowed=True)
print(f"You said: {text}")
```

### Close the Driver

Once you are done, use the `Quit` method to close the ChromeDriver instance:

```python
recognizer.Quit()
```

## Examples

Here is a complete example:

```python
from WebSpeechRecognition import SpeechRecognition

recognizer = SpeechRecognition("path/to/chromedriver", language="en-US")
recognizer.Init()

while True:
    try:
        text = recognizer.Listen(print_allowed=True)
        print(f"You said: {text}")
    except KeyboardInterrupt:
        recognizer.Quit()
        break
```



## Parameters

### `SpeechRecognition(driver_path, language)`
- `driver_path`: The path to the Chrome WebDriver file.
- `language`: The language code for recognition (default: "en-US").

### `Init()`
Sets up the WebDriver with options for speech recognition.

### `Listen(print_allowed=False)`
Starts listening and returns the text it hears.
- `print_allowed`: If True, prints recognized text to the console.

### `Quit()`
Stops the WebDriver and closes everything.


## Contributing
We welcome contributions! If you find a bug or have an idea for a new feature, feel free to open an issue or a pull request on our GitHub repository.

Want to help improve SpeechRecognition? Here's how:

1. Fork the repository.
2. Make a new branch (`git checkout -b feature-branch`).
3. Add your changes (`git commit -m 'Add feature'`).
4. Push your branch (`git push origin feature-branch`).
5. Open a pull request for review.

## License
This project uses the MIT License. See the `LICENSE` file for details.

## Contact
Have questions or suggestions? Contact us:

- Email: authentic.arnav@gmail.com



from setuptools import setup, find_packages

with open("README.md", "r") as f:
  description = f.read()

setup(
  name="WebSpeechRecognition",
  version="0.1.4",
  author= "Arnav Singh",
  author_email= "authentic.arnav@gmail.com",
  long_description=description,
  long_description_content_type="text/markdown",
  description="A Python library for speech-to-text integration using Selenium WebDriver.",
  keywords=["python", "speech", "recognition", "speech recognition", "stt", "selenium", "speech-to-text", "selenium", "voice recognition", "voice interaction", "multilingual", "multilingual support", "chromedriver"],
  packages=find_packages(),
  include_package_data=True,  # Include non-Python files
  package_data={"WebSpeechRecognition": ["web.html"]},  # Specify files to include
  install_requires=[
    "selenium>=4.0.0"
  ],
  python_requires=">=3.7",
)

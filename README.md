# Bitly URL shortener

---
This is a project for creating a URL shortener using the Bitly API. It allows you to shorten long URLs and track the 
number of clicks on Bitlinks.

## Getting Started

---
Before running the project, you need to obtain an access token from Bitly. Follow the steps below:

1. Visit the Bitly Developer Documentation on [Authentication](https://dev.bitly.com/docs/getting-started/authentication/).
2. Generate your access token by following the instructions provided in the documentation.
3. Once you have obtained the access token, create a file named ```config.env``` in the root directory of the project.
4. Inside ```config.env```, add the following line: ```BITLY_ACCESS_TOKEN=<your-access-token>```, 
replacing <your-access-token> with the actual access token you obtained.

## Dependencies

---
Python3 should already be installed. Use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```pip install -r requirements.txt```

## Usage

---
1. Run ```main.py``` in your terminal.
2. The terminal will prompt you to enter a URL.
3. If you enter a regular URL, the program will shorten it using the Bitly API and display the shortened link.
4. If you enter a Bitlink, the program will display the total number of clicks that link has received.

## License

---
This project is licensed under the MIT License.

---

Handmade with ❤️ by AndreiPL



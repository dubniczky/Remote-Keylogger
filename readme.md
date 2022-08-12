# Remote Keylogger

A compiled keylogger written in python with logging to a remote host

## Support ❤️

If you find the project useful, please consider supporting, or contributing.

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/dubniczky)

## Description

This keylogger and server are written in python, using 3.10 features. The logger runs in the background without a window or console and logs key presses. Every few seconds it sends those key presses to a server using an HTTP request.

The server collects the logs from the client and stores them in a file unique for each user based on IP address.

## Usage

### Setting up the keylogger

1. Edit the global settings in `keylogger.py`
2. Install dependencies `make install`
3. Compile the keylogger `make build`
4. Take the file from `dist` directory and run it on the victim's machine

### Setting up the server

1. Download the project locally or to a remote server
2. Install dependencies `make install`
3. Run the server `make server`
4. After logging, collect the logs from `logs` directory

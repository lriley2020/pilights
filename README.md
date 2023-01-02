# pilights
Raspberry Pi Controlled Christmas Lights


## Instructions for installation and use

1. Clone the repo: `git clone https://github.com/lriley2020/pilights.git`

2. `cd pilights`

3. (Optional) Create a virtual environment: `python3 -m venv venv` ... and activate it: `source venv/bin/activate`

4. Install the required packages: `pip3 install -r requirements.txt`

5. Run the API: `python3 api.py`


## Next steps...
### Adding the API as a systemd service to start automatically
Run the `systemd-setup.sh` script as root (you may need to change some paths before running): `sudo ./systemd-setup.sh`

### Adding an Apple Shortcut to trigger the lights
You can use the "Get contents of" block in an Apple shortcut to trigger the webhook with the API key.
Example:
https://www.icloud.com/shortcuts/963fe4e9c4984912a7da0d90fec2f4a0

You can now ask Siri to "Turn the Christmas lights on"!

Note: you will need to change the URL in the "Get contents of" block for this to work!

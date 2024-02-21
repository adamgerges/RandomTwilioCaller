# RandomTwilioCaller

RandomTwilioCaller is an automated dialing system built with Python, utilizing the Twilio API to call a list of numbers at pre-configured intervals. It securely loads Twilio credentials from an .env file, and supports customized dialing schedules and Twilio phone number rotations.

## Features

- Configuration via `.env` for Twilio settings.
- E.164 phone number standard enforcement.
- Auto dialing with managed delay and multi-number handling.

## Prerequisites

- Python 3.6 or newer.
- A Twilio API account with SID and Auth Token.
- Configured list of destination and Twilio host phone numbers.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/adamgerges/RandomTwilioCaller
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the root directory with the following settings:
 - `TWILIO_ACCOUNT_SID`: Your Twilio Account SID.
 - `TWILIO_AUTH_TOKEN`: Your Twilio Auth Token.
 - `TWILIO_PHONE_NUMBERS`: A comma-separated list of your Twilio phone numbers.
 - `CALL_ATTEMPTS`: The number of attempts to call each number in `destination_numbers.txt`. Default is 3.
 - `CYCLE_DELAY_MINUTES`: The delay in minutes between each cycle of calling every number in the list. Default is 2.

2. In `destination_numbers.txt`, list the phone numbers you wish to call, one per line, in E.164 format.


## Usage

To start the dialing script, run:
```bash
python run_script.py
```

This orders the script to make periodical dials, timing and rotation regulated by `.env`.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

[MIT](LICENSE)

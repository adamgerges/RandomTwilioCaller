# Random Dialer Project

This project consists of a Python script that uses Twilio's API to dial a predetermined phone number from a list of Twilio phone numbers at random intervals.

## Prerequisites

- Python 3.6 or higher
- Twilio account with an Auth Token and Account SID
- List of Twilio phone numbers

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

Before running the script, you need to configure your Twilio credentials and phone numbers:

1. Open `phone_random.py`.
2. Replace `Twilio_Account_SID` and `Twilio_Auth_Token` with your Twilio Account SID and Auth Token.
3. Add your Twilio phone numbers to `twilio_phone_numbers_list`.
4. Set the `to_phone_number` variable to the number you wish to dial.

## Usage

To start the dialing script, run:
```bash
python run_script.py
```

This will continuously dial the configured phone number every 90 seconds using a random Twilio number from your list.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

[MIT](LICENSE)

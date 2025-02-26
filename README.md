# CROUS Accommodation Notifier

This script automates the process of checking for available accommodations on the CROUS website. It uses Selenium to scrape the webpage, regex to detect available listings, and Twilio to send an SMS notification if accommodations are found. Additionally, it plays an alert sound when availability is detected.

## Features
- Uses Selenium to scrape accommodation availability.
- Plays an alert sound if a listing is found.
- Sends an SMS notification via Twilio.
- Runs continuously until an accommodation is found.

## Prerequisites
Make sure you have the following installed before running the script:
- Python > 3.10
- Google Chrome
- Chrome WebDriver
- Required Python libraries:
  ```bash
  pip install selenium pygame twilio
  ```

## Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/crous-notifier.git
   cd crous-notifier
   ```

2. **Set Up Twilio**
   - Sign up on [Twilio](https://www.twilio.com/)
   - Get your `account_sid` and `auth_token`
   - Replace `'your_sid'`, `'your_token'`, and `'your_number'` in the script with your actual Twilio credentials and phone number.

3. **Set the Target URL**
   - Replace `'City_Selected_URL'` with the actual CROUS accommodation URL you want to monitor.

4. **Run the Script**
   ```bash
   python script.py
   ```

## How It Works
- The script loads the given URL and checks if there are accommodations available using regex.
- If found, it:
  - Plays an alarm using `pygame`.
  - Sends an SMS notification via Twilio.
  - Keeps the script running to ensure continued alerts.
- If no accommodations are found, it waits for a few seconds and retries.

## Notes
- Ensure that `alert_sound.mp3` is available in the script directory.
- Modify the sleep intervals as needed to avoid excessive requests.
- Running Selenium may require adjusting Chrome WebDriver compatibility with your Chrome version.

## Disclaimer
This script is for personal use only. Be mindful of web scraping policies on the CROUS website.

## License
MIT License

**Authors**: Youxise, LyesYe






import sys
import time
import requests
import json
from datetime import datetime


class MessageSender:
    def __init__(self, api_url, token):
        """Initialize the message sender with API URL and token"""
        self.api_url = api_url
        self.headers = {
            "Content-Type": "application/json",
            "Token": token
        }
        self.messages = self.load_messages()
        self.groups = self.load_groups()

    def load_messages(self):
        """Load message templates from external JSON file"""
        with open('messages.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    def load_groups(self):
        """Load group information from an external text file"""
        groups = []
        with open('group_list.txt', 'r', encoding='utf-8') as file:
            for line in file:
                name, wid, language = line.strip().split(',')
                groups.append({"name": name, "WID": wid, "language": language})
        return groups

    def send_message(self, group_id, message):
        """Send message to the given group using API"""
        data = {"group": group_id, "message": message}
        response = requests.post(self.api_url, headers=self.headers, json=data)

        if response.status_code == 200:
            print(f"Message sent successfully to {group_id}")
        elif response.status_code == 201:
            print(f"Message queued for delivery to {group_id}.")
        else:
            print(f"Error sending message to {group_id}: {response.status_code}, {response.text}")

    def countdown_timer(self, seconds):
        """Start a countdown timer"""
        while seconds > 0:
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            secs = seconds % 60
            timer = f'{hours:02d}:{minutes:02d}:{secs:02d}'
            sys.stdout.write(f"\rTime remaining: {timer}")
            sys.stdout.flush()
            time.sleep(1)
            seconds -= 1
        print("\nTime's up! Sending messages now...")

    def run(self):
        """Main function to control the message sending process with time checks"""
        while True:
            current_time = datetime.now().time()
            if current_time >= datetime.strptime("23:00", "%H:%M").time() or current_time < datetime.strptime("08:00",
                                                                                                              "%H:%M").time():
                print(f"Night mode activated: StandBy. Current time: {current_time.strftime('%H:%M')}")
                time.sleep(60 * 60)  # Sleep for 1 hour during night mode
            else:
                # Start 3-hour countdown
                print(f"Countdown started at: {current_time.strftime('%H:%M')}")
                self.countdown_timer(10800)  # 10800 seconds = 3 hours

                # Send messages after countdown
                for group in self.groups:
                    message = self.messages[group["language"]]
                    self.send_message(group["WID"], message)

                print("\nAll messages sent. Restarting the countdown...")


if __name__ == "__main__":
    API_URL = "https://api.wassenger.com/v1/messages"
    TOKEN = "YOUR_API_TOKEN"  # Replace with your actual API token
    sender = MessageSender(API_URL, TOKEN)
    sender.run()

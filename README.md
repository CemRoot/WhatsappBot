Tabii, işte `README.md` dosyasının düzenlenmiş hali:

```markdown
# WhatsApp Message Automation Script

## Overview

This project is a Python script designed to automate sending messages to multiple WhatsApp groups using the [Wassenger API](https://wassenger.com/). The script sends messages to predefined groups every 3 hours, except during night mode, when it pauses from 11 PM to 8 AM. It dynamically loads messages and groups from external files (`messages.json` and `group_list.txt`), making it easy to modify and customize.

The automation runs continuously, sending messages at the specified intervals until the script is manually stopped.

## Features

- **API Integration**: Connects to the Wassenger API to send WhatsApp messages.
- **Dynamic Message Loading**: Messages for different languages are loaded from an external `messages.json` file.
- **Night Mode**: From 11 PM to 8 AM, the script pauses sending messages to avoid disturbance.
- **Automated Scheduling**: The script sends messages to different groups every 3 hours.
- **External Group Management**: Group information (name, WhatsApp ID, language) is stored in `group_list.txt`.

## Wassenger API Token

You need a valid API token from Wassenger to send messages. Follow these steps to obtain a token:

1. Create an account or log in to Wassenger.
2. Go to your account settings and generate an API token.
3. Copy this token and paste it into the `TOKEN` variable in the `app.py` file.

```python
TOKEN = "YOUR_API_TOKEN"  # Replace with your actual API token
```

## Setup

### Clone the Repository

Clone this project to your local machine:

```bash
git clone https://github.com/CemRoot/whatsapp-message-automation.git
```

### Configure Messages and Groups

- Modify the `messages.json` file to customize the message templates for each language.
- Update the `group_list.txt` file with the group names, WhatsApp IDs, and the language of the messages.

### Run the Script

Once everything is set up, you can run the script:

```bash
python app.py
```

## File Structure

- `app.py`: The main Python script containing the message automation logic.
- `messages.json`: Contains message templates for different languages (e.g., Portuguese, Turkish, English).
- `group_list.txt`: Stores the group names, WhatsApp IDs, and the language in which the message should be sent.

## Example of `messages.json`

This file contains message templates for each supported language. Here is an example of what the structure looks like:

```json
{
  "portuguese": "*🎯 URGENTE: PROCURANDO UM QUARTO/ESTÚDIO PARA ALUGAR!🎯*\n\nOlá! 🙋‍♂🙋‍♀ ...",
  "turkish": "*🎯 ACİL: KİRALIK ODA/STÜDYO ARANIYOR! 🎯*\n\nMerhaba! 🙋‍♂🙋‍♀ ...",
  "english": "*🎯 URGENT: LOOKING FOR A ROOM/STUDIO TO RENT! 🎯*\n\nHello! 🙋‍♂🙋‍♀ ..."
}
```

## Example of `group_list.txt`

This file contains the group name, WhatsApp ID, and the language the message should be sent in. Here is an example of its structure:

```unknown
Classificados Dublin 🇧🇷🇮🇪,353899672287-1512154645,portuguese
Irlanda Türkleri,353831139289-1628162185,turkish
Zenith of Ireland 6,120363307136843795,english
```

## Night Mode

The script will automatically enter "night mode" between 11 PM and 8 AM. During this period, no messages will be sent, and the script will remain in standby mode. After 8 AM, it will resume sending messages every 3 hours.

While in night mode, you will see an output like this:

```sql
Night mode activated: StandBy. Current time: 23:15
```

The script will then pause for an hour and recheck the time until it’s 8 AM.

## Testing the Script

You can test the script by:

- Modifying the `countdown_timer()` method to use a smaller interval (e.g., 10 seconds instead of 3 hours) during development.
- Verifying that messages are sent to the correct groups and in the appropriate language.

## Troubleshooting

- **API Errors**: If the script cannot send messages, double-check the Wassenger API token and ensure it’s correctly pasted in the `TOKEN` variable.
- **Network Issues**: Ensure your internet connection is stable, as the script relies on API calls.
- **Group Formatting**: Ensure that the `group_list.txt` file has the correct formatting (comma-separated values for name, ID, and language).

## Contributing

If you wish to contribute to this project, feel free to fork the repository and submit a pull request. Any improvements, especially on optimizing message handling and additional features, are welcome.

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as needed.
```
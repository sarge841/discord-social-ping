# Discord Social Ping Bot

A fun Discord bot that sends notifications with random, creative messages when members join voice channels. The bot uses a variety of humorous and themed messages to announce when someone enters a voice channel.

## Features

- 🎯 **Voice Channel Monitoring**: Automatically detects when members join voice channels
- 🎲 **Random Messages**: Over 300 unique, creative join messages ranging from casual to anime-themed
- ⏰ **Auto-cleanup**: Messages are automatically deleted after 5 minutes to keep channels clean
- 🧪 **Test Command**: Use `asdf` command to test the bot functionality
- 🐳 **Docker Support**: Easy deployment with Docker containers
- 📝 **Logging**: Comprehensive logging for monitoring and debugging

## Message Themes

The bot includes a variety of message themes:
- Casual and friendly messages
- Gaming and internet culture references
- Anime and weeb culture references
- Magical and fantasy themes
- Sci-fi and technology themes
- And many more creative variations!

## Prerequisites

- Python 3.12 or higher
- A Discord bot token
- Discord server with appropriate permissions

## Installation

### Option 1: Local Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd discord-social-ping
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   ```bash
   export DISCORD_TOKEN="your_bot_token_here"
   export DISCORD_CHANNEL_ID="your_notification_channel_id_here"
   ```

4. **Run the bot**:
   ```bash
   python main.py
   ```

### Option 2: Docker Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd discord-social-ping
   ```

2. **Build the Docker image**:
   ```bash
   docker build -t discord-social-ping .
   ```

3. **Run the container**:
   ```bash
   docker run -e DISCORD_TOKEN="your_bot_token_here" \
              -e DISCORD_CHANNEL_ID="your_notification_channel_id_here" \
              discord-social-ping
   ```

## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `DISCORD_TOKEN` | Your Discord bot token | Yes |
| `DISCORD_CHANNEL_ID` | The channel ID where notifications will be sent | Yes |

### Getting Your Discord Bot Token

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application or select an existing one
3. Go to the "Bot" section
4. Copy the bot token

### Getting Channel ID

1. Enable Developer Mode in Discord (User Settings → Advanced → Developer Mode)
2. Right-click on the channel where you want notifications
3. Select "Copy ID"

### Bot Permissions

Your bot needs the following permissions:
- View Channels
- Send Messages
- Read Message History
- Connect (to voice channels for monitoring)

## Usage

### Basic Operation

Once the bot is running and properly configured:

1. **Automatic Notifications**: The bot will automatically send a notification when someone joins a voice channel
2. **Test Command**: Send `asdf` in any channel the bot can see to test functionality
3. **Message Cleanup**: All notifications are automatically deleted after 5 minutes (300 seconds)

### Customizing Messages

You can customize the join messages by editing the `messages.txt` file:

1. Each line represents a different message template
2. Lines starting with `#` are treated as comments and ignored
3. Empty lines are ignored
4. The bot will randomly select from available messages

Example message format:
```
is now hanging out in
just teleported to
decided to vibe in
```

The final message will be: `[Username] [random message] [channel name]!`

## File Structure

```
discord-social-ping/
├── main.py              # Main bot application
├── messages.txt         # Collection of join messages
├── requirements.txt     # Python dependencies
├── Dockerfile          # Docker configuration
└── README.md           # This file
```

## Logging

The bot includes comprehensive logging that shows:
- Bot startup and login status
- Message loading information
- Voice channel join events
- Error messages and debugging information

Logs are displayed in the console with timestamps and log levels.

## Troubleshooting

### Common Issues

1. **Bot doesn't respond**:
   - Check if the bot token is correct
   - Verify the bot has proper permissions
   - Ensure the bot is online in your Discord server

2. **No voice channel notifications**:
   - Verify the channel ID is correct
   - Check if the bot can see the notification channel
   - Ensure the bot has permission to send messages in that channel

3. **Messages file not loading**:
   - Check if `messages.txt` exists in the same directory as `main.py`
   - Verify the file is readable and properly formatted

### Debug Mode

To enable more detailed logging, you can modify the logging level in `main.py`:

```python
logging.basicConfig(level=logging.DEBUG)
```

## Contributing

Feel free to contribute by:
- Adding new creative messages to `messages.txt`
- Improving the bot functionality
- Reporting bugs or suggesting features

## License

This project is open source. Please check the license file for more details.

## Support

If you encounter any issues or have questions, please create an issue in the repository or contact the maintainers.

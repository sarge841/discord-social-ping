# This example requires the 'message_content' intent.

import discord
import random
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def load_regular_messages(file_path='messages.txt'):
    """
    Load regular messages from a file into a list.
    :param file_path: Path to the file containing messages.
    :return: List of messages.
    """
    messages = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    messages.append(line.strip())
        logger.info(f"Loaded {len(messages)} messages from {file_path}")
    except FileNotFoundError:
        logger.error(f"Message file '{file_path}' not found.")
    return messages

def is_member_joined(before, after):
    """
    Check if a member has joined a voice channel.
    :param before: The previous voice state of the member.
    :param after: The current voice state of the member.
    :return: True if the member joined a voice channel, False otherwise.
    """
    return before.channel is None and after.channel is not None

async def handle_voice_state_update(member, before, after, client, notification_channel_id, regular_messages, notification_role_id):
    """
    Handle the event when a member's voice state is updated.
    :param member: The member whose voice state changed.
    :param before: The previous voice state.
    :param after: The current voice state.
    :param client: The Discord client instance.
    :param notification_channel_id: The ID of the notification channel.
    :param regular_messages: List of messages to choose from.
    :param notification_role_id: Optional role ID to mention at the start of messages.
    """
    if is_member_joined(before, after):
        try:
            to_channel = await client.fetch_channel(notification_channel_id)
            if to_channel is None:
                logger.warning("Notification channel not found.")
                return

            message_text = random.choice(regular_messages)
            mention_prefix = f"<@&{notification_role_id}> " if notification_role_id else ""
            await to_channel.send(
                f'{mention_prefix}{member.display_name} {message_text} {after.channel.name}!',
                delete_after=300
            )
            logger.info(f"Sent message for {member.display_name} joining {after.channel.name}")
        except Exception as e:
            logger.error(f"Error handling voice state update: {e}")

async def handle_message(message, client, notification_channel_id, regular_messages, notification_role_id):
    """
    Handle incoming messages.
    :param message: The message object.
    :param client: The Discord client instance.
    :param notification_channel_id: The ID of the notification channel.
    :param regular_messages: List of messages to choose from.
    :param notification_role_id: Optional role ID to mention at the start of messages.
    """
    if message.author == client.user:
        return

    if message.content.startswith('asdf'):
        try:
            c = await client.fetch_channel(notification_channel_id)
            message_text = random.choice(regular_messages)
            mention_prefix = f"<@&{notification_role_id}> " if notification_role_id else ""
            await c.send(
                f'{mention_prefix}{message.author} {message_text} {c.name}!',
                delete_after=30
            )
            logger.info(f"Sent test message for {message.author}")
        except Exception as e:
            logger.error(f"Error handling message: {e}")

def main():
    """
    Main function to initialize and run the Discord bot.
    """
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    notification_channel_id = os.getenv('DISCORD_CHANNEL_ID')
    if not notification_channel_id:
        logger.error("Environment variable 'DISCORD_CHANNEL_ID' is not set.")
        return

    # Optional role mention for notifications
    notification_role_id = os.getenv('DISCORD_NOTIFICATION_ROLE_ID', '').strip()
    if notification_role_id:
        logger.info(f"Role mention enabled for role ID {notification_role_id}")
    else:
        logger.info("No role mention configured (DISCORD_NOTIFICATION_ROLE_ID is unset or empty)")

    regular_messages = load_regular_messages()

    @client.event
    async def on_ready():
        logger.info(f'Logged in as {client.user}')

    @client.event
    async def on_message(message):
        await handle_message(message, client, notification_channel_id, regular_messages, notification_role_id)

    @client.event
    async def on_voice_state_update(member, before, after):
        await handle_voice_state_update(member, before, after, client, notification_channel_id, regular_messages, notification_role_id)

    token = os.getenv('DISCORD_TOKEN')
    if not token:
        logger.error("Environment variable 'DISCORD_TOKEN' is not set.")
        return

    logger.info("Starting the bot...")
    client.run(token)

if __name__ == "__main__":
    main()

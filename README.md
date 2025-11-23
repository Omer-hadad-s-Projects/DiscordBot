# Discord Music Bot

This bot allows you to play songs in your Discord server using YouTube links.

## Running with Docker (Recommended)

1. **Create a Discord Bot and Get the Token**  
   Visit the [Discord Developer Portal](https://discord.com/developers/applications) to create your bot and retrieve the bot secret key.

2. **Set Up Environment Variables**  
   Create a `.env` file next to this README with at least:

   ```env
   DISCORD_TOKEN=your_bot_token_here
   # (Optional) Comma-separated numeric user IDs who have admin privileges
   # Wrap them in square brackets or leave as plain comma list; both work.
   # Examples:
   # ADMIN_LIST=[123456789012345678,987654321098765432]
   # ADMIN_LIST=123456789012345678,987654321098765432
   ADMIN_LIST=
   ```

3. **Run the Docker Image from Docker Hub**  
   The image is published as `thetemani/discord-bot`:

   ```bash
   docker run --rm --env-file .env thetemani/discord-bot
   ```

## Running Locally (Without Docker)

1. **Create and Activate a Virtual Environment**  
   Run the setup script, which will create `.venv`, install dependencies, and prompt for your bot token:

   ```bash
   ./setup.sh
   ```

2. **Launch the Bot**  
   After setup completes, start the bot with:

   ```bash
   ./launch.sh
   ```

3. **Use the Help Command**  
   In your server chat, type `!help` to see the available commands.

4. **Enjoy Your Music**  
   Play your favorite songs and enjoy! 😃

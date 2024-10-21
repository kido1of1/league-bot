Discord Matchmaking Bot - A Python bot for managing 1v1 matches on Discord. It automates queue management, match reporting, and tracks player scores.

Features:
  Queue System: Players join with !j and leave with !l. The bot pairs players for matches when the queue reaches 2 people.
  Match Reporting: Players report results in the match report channel with a mention and screenshot. The bot verifies and updates scores.
  Score Tracking: Automatically updates scores in player nicknames, reflecting wins/losses.
Setup:
  Install discord.py: pip install discord.py
  Add your bot token, server ID, and match report channel ID.
  Run the bot.

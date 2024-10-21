🏆 Discord Matchmaking Bot - Python
  This Discord Matchmaking Bot is built using Python and the discord.py library to facilitate 1v1 matches between players. The bot automates the process of managing a queue for games, reporting match results, and maintaining player scores based on match outcomes.

⚙️ Features:
Join & Leave Queue:

  Players can join the match queue with the !j command.
  The bot automatically pairs up players when the queue size reaches 2, and announces the match.
  Players can leave the queue with the !l command.
  Match Reporting:
  
  Players report match results by posting a message in the match report channel with a screenshot of the results.
  The bot requires the player to mention their opponent in the report.
  The bot verifies the match report with reactions and ensures both the players and the bot confirm the result.
  Score Tracking:
  
  The bot automatically updates player scores based on match outcomes.
  The winner gains points (default 5 points), and the loser loses points.
  Player scores are tracked in their Discord nicknames, and the bot ensures scores never go negative.
  Automated Score Update:

Once the match report is verified, the bot updates the players' scores directly in their Discord nicknames. Scores are displayed as part of the nickname in the format PlayerName (Score).
🛠️ Commands:
  !j: Join the match queue.
  !l: Leave the match queue.
  💻 How It Works:
  Queue System: The bot maintains a queue, and when two players join, it pairs them up for a match.
  Match Reporting: Players upload a match result screenshot in the designated report channel, mention their opponent, and both players verify it with a reaction.
  Score System: Winners and losers have their scores updated automatically, and their scores are reflected in their Discord nicknames.
🔒 Permissions:
  The bot needs the following permissions:
  Read and send messages
  Add reactions to messages
  Change nicknames
📦 Setup Instructions:
  Install the discord.py library:
  pip install discord.py
  Replace the placeholders in the code with your bot token, server ID, and match report channel ID.
  Run the bot.
🚀 Coming Soon:
More customizable queue sizes
Match history tracking
Leaderboards

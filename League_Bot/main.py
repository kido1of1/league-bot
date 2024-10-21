import discord
from discord.ext import commands
from discord.utils import get


TOKEN = '' # ur bot token
GUILD_ID =   # Replace with your server's ID
MATCH_REPORT_CHANNEL_ID =   # Replace with the channel ID for match reports
QUEUE_SIZE = 2
POINTS_PER_WIN = 5

intents = discord.Intents.default()
intents.message_content = True  # Needed for interacting with messages
intents.guilds = True
intents.members = True  # Needed for changing nicknames and managing the queue
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)

queue = []
processed_messages = set()  # Set to keep track of processed message IDs

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='j')
async def join_queue(ctx):
    if ctx.author in queue:
        await ctx.send(f'{ctx.author.mention}, you are already in the queue!')
        return
    
    queue.append(ctx.author)
    await ctx.send(f'{ctx.author.mention} has joined the queue! ({len(queue)}/{QUEUE_SIZE})')
    
    # Check if queue is full
    if len(queue) >= QUEUE_SIZE:
        player1 = queue.pop(0)
        player2 = queue.pop(0)
        await ctx.send(f'{player1.mention} vs {player2.mention}, your match is ready! Report your results in <#{MATCH_REPORT_CHANNEL_ID}>.')

@bot.command(name='l')
async def leave_queue(ctx):
    if ctx.author not in queue:
        await ctx.send(f'{ctx.author.mention}, you are not in the queue!')
        return
    
    queue.remove(ctx.author)
    await ctx.send(f'{ctx.author.mention} has left the queue! ({len(queue)}/{QUEUE_SIZE})')

@bot.event
async def on_message(message):
    await bot.process_commands(message)

    # Check if message is in the match report channel and contains an attachment (e.g., a screenshot)
    if message.channel.id == MATCH_REPORT_CHANNEL_ID and message.attachments:
        if len(message.mentions) == 1:
            await message.add_reaction('✅')  # Add a checkmark reaction for verification
        else:
            await message.channel.send(
                f'{message.author.mention}, please mention the opponent in your match report message!'
            )

@bot.event
async def on_reaction_add(reaction, user):
    # Check if the reaction is a checkmark in the match report channel
    if reaction.message.channel.id == MATCH_REPORT_CHANNEL_ID and reaction.emoji == '✅':
        # Check if the message has already been processed
        if reaction.message.id in processed_messages:
            return  # Skip if already processed

        # Get all users who reacted with a checkmark
        users_who_reacted = [u async for u in reaction.users()]

        # Ensure that the bot, the player who posted, and one opponent reacted
        bot_user = bot.user
        message_author = reaction.message.author
        reacted_users = [user for user in users_who_reacted if user != bot_user]

        # Check if the message has exactly one mention (the opponent)
        if bot_user in users_who_reacted and len(reacted_users) == 2 and len(reaction.message.mentions) == 1:
            # Mark the message as processed
            processed_messages.add(reaction.message.id)

            # Determine the winner as the author of the message and the loser as the mentioned user
            winner = message_author
            loser = reaction.message.mentions[0]

            # Update the winner's score
            await update_player_score(winner, POINTS_PER_WIN)

            # Deduct points from the loser, ensuring their score doesn't go negative
            await update_player_score(loser, -POINTS_PER_WIN)

            # Notify about the score update
            await reaction.message.channel.send(
                f'{winner.mention} has been awarded {POINTS_PER_WIN} points for the win, and {loser.mention} loses {POINTS_PER_WIN} points!'
            )


async def update_player_score(player, points):
    guild = get(bot.guilds, id=GUILD_ID)
    member = guild.get_member(player.id)

    if member:
        # Extract current score from the player's nickname (assumes nickname ends with score in parentheses, e.g., "Player (10)")
        nickname = member.display_name
        score = 0

        if '(' in nickname and nickname.endswith(')'):
            try:
                score = int(nickname.split('(')[-1][:-1])
            except ValueError:
                pass

        new_score = max(0, score + points)  # Ensure that the score doesn't go below zero
        new_nickname = f"{nickname.split('(')[0].strip()} ({new_score})"
        
        # Change nickname with the updated score
        await member.edit(nick=new_nickname)
        print(f'Updated {player.name}\'s score to {new_score}.')

bot.run(TOKEN)
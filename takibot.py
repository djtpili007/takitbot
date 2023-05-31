import discord
import pytz
import asyncio
from datetime import datetime

TOKEN = 'MTExMzAxNzcwOTg2NTc0NjQ1Mg.GhwESy.P7oOyBfkOJ23gs6VANmS6CKyRGlZjR8MSZPTmE'
GUILD_ID = '840310384766353418'
CATEGORY_ID = '1112940872196177930'

intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    print('------')

    # Get the guild and create the channel
    guild = client.get_guild(int(GUILD_ID))
    category = discord.utils.get(guild.categories, id=int(CATEGORY_ID))
    channel = await guild.create_text_channel('Clock', category=category)

    # Start the clock update loop
    client.loop.create_task(update_clock(channel))

async def update_clock(channel):
     while not client.is_closed():
        # Get the current time in the Asia/Bangkok timezone
        now = datetime.now(pytz.timezone('Asia/Bangkok'))
        current_time = now.replace(minute=(now.minute // 10) * 10, second=0, microsecond=0).strftime('%H:%M:00')

        # Edit the category name with the server time
        category_name = 'Server Time ' + current_time.replace(':', '：')
        await channel.edit(name=category_name)

        # Delay for 600 seconds (10 minutes) before updating the clock again
        await asyncio.sleep(600)

# Run the bot
client.run(TOKEN)

# modbot by fluff

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='^')


@bot.event
async def on_ready():
    print ("Up and running")
    print ("Username: " + bot.user.name)
    print ("ID: " + bot.user.id)


@bot.event
async def on_message(message):
    if((message.server == bot.get_server('490249217290534912'))or((message.author.bot))):
        print('msg sent')
    else:
        author = message.author
        msg = message.content
        channel = message.channel
        msgID = message.id
        timestamp = message.timestamp

        embed = discord.Embed(title="Message sent in {}".format(channel),color=0x66ff66)
        embed.add_field(name='{}'.format(author),value='`{}`'.format(msg))
        embed.set_footer(text='{}, at {}'.format(msgID,timestamp))
        await bot.send_message(bot.get_channel('521459450247249930'),embed=embed)
        await bot.process_commands(message)

@bot.command(pass_context=True)
async def apply(ctx, user:discord.Member):
    await bot.say(f"Sent to {user}")
    embed = discord.Embed(title="**Applying for Helper**",color=0x00e6b8)
    embed.add_field(name="Intro", value="Hello, and thank you for taking the time to apply for Helper here at GS! This guide will give you an overview/tutorial on how to apply." ,inline=True)
    embed.add_field(name="Requirements", value="There are some mandatory requirements that all staff members on our server must meet, these can be found here: https://guardianskies.site/community/threads/helper-requirements.3024/. Additionally, you must have a forums account." ,inline=True)
    embed.add_field(name="Format", value="Once you have read and met the requirements, you must read the Application Format and fill out your application as specified. This can be found here: https://guardianskies.site/community/threads/helper-application-format.3023/" ,inline=True)
    embed.add_field(name="Recommended Preperation", value="It is highly recommended that you read the \"Guide to a Successful Application and Interview\" document before writing your application, to review tips for writing yours (which can be found here: https://guardianskies.site/community/threads/guide-to-a-successful-application-interview.3030/). Additionally, you should read the accepted and denied applications, to get a feel for what your application should be like.",inline=True)    
    embed.add_field(name="Filling out the application", value="Now you are ready to write your application. You do so in the subforum \"Helper Applications\" (found here: https://guardianskies.site/community/forums/helper-applications.82/), and push \"Post New Thread\" to create a new thread. Ensure the thread title includes your username, so we can easily identify applications. Furthermore, please label all of your responses by putting respective question before your response." ,inline=True)    
    embed.add_field(name="You're done!", value="Once you finish your application, post it and good luck! A Sr. Staff member will review your application and get back to you shortly. Do **not** ask staff to read your application, as this will lead to an instant denial." ,inline=True)    
    await bot.send_message(user, embed=embed)



bot.run(TOKEN)

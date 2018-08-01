import discord 
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import aiml


Client = discord.Client()
client = commands.Bot (command_prefix = "!")

@client.event
async def on_ready():
    print("Bot is ready!")
    

@client.event
async def on_message(message):
    if message.content.upper().startswith("!PING"):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    if message.content == "des":
        await client.send_message(message.channel, ":skull:")
    if message.content == "!DoesVengeanceSuck":
        await client.send_message(message.channel, ":thumbsup:")
    if message.content.startswith("!8ball"):
        await client.send_message (message.channel, random.choice(["Oi fuck off mate :8ball:",
                                                                   "Roight, you fink you're clever m8 :8ball:",
                                                                   "Fuckin wanker :8ball:",
                                                                   "Yeah, roit :8ball:",
                                                                   "Fuck that :8ball:",
                                                                   "Not in your wildest fockin dreams :8ball:",
                                                                   "Never :8ball:",
                                                                   "Sure :8ball:",
                                                                   "Uh-huh :8ball:",
                                                                   "I'll be the judge of that :8ball:",
                                                                   "Look up and ask me again :8ball:",
                                                                   "Nar :8ball:",
                                                                   "Ask me again and I'll gut ye :8ball:"
                                                                    ]))
    if message.content.upper().startswith("!WISDOM"):
        await client.send_message (message.channel, random.choice(["Mmm...it's mental.",
                                                                   "After I was interrogated, I din’t wanna talk to anyone. Or do anythin’. An’ din’t even feel like myself.",
                                                                   "We are consumers. We're the by-products of a lifestyle obsession.",
                                                                   "The things you own end up owning you.",
                                                                   "It's only after we've lost everything that we're free to do anything.",
                                                                   "I am Jack's cold sweat.",
                                                                   "I am Jack's smirking revenge.",
                                                                   "I see all this potential, and I see it squandered. God damn it, an entire generation pumping gas, waiting tables - slaves with white collars. Advertising has us chasing cars and clothes, working jobs we hate so we can buy shit we don't need. We're the middle children of history, man. No purpose or place. We have no Great War. No Great Depression. Our great war is a spiritual war... Our great depression is our lives. We've all been raised on television to believe that one day we'd all be millionaires, and movie gods, and rock stars, but we won't. We're slowly learning that fact. And we're very, very pissed off.",
                                                                   "I'm Jack's complete lack of surprise."
                                                                    ]))
                                                        
    if message.content.upper().startswith('!SAY'):
        args = message.content.split(" ")
        #args[0] = !SAY
        #args[1] = Hey
        #args[2] = There
        #args[1:] = Hey There
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))



client.run ("NDczNjY2MDMwNTgyMTA0MDk0.DkFgsw.OBHyp-_XVla7J7SFZ_Db-7_zkxk")

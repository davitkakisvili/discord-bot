import os
import discord
from youtubesearchpython import VideosSearch

token="ODU0MDc4MjU1NTUxNDc5ODI4.YMesXA.FMpEZL4sHtW4NIo1VmRmRLmnAoY"

client = discord.Client()
def search(link):
    videosSearch = VideosSearch(link, limit =1)
    return videosSearch.result()['result']

@client.event
async def on_ready():
    channel = client.get_channel(846371198069243964) 
    print(f'{client.user} has connected to Discord!')
    print(client.guilds[0])
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('>music '):
        msg=message.content.replace('>music ','')
        song=search(msg)[0]
        url=song['link'].replace('youtube','youtubepp')
        result=song['title']+' --> '+url
        
        await message.channel.send(result)
        


    
client.run(token)

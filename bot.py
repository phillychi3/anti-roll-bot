import discord
from discord.ext import commands
import json
import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

bot = commands.Bot(command_prefix= 'r')
#bot.remove_command("help")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless') 


rolllinklist=["https://youtu.be/dQw4w9WgXcQ","https://www.youtube.com/watch?v=dQw4w9WgXcQ"]

with open('set.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

@bot.event
async def on_ready():
    print('我是誰 我在哪')

@bot.command()
async def ping(ctx):
    await ctx.send(F'{round(bot.latency*1000)} (ms)')


@bot.event
async def on_message(msg):
    rolltest=msg.content
    rolllink=msg.content[0:4]
    rollid=msg.id
    if rolllink=="http":
        chrome = webdriver.Chrome(chrome_options=chrome_options)
        chrome.get(rolltest) 
        print(chrome.current_url)
        if chrome.current_url in rolllinklist:
            await msg.channel.send("警告 辨識結果為rick roll")
            de = await msg.channel.fetch_message(rollid)
            await de.delete()
        else:
            chrome.get(rolltest)
            await asyncio.sleep(5)
            #sleep(5)
            webroll=chrome.current_url        
            chrome.close()
            chrome.quit()
            if webroll in rolllinklist:
                await msg.channel.send("警告 辨識結果為rick roll")
                de = await msg.channel.fetch_message(rollid)
                await de.delete()
        chrome.close()

bot.run(jdata['TOKEN'])
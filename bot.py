import discord
from discord.ext import commands
import json
import random
import asyncio
from hentai import Hentai, Format
from covid import Covid
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

bot = commands.Bot(command_prefix= 'r')
#bot.remove_command("help")


chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--disable-notifications")
browser = webdriver.Chrome('./chromedriver.exe', chrome_options=chrome_options)
rolllink=["https://youtu.be/dQw4w9WgXcQ","https://www.youtube.com/watch?v=dQw4w9WgXcQ"]

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
        if rolllink in rolllink:
            await msg.channel.send("警告 辨識結果為rick roll")
            de = await msg.channel.fetch_message(rollid)
            await de.delete()
        else:
            browser.get(req_url)
            asyncio.sleep(5)
            webroll=browser.current_url        
            browser.close()
            browser.quit()
            if webroll in rolllink:
                await msg.channel.send("警告 辨識結果為rick roll")
                de = await msg.channel.fetch_message(rollid)
                await de.delete()



bot.run('ODcwMjU1OTg5MDE2ODk5NjI2.YQKHDA.mh4YWvFbz6BVUcdX1bHGb8rPbrg')
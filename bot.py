import discord
from discord.ext import commands
import json
import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

bot = commands.Bot(command_prefix="r")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")


rolllinklist = [
    "https://youtu.be/dQw4w9WgXcQ",
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "https://www.youtube.com/watch?v=iik25wqIuFo",
    "https://youtu.be/iik25wqIuFo",
    "https://www.youtube.com/watch?v=DLzxrzFCyOs",
    "https://youtu.be/DLzxrzFCyOs",
    "https://www.youtube.com/watch?v=O_vMqGuoxv8",
    "https://www.youtube.com/watch?v=Ui_ldWQsJwo",
    "https://www.youtube.com/watch?v=-g03jC71GBw",
    "https://www.youtube.com/watch?v=aYsgsSo1aow",
    "https://www.youtube.com/watch?v=6omHDfHITZ4",
    "https://www.youtube.com/watch?v=GtL1huin9EE",
    "https://www.youtube.com/watch?v=xvFZjo5PgG0",
    "https://www.youtube.com/watch?v=iKRXIkboIqo"
]

with open("set.json", "r", encoding="utf8") as jfile:
    jdata = json.load(jfile)


@bot.event
async def on_ready():
    print("Anti rick-roll")


@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)} (ms)")


@bot.event
async def on_message(msg):
    rolltest = msg.content
    rolllink = msg.content[0:4]
    rollid = msg.id
    if rolllink == "http":
        chrome = webdriver.Chrome(
            ChromeDriverManager().install(), chrome_options=chrome_options
        )
        if rolltest in rolllinklist:
            await msg.channel.send("警告 辨識結果為rick roll")
            de = await msg.channel.fetch_message(rollid)
            await de.delete()
        else:
            chrome.get(rolltest)
            await asyncio.sleep(5)
            webroll = chrome.current_url
            chrome.close()
            chrome.quit()
            if webroll in rolllinklist:
                await msg.channel.send("警告 辨識結果為rick roll")
                de = await msg.channel.fetch_message(rollid)
                await de.delete()
        chrome.close()

bot.run(jdata["TOKEN"])

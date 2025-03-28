#!/usr/bin/python3
# coding: utf-8
'''
https://github.com/siiway/JMComic-Discord-Bot
适用 MIT License
'''

# 创建一个 bot 实例
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)

# 定义一个简单的斜杠指令
@slash.slash(name="hello", description="Say hello!")
async def hello(ctx: SlashContext):
    await ctx.send(content="Hello, world!")

# 运行 bot
bot.run("YOUR_BOT_TOKEN")

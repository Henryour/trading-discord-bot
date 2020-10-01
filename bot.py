import discord
from discord.ext import commands
from yahoo_fin import stock_info as si
from yahoo_fin.stock_info import *
TOKEN = 'NzYxMTAyNTkzNzQ1MDkyNjM4.X3VuBg.eI1wWjF-hHB5g7rtC9qw38zd8jo'
client = commands.Bot(command_prefix = '!')
# api_key = 'RI9uMBS5Uv0jE3zLNZyM6wE2plX7hdoK'
def stock(ticker):
    try:
        return str(round(si.get_live_price(ticker), 2))
    except:
        return 'stock not found'

@client.event
async def on_ready():
    print('Bot is ready')
# all of the bot commands are below
@client.command()
async def price(ctx, *, ticker):
    await ctx.send('latest price is: ' + stock(ticker))

@client.command()
async def quote(ctx, *, ticker):
    await ctx.send(si.get_quote_table(ticker, dict_result = False))

@client.command()
async def balance_sheet(ctx, *, ticker):
    await ctx.send(si.get_balance_sheet(ticker))

@client.command()
async def cash_flow(ctx, *, ticker):
    await ctx.send(si.get_cash_flow(ticker))

@client.command()
async def day_gainers(ctx):
    await ctx.send(si.get_day_gainers())

@client.command()
async def day_losers(ctx):
    await ctx.send(si.get_day_losers())

@client.command()
async def day_day_most_active(ctx):
    await ctx.send(si.get_day_most_active())

@client.command()
async def income_statement(ctx, *, ticker):
    await ctx.send(si.get_income_statement(ticker))

@client.command()
async def live_price(ctx, *, ticker):
    await ctx.send(si.get_live_price(ticker))



client.run(TOKEN)

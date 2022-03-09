import lightbulb
import hikari

bot = lightbulb.BotApp(
    token="OTUwMjM4MzM5NjQxMDE2MzUw.YiWAag.MCMlsJyFyAWsvMveg2uB_9pY6dY",
    default_enabled_guilds=933809192215654400
)


@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print("Clyde is up and running")


@bot.command
@lightbulb.command('ping', 'says pong')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong')


bot.run()

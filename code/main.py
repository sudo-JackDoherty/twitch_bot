import pyttsx3
from twitchio.ext import commands

class Bot(commands.Bot):

    def __init__(self):
        with open('conf.txt') as f:
            channel_token = f.readline().replace('\n', '')
            channel_name = f.readline().replace('\n', '')
        super().__init__(token=channel_token, prefix='?', initial_channels=[channel_name])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command()
    async def radio(self, ctx: commands.Context):
        message_content = ctx.message.content[:].replace('?radio', '')
        str = ctx.author.name + ' says ' + message_content
        engine.say(str)
        engine.runAndWait()

if __name__ == '__main__':
    engine = pyttsx3.init()
    bot = Bot()
    bot.run()

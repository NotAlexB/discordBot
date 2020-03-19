import discord
from datetime import datetime
answer = "1587000"
submited = {"test" : 1}
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    async def on_message(self, message):
        print("{0.author} said {0.content} in {0.channel.type}".format(message))
        if "{0.channel.type}".format(message) == "private" and "{0.author}".format(message) != "Puzzle Bot#5865":
            #print("{0.author} said {0.content} in {0.channel.type}".format(message))
            if '{0.content}'.format(message) == answer :
                if '{0.author}'.format(message) in submited:
                    if submited['{0.author}'.format(message)] < 3:
                        await message.author.send("correct")
                    else:
                        await message.author.send("too many tries")
                else:
                    await message.author.send("good")
            elif '{0.author}'.format(message) in submited:
                if submited['{0.author}'.format(message)] < 3:
                    submited['{0.author}'.format(message)] += 1
                    print(submited['{0.author}'.format(message)])
                    await message.author.send("wrong")
                else:
                    await message.author.send("too many tries")
            else:
                submited['{0.author}'.format(message)] = 1
                await message.author.send("wrong")
client = MyClient()
client.run('Njg5ODU4ODExMDAzMDExMTc0.XnJpEw.LX9a37cloN6OIcRi9tqTnn4vSK8')
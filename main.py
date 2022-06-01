import discord
import os
import requests
import json

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('抽签'):
    res = requests.get("http://ovooa.com/API/chouq/api.php", params={"type": "json"})
    res_json = json.loads(res.text)
    state = res_json['text']
    draw = res_json['data']['draw']
    annotate = res_json['data']['annotate']
    explain = res_json['data']['explain']
    details = res_json['data']['details']
    source = res_json['data']['source']
    print(res_json['data']['image'])
    await message.channel.send(state + "\n\n" + draw + "\n\n" + "签语：" + annotate + "\n\n" + "解曰：" + explain + "\n\n" + "仙机："+ details + "\n\n" + "来源：" + source)

client.run(os.getenv('OTgxNTcyMjM5ODIyNTc3Njk1.GUCZWy.zTDG_oaWgzQcuF75N6m7EQXQ4amYWwA8F-SC5o'))

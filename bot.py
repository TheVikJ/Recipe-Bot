import requests
import json
import discord

client = discord.Client()
TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
spoonacular = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
url = "https://api.spoonacular.com/recipes/"

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!random'):
    response = json.loads(requests.get(url + "random?apiKey=" + spoonacular).text)
    print(response)
    msg = response['recipes'][0]['image'] + "\n"
    msg += "Recipe: " + response['recipes'][0]['title'] + "\n"
    msg += "Link: " + response['recipes'][0]['sourceUrl'] + "\n"
    msg += "Servings: " + str(response['recipes'][0]['servings'])
    await message.channel.send(msg)

  if message.content.startswith('!diet'):
    diet = message.content.replace("!diet ", "")
    response = json.loads(requests.get(url + "complexsearch?diet=" + diet + "&apiKey=" + spoonacular  + "&number=1").text)
    print(response)
    msg = response['results'][0]['image'] + "\n"
    msg += "Recipe: " + response['results'][0]['title'] + "\n"
    msg += "Link: " + response['results'][0]['sourceUrl'] + "\n"
    msg += "Servings: " + str(response['results'][0]['servings'])
    await message.channel.send(msg)

  if message.content.startswith('!search'):
    terms = message.content.replace("!search ", "")
    response = json.loads(requests.get(url + "complexsearch?query=" + terms + "&apiKey=" + spoonacular + "&number=1").text)
    print(response)
    msg = response['results'][0]['image'] + "\n"
    msg += "Recipe: " + response['results'][0]['title'] + "\n"
    msg += "Link: " + response['results'][0]['sourceUrl'] + "\n"
    msg += "Servings: " + str(response['results'][0]['servings'])
    await message.channel.send(msg)

  if message.content.startswith('!cuisine'):
    cuisine = message.content.replace("!cuisine ", "")
    response = json.loads(requests.get(url + "complexsearch?cuisine=" + cuisine + "&apiKey=" + spoonacular  + "&number=1").text)
    print(response)
    msg = response['results'][0]['image'] + "\n"
    msg += "Recipe: " + response['results'][0]['title'] + "\n"
    msg += "Link: " + response['results'][0]['sourceUrl'] + "\n"
    msg += "Servings: " + str(response['results'][0]['servings'])
    await message.channel.send(msg)

  if message.content.startswith('!intolerance'):
    cuisine = message.content.replace("!intolerance ", "")
    response = json.loads(requests.get(url + "complexsearch?intolerances=" + cuisine + "&apiKey=" + spoonacular  + "&number=1").text)
    print(response)
    msg = response['results'][0]['image'] + "\n"
    msg += "Recipe: " + response['results'][0]['title'] + "\n"
    msg += "Link: " + response['results'][0]['sourceUrl'] + "\n"
    msg += "Servings: " + str(response['results'][0]['servings'])
    await message.channel.send(msg)

  if message.content.startswith('!ingredients'):
    ingredients = message.content.replace("!ingredients ", "")
    response = json.loads(requests.get(url + "complexsearch?includeIngredients=" + ingredients + "&apiKey=" + spoonacular  + "&number=1").text)
    print(response)
    msg = response['results'][0]['image'] + "\n"
    msg += "Recipe: " + response['results'][0]['title'] + "\n"
    msg += "Link: " + response['results'][0]['sourceUrl'] + "\n"
    msg += "Servings: " + str(response['results'][0]['servings'])
    await message.channel.send(msg)

@client.event
async def on_ready():
       print('Logged in as')
       print(client.user.name)
       print(client.user.id)
       print('------')

client.run(TOKEN)

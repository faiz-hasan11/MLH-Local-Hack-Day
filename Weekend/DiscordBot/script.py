import discord
import requests
from pprint import pprint
import json
token = "Discord Token"
api_key = "Weather API key"
client = discord.Client()

key_features = {
    "temp": "Temperature",
    "feels_like": "Feels Like",
    "temp_min": "Minimum Temperature",
    "temp_max": "Maximum Temperature"
}


def parse_data(data):
    data = data["main"]
    del data["humidity"]
    del data["pressure"]
    return data


def weather_message(data, location):
    location = location.title()
    message = discord.Embed(
        title=f"{location} Waether", description=f"Here is the weather data for {location}.", color=0xFF6500)
    for key in data:
        message.add_field(name=key_features[key], value=str(
            data[key]), inline=False)
    return message


def error_message(location):
    location = location.title()
    message = discord.Embed(
        title="Error", description="There Was An Error", color=0xFF6500)
    return message


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="w.[location]"))


@client.event
async def on_message(message):
    if message.author != client.user and message.content.startswith("w."):
        location = message.content.replace("w.", "").lower()
        if len(location) > 1:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
            try:
                data = json.loads(requests.get(url).content)
                data = parse_data(data)
                await message.channel.send(embed=weather_message(data, location))
            except:
                await message.channel.send(embed=error_message(location))
client.run(token)

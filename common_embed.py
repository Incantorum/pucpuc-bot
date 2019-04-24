import discord

error_thumbnail = ""

def generic_embed(title, description, image, thumbnail):
    embed = discord.Embed(
        title = title,
        description = description,
        colour = discord.Colour.dark_blue()
    )
    embed.set_image(url = image)
    embed.set_thumbnail(url = thumbnail)
    return embed

def error_embed(error = "Wrong format"):
    embed = discord.Embed(
        title = "Error",
        description = error,
        colour = discord.Colour.red()
    )
    embed.set_thumbnail(url = error_thumbnail)
    return embed

def field_embed(title, description, fields, image, thumbnail):
    embed = discord.Embed(
        title = title,
        description = description,
        colour = discord.Colour.dark_blue()
    )
    for field in fields:
        embed.add_field(name=field[0], value =field[1], inline=field[2])
    embed.set_image(url = thumbnail)
    embed.set_thumbnail(url = thumbnail)
    return embed
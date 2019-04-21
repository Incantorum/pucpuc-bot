import discord

def generic_embed(title, description, image, thumbnail):
    embed = discord.Embed(
        title = title,
        description = description,
        colour = discord.Colour.dark_blue()
    )
    embed.set_image(url = image)
    embed.set_thumbnail(url = thumbnail)
    return embed

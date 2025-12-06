import random
import string as  s
import discord as d
def create_pasword(length =25):
    elements = s.ascii_letters+s.digits+s.punctuation
    password = ""
    for i in range(length):
        password += random.choice(elements)
    return password


def meme():
    with open("IMG/Meme1.png", "rb") as f:
        Picture = d.File(f)
    return Picture

def etiqueta_eco():
    embed = d.Embed(
        title="Reciclaje en el mar",
        description="Hoy vamos a saver el ",
        color=0x32CD32
    )
    embed.add_field(
        name="Recoger basura",
        value="Hello",
        inline=False
    )
    embed.add_field(
        name="Recoger basura",
        value="Hello",
        inline=False
    )
    embed.add_field(
        name="Recoger basura",
        value="Hello",
        inline=False
    )
    embed.set_thumbnail(
        url="https://i.postimg.cc/vZgJS554/Lingangu.jpg"
    )
    return embed
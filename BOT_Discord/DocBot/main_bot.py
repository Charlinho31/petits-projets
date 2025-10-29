
from discord.ext import commands
from dotenv import load_dotenv
import discord
import os

load_dotenv(dotenv_path="config")  # Charger les variables d'environnement depuis le fichier .env qui s'appelle ici "config"


class DocBot(commands.Bot): # Créer le bot avec le préfixe "!"
    def __init__(self):
        intents = discord.Intents.all()
        intents.members = True
        intents.message_content = True
        super().__init__(command_prefix="!")


    async def on_ready(self): # Événement prêt
        print(f"Bot connecté en tant que {self.user.display_name}")


    async def on_member_join(self, member): # Événement lorsqu'un membre rejoint le serveur
        general_channel = self.get_channel(1418962720908382270)  # Remplacez par l'ID de votre canal
        await general_channel.send(content=f"Bienvenue sur le serveur, {member.mention} ! 🎉")


    async def on_message(self, message): # Événement simple sur les messages
        if message.author == self.user:
            return

        salutations = ["bonjour", "Bonjour", "Salut", "salut", "coucou", "hello", "yo", "Wsh", "wsh", "Selem", "selem"]
        if message.content.lower() in salutations:
            await message.channel.send("Salut 👋 !")

        if message.content.lower() == "ping": 
            await message.channel.send("Pong 🏓 !")

        await self.process_commands(message)

# commandes séparrées de la classe

bot = DocBot() # Créer le bot avec le préfixe "!"

@bot.command(name="ping") # verifier si le bot est en ligne
async def ping(ctx):
    await ctx.send("Pong 🏓 !")

@bot.command(name="del") # Supprimer les messages
async def delete(ctx, number_of_messages: int): 
    messages = await ctx.channel.history(limit=number_of_messages + 1).flatten()
    
    for each_message in messages:
        await each_message.delete()
    await ctx.send(f"{number_of_messages} messages supprimés! 🗑️")

# Commande help avec embed
@bot.command(name="help")
async def help_command(ctx, command_name=None):
    """Commande d'aide personnalisée avec embed"""
    commands_info = {
        "del": {"desc": "Supprime le nombre de messages indiqué.", "usage": "!del <nombre>"},
        "ping": {"desc": "Vérifie si le bot est en ligne.", "usage": "!ping"},
        "help": {"desc": "Affiche ce message d'aide.", "usage": "!help [commande]"},
    }

    embed = discord.Embed(title="📚 Aide du bot", color=discord.Color.blurple())

    if command_name is None or command_name.lower() == "all":
        embed.description = "Voici la liste des commandes disponibles :"
        for name, info in commands_info.items():
            embed.add_field(name=f"!{name}", value=f"{info['desc']}\nUsage : `{info['usage']}`", inline=False)
    else:
        info = commands_info.get(command_name.lower())
        if info:
            embed.add_field(name=f"!{command_name.lower()}", value=f"{info['desc']}\nUsage : `{info['usage']}`", inline=False)
        else:
            embed.description = f"❌ Aucune aide trouvée pour `{command_name}`. Utilise `!help all` pour voir toutes les commandes."

    await ctx.send(embed=embed)

# Lancer le bot
bot.run(os.getenv("TOKEN"))  # Remplacez par votre token réel
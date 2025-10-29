import discord
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")  # Charger les variables d'environnement depuis le fichier .env qui s'appelle ici "config"

class Client(discord.Client):
    
    def __init__(self):
    intents = discord.Intents.all()
    intents.members = True
    intents.message_content = True
    super().__init__(intents=intents)

# Événement prêt

    async def on_ready(self): # async = asynchrone (évite de bloquer le programme)
        print(f"✅ Connecté en tant que {self.user}")

# Événement simple sur les messages

    async def on_message(self, msg):
        if msg.author == self.user:
            return
        content = msg.content.lower()

        # Salutations
        salutations = ["bonjour", "Bonjour", "Salut", "salut", "coucou", "hello", "yo", "Wsh", "wsh", "Selem", "selem"]
        if content in salutations: 
            await msg.channel.send("Salut 👋 !")
    
        elif content == "ping":
            await msg.channel.send("Pong 🏓 !")

        elif content.startswith("!del"): # Supprimer les messages
            try:
                number = int(msg.content.split(" ")[1])
                messages = await msg.channel.history(limit=number + 1).flatten()

                for each_message in messages:
                    await each_message.delete()
                await msg.channel.send(f"{number} messages supprimés! 🗑️")
            except (IndexError, ValueError):
                await msg.channel.send("❗ Utilisation correcte : `!del <nombre>`")
        
    # Commande help avec embed
        elif content.startswith("!help"):
            await self.send_help(msg)

# Événement lorsqu'un membre rejoint le serveur
    async def on_member_join(self, member):
        channel = self.get_channel(1418962720908382270)  # Remplacez par l'ID de votre canal
        if channel:
            await channel.send(content=f"Bienvenue sur le serveur, {member.mention} ! 🎉")

# Méthode d'aide avec embed
    async def send_help(self, msg):
        parts = msg.content.split(" ")
        command_name = parts[1].lower() if len(parts) > 1 else "all"

        embed = discord.Embed(
            title="📚 Aide du bot",
            color=discord.Color.blurple(),
            description="Voici les commandes disponibles :"
        )

        if command_name == "all":
            embed.add_field(name="🗑️ !del <nombre>", value="Supprime le nombre de messages indiqué.", inline=False)
            embed.add_field(name="🏓 !ping", value="Vérifie si le bot est en ligne.", inline=False)
            embed.add_field(name="❓ !help [commande]", value="Affiche l'aide pour une commande.", inline=False)
        else:
            helps = {
                "del": "🗑️ **!del <nombre>** — Supprime le nombre de messages indiqué.",
                "ping": "🏓 **!ping** — Vérifie si le bot est en ligne.",
            }
            if command_name in helps:
                embed.add_field(name=f"ℹ️ !{command_name}", value=helps[command_name], inline=False)
            else:
                embed.description = f"❗ Commande inconnue : `{command_name}`. Utilise `!help all` pour voir toutes les commandes."

        await msg.channel.send(embed=embed)


# Lancer le bot avec le token
if __name__ == "__main__":
    client = Client()

    client.run(os.getenv("TOKEN"))  # Remplacez par votre token réel
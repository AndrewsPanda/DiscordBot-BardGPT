import discord
from core.classes import Cog_Extension
from discord import app_commands

class Help(Cog_Extension):
    @app_commands.command(name = "help", description = "Show how to use")
    async def help(self, interaction: discord.Interaction):
        embed=discord.Embed(title="Help - link below", description="[Click Here to Learn How to Set Cookies](https://docs.google.com/document/d/12N82-QlmWQVPLNswnE7w15WU8cb1YAOCYQuIyec5B3A/edit?usp=sharing)\n\n**COMMANDS -**")
        embed.add_field(name="/bard_cookies", value="Set and delete your Google Bard Cookies.", inline=False)
        embed.add_field(name="/bard", value="Chat with Google Bard.", inline=False)
        embed.add_field(name="/reset_bard_conversation", value="Reset chatbot conversation.", inline=False)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))

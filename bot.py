#!/usr/bin/env python3
"""Praetoris Wiki Bot — serves wiki sections via button interactions."""

import os

import discord
from dotenv import load_dotenv

from sections import ICON_URL, SECTIONS

load_dotenv()

TOKEN = os.environ["DISCORD_BOT_TOKEN"]
GUILD_ID = 1289659443780255902
WIKI_COLOR = 0x992D22


# ── Persistent view (survives bot restarts) ──


class WikiView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    async def _respond(self, interaction: discord.Interaction, key: str):
        section = SECTIONS[key]
        embed = discord.Embed(
            title=section["title"],
            description=section["description"],
            color=section["color"],
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(
        label="How to Join",
        custom_id="wiki:how_to_join",
        style=discord.ButtonStyle.success,
        row=0,
    )
    async def how_to_join(self, interaction, button):
        await self._respond(interaction, "how_to_join")

    @discord.ui.button(
        label="World Settings",
        custom_id="wiki:world_settings",
        style=discord.ButtonStyle.primary,
        row=0,
    )
    async def world_settings(self, interaction, button):
        await self._respond(interaction, "world_settings")

    @discord.ui.button(
        label="Mod Features",
        custom_id="wiki:mod_features",
        style=discord.ButtonStyle.primary,
        row=0,
    )
    async def mod_features(self, interaction, button):
        await self._respond(interaction, "mod_features")

    @discord.ui.button(
        label="Wild Shrine Rewards",
        custom_id="wiki:wild_shrine",
        style=discord.ButtonStyle.secondary,
        row=1,
    )
    async def wild_shrine(self, interaction, button):
        await self._respond(interaction, "wild_shrine")

    @discord.ui.button(
        label="Star Levels",
        custom_id="wiki:star_levels",
        style=discord.ButtonStyle.secondary,
        row=1,
    )
    async def star_levels(self, interaction, button):
        await self._respond(interaction, "star_levels")

    @discord.ui.button(
        label="Spawn Chances",
        custom_id="wiki:star_spawns",
        style=discord.ButtonStyle.secondary,
        row=1,
    )
    async def star_spawns(self, interaction, button):
        await self._respond(interaction, "star_spawns")

    @discord.ui.button(
        label="Distance Table",
        custom_id="wiki:star_distance",
        style=discord.ButtonStyle.secondary,
        row=2,
    )
    async def star_distance(self, interaction, button):
        await self._respond(interaction, "star_distance")

    @discord.ui.button(
        label="Greylisted Mods",
        custom_id="wiki:greylisted",
        style=discord.ButtonStyle.secondary,
        row=2,
    )
    async def greylisted(self, interaction, button):
        await self._respond(interaction, "greylisted")


# ── Bot ──


class WikiBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = discord.app_commands.CommandTree(self)

    async def setup_hook(self):
        self.add_view(WikiView())

        @self.tree.command(
            name="wiki",
            description="Post the Praetoris server wiki",
            guild=discord.Object(id=GUILD_ID),
        )
        @discord.app_commands.checks.has_permissions(manage_messages=True)
        async def wiki_command(interaction: discord.Interaction):
            embed = discord.Embed(
                title="Praetoris \u2014 Server Wiki",
                description=(
                    "*Season 5 \u2014 Hardcore exploration modpack*\n\n"
                    "Click a button below to view a section."
                ),
                color=WIKI_COLOR,
            )
            embed.set_thumbnail(url=ICON_URL)
            await interaction.response.send_message(embed=embed, view=WikiView())

        await self.tree.sync(guild=discord.Object(id=GUILD_ID))

    async def on_ready(self):
        print(f"Wiki bot ready: {self.user} (guilds: {len(self.guilds)})")


if __name__ == "__main__":
    WikiBot().run(TOKEN)

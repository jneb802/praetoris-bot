#!/usr/bin/env python3
"""Praetoris Wiki Bot — serves wiki sections via button interactions."""

import asyncio
import json
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path

import discord
from dotenv import load_dotenv

from gamestate import get_state, start_server

from sections import (
    GUIDES,
    ICON_URL,
    MOD_CONFIGS,
    MODPACK_URL,
    SECTIONS,
    WIKI_DESCRIPTION,
    WIKI_FIELDS,
)

load_dotenv()

TOKEN = os.environ["DISCORD_BOT_TOKEN"]
GUILD_ID = 1289659443780255902
RESET_CHANNEL_ID = 1484994286880690297
WIKI_COLOR = 0x992D22
STATE_FILE = Path(__file__).parent / "state.json"

# ── Reset tracking ──

RESET_TYPES = {
    "locations": {
        "match": "Resetting Meadows locations",
        "label": "Location Reset",
        "interval": timedelta(days=3),
    },
    "vegetation": {
        "match": "vegetation_reset Pickable_Stone",
        "label": "Vegetation Reset (trees & stones)",
        "interval": timedelta(hours=12),
    },
    "tin": {
        "match": "vegetation_reset Rocks_4_tin",
        "label": "Tin Node Reset",
        "interval": timedelta(hours=24),
    },
}

reset_state: dict[str, datetime] = {}


def load_state():
    if STATE_FILE.exists():
        data = json.loads(STATE_FILE.read_text())
        for key, ts in data.items():
            reset_state[key] = datetime.fromisoformat(ts)
        print(f"Loaded reset state: {list(reset_state.keys())}")


def save_state():
    data = {k: v.isoformat() for k, v in reset_state.items()}
    STATE_FILE.write_text(json.dumps(data))


def check_reset_message(content: str, timestamp: datetime):
    for key, cfg in RESET_TYPES.items():
        if cfg["match"] in content:
            if key not in reset_state or timestamp > reset_state[key]:
                reset_state[key] = timestamp
                save_state()
            return


def build_resets_embed() -> discord.Embed:
    embed = discord.Embed(
        title="Location & Vegetation Resets",
        color=0x3498DB,
    )
    description_parts = [
        "**Location Resets** \u2014 All locations reset every **3 real-life days**\n"
        "**Vegetation Resets** \u2014 Trees and pickable stones within **500m** reset every **12 hours**\n"
        "**Tin Resets** \u2014 10\u201320 tin nodes reset every **24 hours**\n",
    ]

    for key, cfg in RESET_TYPES.items():
        last = reset_state.get(key)
        if last:
            last_ts = int(last.timestamp())
            next_ts = int((last + cfg["interval"]).timestamp())
            description_parts.append(
                f"**{cfg['label']}**\n"
                f"Last: <t:{last_ts}:R> (<t:{last_ts}:f>)\n"
                f"Next: <t:{next_ts}:R> (<t:{next_ts}:f>)\n"
            )
        else:
            description_parts.append(
                f"**{cfg['label']}**\n"
                f"Last: Unknown\nNext: Unknown\n"
            )

    embed.description = "\n".join(description_parts)
    return embed


def build_status_embed() -> discord.Embed:
    state = get_state()
    if state is None:
        return discord.Embed(
            title="Praetoris Server Status",
            description="No data received yet.",
            color=0x95A5A6,
        )

    age = datetime.now(timezone.utc) - state["last_updated"]
    last_ts = int(state["last_updated"].timestamp())

    if age < timedelta(minutes=2):
        color = 0x2ECC71  # green
        status = "Online"
    elif age < timedelta(minutes=5):
        color = 0xF39C12  # yellow
        status = "Online (data may be stale)"
    else:
        color = 0xE74C3C  # red
        status = "Offline"

    players = state["players"]
    if players:
        player_list = "\n".join(f"- {name}" for name in players)
        player_field = f"**{len(players)}** online\n{player_list}"
    else:
        player_field = "No players online"

    embed = discord.Embed(title="Praetoris Server Status", color=color)
    embed.add_field(name="Status", value=status, inline=True)
    embed.add_field(
        name="World",
        value=f"Day {state['day']} \u2014 {state['game_time']}",
        inline=True,
    )
    embed.add_field(name="Players", value=player_field, inline=False)
    embed.set_footer(text=f"Last updated")
    embed.timestamp = state["last_updated"]

    return embed


# ── Persistent view (survives bot restarts) ──


class WikiView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(discord.ui.Button(
            label="Modpack",
            style=discord.ButtonStyle.link,
            url=MODPACK_URL,
            row=0,
        ))
        self.add_item(ModConfigSelect())
        self.add_item(GuidesSelect())

    async def _respond(self, interaction: discord.Interaction, key: str):
        section = SECTIONS[key]
        embed = discord.Embed(
            title=section["title"],
            description=section["description"],
            color=section["color"],
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

    # ── Row 0: Quick Links ──

    @discord.ui.button(
        label="How to Join",
        custom_id="wiki:how_to_join",
        style=discord.ButtonStyle.success,
        row=0,
    )
    async def how_to_join(self, interaction, button):
        await self._respond(interaction, "how_to_join")

    @discord.ui.button(
        label="Resets",
        custom_id="wiki:resets",
        style=discord.ButtonStyle.primary,
        row=0,
    )
    async def resets(self, interaction, button):
        embed = build_resets_embed()
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(
        label="Greylisted Mods",
        custom_id="wiki:greylisted",
        style=discord.ButtonStyle.primary,
        row=0,
    )
    async def greylisted(self, interaction, button):
        await self._respond(interaction, "greylisted")

    @discord.ui.button(
        label="Server Status",
        custom_id="wiki:server_status",
        style=discord.ButtonStyle.success,
        row=0,
    )
    async def server_status(self, interaction, button):
        embed = build_status_embed()
        await interaction.response.send_message(embed=embed, ephemeral=True)


class ModConfigSelect(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label=cfg["label"],
                value=key,
                description=cfg["description"],
            )
            for key, cfg in MOD_CONFIGS.items()
        ]
        super().__init__(
            custom_id="wiki:mod_config",
            placeholder="Mod Configs",
            options=options,
            row=1,
        )

    async def callback(self, interaction: discord.Interaction):
        key = self.values[0]
        cfg = MOD_CONFIGS[key]
        embed = discord.Embed(
            title=cfg["title"],
            description=cfg["content"],
            color=cfg["color"],
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)


class GuidesSelect(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label=guide["label"],
                value=key,
                description=guide["description"],
            )
            for key, guide in GUIDES.items()
        ]
        super().__init__(
            custom_id="wiki:guide",
            placeholder="Guides & Tips",
            options=options,
            row=2,
        )

    async def callback(self, interaction: discord.Interaction):
        key = self.values[0]
        guide = GUIDES[key]
        embed = discord.Embed(
            title=guide["title"],
            description=guide["content"],
            color=guide["color"],
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)


# ── Bot ──


class WikiBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.tree = discord.app_commands.CommandTree(self)

    async def setup_hook(self):
        load_state()
        self.add_view(WikiView())

        api_key = os.environ.get("GAMESTATE_API_KEY", "")
        port = int(os.environ.get("GAMESTATE_PORT", "8099"))
        if api_key:
            asyncio.create_task(start_server(port, api_key))
        else:
            print("GAMESTATE_API_KEY not set — game state server disabled")

        @self.tree.command(
            name="wiki",
            description="Post the Praetoris server wiki",
            guild=discord.Object(id=GUILD_ID),
        )
        @discord.app_commands.checks.has_permissions(manage_messages=True)
        async def wiki_command(interaction: discord.Interaction):
            await interaction.response.defer()
            embed = discord.Embed(
                title="Praetoris \u2014 Server Wiki",
                description=WIKI_DESCRIPTION,
                color=WIKI_COLOR,
            )
            embed.set_thumbnail(url=ICON_URL)
            for field in WIKI_FIELDS:
                embed.add_field(
                    name=field["name"],
                    value=field["value"],
                    inline=field.get("inline", False),
                )
            await interaction.followup.send(embed=embed, view=WikiView())

        await self.tree.sync(guild=discord.Object(id=GUILD_ID))

    async def on_ready(self):
        print(f"Wiki bot ready: {self.user} (guilds: {len(self.guilds)})")

    async def on_message(self, message: discord.Message):
        if message.channel.id != RESET_CHANNEL_ID:
            return
        if message.content:
            check_reset_message(message.content, message.created_at)


if __name__ == "__main__":
    WikiBot().run(TOKEN)

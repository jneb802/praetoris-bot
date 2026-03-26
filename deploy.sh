#!/usr/bin/env bash
# Deploy praetoris-bot to moonmail VPS.
# First run: also does initial setup (venv, systemd).
set -euo pipefail

HOST="root@moonmail"
REMOTE_DIR="/opt/praetoris-bot"

echo "Syncing files to moonmail..."
rsync -avz --exclude '.env' --exclude '.venv' --exclude '__pycache__' --exclude 'state.json' \
  "$(dirname "$0")/" "$HOST:$REMOTE_DIR/"

echo "Setting up and restarting on moonmail..."
ssh "$HOST" bash -s <<'EOF'
cd /opt/praetoris-bot

# Create venv if missing
if [ ! -d .venv ]; then
  python3 -m venv .venv
fi
.venv/bin/pip install -q -r requirements.txt

# Install systemd service if missing
if [ ! -f /etc/systemd/system/praetoris-bot.service ]; then
  cp praetoris-bot.service /etc/systemd/system/
  systemctl daemon-reload
  systemctl enable praetoris-bot
fi

# Check .env exists
if [ ! -f .env ]; then
  cp .env.example .env
  echo "WARNING: .env created from example — add DISCORD_BOT_TOKEN before starting"
  exit 0
fi

systemctl restart praetoris-bot
systemctl status praetoris-bot --no-pager
EOF

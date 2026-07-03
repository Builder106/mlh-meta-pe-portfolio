#!/bin/bash
set -e

PROJECT_DIR="$HOME/MLH-Meta-PE-Portfolio"
VENV_DIR="$PROJECT_DIR/python3-virtualenv"

echo "Pulling latest changes from main..."
cd "$PROJECT_DIR"
git fetch
git reset origin/main --hard

echo "Installing dependencies..."
source "$VENV_DIR/bin/activate"
pip install -r requirements.txt
deactivate

echo "Restarting Flask server (gunicorn via systemd)..."
systemctl restart portfolio.service

echo "Done. Service status:"
systemctl is-active portfolio.service

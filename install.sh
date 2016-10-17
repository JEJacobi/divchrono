#!/bin/sh

PACKAGES="git curl rsync htop vim tmux python3 python3-doc python3-dev python3-pip python3-requests python3-rpi.gpio python3-smbus i2c-tools"

# Install required packages:

echo "Installing required packages."

apt-get -qq install $PACKAGES

# Set up the software as a daemon:

echo "Setting up daemon."

# TODO

# Set up the new default password:

echo "Setting up root password (check documentation)."

echo "root:diverge" | chpasswd

# Set up the motd:

echo "Setting up motd."

cat > /etc/motd << EOM
 ______  _____ _    _ _______  ______  ______ _______ __   _ _______ _______
 |     \   |    \  /  |______ |_____/ |  ____ |______ | \  | |       |______
 |_____/ __|__   \/   |______ |    \_ |_____| |______ |  \_| |_____  |______

 _______ _     _  ______  _____  __   _  _____  _______ _______ _______ _______  ______
 |       |_____| |_____/ |     | | \  | |     | |  |  | |______    |    |______ |_____/
 |_____  |     | |    \_ |_____| |  \_| |_____| |  |  | |______    |    |______ |    \_

Made by: $(curl https://api.github.com/repos/JEJacobi/divchrono/contributors 2>/dev/null | grep -Po '(?<="login": ")[^"]*' | xargs echo | sed 's/ /, /g')
Compiled on: $(date)

EOM


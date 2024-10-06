#!/bin/bash

# Check if Homebrew is installed, install if not
if ! command -v brew &>/dev/null; then
  echo "Homebrew not found. Installing Homebrew..."
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
  echo "Homebrew is already installed."
fi

# Use chezmoi to get the correct path to the Brewfile
BREWFILE_PATH="$(chezmoi source-path)/Brewfile"

# Use the Brewfile to install packages
if [ -f "$BREWFILE_PATH" ]; then
  echo "Installing packages from Brewfile..."
  brew bundle --file="$BREWFILE_PATH"
else
  echo "Brewfile not found in chezmoi source directory. Skipping package installation."
fi

echo "Brew setup complete."

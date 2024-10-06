#!/bin/bash
set -e

# Hide the Dock
defaults write com.apple.dock autohide -bool true
killall Dock

# Show all hidden files
defaults write com.apple.finder AppleShowAllFiles -bool true
killall Finder

echo "Mac settings have been updated. Some changes may require a logout/login to take effect."

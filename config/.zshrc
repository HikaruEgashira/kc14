#!/usr/bin/env zsh

export EDITOR='code --wait'

# starship prompt
eval "$(starship init zsh)"
export STARSHIP_CONFIG=~/.starship.toml

# zsh-autosuggestions
source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh

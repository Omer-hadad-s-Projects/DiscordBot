activate_venv() {
  if [ -f ".venv/bin/activate" ]; then
    # For bash and zsh
    . .venv/bin/activate
  else
    echo "Virtual environment not found in .venv directory."
    exit 1
  fi
}

sh discord_token_saver.sh
python3 -m venv .venv
activate_venv
pip3 install -U pip
pip3 install -U python-dotenv
pip3 install -U discord
pip3 install -U yt_dlp
pip3 install -U pynacl
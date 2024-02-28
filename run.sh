cd "$(dirname "$0")"/scripts
printf '\e[8;57;200t'

MainMenu() {
    clear
    echo "--OPTIONS--"
    echo "[0] Convert Video"
    echo "[1] Play Video"
    echo "[2] Delete Converted Video"
    echo "[~] Quit"

    read -p "Enter your choice: " choice
    return $choice
}

MainMenu
choice=$?

if [ $choice -eq 0 ]; then
    python3 process.py 1
elif [ $choice -eq 1 ]; then
    ./video_play
elif [ $choice -eq 2 ]; then
    python3 process.py 0
fi

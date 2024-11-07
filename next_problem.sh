acc add

current=$(basename "$PWD")
next_dir=$(ls -d ../*/ | sort | awk -v curr="$current/" '$0 == ("../" curr) {getline; print $0}')
if [ -n "$next_dir" ]; then
    cd "$next_dir"
    code "main.py"
else
    echo "You answered ALL problem!!! Congratulations!!"
fi
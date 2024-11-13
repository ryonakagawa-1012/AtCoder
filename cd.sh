dir=$1

cd ../"$dir"

if [ $? -eq 0 ]; then
    code main.py
fi
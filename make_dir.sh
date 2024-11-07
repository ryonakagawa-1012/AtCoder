contest=$1

dir=$(echo "$contest" | grep -o '^[^0-9]\+'|tr 'a-z' 'A-Z') # コンテスト名の最初の文字列群を抽出し、全て大文字に変換

mkdir "$dir" && cd "$dir"

acc new "$contest"

cd "$contest"

cd "$(ls -d */ | head -1)"

code "main.py"
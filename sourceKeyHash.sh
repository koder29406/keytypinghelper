#!/bin/bash

input="key"
readarray keylines < $input

echo "${keylines[@]}"

sha_result=$(shasum -a 1 $input)
key_hash=${sha_result% *}
count=0
echo "   KEY HASH: $key_hash"
for i in "${keylines[@]}"
do
	let "count=$count + 1"
	sha_result=$(echo $i | shasum --algorithm 1)
	line_hash=${sha_result% *}
	echo "LINE $count HASH: $line_hash"
done

awk 'NR == 10' file.txt

sed -n 10p file.txt

tail -n+10 file.txt|head -1

cnt=0
while read line && [ $cnt -le 10 ]; do
    let 'cnt = cnt + 1'
    if [ $cnt -eq 10 ]; then
        echo $line
        exit 0
    fi
done < file.txt
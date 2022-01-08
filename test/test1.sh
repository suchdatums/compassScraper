
while true ; do
    read inp
    if [ -z $inp ]; then
        echo "NO INPUT"
        break
    fi
    echo "inp is $inp"
done

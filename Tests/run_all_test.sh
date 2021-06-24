cd "$(dirname "$0")"

array=()

for i in *.py
do
    python $i
    if [ $? -eq 0 ]
    then
        echo "test successful"
    else
	echo "test not successfull"
	exit 1
    fi
done
exit 0

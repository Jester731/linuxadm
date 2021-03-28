  
#!/bin/bash
if [ "$#" -ne 4 ]

then
	echo "Correct paramethres: height width fill paint"
	exit 1
fi

h=$1
w=$2
f=$3
p=$4
rect=""

for (( i = 1; i <= $h; i++ ))
do

	for (( j = 1; j <= $w; j++ ))
	do

		if [ "$i" -eq 1 -o "$i" -eq "$h" -o "$j" -eq 1 -o "$j" -eq "$w" -o "$f" -eq 1 ] 
		then 
			echo -n "$p"
		else
			echo -n " "
		fi
        
	done

	echo

done
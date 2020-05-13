#!/bin/bash

echo '' > energy.txt
echo '' > time.txt

for file in *.out
do
	grep "PWSCF        :" $file | cut -d":" -f2 | cut -d's' -f1 >> time.txt
	grep "!" $file | cut -d'=' -f2 >> energy.txt
done


#!/bin/bash

echo `./Si_scf.sh`

echo '' > energy.txt
echo '' > time.txt

for file in *.out
do
	grep "PWSCF        :" $file | cut -d":" -f2 | cut -d's' -f1 >> time.txt
	grep "!" $file | cut -d'=' -f2 >> energy.txt
done

echo `python3 script1_python.py | python3`


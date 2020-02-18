#!/bin/sh

for file in $(find . -name "*.dot")
do {
    filename=`echo $file|awk -F . '{print $1}'`
    dot -Tpng $file -o $filename.png
}
done

for file in $(find . -name "*.py")
do {
    python $file
}
done

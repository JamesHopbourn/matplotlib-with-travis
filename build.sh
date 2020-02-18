#!/bin/sh

for file in $(find . -name "*.dot"|xargs basename)
do {
    filename=`echo $file|awk -F . '{print $1}'`
    dot -Tpng $file -o $filename.png
}
done

for file in $(find . -name "*.py"|xargs basename)
do {
    python $file
}
done

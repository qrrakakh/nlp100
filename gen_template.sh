#!/bin/bash

exit 1
for z in 1 2 3 4 5 6 7 8 9 10
do
    num=`printf "%02d" $z`
    filename=chap${num}.py
    enumfrom=`expr $z \* 10 - 10`
    enumto=`expr ${enumfrom} + 9`
    echo -e '#!/usr/bin/env python' > ${filename}
    for i in `seq -w ${enumfrom} ${enumto}`
    do
        echo -e "\n" >> ${filename}
        echo "def chap${num}_$i(s):" >> ${filename}
        echo "    pass" >> ${filename}
    done
done

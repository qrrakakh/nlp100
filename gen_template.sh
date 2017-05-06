#!/bin/bash

exit 1
for z in 1 2 3 4 5 6 7 8 9 10
do
    num=`printf "%02d" $z`
    filename=chap${num}.py
    enumfrom=`expr $z \* 10 - 10`
    enumto=`expr ${enumfrom} + 9`
    echo '#!/usr/bin/env python' > ${filename}
    echo '# -*- coding: utf-8 -*-' >> ${filename}
    for i in `seq -w ${enumfrom} ${enumto}`
    do
        echo -e "\n" >> ${filename}
        echo "def chap${num}_$i(s):" >> ${filename}
        echo "    pass" >> ${filename}
    done


    filename="./tests/test_chap${num}.py"
    echo '#!/usr/bin/env python' > ${filename}
    echo '# -*- coding: utf-8 -*-' >> ${filename}
    echo "" >> ${filename}
    echo "import unittest" >> ${filename}
    echo "import chap${num}" >> ${filename}
    echo -e "\n" >> ${filename}
    echo "class TestChap${num}(unittest.TestCase):" >> ${filename}
    for i in `seq -w ${enumfrom} ${enumto}`
    do
        echo -e "\n" >> ${filename}
        echo "    def test_${i}(self):" >> ${filename}
        echo "        self.assertEqual(chap${num}.chap${num}_${i}(None), \"\")" >> ${filename}
    done
done

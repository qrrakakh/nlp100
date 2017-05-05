#!/bin/sh

mkdir -p data/
wget -q -nc -P data/ http://www.cl.ecei.tohoku.ac.jp/nlp100/data/hightemp.txt
wget -q -nc -P data/ http://www.cl.ecei.tohoku.ac.jp/nlp100/data/jawiki-country.json.gz
wget -q -nc -P data/ http://www.cl.ecei.tohoku.ac.jp/nlp100/data/neko.txt
wget -q -nc -P data/ http://www.cl.ecei.tohoku.ac.jp/nlp100/data/nlp.txt
wget -q -nc -P data/ http://www.cl.ecei.tohoku.ac.jp/nlp100/data/artist.json.gz
wget -q -nc -P data/ http://www.cl.ecei.tohoku.ac.jp/nlp100/data/enwiki-20150112-400-r10-105752.txt.bz2

python3 -m unittest tests.test_chap01
#python3 -m unittest tests.test_chap02
#python3 -m unittest tests.test_chap03
#python3 -m unittest tests.test_chap04
#python3 -m unittest tests.test_chap05
#python3 -m unittest tests.test_chap06
#python3 -m unittest tests.test_chap07
#python3 -m unittest tests.test_chap08
#python3 -m unittest tests.test_chap09
#python3 -m unittest tests.test_chap10

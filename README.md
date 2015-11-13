attn: this repo is in beta mode, use at your own risk.

py-bitcoin-address-extractor-f-i-a
=====================

python script to parse bitcoin addresses from insight api's level db



![](http://i.imgur.com/o1u9icI.png)

usage
=====================
python ./py-bitcoin-address-extractor-f-i-a.py -o output_file.txt

or

python ./py-bitcoin-address-extractor-f-i-a.py --help

install pre-requisites
=====================
```
sudo apt-get install -y build-essential autoconf libtool pkg-config python-opengl python-imaging python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev python-pip libleveldb1 libleveldb-dev

sudo pip install ez_setup leveldb plyvel
```

requirements
=====================
1) linux/mac (not tested on windows)

2) [python 2.7+](https://www.python.org/downloads/) ,
[libleveldb1](http://packages.ubuntu.com/trusty/libs/libleveldb1),
[libleveldb-dev](http://packages.ubuntu.com/search?keywords=libleveldb-dev),
[plyvel](http://plyvel.readthedocs.org/en/latest/installation.html) , [insight-api/Insight](https://github.com/bitpay/insight-api) integrated & synched with [Bitcoin](https://github.com/bitcoin/bitcoin)

3) for fastest perfomance RAM > 8 Gb is required, if your RAM is limited use option "liteonmemory" ...

4) old insight-api 

python ./py-bitcoin-address-extractor-f-i-a.py -liteonmemory -o output_file.txt



execution
=====================
insight-api server needs to be stopped before running script


license
=====================
standard MIT license

bitcoin tips
=====================
16QcZYETFbWRijK3xBVbDgpvW1ZWsdNujY

![](http://i.imgur.com/0YvZ6sA.png)

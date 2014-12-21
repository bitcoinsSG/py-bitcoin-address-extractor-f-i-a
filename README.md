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

requirements
=====================
1) Linux/Mac (not tested on windows)

2) [python 2.7+](https://www.python.org/downloads/) , [plyvel](http://plyvel.readthedocs.org/en/latest/installation.html) , [insight-api/Insight](https://github.com/bitpay/insight-api) integrated & synched with [Bitcoin](https://github.com/bitcoin/bitcoin)

3) for fastest perfomance RAM > 8 Gb is required, if RAM is limited use option "liteonmemory" ...

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

#requirements
# bitcoind and insight api installed, 
# insight might have to stopped so the leveldb dir isn't locked
# sudo pip install leveldb
# sudo pip install plyvel
import sys
import argparse
import logging
import os
import leveldb
import plyvel
import codecs
import subprocess
import datetime

### Start of declaration of global variables
default_dir_for_testnet_db=os.path.expanduser('~') + '/.insight/testnet' 
default_dir_for_livenet_db=os.path.expanduser('~') + '/.insight' 
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(levelname)-6s %(message)s',datefmt="%H:%M:%S")
database_dir=""
start_time=datetime.datetime.now()
### End of declaration of global variables



def main():
	parser = argparse.ArgumentParser(description='python script to parse bitcoin addresses from insight api\'s level db')
	parser.add_argument('-testnet', action='store_true', dest='db_type', help='turn this on to process testnet db instead of livenet', required=False)
	parser.add_argument('-sort', action='store_true', dest='sorted', help='turn this on to sort addresses', required=False)
	parser.add_argument('-d', action='store', dest='directory_for_db', help='if db directory is not default (i.e. ~/.insight..); specify', required=False)
	parser.add_argument('-o', action='store', dest='output_file', help='\033[31m' +'(Rq)' + '\033[0m' + ' output file (e.g. extracted_add.txt)', required=True)
	#parser.add_argument('-anon', action='store_true', dest='route_via_tor', help='route via tor or not', required=False)
	parser.add_argument('--version', action='version', version='%(prog)s 1.0')
	args = parser.parse_args()
	print_logo()
	#logging.info("parameters")
	if args.db_type: # Testnet
		logging.info("db: testnet")
		if not args.directory_for_db: # If no dir was mentioned, assign as default
			args.directory_for_db=default_dir_for_testnet_db
		extraction_core_txs_optimized_three(directory=args.directory_for_db,args=args)
	else:			 # Livenet
		logging.info("db: livenet")
		if not args.directory_for_db:
			args.directory_for_db=default_dir_for_livenet_db
        extraction_core_txs_optimized_three(directory=args.directory_for_db,args=args)


def extraction_core_txs_optimized_three(directory,args):
	output_file = codecs.open(args.output_file, 'w', 'utf8')
	logging.info("processing db dir: " + directory + "/txs")
	logging.info("algo: extract-core optimized 3")
	if(args.sorted):
		logging.info("sorting: True")
	else:
		logging.info("sorting: False")
	number_of_addreses=0
	count=0
	show_interval = 1000
	currentaddress=["thisisatemplateusedforbootstrapping-",0]
	currentaddresslen=len(currentaddress)
	list_of_addresses=""
	for key, value in plyvel.DB(directory+"/txs", create_if_missing=False):
		#print key[0][0:2]
		if key[2] != "a":
			break
		if not currentaddress == key[5:currentaddresslen+5]:
			currentaddress = key[5:6+(key[5:].index("-"))]
			currentaddresslen=len(currentaddress)
			list_of_addresses=list_of_addresses+currentaddress
			number_of_addreses+=1
			#output_file.write(currentaddress + '\n')
		count+=1
		if (count % show_interval) == 0:
			logging.info('tx: ' + str(count) + '\t add: ' + str(number_of_addreses) )
			show_interval = show_interval * 2
	logging.info('done')
	output_file.write(list_of_addresses)
	output_file.close()
	#for item in list_of_addresses:
		#output_file.write("%s\n" % item)
	if(args.sorted):
		logging.info('sorting addresses')
		subprocess.call(["tr '-' '\n' < " + args.output_file +" | sort -o " + args.output_file],shell=True)
	else:
		logging.info('processing file')
		subprocess.call(["tr '-' '\n' < " + args.output_file +" > " + "temp_" + args.output_file],shell=True)
		subprocess.call(["mv -f" + " temp_" + args.output_file + "  " + args.output_file],shell=True)
	#subprocess.call(["awk -F'-' '{print $2}' " + args.output_file + " | sort -u -o " + args.output_file], shell=True)
	logging.info('output file: ' + args.output_file)
	logging.info('# of transactions: ' + str(count))
	logging.info('   # of addresses: ' + str(number_of_addreses))
	logging.info("total time: " + '\033[92m' + (datetime.datetime.now()-start_time).__str__().split('.')[0] + '\033[0m' + ' on ' + datetime.datetime.today().strftime('%b, %d, %Y') )
	logging.info('\033[92m' + 'completed.'+ '\033[0m')
	print("") 
	exit(0)


def extraction_core_txs_optimized_two(directory,args):
	output_file = codecs.open(args.output_file, 'w', 'utf8')
	logging.info("processing db dir: " + directory + "/txs")
	logging.info("algorithm: extraction core optimized 2")
	if(args.sorted):
		logging.info("sorting: True")
	else:
		logging.info("sorting: False")
	number_of_addreses=0
	count=0
	show_interval = 1000
	currentaddress=["-thisisatemplateusedforbootstrapping-",0]
	currentaddress[1]=len(currentaddress[0])
	list_of_addresses=""
	for key in plyvel.DB(directory+"/txs", create_if_missing=False):
		#print key[0]
		if key[0][0:4] != "txa2":
			break
		if not currentaddress[0] == key[0][4:currentaddress[1]+4]:
			currentaddress[0] = key[0][4:6+(key[0][5:].index("-"))]
			currentaddress[1]=len(currentaddress[0])
			list_of_addresses=list_of_addresses+currentaddress[0][1:]
			number_of_addreses+=1
			#output_file.write(currentaddress[0] + '\n')
		count+=1
		if (count % show_interval) == 0:
			logging.info('processed ' + str(count) +' txs')
			show_interval = show_interval * 2
	logging.info('processed ' + str(count) +' txs .. '+  'done')
	output_file.write(list_of_addresses)
	output_file.close()
	#for item in list_of_addresses:
		#output_file.write("%s\n" % item)
	if(args.sorted):
		logging.info('sorting addresses')
		subprocess.call(["tr '-' '\n' < " + args.output_file +" | sort -u -o " + args.output_file],shell=True)
	else:
		logging.info('processing file')
		subprocess.call(["tr '-' '\n' < " + args.output_file +" > " + "temp_" + args.output_file],shell=True)
		subprocess.call(["mv -f" + " temp_" + args.output_file + "  " + args.output_file],shell=True)
	#subprocess.call(["awk -F'-' '{print $2}' " + args.output_file + " | sort -u -o " + args.output_file], shell=True)
	logging.info('output file: ' + args.output_file)
	logging.info('# of addresses: ' + str(number_of_addreses))
	logging.info("total time: " + '\033[92m' + (datetime.datetime.now()-start_time).__str__().split('.')[0] + '\033[0m' + ' on ' + datetime.datetime.today().strftime('%b, %d, %Y') )
	logging.info('\033[92m' + 'completed.'+ '\033[0m')
	print("") 
	exit(0)


def print_logo(indent="           "):
	# print ello logo
	new_lines_before=2
	new_lines_after=2
	for i in range(1,new_lines_before):
		print("")
	print("          py-bitcoin-address-extractor-f-i-a")
	print("-------------------------------------------------------")
	print("       python script to parse bitcoin addresses        ")
	print("              from insight api's level db ")
	print("                     version: Alpha")
	print("-------------------------------------------------------")
	#print("")
	print(" o                                                    ")
	print("O     o                  o                            ")
	print("O        O                                            ")
	print("o       oOo                                           ")
	print("OoOo. O  o   .oOo  .oOo. O 'OoOo. .oOo     .oOo  .oOoO")
	print("O   o o  O   O     O   o o  o   O `Ooo.    `Ooo. o   O")
	print("o   O O  o   o     o   O O  O   o     O        O O   o")
	print("`OoO' o' `oO `OoO' `OoO' o  o   O `OoO'  O `OoO' `OoOo")
	print("                                                     O ")
	print("16QcZYETFbWRijK3xBVbDgpvW1ZWsdNujY                OoO' ")    
	for i in range(1,new_lines_after):
		print("")
	# Initialize default logging behaviour

def print_after_end(indent="           "):
	print("\033[92m" + "@bitcoinsg" + "\033[0m")



# old functions
def extraction_core_txs(directory,args):
	output_file = codecs.open(args.output_file, 'w', 'utf8')
	logging.info("processing db dir: " + directory + "/txs")
	logging.info("algorithm: extraction core 0")
	count=0
	show_interval = 100
	for key, value in plyvel.DB(directory+"/txs", create_if_missing=False):
		if key[0:4] != "txa2":
			break
		output_file.write(key + ' ' + value + '\n')
		count+=1
		if (count % show_interval) == 0:
			logging.info('processed ' + str(count) +' txs')
			show_interval = show_interval * 2
	logging.info('processed ' + str(count) +' txs .. '+ '\033[92m' + 'done' + '\033[0m')
	logging.info('sorting and removing redundancies')
	output_file.close()
	subprocess.call(["awk -F'-' '{print $2}' " + args.output_file + " | sort -u -o " + args.output_file], shell=True)
	logging.info('output file: ' + args.output_file)
	logging.info("total time: " + str(datetime.datetime.now()-start_time) )
	logging.info('\033[92m' + 'completed.'+ '\033[0m')
	print("") 
	exit(0)


def extraction_core_txs_optimized(directory,args):
	output_file = codecs.open(args.output_file, 'w', 'utf8')
	logging.info("processing db dir: " + directory + "/txs")
	logging.info("algorithm: extraction core optimized 1")
	count=0
	show_interval = 100
	for key in plyvel.DB(directory+"/txs", create_if_missing=False):
		#print key[0]
		if key[0][0:4] != "txa2":
			break
		output_file.write(key[0] + '\n')
		count+=1
		if (count % show_interval) == 0:
			logging.info('processed ' + str(count) +' txs')
			show_interval = show_interval * 2
	logging.info('processed ' + str(count) +' txs .. done')
	logging.info('sorting and removing redundancies')
	output_file.close()
	subprocess.call(["awk -F'-' '{print $2}' " + args.output_file + " | sort -u -o " + args.output_file], shell=True)
	logging.info('output file: ' + args.output_file)
	logging.info("total time: " + str(datetime.datetime.now()-start_time) )
	logging.info('\033[92m' + 'completed.'+ '\033[0m')
	print("") 
	exit(0)
if __name__ == '__main__':
    main()

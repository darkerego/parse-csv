#!/usr/bin/env python
import os,sys,argparse
import pprint
import csv
DATADIR = ""

try:
        # For Python 3+
        from configparser import ConfigParser, NoSectionError
except ImportError:
        # Fallback to Python 2.7
        from ConfigParser import ConfigParser, NoSectionError
def main(argv):
        # Setup Argument Parser
        parser = argparse.ArgumentParser(description='Generic Parser')
        #parser.add_argument('-c', '--config_file', default='csv.cfg', type=str, required=False, help='config .cfg file')
        parser.add_argument('-f', '--input_file', default='input.csv', type=str, required=True, help='File to parse')
        # parse args
        args = parser.parse_args()
        input_file = args.input_file
        DATAFILE = str(input_file)
        return DATAFILE

def parse_csv(datafile):
	data = []
	n = 0

	with open(datafile, 'rb') as sd:
		r = csv.DictReader(sd)

		for line in r:
			data.append(line)
	return data


if __name__ == '__main__':
        DATAFILE = main(sys.argv[1:])
	datafile = os.path.join(DATADIR, DATAFILE)
	#parse_csv(datafile)
	d = parse_csv(datafile)
	pprint.pprint(d)


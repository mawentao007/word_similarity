#coding=utf8
import Levenshtein
import os
import codecs
import sys


def main(input, output):
	result = []
	wrong_data = []
	with codecs.open(input, encoding="utf-8") as f:
		for row in f.readlines():
			eid, id, name, reason, baike_url = row.strip().split('\t')
			lev_dis = Levenshtein.distance(name.lower(), reason.lower())
			lreason = len(reason)
			lname = len(name)
			shorter = min(lreason, lname)
			if shorter == 0:
				wrong_data.append([eid, name, reason])
				continue
			longer = max(lreason, lname)
			len_dis = longer - shorter
			if len_dis >= 4:
				continue;
			coff = float(lev_dis - len_dis)/shorter
			if coff < 0.1:
				result.append([eid, name, reason, baike_url, str(coff)])

	with codecs.open(output, 'w', encoding='utf-8') as co:
		for row in result:
			co.write("\t".join(row) + '\n')

	with codecs.open(os.path.join(os.path.dirname(__file__),"./data/wrong_file"), 'w', encoding='utf-8') as cw:
		for row in wrong_data:
			cw.write("\t".join(row) + '\n')


if __name__ == '__main__':
	input= sys.argv[1]
	output = sys.argv[2]
	main(input, output)

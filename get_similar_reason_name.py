#coding=utf8
import Levenshtein
import codecs


def main():
	result = []
	wrong_data = []
	with codecs.open("./data/reason_name_file", encoding="utf-8") as f:
		for row in f.readlines():
			eid,reason,name = row.strip().split('\t')
			lev_dis = Levenshtein.distance(name.lower(), reason.lower())

			lreason = len(reason)
			lname = len(name)
			shorter = min(lreason, lname)
			if shorter == 0:
				wrong_data.append([eid, name, reason])
				continue
			longer = max(lreason, lname)
			len_dis = longer - shorter

			coff = float(lev_dis - len_dis)/shorter
			if coff < 0.5:
				result.append([eid, name, reason])

	with codecs.open("./data/result_file", 'w', encoding='utf-8') as co:
		for row in result:
			co.write("\t".join(row) + '\n')

	with codecs.open("./data/wrong_file", 'w', encoding='utf-8') as cw:
		for row in wrong_data:
			cw.write("\t".join(row) + '\n')


if __name__ == '__main__':
	main()
#coding=utf8
#对同一个实体的多个推荐理由进行去重
id2reasons = {}

with open("./data/reason_status") as f:
	for row in f.readlines():
		eid,reason = row.split('\t')
		if not id2reasons.has_key(eid):
			id2reasons[eid] = [list(reason.strip('\n').decode('utf8'))]
		else:
			id2reasons[eid].append(list(reason.strip('\n').decode('utf8')))


#重复比例超过阈值，丢弃该描述
def clean_dup(reasons,reduntant = 0.5):
	if len(reasons) == 1:
		return reasons
	#返回的最终结果
	result = []


	longest = max(reasons,key=len)
	#print longest
	#print reasons
	result.append(longest)
	reasons.remove(longest)
	# 最长字符串作为对比字典
	reasonSet = set(longest)

#设定一个阈值，超过该值，丢弃相关字符串;否则将该字符串加入到结果中，并扩充库。
	for rea in reasons:
		if(same_percent(reasonSet,rea) >= reduntant):
			continue
		else:
			result.append(rea)
			for wd in rea:
				reasonSet.add(wd)

	return result

#计算共有字符占比
def same_percent(lib,target):
	samepart = 0.0
	for wd in target:
		if wd in lib:
			samepart += 1
	return samepart / len(target)

with open("./data/reason_dereplicated",'w') as f:
	for key,reasons in id2reasons.iteritems():
		new_reasons = clean_dup(reasons)
		for reason in new_reasons:
			f.write("%s\t%s\t\n"%(key.encode("utf8"),''.join(reason).encode("utf8")))
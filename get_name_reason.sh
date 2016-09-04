
#	get entity_kgid,name,reason with some filter

#	get reason which can be shown by with id; the smallest id can be shown 


#	select entity_kgid, id, reason from entity_reason where from_info != "zhongce"  order by id ASC into outfile "/home/img/tmp/reason_file" ;
#	select entity_kgid, entity_name, baike_url from entity_basic_info order by entity_kgid ASC into outfile "/home/img/tmp/name_file";


awk -F'[\t]' '{if(d[$1] != 1 && length($1)==32){print;d[$1]=1}}' reason_file > reason_file_shown

sort -t $'\t' -k 1 reason_file_shown >reason_file_sorted;

join -t $'\t' -1 1 -2 1  reason_file_sorted name_file > reason_name_file

awk -F'[\t]' '{if($4!="") {print}}' reason_name_file > Reason_name

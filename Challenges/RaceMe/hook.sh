#!/bin/sh

# echo "" >> /tmp/nsjail.cfg
# echo "mount {" >> /tmp/nsjail.cfg
# echo "src: \"/dev\"" >> /tmp/nsjail.cfg
# echo "dst: \"/dev\"" >> /tmp/nsjail.cfg
# echo "is_bind: true" >> /tmp/nsjail.cfg
# echo "}" >> /tmp/nsjail.cfg
# 
# sed -i -e 's/src:"\/srv"  dst:"\/"  is_bind:true  nosuid:true/src:"\/srv"  dst:"\/"  is_bind:true  nosuid:false/g' /tmp/nsjail.cfg
# 
# echo "envar: \"TERM=linux\"" >> /tmp/nsjail.cfg
# # echo "envar: \"PS1=$ \"" >> /tmp/nsjail.cfg
# 
# # echo "seccomp_string: \"ALLOW {\"" >> /tmp/nsjail.cfg
# # echo "seccomp_string: \" renameat2, renameat, remap_file_pages, rename\"" >> /tmp/nsjail.cfg
# # echo "seccomp_string: \"}\"" >> /tmp/nsjail.cfg
# # echo "seccomp_string: \"DEFAULT ALLOW\"" >> /tmp/nsjail.cfg
# echo "cap: \"CAP_SETUID\"" >> /tmp/nsjail.cfg
# 
# cat << EOF >> /tmp/nsjail.cfg
# uidmap: [
# 	{
# 		inside_id: "0"
# 		outside_id: "0"
# 		count: 1
# 	}
# ]
# 
# gidmap: [
# 	{
# 		inside_id: "0"
# 		outside_id: "0"
# 		count: 1
# 	}
# ]
# 
# mount: [
# 	{
# 		dst: "/proc"
# 		fstype: "proc"
# 		rw: false
# 	        nosuid: true
# 		nodev: true
# 		noexec: true
# 	}
# ]
# EOF
# 
# 	#{
# 	#	inside_id: "1000"
# 	#	outside_id: "1000"
# 	#	count: 1
# 	#}
# 	
# 	#{
# 	#	inside_id: "1000"
# 	#	outside_id: "1000"
# 	#	count: 1
# 	#}
# 
# 
# # echo "clone_newuser: false" >> /tmp/nsjail.cfg
# 
# cat /tmp/nsjail.cfg
# 
# chmod +s /srv/app/catto

cp /srv/nsjail.conf /tmp/nsjail.cfg

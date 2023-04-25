#!/bin/bash
tag=2
name="dumped"
flag_id=12

echo "sseCTF{1\$_Tr45#_=_4n0t#3r\$_G01d_$RANDOM}" > dumped_flag.txt
cat dumped_flag.txt
flag=$(cat dumped_flag.txt)

docker build -t $name .
docker tag $name cookie303/$name:$tag
docker push cookie303/$name:$tag

patch='{"spec":{"template":{"spec":{"containers":[{"name":"'$name'-challenge","image":"docker.io/cookie303/'$name':'$tag'"}]}}}}'

# microk8s.kubectl patch deployment a5 --patch-file patch.yaml
microk8s.kubectl patch deployment $name --patch $patch

curl \
    -X PATCH "http://13.126.197.34/api/v1/flags/$flag_id" \
    -H "Authorization: Token feb566432a58da3ac62227579b5d90e128efe527e7dc41f7e3add57e61149a50" \
    -H "Content-Type: application/json" \
    -d '{"content": "'$flag'", "id": "'$flag_id'"}'



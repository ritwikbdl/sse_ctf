#!/bin/bash
# name=$1

# docker build -t $name .
# docker tag $name cookie303/$name:1
# docker push cookie303/$name:1


# microk8s.kubectl apply -f "1. deployment.yaml"
# microk8s.kubectl apply -f "2. service.yaml"
# microk8s.kubectl patch configmaps nginx-ingress-tcp-microk8s-conf --namespace ingress --patch-file "3. ingress.yaml"
# # microk8s.kubectl apply -f "3. ingress.yaml"
# microk8s.kubectl patch daemonsets.apps --namespace=ingress nginx-ingress-microk8s-controller --patch "$(cat "4. daemonset.yaml")"
# microk8s.kubectl apply -f "5. hpa.yaml"


tag=13

echo "sseCTF{hE@P_Is_haRd_70_Prot3cT_Bu7_fUn_7O_EXPlO1t_$RANDOM}" > flag.txt
cat flag.txt
flag=$(cat flag.txt)

docker build -t notes .
docker tag notes cookie303/notes:$tag
docker push cookie303/notes:$tag

patch='{"spec":{"revisionHistoryLimit":0,"template":{"spec":{"containers":[{"name":"a5-challenge","image":"docker.io/cookie303/notes:'$tag'"}]}}}}'

# microk8s.kubectl patch deployment a5 --patch-file patch.yaml
microk8s.kubectl patch deployment a5  --patch $patch

curl \
    -X PATCH "http://13.126.197.34/api/v1/flags/6" \
    -H "Authorization: Token feb566432a58da3ac62227579b5d90e128efe527e7dc41f7e3add57e61149a50" \
    -H "Content-Type: application/json" \
    -d '{"content": "'$flag'", "id": "6"}'




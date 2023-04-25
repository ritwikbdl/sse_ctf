#!/bin/bash
name=$1

docker build -t $name .
docker tag $name cookie303/$name:1
docker push cookie303/$name:1


microk8s.kubectl apply -f "1. deployment.yaml"
microk8s.kubectl apply -f "2. service.yaml"
microk8s.kubectl patch configmaps nginx-ingress-tcp-microk8s-conf --namespace ingress --patch-file "3. ingress.yaml"
# microk8s.kubectl apply -f "3. ingress.yaml"
microk8s.kubectl patch daemonsets.apps --namespace=ingress nginx-ingress-microk8s-controller --patch "$(cat "4. daemonset.yaml")"
microk8s.kubectl apply -f "5. hpa.yaml"
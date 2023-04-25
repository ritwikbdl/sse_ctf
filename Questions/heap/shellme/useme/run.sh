#!/bin/bash
# name=$1

# docker build -t $name .
# docker tag $name cookie303/$name:latest
# docker push cookie303/$name:latest


microk8s.kubectl apply -f "deployment.yaml"
microk8s.kubectl apply -f "service.yaml"
microk8s.kubectl patch configmaps nginx-ingress-tcp-microk8s-conf --namespace ingress --patch-file "ingress.yaml"
# microk8s.kubectl apply -f "ingress.yaml"
microk8s.kubectl patch daemonsets.apps --namespace=ingress nginx-ingress-microk8s-controller --patch "$(cat "daemonset.yaml")"
microk8s.kubectl apply -f "hpa.yaml"
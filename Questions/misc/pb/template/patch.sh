docker build -t got2win .
docker tag got2win:latest cookie303/got2win:5
docker push cookie303/got2win:5
microk8s.kubectl patch deployment got2win --patch-file "1. deployment.yaml"
name="catchme"
# external port
xport=8888
# container port
cport=1024
folder=$1

mkdir -p $folder


sed "s/\$name/$name/g; s/\$cport/$cport/g; s/\$cport/$cport/g" '1. deployment.yaml' > $folder/deployment.yaml 

sed "s/\$name/$name/g; s/\$cport/$cport/g; s/\$xport/$xport/g" '2. service.yaml' > $folder/service.yaml

sed "s/\$name/$name/g; s/\$cport/$cport/g; s/\$xport/$xport/g" '3. ingress.yaml' > $folder/ingress.yaml

sed "s/\$name/$name/g; s/\$cport/$cport/g; s/\$xport/$xport/g" '4. daemonset.yaml' > $folder/daemonset.yaml

sed "s/\$name/$name/g; s/\$cport/$cport/g; s/\$xport/$xport/g" '1. deployment.yaml' > $folder/deployment.yaml

sed "s/\$name/$name/g; s/\$cport/$cport/g; s/\$xport/$xport/g" '5. hpa.yaml' > $folder/hpa.yaml

cp run.sh patch.sh modify.sh $folder/

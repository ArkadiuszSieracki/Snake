echo "Starting Minikube..."



echo "Deploying Promtail..."
kubectl apply -f promtail-configmap.yaml
kubectl apply -f promtail-deployment.yaml
kubectl apply -f promtail-service.yaml

echo "Deploying Grafana..."
kubectl apply -f grafana-deployment.yaml
kubectl apply -f grafana-service.yaml


echo "Deploying LOKI"
kubectl apply -f loki.yaml
echo "All components have been deployed successfully!"
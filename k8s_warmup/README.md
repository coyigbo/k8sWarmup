## K8s warm-up (quick start)

```bash
export DOCKER_USER=coyigbo

# Build + local test
docker build -t $DOCKER_USER/k8s-warmup:dev .
docker run --rm -p 8000:8000 -e PORT=8000 $DOCKER_USER/k8s-warmup:dev

# Push
docker tag $DOCKER_USER/k8s-warmup:dev $DOCKER_USER/k8s-warmup:v0.1
docker push $DOCKER_USER/k8s-warmup:v0.1

# kind + deploy
kind create cluster --name k8s101
kubectl apply -f deploy.yaml
kubectl apply -f service.yaml

# Port-forward
kubectl port-forward svc/web 8080:80
```

# Kubernetes

## private registry

https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/

1. Create a Gitlab Personal Access Token with `read-registry` scope
2. Create a Kubernetes Secret with the Gitlab Personal Access Token

```bash
kubectl create secret docker-registry gitlab-registry-secret \
  --docker-server=registry.gitlab.com \
  --docker-username=USERNAME \
  --docker-password=ACCESS-TOKEN
```

3. Reference the secret in the pod definition

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: private-reg
spec:
  containers:
    - name: private-reg-container
      image: registry.gitlab.com/image:tag
  imagePullSecrets:
    - name: gitlab-registry-secret
 ```

## cert-manager

https://cert-manager.io/v1.1-docs/installation/kubernetes/

```bash
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.1.1/cert-manager.yaml
```

### Apply issuers

```bash
kubectl apply -f kubernetes/prod-issuer.yaml
kubectl apply -f kubernetes/staging-issuer.yaml
```

## nginx-ingress

https://kubernetes.github.io/ingress-nginx/deploy/#digital-ocean

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.2/deploy/static/provider/do/deploy.yaml
```

### First create Ingress with staging issuer and then change to prod issuer if everything is ok

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: django-ingress
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-staging"
...
```

## external-secrets

https://external-secrets.io/latest/introduction/getting-started/

```bash
helm repo add external-secrets https://charts.external-secrets.io

helm install external-secrets \
   external-secrets/external-secrets \
    -n external-secrets \
    --create-namespace
```

### Gitlab variables

https://external-secrets.io/latest/provider/gitlab-variables/

1. Create a Gitlab Personal Access Token with `api` scope
2. Create a Kubernetes Secret with the Gitlab Personal Access Token

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: gitlab-secret
  labels:
    type: gitlab
type: Opaque
stringData:
  token: "ACCESS-TOKEN"
---
apiVersion: external-secrets.io/v1beta1
kind: SecretStore
metadata:
  name: gitlab-secret-store
spec:
  provider:
    gitlab:
      auth:
        SecretRef:
          accessToken:
            name: gitlab-secret
            key: token
      projectID: "PROJECT-ID"
```

3. Now you can create ExternalSecrets

```yaml
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: gitlab-external-secret
spec:
  refreshInterval: 60s

  secretStoreRef:
    kind: SecretStore
    name: gitlab-secret-store # Must match SecretStore on the cluster

  target:
    name: gitlab-external-secret # Name for the secret to be created on the cluster
    creationPolicy: Owner

  data:
    - secretKey: DEBUG # Key given to the secret to be created on the cluster
      remoteRef:
        key: DEBUG # Key of the variable on Gitlab
```
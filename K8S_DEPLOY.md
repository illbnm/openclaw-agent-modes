# OpenClaw Kubernetes Deployment Guide

> OpenClaw v2026.3.12 adds K8s support. Here's how to deploy.

## Prerequisites

- Kubernetes cluster (minikube, Kind, or cloud)
- kubectl configured
- Helm (optional)

## Quick Start with Kind

```bash
# Create a local cluster
kind create cluster --name openclaw

# Apply the manifests
kubectl apply -f https://raw.githubusercontent.com/openclaw/openclaw/main/deploy/k8s/
```

## Using Helm

```bash
# Add OpenClaw Helm repo (if available)
helm repo add openclaw https://charts.openclaw.ai

# Install
helm install openclaw openclaw/openclaw
```

## Manual Deployment

### 1. Namespace

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: openclaw
```

### 2. Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: openclaw
  namespace: openclaw
spec:
  replicas: 1
  selector:
    matchLabels:
      app: openclaw
  template:
    metadata:
      labels:
        app: openclaw
    spec:
      containers:
      - name: openclaw
        image: openclaw/openclaw:latest
        ports:
        - containerPort: 3000
        env:
        - name: OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: openclaw-secrets
              key: openai-api-key
```

### 3. Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: openclaw
  namespace: openclaw
spec:
  type: LoadBalancer
  ports:
  - port: 80
    targetPort: 3000
  selector:
    app: openclaw
```

## Configuration

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `OPENAI_API_KEY` | Yes | OpenAI API key |
| `ANTHROPIC_API_KEY` | No | Claude API key |
| `GATEWAY_PORT` | No | Default: 3000 |

### Secrets

```bash
kubectl create secret generic openclaw-secrets \
  --from-literal=openai-api-key=sk-xxx \
  --from-literal=anthropic-api-key=sk-xxx \
  -n openclaw
```

## Scaling

```bash
# Scale up
kubectl scale deployment openclaw --replicas=3 -n openclaw

# Horizontal Pod Autoscaler
kubectl autoscale deployment openclaw --min=2 --max=10 --cpu-percent=80 -n openclaw
```

## Monitoring

```bash
# Check status
kubectl get pods -n openclaw

# View logs
kubectl logs -f deployment/openclaw -n openclaw

# Port forward for local access
kubectl port-forward svc/openclaw 3000:80 -n openclaw
```

## Captain vs Abdicator on K8s

| Mode | Behavior |
|------|----------|
| **Captain** | Understands K8s concepts, verifies deployments |
| **Architect** | Designs the K8s architecture, sets up monitoring |
| **Abdicator** | Just runs the commands without understanding |

> The first two are using AI. The third is being used by AI.

---

## Troubleshooting

### Pod won't start

```bash
kubectl describe pod <pod-name> -n openclaw
kubectl logs <pod-name> -n openclaw
```

### API key issues

```bash
kubectl get secrets -n openclaw
kubectl describe secret openclaw-secrets -n openclaw
```

### Network issues

```bash
kubectl get svc -n openclaw
kubectl get endpoints -n openclaw
```

---

*Updated for OpenClaw v2026.3.12*

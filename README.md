
# K8s Manifest Validator & Health Checker

A dual-purpose utility designed to ensure Kubernetes manifests are syntactically valid and the resulting resources are healthy within the cluster.

## Features
- **Static Validation**: Uses JSON Schema to enforce Kubernetes API specifications.
- **Dynamic Health Checking**: Asynchronously queries the Kubernetes API to verify if a pod is in the `Running` phase.
- **Modular Design**: Separated validation logic and cluster monitoring for better maintainability.

## Installation
```bash
pip install -r requirements.txt

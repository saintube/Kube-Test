# Kube Test Action

This [GitHub action](https://github.com/features/actions) will handle the CI workflow and help run testing experiments on Kubernetes.

## Getting Started

```yaml
name: CI
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: KinD (Kubernetes in Docker) Action
      uses: engineerd/setup-kind@v0.1.0
    - name: Kube Test Action
      uses: saintube/Kube-Test@master
      with:
        who-to-greet: 'Mona the Octocat'
    - name: Testing - Create Deployment
      run: |
        export KUBECONFIG="$(kind get kubeconfig-path)"
        kubectl get pods --all-namespaces
```

## Configuration

(null)

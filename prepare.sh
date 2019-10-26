#!/bin/bash

cd "$( dirname "${BASH_SOURCE[0]}" )";

echo "check if KinD can be accessed outside..."
kubectl version --kubeconfig=$PWD/kubeconfig
echo "ansible is starting..."

#kubeconfig=(`kind get kubeconfig-path`)
kubeconfig="$PWD/kubeconfig"
echo "KUBECONFIG: $kubeconfig"
echo "kube_config: \"$kubeconfig\"" > env.yml

#ansible-playbook -v $GITHUB_WORKSPACE/.kubetest/ci.yml

#ls $GITHUB_WORKSPACE/

#cat log

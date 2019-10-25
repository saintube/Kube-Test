#!/bin/bash

cd "$( dirname "${BASH_SOURCE[0]}" )";
#kubeconfig=(`kind get kubeconfig-path`)
kubeconfig="$HOME/.kube/config"
echo "kube_config: \"$kubeconfig\"" > env.yml

ansible-playbook -v $GITHUB_WORKSPACE/.kubetest/ci.yml

#ls $GITHUB_WORKSPACE/

#cat log

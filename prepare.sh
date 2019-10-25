#!/bin/bash

cd "$( dirname "${BASH_SOURCE[0]}" )";
#kubeconfig=(`kind get kubeconfig-path`)
kubeconfig="$PWD/kubeconfig"
echo "kube_config: \"$kubeconfig\"" > env.yml

ansible-playbook -v $GITHUB_WORKSPACE/.kubetest/ci.yml

#ls $GITHUB_WORKSPACE/

#cat log

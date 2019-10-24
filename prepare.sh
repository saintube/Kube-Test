#!/bin/bash

cd "$( dirname "${BASH_SOURCE[0]}" )";
kubeconfig=(`kind get kubeconfig-path`)
echo "kube_config: \"$kubeconfig\"" > env.yml

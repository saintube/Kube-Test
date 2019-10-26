#!/bin/bash

cd "$( dirname "${BASH_SOURCE[0]}" )";

echo "Check if KinD can be accessed outside..."
kubectl version --kubeconfig=$PWD/kubeconfig

kubeconfig="$PWD/kubeconfig"
echo "KUBECONFIG: $kubeconfig"
echo "kube_config: \"$kubeconfig\"" > env.yml

ansible-playbook -v $GITHUB_WORKSPACE/.kubetest/ci.yml  2>&1 | tee demo.log
echo $GITHUB_SHA >> demo.log
cp $GITHUB_WORKSPACE/.kubetest/*.yaml ./
cat $GITHUB_WORKSPACE/.kubetest/*.yaml

#cp $GITHUB_WORKSPACE/Kube-Test/kubeTestMarkdownGen.py ./

python3 kubeTestMarkdownGen.py
ls

#cp dashboard.json $GITHUB_WORKSPACE/src/dashboardData/
#cat $GITHUB_WORKSPACE/src/dashboardData/dashboard.json
#cp -r posts/* $GITHUB_WORKSPACE/src/posts/

#ls $GITHUB_WORKSPACE/

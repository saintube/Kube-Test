#!/bin/bash

cd "$( dirname "${BASH_SOURCE[0]}" )";
kubeconfig=(`kind get kubeconfig-path`)
echo "kube_config: \"$kubeconfig\"" > env.yml

ansible-playbook -v $GITHUB_WORKSPACE/.kubetest/ci.yml >> demo.log
echo $GITHUB_SHA >> demo.log
cat demo.log
cp $GITHUB_WORKSPACE/.kubetest/*.yaml ./
cat $GITHUB_WORKSPACE/.kubetest/pod-delete-litmus-result.yaml

#cp $GITHUB_WORKSPACE/Kube-Test/kubeTestMarkdownGen.py ./

python3 kubeTestMarkdownGen.py
ls

cp dashboard.json $GITHUB_WORKSPACE/src/dashboardData/
cat $GITHUB_WORKSPACE/src/dashboardData/dashboard.json
cp -r posts/* $GITHUB_WORKSPACE/src/posts/


#ls $GITHUB_WORKSPACE/



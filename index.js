const core = require('@actions/core');
const github = require('@actions/github');
const exec = require('@actions/exec');

(async() => {
    try {
    console.log("Kube Test Action is running...");
    // provision a KinD cluster
    await exec.exec('git', ['clone', '-b', 'provision-cluster', 'https://github.com/saintube/Kube-Test.git']);

    console.log("Pulling KinD image from DockerHub...")
    await exec.exec('docker pull saintube/kind:v1.14.4')
    await exec.exec('bash ./Kube-Test/print_KinD.sh')
    await exec.exec('sleep 120s')

    await exec.exec('wget -O ./Kube-Test/kubeconfig http://172.17.0.2:10080/config')
    await exec.exec('sed -i "s/172.17.0.2/minikube/g" ./Kube-Test/kubeconfig')

    console.log("KinD cluster is running now.")

    await exec.exec('sudo touch /mnt/parameters.yml');
    await exec.exec('sudo echo "[local]" >> /etc/ansible/hosts');
    await exec.exec('sudo echo "127.0.0.1" >> /etc/ansible/hosts');
    await exec.exec('bash ./Kube-Test/prepare.sh');
    //await exec.exec('ansible-playbook', ['-v', './.kubetest/ci.yml'])
    
    console.log("Kube Test Action is terminating...")
  } catch (error) {
    core.setFailed(error.message);
  }
})();

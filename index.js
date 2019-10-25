const core = require('@actions/core');
const github = require('@actions/github');
const exec = require('@actions/exec');

(async() => {
    try {
    console.log("Kube Test Action is running...");
    // provision a KinD cluster
    console.log("Pulling KinD image from DockerHub...")
    await exec.exec('docker pull saintube/kind:v1.14.4')
    await exec.exec('cid=`docker run -itd --privileged saintube/kind:v1.14.4`')
    await exec.exec('sleep 15s')
    await exec.exec('mkdir -p ~/.kube/')
    
    await exec.exec('docker ps')
    await exec.exec('docker exec -it $cid cat /etc/hosts')

    await exec.exec('wget -O ~/.kube/config http://172.17.0.2:10080/config')
    await exec.exec('sed -i \'s/172.17.0.2/minikube/g\' ~/.kube/config')

    console.log("KinD cluster is running now.")
    await exec.exec('kubectl version')

    await exec.exec('git', ['clone', '-b', 'provision-cluster', 'https://github.com/saintube/Kube-Test.git']);
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

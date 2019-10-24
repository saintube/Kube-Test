const core = require('@actions/core');
const github = require('@actions/github');
const exec = require('@actions/exec');

(async() => {
    try {
    console.log("Kube Test Action is running...");
    await exec.exec('git', ['clone', 'https://github.com/saintube/Kube-Test.git']);
    await exec.exec('sudo touch /mnt/parameters.yml');
    await exec.exec('sudo echo "[local]" >> /etc/ansible/hosts');
    await exec.exec('sudo echo "127.0.0.1" >> /etc/ansible/hosts');
    await exec.exec('bash ./Kube-Test/prepare.sh');
    //await exec.exec('ansible-playbook', ['-v', './.kubetest/ci.yml'])
  } catch (error) {
    core.setFailed(error.message);
  }
})();

const core = require('@actions/core');
const github = require('@actions/github');
const exec = require('@actions/exec');

try {
  (async() => {
    console.log("Kube Test Action is running...");
    await exec.exec('git', ['clone', 'https://github.com/saintube/Kube-Test.git']);
    console.log("DEBUG:");
    await exec.exec('ls Kube-Test/lib');
    await exec.exec('sudo touch /mnt/parameters.yml');
    await exec.exec('sudo echo "[local]" >> /etc/ansible/hosts');
    await exec.exec('sudo echo "127.0.0.1" >> /etc/ansible/hosts');
    await exec.exec('sudo export KUBECONFIG="$(kind get kubeconfig-path)"');
    await exec.exec('ansible-playbook', ['-v', './.kubetest/ci.yml']);
  })();
} catch (error) {
  core.setFailed(error.message);
}

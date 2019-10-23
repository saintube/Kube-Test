const core = require('@actions/core');
const github = require('@actions/github');
const exec = require('@actions/exec');

try {
  (async() => {
    
    await exec.exec('git', ['clone', 'https://github.com/saintube/Kube-Test.git']);
    await exec.exec('ls Kube-Test');
    await exec.exec('ansible-playbook', ['-v', 'Kube-Test/lib/ci.yml']);

  })();
} catch (error) {
  core.setFailed(error.message);
}

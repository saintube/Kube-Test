# Chaos Experiment

## Experiment Metadata

| Type  | Description              | Storage |       Applications     | K8s Platform |
| ----- | ------------------------ | ------- | ---------------------- | ------------ |
| Chaos | Fail the application pod |   Any   | Deployment/Statefulset | >= 1.1.0     |

## Entry-Criteria

- Application services are accessible & pods are healthy
- Application writes are successful

## Exit-Criteria

- Application services are accessible & pods are healthy
- Data written prior to chaos is successfully retrieved/read
- Database consistency is maintained as per db integrity check utils
- Storage target pods are healthy

## Notes

- Typically used as a disruptive test, to cause loss of access to storage by failing the application pod.
- Tests Recovery workflow of the application pod.

## Associated Utils

- `chaoslib/pumba/pod_failure_by_sigkill.yaml`

## Playbook Environment Variables

### Application

| Parameter     | Description                                                   | Type      |
| ------------- | ------------------------------------------------------------- | --------- |
| APP_NAMESPACE | Namespace in which application pods are deployed              | Mandatory |
| APP_LABEL     | Unique Labels in `key=value` format of application deployment | Mandatory |
| DEPLOY_TYPE   | K8s resource type of application pods                         | Mandatory |

### Additional Health Checks

| Parameter              | Description                                                                | Type      |
| ---------------------- | -------------------------------------------------------------------------- | --------- |
| LIVENESS_APP_NAMESPACE | Namespace in which external liveness pods are deployed, if any             | Optional  |
| LIVENESS_APP_LABEL     | Unique Labels in `key=value` format for external liveness pod, if any      | Optional  |
| CHECK_SCRIPT           | Checkpoint script performs custom inspection for target app or pod, if any | Optional  |

### Lifecycle

| Parameter      | Description                                                 | Type      |
| -------------- | ----------------------------------------------------------- | --------- |
| SETUP_SCRIPT   | Setup script is used to provision the target app, if needed | Optional  |
| CLEANUP_SCRIPT | Cleanup script is used to cleanup the target app, if needed | Optional  |

## Config Example

```yaml
appinfo:
  appns: default
  applabel: "target=label"
  deploy_type: "deployment"
experiment:
  name: app-pod-failure
  setup_script: ""
  check_script: ""
  cleanup_script: ""
  spec:
    - name: LIVENESS_APP_LABEL
      value: ""
    - name: LIVENESS_APP_NAMESPACE
      value: ""
```

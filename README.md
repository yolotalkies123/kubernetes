# kubernetes



# Kubernetes Deployment Replicas Adjuster

This Python script allows you to adjust the replicas of a specific deployment in Kubernetes through command-line arguments.

## Usage

Run the script with the following command:

```bash
python k8s_patch_app.py -n <namespace> -d <deployment_name> -p "<json_patch>"
Replace <namespace> with the namespace of the deployment, <deployment_name> with the name of the deployment, and <json_patch> with the JSON patch string for adjusting the replicas.


python k8s_patch_app.py -n <namespace> -d <deployment-name> -p '{"spec":{"replicas":<new-replica-count>}}'
for eg in my case, python k8s_patch_app.py -n default -d test-deployment -p "{\"spec\":{\"replicas\":5}}"

This command will adjust the replicas of the deployment named test-deployment in the default namespace to 5.


Requirements:
1.Python3
2.Kubernetes python client library
3.Access to Kubernetes cluster

Installation:
pip install kubernetes







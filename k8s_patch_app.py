import argparse
import json
from kubernetes import client, config


def patch_deployment(namespace, deployment_name, patch):
    # Load Kubernetes configuration from default location
    config.load_kube_config()

    # Print the value of patch argument for debugging
    print("Patch argument:", patch)

    # Create API client objects
    api_instance = client.AppsV1Api()

    # Attempt to parse patch as JSON
    try:
        patch_content = json.loads(patch)
    except json.JSONDecodeError as e:
        print("Error parsing JSON patch:", e)
        return

    # Patch the deployment
    try:
        api_response = api_instance.patch_namespaced_deployment_scale(
            name=deployment_name,
            namespace=namespace,
            body=patch_content
        )
        print("Deployment scale patched successfully.")
    except Exception as e:
        print(f"Error patching deployment scale: {e}")



def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Adjust replicas of a specific deployment in Kubernetes")
    parser.add_argument("-n", "--namespace", type=str, required=True, help="Namespace of the deployment")
    parser.add_argument("-d", "--deployment", type=str, required=True, help="Name of the deployment")
    parser.add_argument("-p", "--patch", type=str, required=True, help="JSON patch for replicas")
    args = parser.parse_args()

    # Patch the deployment
    patch_deployment(args.namespace, args.deployment, args.patch)


if __name__ == "__main__":
    main()


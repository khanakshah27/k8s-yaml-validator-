from kubernetes_asyncio import client, config

async def check_pod_health(pod_name, namespace="default"):
    try:
        # Load kubeconfig for local dev or incluster for pod deployment
        try:
            await config.load_incluster_config()
        except:
            await config.load_kube_config()
            
        v1 = client.CoreV1Api()
        pod = await v1.read_namespaced_pod(name=pod_name, namespace=namespace)
        
        # Check pod phase and container status
        if pod.status.phase == "Running":
            return True, "Pod is Running"
        return False, f"Pod is in phase: {pod.status.phase}"
    except Exception as e:
        return False, f"Error checking pod: {e}"

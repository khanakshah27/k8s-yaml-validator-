import asyncio
import sys
from src.validator import validate_yaml
from src.checker import check_pod_health

async def main(file_path, pod_name):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # 1. Validate Format
    is_valid, msg = validate_yaml(content)
    if not is_valid:
        print(f"FAILED: {msg}")
        sys.exit(1)
        
    print(f"SUCCESS: {msg}")
    
    # 2. Check Live Health
    healthy, status = await check_pod_health(pod_name)
    if healthy:
        print(f"HEALTHY: {status}")
    else:
        print(f"UNHEALTHY: {status}")

if __name__ == '__main__':
    # Usage: python main.py <file.yaml> <pod-name>
    asyncio.run(main(sys.argv[1], sys.argv[2]))

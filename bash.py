start_deployment = """curl -X POST
    https://api.stackify.net/api/v1/deployments/start
    -H 'authorization: ApiKey  3Id0Ia4Bw3Cq8Fd3Nz3Id6Iu2Yd8Wc6Zx4Nj1Fl'
    -H 'content-type: application/json'
    -d '{
        "Name": "PythonSandboxApp",
        "Uri": "localhost",
        "Branch": "master",
        "Commit": "rOapzPyAtzUR9s7yDJYlGz2vUYbcl0P6gMVglrygJ2",
        "Version": "v1.0",
        "AppName": "PythonSandboxApp",
        "EnvironmentName": "SandboxTest"
}'"""

complete_deployment = """curl -X POST
    https://api.stackify.net/api/v1/deployments/complete
    -H 'authorization: ApiKey 3Id0Ia4Bw3Cq8Fd3Nz3Id6Iu2Yd8Wc6Zx4Nj1Fl'
    -H 'content-type: application/json'
    -d '{
        "Version": "v1.0",
        "AppName": "PythonSandboxApp",
        "EnvironmentName": "SandboxTest"
}'
"""

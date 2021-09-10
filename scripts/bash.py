start_deployment = """curl -X POST
    https://api.stackify.net/api/v1/deployments/start
    -H 'authorization: ApiKey  ENTER_YOUR_LICENSE_KEY'
    -H 'content-type: application/json'
    -d '{
        "Name": "BourneAgain",
        "Uri": "localhost",
        "Branch": "master",
        "Commit": "rOapzPyAtzUR9s7yDJYlGz2vUYbcl0P6gMVglrygJ2",
        "Version": "v1.0",
        "AppName": "FooApp",
        "EnvironmentName": "Prod"
}'"""

complete_deployment = """curl -X POST
    https://api.stackify.net/api/v1/deployments/complete
    -H 'authorization: ApiKey ENTER_YOUR_LICENSE_KEY'
    -H 'content-type: application/json'
    -d '{
        "Version": "v1.0",
        "AppName": "FooApp",
        "EnvironmentName": "Prod"
}'
"""

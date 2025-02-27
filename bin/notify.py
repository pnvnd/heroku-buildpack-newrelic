import os
import requests
import subprocess
import traceback

env_dir = os.environ['ENV_DIR']
new_relic_api_key = os.popen('cat {}/NEW_RELIC_API_KEY'.format(env_dir)).read()
new_relic_app_id = os.popen('cat {}/NEW_RELIC_APP_ID'.format(env_dir)).read()
deployer = os.popen('cat {}/DEPLOYER'.format(env_dir)).read()
release_version = os.popen('cat {}/HEROKU_RELEASE_VERSION'.format(env_dir)).read()
commit_id = os.environ['SOURCE_VERSION']

url = 'https://api.newrelic.com/v2/applications/{}/deployments.json'.format(new_relic_app_id)

deployment_info = {
    "deployment": {
        "revision": release_version,
        "changelog": "Deploying {}".format(commit_id),
        "description": "Deploying {}".format(commit_id),
        "user": deployer
    }
}

newrelic_headers = {'X-Api-Key': new_relic_api_key}

print("-----> Creating New Relic deployment marker.")

try:
    requests.post(url, json=deployment_info, headers=newrelic_headers)
except:
    exc = traceback.format_exc()
    msg = "-----> Failed to create New Relic Deployment Marker - Details:\n\t{}".format(exc)
    print(msg)

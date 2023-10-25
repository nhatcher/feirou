import configparser

import requests


"""
This script downloads the React build from GitHub and puts it in:

/var/www/{repository_name}/dist.zip

Assumes that the commit_id is in:

/var/lib/django/deployed_commit_id.txt

And expects that the correct value for the GitHub PAT is stored in the config file
"""


def get_artifacts(url, token):
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    r = requests.get(url, headers=headers)

    return r.json()


def download_artifact(archive_download_url, token, path):
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    r = requests.get(archive_download_url, headers=headers)
    open(path, "wb").write(r.content)


def download_artifact_for_commit(github, commit_id, path):
    token = github["token"]
    url = github["artifacts_url"]
    artifacts = get_artifacts(url, token)["artifacts"]
    for artifact in artifacts:
        if commit_id == artifact["workflow_run"]["head_sha"]:
            archive_download_url = artifact["archive_download_url"]
            download_artifact(archive_download_url, token, path)
            return
    raise Exception("Artifact not found. Perhaps expired or not yet created?")


if __name__ == "__main__":
    commit_id = open("/var/lib/django/deployed_commit_id.txt").read().strip()

    # Load the configuration file
    # interpolation=None means % is just a percentage sign
    config = configparser.ConfigParser(interpolation=None)
    config.read("/etc/server_config.ini")
    repository_name = config["github"]["name"]
    path = f"/var/www/{repository_name}/dist.zip"
    github = config["github"]
    download_artifact_for_commit(github, commit_id, path)

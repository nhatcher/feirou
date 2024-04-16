"""
This script generates test data for Django models using Factory Boy and exports the
data to JSON files. This tool is instrumental in setting up environments for development
or quality assurance testing, allowing for the creation of comprehensive and complex test scenarios.
For example, testing multiple user groups placing orders.

Steps performed by this script:
1. Flushes the current database to start with a clean slate. Warning: This will result in the loss of all current data in the database.
2. Generates and exports instances for supported apps like users, user profiles, pending users,
   and password recovery processes using a fixed seed to ensure repeatable data generation.
   This is particularly useful when extending or refining test fixtures.
3. Saves the generated instances to JSON files for use as fixtures or for testing purposes.

Run this script to generate fixture files in the PROJECT_PATH/fixtures directory. Adjust the parameters (date_now_ref, n_user, n_recover) as needed to fit your specific testing requirements.

Warning: Ensure to back up your data before running this script, as it will flush the existing database, resulting in data loss.
"""

import json
import os
import sys
import django
from django.core.management import call_command
from django.core.serializers import serialize
from datetime import datetime

# Setting up the environment paths and Django settings
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIXTURES_DIR = os.path.join(PROJECT_PATH, "fixtures")
sys.path.append(PROJECT_PATH)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.settings.development")
django.setup()

# Importing Factory definitions and models
from factory_users import generate_data_user  # noqa: E402

# Parameters Configuration

# date_now_ref: This parameter sets the reference date used for generating date-related data in the models.
# It is considered the "current" date for the purpose of data generation.
# Default is set to March 1, 2024
date_now_ref = datetime(2024, 3, 1)

# n_user: Specifies the number of user instances to generate.
# Default is 20 users.
n_user = 20

# n_recover: Specifies the number of recover password instances to generate.
# Default is 5 instances.
n_recover = 5

def get_user_input():
    apps = ["users", "groups"]  # Extend this list based on your app models
    selections = {app: False for app in apps}
    for app in apps:
        response = input(f"Generate data for {app}? (y/n): ").strip().lower()
        selections[app] = (response == 'y')
    return selections

def exporting_data(data_to_write, fixtures_dir):
    for app, files in data_to_write.items():
        for file_name, data in files.items():
            file_path = os.path.join(fixtures_dir, app, file_name)
            # Saving data in JSON format, nicely formatted
            with open(file_path, "w") as file:
                # Deserialize the data, serialize to JSON, then dump with formatting
                obj = json.loads(serialize("json", data))
                json.dump(obj, file, indent=4)  # Use indent for pretty-printing
                file.write("\n")  # Write a newline character at the end of the file

def generate_data(apps_to_generate):
    """Main function to generate all data and export to JSON files."""
    data_to_write = {}

    if apps_to_generate.get("users"):
        # Generating data for "users" app
        generated_data_users = generate_data_user(n_user, n_recover, date_now_ref)
        data_to_write.update(generated_data_users)

    if apps_to_generate.get("groups"):
        # TODO: Generating data for "groups" app
        # generated_data_groups = generate_data_groups(n_user, n_recover, date_now_ref)
        # data_to_write.update(generated_data_groups)
        pass

    # Exporting data
    exporting_data(data_to_write, FIXTURES_DIR)

if __name__ == "__main__":
    apps_to_generate = get_user_input()
    if any(apps_to_generate.values()):
        confirm = input("Are you sure you want to continue? This will delete existing data. (y/n): ").strip().lower()
        if confirm == 'y':
            call_command("flush", "--noinput")  # Clearing the database
            generate_data(apps_to_generate)
            print("Success: Data has been created and exported.")
        else:
            print("Operation canceled.")
    else:
        print("No data to be created.")

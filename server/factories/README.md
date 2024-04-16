
# Fixture Generation for Django Projects

This directory contains scripts designed to generate fixtures for testing Django applications. The primary script, `generate_fixtures.py`, leverages Factory Boy to create realistic data models that are exported to JSON files. These fixtures are crucial for setting up environments for development or quality assurance testing.

## Overview

The `generate_fixtures.py` script automates the creation of test data for Django models. It is instrumental for developers and testers who need to ensure their applications handle data correctly across various scenarios, such as user group interactions and order processes.

## Benefits of Using Fixtures in Tests

- **Consistency:** Fixtures ensure that your tests always run with the same data, leading to more predictable and stable test outcomes.
- **Efficiency:** Automating fixture creation saves time compared to manually setting up test data, allowing for more rapid testing cycles.
- **Complexity Handling:** Easily test complex interactions and data models without the need to manually recreate these scenarios each time.
- **Isolation:** Test data can be loaded in isolation, which helps in identifying issues and bugs without side effects from other data.

## How to Generate Fixtures

To generate fixtures, simply run the `generate_fixtures.py` script located in this directory:

```bash
python generate_fixtures.py
```

### Steps Performed by the Script

1. **Database Reset**: The script starts by flushing the current database to ensure a clean slate. *Warning: This will remove all existing data in the database.*
2. **Data Generation**: It then generates and exports instances for supported apps such as users, user profiles, pending users, and password recovery processes. A fixed seed is used to ensure repeatable data generation.
3. **Export**: The generated data is saved to JSON files in the `PROJECT_PATH/fixtures` directory.

### Customization

You can customize which apps to generate data for and adjust parameters like `date_now_ref`, `n_user`, and `n_recover` within the `generate_fixtures.py` script to fit your specific testing requirements.

### Important Notice

Before running this script, **ensure to back up your data** to avoid accidental loss due to database flushing.

## File Structure

- **generate_fixtures.py**: The main script for generating data.
- **factory_{app_name}.py**: Libraries of functions utilized by `generate_fixtures.py` to create data models.
import os
import subprocess


def add_submodule_to_dojo_module(module_folder, submodule_url, submodule_name):
    """
    Adds a submodule to every challenge in a dojo's module. Skips if submodule already exists in challenge

    :param module_folder: Path to the module folder containing the challenges
    :param submodule_url: URL of the submodule repository
    :param submodule_name: Name of the submodule
    """
    # Ensure module folder exists
    if not os.path.isdir(module_folder):
        print(f"Module folder '{module_folder}' does not exist")
        return
    
    # Iterate through each challenge in the module folder
    for challenge in os.listdir(module_folder):
        challenge_path = os.path.join(module_folder, challenge)

        # Check if it's a directory
        if os.path.isdir(challenge_path):
            submodule_path = os.path.join(challenge_path, submodule_name)

            # Skip if the submodule folder already exists in the challenge
            if os.path.exists(submodule_path):
                print(f"Submodule '{submodule_name}' already exists in '{challenge_path}', skipping")
                continue

            # Add the submodule
            try:
                print(f"Adding submodule to '{challenge_path}'...")
                subprocess.run(['git', 'submodule', 'add', submodule_url, submodule_path], check=True)
                print('Done')
            except subprocess.CalledProcessError as e:
                print(f"Failed to add submodule to '{challenge_path}': {e}")


if __name__ == '__main__':
    module_folder = 'machine-learning'
    submodule_url = 'https://github.com/dsu-arl/paceAITester'
    submodule_name = 'paceAITester'

    add_submodule_to_dojo_module(module_folder, submodule_url, submodule_name)

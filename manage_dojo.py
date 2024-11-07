from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
import os
import shutil
import yaml


# Stores the modules for this dojo from dojo.yml to reduce amount
# of reading/writing to file
modules = []


def read_dojo_yml():
    with open('dojo.yml', 'r') as file:
        dojo_data = yaml.safe_load(file)
    return dojo_data

def write_dojo_yml(dojo_data):
    with open('dojo.yml', 'w') as file:
        yaml.safe_dump(dojo_data, file, sort_keys=False, allow_unicode=True)

def read_module_yml(module_id):
    module_path = os.path.join(module_id, 'module.yml')
    with open(module_path, 'r') as file:
        module_data = yaml.safe_load(file)
    return module_data

def write_module_yml(module_id, data):
    module_path = os.path.join(module_id, 'module.yml')
    with open(module_path, 'w') as file:
        yaml.safe_dump(data, file, sort_keys=False)


######################### CREATE MODULE #########################
def create_module():
    module_name = inquirer.text(
        message='Enter module name (what will be displayed on pwn.college):'
    ).execute()
    module_path = module_name.lower().replace(' ', '-')
    try:
        print(f"Creating directory '{module_path}'...", end='', flush=True)
        os.makedirs(module_path)
        print(' Done')
    except FileExistsError:
        print(' Error')
        print(f"Directory '{module_path}' already exists")
    except Exception as e:
        print(' Error')
        print(f'An error occurred trying to create the folder: {e}')

    # Add to dojo.yml modules
    print('Adding module to dojo.yml file...', end='', flush=True)
    dojo_data = read_dojo_yml()
    dojo_data['modules'].append({'id': module_path})
    write_dojo_yml(dojo_data)
    print(' Done')

    # Create module.yml file
    print('Creating module.yml file...', end='', flush=True)
    filepath = os.path.join(module_path, 'module.yml')
    with open(filepath, 'w', encoding='utf-8') as file:
        yaml.safe_dump({'name': module_name}, file, sort_keys=False)
    print(' Done')

    # Create DESCRIPTION.md file
    print('Creating DESCRIPTION.md file...', end='', flush=True)
    filepath = os.path.join(module_path, 'DESCRIPTION.md')
    with open(filepath, 'w'):
        pass
    print(' Done')


######################### CREATE CHALLENGE #########################
def create_challenge():
    global modules

    # Display menu with module options
    module_choice = inquirer.rawlist(
        message='Which module are you adding this challenge to?',
        choices=modules,
        default=None
    ).execute()

    challenge_name = inquirer.text(
        message='Enter challenge name:'
    ).execute()
    default_challenge_id = challenge_name.lower().replace(' ', '-')
    challenge_id = inquirer.text(
        message='Enter challenge ID:',
        default=default_challenge_id
    ).execute()

    # Create challenge folder
    try:
        print(f"Creating directory '{challenge_id}'...", end='', flush=True)
        module_path = os.path.join(module_choice, challenge_id)
        os.makedirs(module_path)
        print(' Done')
    except FileExistsError:
        print(' Error')
        print(f"Directory '{challenge_id}' already exists")
    except Exception as e:
        print(' Error')
        print(f'An error occurred trying to create the folder: {e}')

    # Create DESCRIPTION.md file
    print('Creating DESCRIPTION.md file...', end='', flush=True)
    filepath = os.path.join(module_path, 'DESCRIPTION.md')
    with open(filepath, 'w'):
        pass
    print(' Done')

    # Add challenge to module.yml file section
    challenge = {
        'id': challenge_id,
        'name': challenge_name,
        'allow_privileged': False
    }
    module_data = read_module_yml(module_choice)
    if 'challenges' not in module_data:
        module_data['challenges'] = []
    module_data['challenges'].append(challenge)
    write_module_yml(module_choice, module_data)


######################### DELETE MODULE #########################
def delete_module():
    # Deletes folder and removes from dojo.yml
    global modules

    # Display menu with module options
    module_choice = inquirer.rawlist(
        message='Which module do you want to delete?',
        choices=modules,
        default=None
    ).execute()

    confirm = False
    confirm = inquirer.confirm(
        message=f"Are you sure you want to delete the module '{module_choice}'?",
        default=False
    ).execute()

    if confirm:
        # Delete folder
        if os.path.exists(module_choice):
            shutil.rmtree(module_choice)
            # Remove from modules list in dojo.yml
            dojo_data = read_dojo_yml()
            dojo_data['modules'] = [item for item in dojo_data['modules'] if item.get('id') != module_choice]
            write_dojo_yml(dojo_data)


######################### DELETE CHALLENGE #########################
def delete_challenge():
    # Delete from challenges in module.yml
    # Delete challenge folder in module folder
    global modules
    module_choice = inquirer.rawlist(
        message='Which module do you want to delete the challenge from?',
        choices=modules,
        default=None
    ).execute()

    # Get the list of challenges
    module_info = read_module_yml(module_choice)
    challenges = module_info['challenges']
    choices = []
    for challenge in challenges:
        choices.append(Choice(
            name=challenge['name'],
            value=(challenge['id'], challenge['name'])
        ))
    choice = inquirer.select(
        message='Choose a challenge to delete:',
        choices=choices,
        default=None
    ).execute()
    challenge_id, challenge_name = choice

    confirm = False
    confirm = inquirer.confirm(
        message=f"Are you sure you want to delete the challenge '{challenge_name}'",
        default=False
    ).execute()
    if confirm:
        module_info['challenges'] = [item for item in module_info['challenges'] if item.get('id') != challenge_id]
        challenge_path = os.path.join(module_choice, challenge_id)
        if os.path.exists(challenge_path):
            write_module_yml(module_choice, module_info)
            shutil.rmtree(challenge_path)
        else:
            print('Challenge directory does not exist')
    else:
        print('Not deleting the challenge')


######################### DISPLAY MENU #########################
def display_menu():
    global modules

    dojo_data = read_dojo_yml()
    for module in dojo_data['modules']:
        module_data = read_module_yml(module['id'])
        module_name = module_data['name']
        modules.append({'name': module_name, 'value': module['id']})

    choice = inquirer.rawlist(
        message='Choose an option:',
        choices=[
            Choice(name='Create Module', value=create_module),
            Choice(name='Create Challenge', value=create_challenge),
            Separator(),
            Choice(name='Delete Module', value=delete_module),
            Choice(name='Delete Challenge', value=delete_challenge),
            Separator(),
            Choice(name='Quit', value=None),
        ],
        default=1
    ).execute()

    if choice:
        choice()


if __name__ == '__main__':
    display_menu()
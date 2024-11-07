import os
import sys
import yaml


# Open dojo.yml and get all modules into list
with open('dojo.yml', 'r') as file:
    dojo_data = yaml.safe_load(file)

print('Which module are you adding this challenge to?')
count = 1
for module in dojo_data['modules']:
    module_path = os.path.join(module['id'], 'module.yml')
    with open(module_path, 'r') as file:
        module_data = yaml.safe_load(file)
    module_name = module_data['name']
    print(f'\t[{count}] {module_name}')
    count += 1

module_input = input('Enter module to add challenge to (number next to name): ')
try:
    index = int(module_input) - 1
except ValueError:
    print('Invalid input. Please choose one of the numbers next to the module name.')
    sys.exit()

module_folder = dojo_data['modules'][index]['id']

challenge_name = input('Enter challenge name: ')
default_challenge_id = challenge_name.lower().replace(' ', '-')
challenge_id = input(f'Enter challenge ID ({default_challenge_id}): ')
if ''.join(challenge_id.split()) == '':
    challenge_id = default_challenge_id

# Create challenge folder
try:
    print(f"Creating directory '{challenge_id}'...", end='', flush=True)
    module_path = os.path.join(module_folder, challenge_id)
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
module_yaml_path = os.path.join(module_folder, 'module.yml')
with open(module_yaml_path, 'r') as file:
    module_data = yaml.safe_load(file)

if 'challenges' not in module_data:
    module_data['challenges'] = []
module_data['challenges'].append({'id': challenge_id})

with open(module_yaml_path, 'w') as file:
    yaml.safe_dump(module_data, file, sort_keys=False)
import os
import yaml

module_name = input('Enter module name (what will be displayed on pwn.college): ')
module_path = module_name.lower().replace(' ', '-')

# Create folder
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
with open('dojo.yml', 'r') as file:
    dojo_data = yaml.safe_load(file)
dojo_data['modules'].append({'id': module_path})
with open('dojo.yml', 'w') as file:
    yaml.safe_dump(dojo_data, file, sort_keys=False, allow_unicode=True)
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
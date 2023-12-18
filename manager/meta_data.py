'''
Add functionality to Qumpel to maintain and updated metadata
in the data directory.
'''
import uuid
from pathlib import Path
from shutil import copytree
from ruamel.yaml import YAML
import yaml


path = Path('data/meta')


def _get_config():
    with open('manager_config.yml', 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    return config


def _save_config(config):
    with open('manager_config.yml', 'w', encoding='utf-8') as file:
        yaml.dump(config, file)


def new_metadata_package():
    identifier = str(uuid.uuid4())
    Path(path / identifier).mkdir(parents=True)
    _update_current_metadata_identifier(identifier)
    _update_instruction_files(identifier)


def _update_instruction_files(identifier):
    instruction_files = Path("instructions").glob('*.yaml')
    for file in instruction_files:
        _update_instruction_files_identifier(file, identifier)


def _update_instruction_files_identifier(instruction_file, identifier):
    yml = YAML()
    yml.preserve_quotes = True
    with open(instruction_file, 'r', encoding='utf-8') as file:
        instructions = yml.load(file)
    instructions['metadata_id'] = identifier
    with open(instruction_file, 'w', encoding='utf-8') as file:
        yml.dump(instructions, file)


def _update_current_metadata_identifier(identifier):
    config = _get_config()
    config['metadata_identifier'] = identifier
    _save_config(config)


def update_metadata():
    target = _get_config()['metadata_identifier']
    print(target)
    copytree(Path('meta'), path/target, dirs_exist_ok=True)

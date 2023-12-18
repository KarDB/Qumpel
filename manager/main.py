import argparse
from manager.new_folder_setup import new
from manager.move_files import move_data, move_sweep
from manager.meta_data import new_metadata_package, update_metadata

parser = argparse.ArgumentParser(
    description='Handle measurement folder and live lab logs')
parser.add_argument('action',
                    help='choose wether to init a new folder, or to move data',
                    choices=['new',
                             'move',
                             'movesweep',
                             'new_meta',
                             'update_meta']
                    )
args = parser.parse_args()


def main():
    """Match through argparse arguments to determine course of action"""
    match args.action:
        case 'new':
            new()
        case 'move':
            move_data()
        case 'movesweep':
            move_sweep()
        case 'new_meta':
            new_metadata_package()
        case 'update_meta':
            update_metadata()
        case _:
            print('invalid option')


if __name__ == '__main__':
    main()

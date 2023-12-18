
import yaml
import os

logo = '''
  _____       _           _                __  __                                   
 |  __ \     | |         | |              |  \/  |                                  
 | |__) |   _| |     __ _| |__    ______  | \  / | __ _ _ __   __ _  __ _  ___ _ __ 
 |  ___/ | | | |    / _` | '_ \  |______| | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
 | |   | |_| | |___| (_| | |_) |          | |  | | (_| | | | | (_| | (_| |  __/ |   
 |_|    \__, |______\__,_|_.__/           |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
         __/ |                                                       __/ |          
        |___/                                                       |___/           

'''


def new():
    print(logo)
    print('\nWelcome to your PyLab Manger.')
    print("\nTo set up the new measurement directory we'll need to ask"
          "\nyou some questions in order so set everything up for you.\n"
          "\nIf you change your mind about some settings you can always re-run"
          "\nthis script or edit the config.yml file.\n")
    manager_config = {}
    file_type = input(
        "What file type to you want to trigger a move? [default .npy]: ")
    if file_type == '':
        manager_config['file_type'] = '.npy'
        file_type = '.npy'
    else:
        manager_config['file_type'] = file_type
    print('You selected "{}" files to be tracked'.format(file_type))

    print('\nBy default pylab produces ".yaml" files containing metadata.')
    track_yaml = input(
        'Do you want to track these too (recommended - default y) [y/n]: ')
    if track_yaml in ['yes', 'y', 'Y', 'Yes', '']:
        manager_config['track_yaml'] = True
    elif track_yaml in ['n', 'no', 'N', 'No']:
        manager_config['track_yaml'] = False
    else:
        print('Option not recognised - setting to default - yes')
        manager_config['track_yaml'] = True

    print('\nAs part of you preliminary analysis you may produce plots.'
          '\nIf you want us to move the plot files to the saving directory'
          '\nPlease provide the format you plan to save your plot as.'
          '\nAll files with this format will be moved to the saving directory.\n'
          '\nPress enter if you dont want to save images')
    image_format = input('What format would you like to use?: ')
    if image_format != '':
        manager_config['image_format'] = image_format
        manager_config['save_images'] = True
        print('You selected the {} format\n'.format(image_format))
        prepend_timestamp = input(
            'Do you want us to prepend the name of the datafile to the image files (default y)? [y/n]: ')
        if prepend_timestamp in ['yes', 'y', 'Y', 'Yes', '']:
            manager_config['prepend_filename'] = True
        elif prepend_timestamp in ['n', 'no', 'N', 'No']:
            manager_config['prepend_filename'] = False
        else:
            print('Option not recognised - setting to default - yes')
            manager_config['prepend_filename'] = True
    else:
        manager_config['save_images'] = False
        print('You chose not to save images\n')

    print('\nDo you want to track your measurements in a live lab log?'
          '\nThis will include your analysis image (if any) and some context'
          '\nYou may provide when running PyLab-Manager\n')
    keep_lab_log = input('Create live lab log (default y)? [y/n]: ')
    if keep_lab_log in ['yes', 'y', 'Y', 'Yes', '']:
        manager_config['keep_lab_log'] = True
    elif keep_lab_log in ['n', 'no', 'N', 'No']:
        manager_config['keep_lab_log'] = False
    else:
        print('Option not recognised - setting to default - yes')
        manager_config['keep_lab_log'] = True

    with open('manager_config.yml', 'w', encoding='utf-8') as f:
        yaml.dump(manager_config, f)

    os.makedirs('data', exist_ok=True)

    print('\nThank you for configuring PyLab-Manager!'
          '\nYou are now ready to get going.')

    print('\nAs a final note - we assume that you analyse your measurements'
          '\nusing either Jupyter notebooks of python files.'
          '\nWe will try to infer which file you used to analyse by extracting'
          '\nthe measurement type from the tracked file name.'
          '\n\nThis file name will be matched against the .ipynb and .py files'
          '\nin the measurement folder and exported and copied / copied to the'
          '\ntarget directory.'
          '\n\nFor further help run manager --help\n')

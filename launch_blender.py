import argparse
import os

parser = argparse.ArgumentParser(description="Launching Blender from Emacs")
parser.add_argument('-b', '--blender',
                    help='Source to Blender',
                    required=True,
                    dest='blender_path',
                    action='append')
parser.add_argument('-be', '--blender-emacs',
                    help='Source to Blender Emacs',
                    required=True,
                    dest='blender_emacs_path',
                    action='append')
parser.add_argument('-sp', '--source-path',
                    help='Source path to the addon',
                    required=True,
                    dest='source_path',
                    action='append')
parser.add_argument('-an', '--addon-name',
                    help='Addon name',
                    dest='addon_name',
                    action='append')

args = parser.parse_args()

command = ''
blender_path = str(args.blender_path[0])
command += blender_path + ' --python '
blender_emacs_path = str(args.blender_emacs_path[0])
command += blender_emacs_path + ' -- --source-path '
source_path = str(args.source_path[0])
command += source_path
if args.addon_name:
    addon_name = str(args.addon_name[0])
    command += ' ' + addon_name

os.system(command)

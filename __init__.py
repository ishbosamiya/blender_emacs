import argparse

import load_addons


def launch(source_path, addon_name):
    addons_to_load = [(source_path, addon_name)]
    load_addons.setup_addon_links(addons_to_load)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Parsing addon information")
    parser.add_argument('-sp', '--source_path',
                        help='Source path to the addon',
                        required=True,
                        dest='source_path',
                        action='append')
    parser.add_argument('-an', '--addon_name',
                        help='Addon name',
                        required=True,
                        dest='addon_name',
                        action='append')

    args = parser.parse_args()

    source_path = args.source_path
    addon_name = args.addon_name

    launch(source_path, addon_name)

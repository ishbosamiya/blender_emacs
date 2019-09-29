import argparse
import sys
import os
from pathlib import Path

sys.path.append(os.path.abspath(os.path.curdir))
import load_addons


class ArgumentParserForBlender(argparse.ArgumentParser):
    """
    This class is identical to its superclass, except for the parse_args
    method (see docstring). It resolves the ambiguity generated when calling
    Blender from the CLI with a python script, and both Blender and the script
    have arguments. E.g., the following call will make Blender crash because
    it will try to process the script's -a and -b flags:
    >>> blender --python my_script.py -a 1 -b 2

    To bypass this issue this class uses the fact that Blender will ignore all
    arguments given after a double-dash ('--'). The approach is that all
    arguments before '--' go to Blender, arguments after go to the script.
    The following calls work fine:
    >>> blender --python my_script.py -- -a 1 -b 2
    >>> blender --python my_script.py --
    """

    def _get_argv_after_doubledash(self):
        """
        Given the sys.argv as a list of strings, this method returns the
        sublist right after the '--' element (if present, otherwise returns
        an empty list).
        """
        try:
            idx = sys.argv.index("--")
            return sys.argv[idx+1:]  # the list after '--'
        except ValueError as e:  # '--' not in the list:
            return []

    # overrides superclass
    def parse_args(self):
        """
        This method is expected to behave identically as in the superclass,
        except that the sys.argv list will be pre-processed using
        _get_argv_after_doubledash before. See the docstring of the class for
        usage examples and details.
        """
        return super().parse_args(args=self._get_argv_after_doubledash())


def launch(source_path, addon_name):
    addons_to_load = [(source_path, addon_name)]
    load_addons.setup_addon_links(addons_to_load)


if __name__ == '__main__':
    parser = ArgumentParserForBlender(description="Parsing addon information")
    parser.add_argument('-sp', '--source_path',
                        help='Source path to the addon',
                        required=True,
                        dest='source_path',
                        action='append')
    parser.add_argument('-an', '--addon_name',
                        help='Addon name',
                        dest='addon_name',
                        action='append')

    args = parser.parse_args()

    source_path = Path(os.path.abspath(str(args.source_path[0])))
    print(type(source_path))
    if args.addon_name:
        addon_name = str(args.addon_name[0])
    else:
        addon_name = str(os.path.basename(source_path))
    print(addon_name)

    launch(source_path, addon_name)

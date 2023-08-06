import f90nml
import json
import copy

def dict_merge(dct: dict, merge_dct: dict) -> dict:
    """ Recursive dict merge. Inspired by :meth:``dict.update()``, instead of
    updating only top-level keys, dict_merge recurses down into dicts nested
    to an arbitrary depth, updating keys. The ``merge_dct`` is merged into
    ``dct``.
    Args:
     dct: dict onto which the merge is executed
     merge_dct: dct merged into dct
    Returns:
        The merged dict
    """

    for key, value in merge_dct.items():
        if key in dct.keys() and type(value) is dict:
            dict_merge(dct[key], merge_dct[key])
        else:
            dct[key] = merge_dct[key]

    return(dct)

class JSONNamelist(object):
    """Class for a WRF-Hydro JSON namelist containing one more configurations"""
    def __init__(
            self,
            file_path: str):
        """Instantiate a Namelist object.
        Args:
            file_path: Path to the namelist file to open, can be a json or fortran90 namelist.
        """
        self._json_namelist = json.load(open(file_path,mode='r'))
        self.configs = self._json_namelist.keys()

    def get_config(self,config: str):
        """Get a namelist for a given configuration. This works internally by grabbing the base
        namelist and updating with the config-specific changes.
        Args:
            config: The configuration to retrieve
        """

        base_namelist = copy.deepcopy(self._json_namelist['base'])
        config_patches = copy.deepcopy(self._json_namelist[config])

        #Update the base namelist with the config patches
        config_namelist = dict_merge(base_namelist,config_patches)

        return Namelist(config_namelist)

class Namelist(dict):
    """Class for a WRF-Hydro namelist"""
    def write(self, path: str):
        """Write a namelist to file as a fortran-compatible namelist
        Args:
            path: The file path
        """

        f90nml.write(self,str(path))

    def patch(self,patch: dict):
        """Recursively patch a namelist with key values from another namelist
        Args:
            patch: A Namelist or dict object containing the patches
        """

        patched_namelist = dict_merge(copy.deepcopy(self),copy.deepcopy(patch))

        return patched_namelist
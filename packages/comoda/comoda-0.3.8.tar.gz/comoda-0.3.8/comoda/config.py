import os

from appdirs import user_config_dir
from pkg_resources import resource_filename
from shutil import copyfile

from . import ensure_dir, path_exists


class WeightedPath:
    def __init__(self, path, weight):
        self.path = path
        self.weight = weight

    def __repr__(self):
        return '{}: {} {}'.format(self.__class__.__name__,
                                  self.path,
                                  self.weight)

    def __cmp__(self, other):
        if hasattr(other, 'weight'):
            return self.weight.__cmp__(other.weight)


class ConfigurationManager(object):
    def __init__(self, appname, loglevel='INFO',
                 cf_from_cli=None,
                 cf_from_package=None,
                 cf_label='config.yaml'):
        def copy_config_file_from_package(appname, src, dst):
            cf_from_package = resource_filename(appname, src)
            copyfile(cf_from_package, dst)

        logger = a_logger(self.__class__.__name__, level=loglevel)

        config_dir = os.path.join(user_config_dir(__appname__))
        config_file_into_home = os.path.join(config_dir, cf_label)

        if not path_exists(config_file_into_home, logger, force=False):
            logger.info('Creating config path {}'.format(config_dir))
            ensure_dir(config_dir)
            config_file_path = '/'.join(['config', cf_label])
            copy_config_file_from_package(__appname__, config_file_path,
                                          config_file_into_home)

        config_file_paths = []
        if cf_from_cli and path_exists(cf_from_cli, logger, force=False):
            config_file_paths.append(WeightedPath(cf_from_cli, 0))
        if path_exists(config_file_into_home, logger, force=False):
            config_file_paths.append(WeightedPath(config_file_into_home, 1))

        logger.debug("config file paths: {}".format(config_file_paths))

        config_file_path = sorted(config_file_paths)[0].path
        logger.info('Reading configuration from {}'.format(config_file_path))

        c = load_config(config_file_path)
        self.pipes_conf = c['pipelines'] if 'pipelines' in c else None


class ConfigurationManager:
    def __init__(self, args=None, logger=None, cf_label='config.yaml'):
        def copy_config_file_from_package(appname, src, dst):
            config_file_from_package = resource_filename(appname, src)
            copyfile(config_file_from_package, dst)


def config_file_setup(appname, cf_from_cli=None, cf_label='config.yaml',
                      logger=None):
    """
    Return a configuration file path from cli args if present, otherwise return
    a file path from the user_config_dir
    Create a config file if does not exists, copying it from the package
    default into the user_config_dir.
    :param appname:
    :param logger: logger
    :param cf_label: label of the configuration file (required)
    :param cf_from_cli: path to configuration file from cli arg
    :return: File path
    """
    presta_config_dir = os.path.join(user_config_dir(appname))
    config_file_from_home = os.path.join(presta_config_dir, cf_label)

    if not path_exists(config_file_from_home, logger, force=False):
        logger.info('Creating config path {}'.format(presta_config_dir))
        ensure_dir(presta_config_dir)
        config_file_path = '/'.join(['config', cf_label])
        config_file_from_package = resource_filename(appname,
                                                     config_file_path)
        copyfile(config_file_from_package, config_file_from_home)

    config_file_paths = []
    if cf_from_cli and path_exists(cf_from_cli, logger, force=False):
        config_file_paths.append(WeightedPath(cf_from_cli, 0))
    if path_exists(config_file_from_home, logger, force=False):
        config_file_paths.append(WeightedPath(config_file_from_home, 1))

    logger.debug("config file paths: {}".format(config_file_paths))

    config_file_path = sorted(config_file_paths)[0].path
    logger.info('Reading configuration from {}'.format(config_file_path))
    return config_file_path


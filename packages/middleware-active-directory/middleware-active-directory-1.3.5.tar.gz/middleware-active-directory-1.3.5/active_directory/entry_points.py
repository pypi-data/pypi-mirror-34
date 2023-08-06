import errno
import logging
import os

from middleware import model, config
from setuptools.command.install import install


def copy_file():
    from shutil import copyfile
    import active_directory
    path = os.path.dirname(active_directory.__file__)
    file = os.path.join(path, "abstract.py")
    file_path = os.path.join(os.getcwd(), 'providers', 'active_directory.py')
    if not os.path.exists(os.path.dirname(file_path)):
        try:
            os.makedirs(os.path.dirname(file_path))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
        copyfile(file, file_path)



    def init():
        config.initialize()
        copy_file()
        logging.info("Created abstract class for ActiveDirectory provider")

        '''import argparse

        # Instantiate the parser
        parser = argparse.ArgumentParser(description='Optional app description')
        # Required positional argument
        parser.add_argument('user', type=str,
                            help='A required mysql user positional argument')

        # Optional positional argument
        parser.add_argument('password', type=str,
                            help='An optional password positional argument')

        # Optional argument
        parser.add_argument('--database', type=str,
                            help='An optional database argument')
        # Execute every command from the input file'''
        '''args = parser.parse_args()
        options.mysql_user = args.user
        options.mysql_password = args.password'''
        model.System.add_system(system_id=1, name="ActiveDirectory", description="", sync_enabled=1)
        logging.info("Applied new system")


from com.scoredata.datatransfer.LocalDataTransfer import LocalDataTransfer
from com.scoredata.datatransfer.Watcher import Watcher
import logging.config
from com.scoredata.datatransfer import Constants
import sys
import configparser
import json
import argparse
from logging.handlers import TimedRotatingFileHandler


class DataTransferDriver:

    def __init__(self, args):

        config = configparser.ConfigParser()
        config.read(args.conf)

        # initialize logger
        self.logger = logging.getLogger(Constants.Constant.logger_module_name.value)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        logger_handler = logging.StreamHandler(sys.stdout)
        logger_handler.setLevel(logging.INFO)
        logger_handler.setFormatter(formatter)
        self.logger.addHandler(logger_handler)
        app_log = ""
        try:
            app_log = config.get(Constants.Config.section_log_location.value,
                   Constants.Config.application_log.value)
        except Exception:
            pass
        if len(app_log) == 0:
            app_log = Constants.Constant.app_log_path.value

        time_log_handler = TimedRotatingFileHandler(app_log, when="D", interval=1, backupCount=10)
        time_log_handler.setFormatter(formatter)
        time_log_handler.setLevel(logging.INFO)
        self.logger.addHandler(time_log_handler)

        file_process_log = ""
        try:
            file_process_log = config.get(Constants.Config.section_log_location.value,
                                          Constants.Config.file_process_log.value)
        except Exception:
            pass
        if len(file_process_log) == 0:
            file_process_log = Constants.Constant.file_checkpoint_path.value

        Constants.SavedObj.config[Constants.Config.file_process_log.value] = file_process_log

        user_name = config.get(Constants.Config.section_client_credential.value,
                   Constants.Config.client_credential_user.value)
        password = config.get(Constants.Config.section_client_credential.value,
                                    Constants.Config.client_credential_password.value)
        if len(user_name) == 0 or len(password) == 0:
            self.logger.error("Missing username and password")
            sys.exit(Constants.Constant.exit_missing_credential.value)

        Constants.SavedObj.config[Constants.Config.client_credential_user.value]=user_name
        Constants.SavedObj.config[Constants.Config.client_credential_password.value]=password

        Constants.SavedObj.config[Constants.Config.dir_path_list.value] = json.loads(
            config.get(Constants.Config.section_data_location.value
                                               ,Constants.Config.dir_path_list.value))
        if type(Constants.SavedObj.config[Constants.Config.dir_path_list.value]).__name__ != 'list':
            self.logger.error("Provide list of dir name in list [] format in config.conf file")
            sys.exit(Constants.Constant.exit_data_path_location.value)
        if len(Constants.SavedObj.config[Constants.Config.dir_path_list.value]) == 0:
            self.logger.error("Provide dir name in configuration file")
            sys.exit(Constants.Constant.exit_data_path_location.value)

        compression_type = ""
        try:
            compression_type = config.get(Constants.Config.section_app_settings.value,
                                          Constants.Config.compression_type.value)
        except Exception:
            pass
        if len(compression_type) == 0:
            compression_type = Constants.Constant.default_compression_type.value
        Constants.SavedObj.config[Constants.Config.compression_type.value] = compression_type

        delete_file = False
        try:
            delete_file = config.getboolean(Constants.Config.section_app_settings.value,
                                            Constants.Config.delete_file.value)
        except Exception as ex:
            delete_file = False
            self.logger.warn(ex)
            pass
        Constants.SavedObj.config[Constants.Config.delete_file.value] = delete_file

    def load(self):
        try:
            # add existing data
            self.load_data()
            # add watcher
            w = Watcher()
            w.run()
        except Exception as ex:
            self.logger.error(ex)
            sys.exit("Stopped")

    @staticmethod
    def load_data():
        file_transfer = LocalDataTransfer()
        for dir_path in Constants.SavedObj.config[Constants.Config.dir_path_list.value]:
            file_transfer.upload(dir_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--conf', action='store',
                        dest='conf',
                        help='Config file location.')

    args = parser.parse_args()

    if args.conf is None:
        parser.error("missing config file")
        sys.exit()
    driver = DataTransferDriver(args)
    driver.load()




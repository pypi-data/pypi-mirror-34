import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from com.scoredata.datatransfer import Constants
import logging

class Watcher:


    def __init__(self):
        self.observer = Observer()
        self.logger = logging.getLogger(Constants.Constant.logger_module_name.value)

    def run(self):
        event_handler = Handler()
        for dir_path in Constants.SavedObj.config[Constants.Config.dir_path_list.value]:
            self.observer.schedule(event_handler, dir_path, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            self.logger.error("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        logger = logging.getLogger(Constants.Constant.logger_module_name.value)

        if event.is_directory:
            return None
        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            logger.info("received created event - %s." % event.src_path)
            from com.scoredata.datatransfer.LocalDataTransfer import LocalDataTransfer
            df = LocalDataTransfer()
            df.upload(event.src_path)


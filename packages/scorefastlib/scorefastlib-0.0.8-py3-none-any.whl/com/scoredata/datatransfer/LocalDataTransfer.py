import os
import threading
from boto3.s3.transfer import S3Transfer
from botocore import exceptions
import boto3
import logging.config
import sys
from com.scoredata.datatransfer import Constants
from com.scoredata.datatransfer.RestClient import RestClient
import gzip
import shutil
import socket
import time


class LocalDataTransfer:

    def __init__(self):
        self.logger = logging.getLogger(Constants.Constant.logger_module_name.value)

    def __get_files__(self, path):
        files = []
        if os.path.isdir(path):
            for entry in os.scandir(path):
                if entry.is_file():
                    files.append(entry.path)
        else:
            files.append(path)
        return files

    def upload(self, path):
        try:
            user_name = Constants.SavedObj.config[Constants.Config.client_credential_user.value]
            password = Constants.SavedObj.config[Constants.Config.client_credential_password.value]
            s3_conf = self.__authenticate_request__(user_name, password)
            access_key = s3_conf.get('access_key')
            secret_key = s3_conf.get('secret_key')
            bucket_name = s3_conf.get('bucket')

            transfer = S3Transfer(boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key))
            files = self.__get_files__(path)
            for file in files:
                self.logger.info("start processing for " + file)
                # ignore "." files
                if self.__ignore_file(file):
                    self.logger.info("ignoring " + file)
                    continue
                #check file processing status
                if self.__is_file_processed__(file):
                    self.logger.info("skipping "+file+" cause it has been processed already")
                    continue

                client_id = "2"
                date_format = s3_conf.get('namespace')[2:]

                # compress file
                compress_file = self.__compress_file__(file)
                # check configure limit
                if self.__is_s3_size_limit_exceeded__(compress_file,client_id,access_key,secret_key,bucket_name):
                    continue

                dir_name = os.path.basename(os.path.dirname(file))
                file_name = os.path.basename(compress_file)
                hostname_unixtime = socket.gethostname() + "_" + str(int(time.time()))
                file_name = hostname_unixtime + "_" + file_name
                dest_path = client_id + "/" + dir_name + "/" + date_format + "/" + file_name

                # upload file
                transfer.upload_file(compress_file, bucket_name, dest_path, callback=ProgressPercentage(compress_file))
                # save file status
                self.__save_file_status__(file)
                self.logger.info(compress_file + " has been uploaded to S3")

                # clean files
                if Constants.SavedObj.config.get(Constants.Config.delete_file.value):
                    os.remove(file)
                    self.logger.info("delete file "+file)
                    os.remove(compress_file)
                    self.logger.info("delete compressed file " + compress_file)

        except FileNotFoundError as file_nf_err:
            self.logger.error(file_nf_err)
            sys.exit("File not found")
        except exceptions.ClientError as aws_err:
            self.logger.error("AWS authentication exception. Check your access and secret key")
            sys.exit("AWS authentication exception")
        except Exception as ex:
            self.logger.error(ex)
            raise

    def __authenticate_request__(self, user_name, password):

        token_res = RestClient.get(url=Constants.Constant.score_token_url.value,
                                    auth={'user': user_name,
                                          'password': password}).json()
        if token_res.get('status') != 'success':
            self.logger.error(token_res.get('detail'))
            raise Exception("Unauthorized Request")

        token = token_res.get('token')
        s3_conf = RestClient.post(url=Constants.Constant.score_s3_config_url.value, headers={'Authorization': 'Token ' + token},
                                   data={"token": token}).json()
        if token_res.get('status') != 'success':
            self.logger.error("Unauthorized Request, Connect to admin")
            raise Exception("Unauthorized Request")
        return s3_conf.get('data')

    def __is_file_processed__(self, path):
        is_processed = False
        try:
            file = open(Constants.SavedObj.config[Constants.Config.file_process_log.value],'r')
            lines = list(file)
            is_processed = lines.__contains__(path+"\n")
            file.close()
        except FileNotFoundError:
            self.logger.info("initialize process log")
            f = open(Constants.SavedObj.config[Constants.Config.file_process_log.value], "w+")
            f.close()

        return is_processed

    def __ignore_file(self,path):
        is_processed = False
        file_name = os.path.basename(path)
        if file_name.startswith("."):
            is_processed = True
        return is_processed

    def __compress_file__(self,path):
        if Constants.SavedObj.config[Constants.Config.compression_type.value] == "gz":
            compressed_path = os.path.join("/tmp",os.path.basename(path)+".gz")
            with open(path, 'rb') as f_in:
                with gzip.open(compressed_path, 'wb', compresslevel=6) as f_out:
                    shutil.copyfileobj(f_in, f_out)
            return compressed_path
        else:
            return path

    def __is_s3_size_limit_exceeded__(self,path,client_id,access_key,secret_key,bucket_name):
        current_s3_size = self._s3_folder_size(client_id,access_key,secret_key,bucket_name)
        input_size = self.__input_path_size(path)
        if Constants.Constant.default_s3_limit_mb.value < current_s3_size + input_size:
            self.logger.error("Exceeding size limit. Max limit is %sMB. Current input size %sMB and used space is %sMB",
                              Constants.Constant.default_s3_limit_mb.value, input_size, current_s3_size)
            return True
        else:
            return False

    def _s3_folder_size(self,client_id,access_key,secret_key,bucket_name):
        session = boto3.Session(aws_access_key_id=access_key,
                                aws_secret_access_key=secret_key)
        s3 = session.resource('s3')
        total_size = 0
        for obj in s3.Bucket(bucket_name).objects.filter(Prefix=client_id):
            total_size += obj.size
        return int(total_size / 1024 / 1024)

    def __input_path_size(self, path):
        total_input_size = 0
        if os.path.isdir(path):
            total_input_size = sum(entry.stat().st_size for entry in os.scandir(path))
        else:
            total_input_size = os.stat(path).st_size
        return int(total_input_size / 1024 / 1024)

    def __save_file_status__(self,path):
        file = open(Constants.SavedObj.config[Constants.Config.file_process_log.value], 'a+')
        file.write(path+"\n")
        self.logger.info("write the file processing status "+path)
        file.close()


class ProgressPercentage(object):

    logger = logging.getLogger(Constants.Constant.logger_module_name.value)

    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify we'll assume this is hooked up
        # to a single filename.
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            self.logger.info(
                "%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))

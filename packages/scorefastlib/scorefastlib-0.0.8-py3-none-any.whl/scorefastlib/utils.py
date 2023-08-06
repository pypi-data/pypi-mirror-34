# -*- coding: utf-8 -*-
import os
import time
import requests
import boto3
import pickle
from gzip import GzipFile
from io import BytesIO
from scorefastlib.common.rest_client import RestClient
from scorefastlib.common.constants import Constant


def list_dataset():
    """ list dataset """
    AUTH_TOKEN = os.environ.get('AUTH_TOKEN', '')
    assert AUTH_TOKEN
    dataset_ret = RestClient.get(
        url=Constant.dataset_url.value,
        headers={'Authorization': 'Token ' + AUTH_TOKEN}).json()
    if dataset_ret.get('status') != 'success':
        raise Exception("Failed to retrieve the list of dataset")
    return dataset_ret.get('data')

def read_dataset(dataset_id):
    """ read the dataset """
    AUTH_TOKEN = os.environ.get('AUTH_TOKEN', '')
    assert AUTH_TOKEN
    dataset_url = os.path.join(Constant.dataset_url.value, dataset_id)
    dataset_ret = RestClient.get(
        url=dataset_url,
        headers={'Authorization': 'Token ' + AUTH_TOKEN}).json()
    if dataset_ret.get('status') != 'success':
        raise Exception("Failed to retrieve the list of dataset")
    data = dataset_ret.get('data')
    file_path = data.get('path')
    
    # due to deprecated api
    if not file_path.startswith('api'):
        file_path = os.path.join('api', file_path)
    file_download_path = os.path.join(Constant.root_url.value, file_path)

    file_path, ext = os.path.splitext(file_download_path)
    
    headers = {'Authorization': 'Token ' + AUTH_TOKEN}
    r = requests.get(file_download_path, allow_redirects=True, headers=headers)

    if ext == '.gz':
        bytestream = BytesIO(r.content)
        return GzipFile(None, 'rb', fileobj=bytestream).read().decode('utf-8')
    else:
        return r.content.decode('utf-8')

def deploy_model(model, name):
    """ deploy the model """
    AUTH_TOKEN = os.environ.get('AUTH_TOKEN', '')
    assert AUTH_TOKEN

    user_summary_ret = RestClient.get(
        url=Constant.user_summary_url.value,
        headers={'Authorization': 'Token ' + AUTH_TOKEN}).json()
    if user_summary_ret.get('status') != 'success':
        raise Exception("Failed to retrieve the user summary")
    data = user_summary_ret.get('data')
    user_id = data.get('user_id')
    group_id = data.get('group_id', 1)
    
    # create pickle
    directory = os.path.join('/tmp', str(group_id))
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_name = '{}.pkl'.format(name)
    file_path = '{}/{}'.format(directory, file_name)
    if os.path.exists(file_path):
        os.remove(file_path)
    pickle.dump(model, open(file_path, 'wb'))

    # upload the model to S3
    uuid = int(time.time() * 1000000)
    file_size = os.path.getsize(file_path)
    s3_namespace = "{}/customer/{}/{}/{}".format(
        Constant.s3_environment.value,
        group_id,
        uuid,
        file_name)
    s3_client = boto3.client('s3')
    s3_client.upload_file(
        file_path, Constant.s3_bucket.value, s3_namespace)
    
    # ping API end point to set
    params = {
        "name": name,
        "type": 3,
        "file_array": [{
            "name": file_name,
            "file_size": file_size,
            "path": s3_namespace}]
    }
    model_import_ret = RestClient.post(
        url=Constant.model_import_url.value,
        headers={'Authorization': 'Token ' + AUTH_TOKEN},
        data=params).json()
    if model_import_ret.get('status') != 'success':
        raise Exception("Failed to deploy the model")

if __name__ == '__main__':
    read_dataset("1377")
    set_model("", name="finalized_model")

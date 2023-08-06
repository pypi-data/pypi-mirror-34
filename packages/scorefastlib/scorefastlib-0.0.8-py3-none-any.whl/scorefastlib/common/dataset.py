# -*- coding: utf-8 -*-
from scorefastlib.common.constants import Constant

class Dataset(object):
    """ Dataset """
    def __init__(self, user_id, group_id):
        self.user_id = user_id
        self.group_id = group_id

    def get(self, id=None):
        """ get dataset into local user directory """
        Constant.dataset_url.value
        pass

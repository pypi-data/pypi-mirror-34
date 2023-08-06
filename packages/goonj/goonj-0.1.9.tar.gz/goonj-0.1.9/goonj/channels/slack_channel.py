import logging
import threading

import requests

from goonj.channels.base_channel import BaseChannel
from goonj.conf.constants import Sev
from goonj.exception import SlackChannelNameNotDefined
from goonj.utils import empty_string_check

logger = logging.getLogger(__name__)


class SlackChannel(BaseChannel):

    def __init__(self, **kwargs):

        if 'name' not in kwargs:
            raise SlackChannelNameNotDefined(
                'Slack channel name not defined ,\'name\' attribute is '
                'required')

        if 'webhook' not in kwargs:
            raise SlackChannelNameNotDefined(
                'Slack channel webhook not defined ,\'webhook\' attribute is '
                'required')

        self.name = kwargs['name']
        self.webhook = kwargs['webhook']

    def send_message(self, sev, message, subject=None, error_id=None,
                     error=None,
                     tag_list=None):

        if not isinstance(sev, Sev):
            raise TypeError('Sev must be an instance of type   Sev')

        try:
            headers = {'content-type': 'application/json'}
            final_text = ''.join(["Sev: ", empty_string_check(sev.value),
                                  "\nsubject: ", empty_string_check(subject),
                                  "\ndescription: ", empty_string_check(
                message),
                "\n error_id: ", empty_string_check(
                error_id),
                "\nerror: ", empty_string_check(error),
                "\ntags: ", empty_string_check(tag_list)])

            requests.post(self.webhook, json={"text": final_text},
                          headers=headers, timeout=500)

        except Exception as e:
            logger.error("Error while alerting in slack(Ignoring) %s", e)

    # should it be asynchronous or synchrnoonus
    def send(self, sev, message, subject=None, error_id=None,
             error=None,
             tag_list=None):
        if not isinstance(sev, Sev):
            raise TypeError('Sev must be an instance of type Sev')

        thread = threading.Thread(target=self.send_message, args=(sev, message,
                                                                  subject,
                                                                  error_id,
                                                                  error,
                                                                  tag_list),
                                  kwargs={})
        thread.start()
        # thread.join()  #no need to wait for notfication thread

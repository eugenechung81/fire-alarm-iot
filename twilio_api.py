__author__ = 'eugene'

import conf

from twilio.rest import TwilioRestClient

ACCOUNT_SID = conf.TWILIO_ACCOUNT_SID
AUTH_TOKEN = conf.TWILIO_AUTH_TOKEN

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)


def send_message(sender_phone,msg):
    '''
    # send_message("9492664065", "test1")

    :param sender_phone:
    :param msg:
    :return:
    '''
    message = client.messages.create(
        body=msg,  # Message body, if any
        to=sender_phone,
        from_=conf.TWILIO_FROM_NUMBER,
    )
    print message.sid

# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

import credentials
import os
import sys
from argparse import ArgumentParser
import twitter_data_handle as twitter

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

import json

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = credentials.LINE_CHANNEL_SECRET
channel_access_token = credentials.LINE_CHANNEL_ACCESS_TOKEN
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    profile = line_bot_api.get_profile(event.source.user_id)
    id = profile.user_id
    print("id is {0}".format(id))

    message = event.message.text

    sending_message = determine_message_to_send(message)

    line_bot_api.reply_message(
        event.reply_token,
        sending_message
    )


authentication_in_process = False
def determine_message_to_send(user_message):
    sending_message = [TextSendMessage(text="ツイートしたよ")]
    global authentication_in_process

    if user_message == "認証":
        sending_message = [TextSendMessage(text="ここにアクセスして認証してください"), TextSendMessage(text=twitter.authentication()),TextSendMessage(text="承認番号を送ってください")]
        authentication_in_process = True;
        return sending_message
    elif authentication_in_process: # add regex to make sure the format matches
        authentication_in_process = False
        twitter.authentication_final(user_message)
        return TextSendMessage(text="認証されたよ！")
    else:
        twitter.tweet(user_message)

    return sending_message


def sendM(id):
    try:
        line_bot_api.push_message(id, TextSendMessage(text='Hello World!'))
    except:
        print("id is {0}".format(id))


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    app.run(host="0.0.0.0", port=port)

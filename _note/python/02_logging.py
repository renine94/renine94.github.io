# 아래와 같이 설정하면, 로깅할 때, 특정 슬랙 채널에 로그 목록이 쌓인다.

import logging


CHANNEL_ID = "C05E5PEV9DM"
SLACK_TOKEN = ""


class SlackHandler(logging.handlers.HTTPHandler):
    def __init__(self, token, channel=CHANNEL_ID, emoji=True):
        super().__init__(host="slack.com", url="/api/chat.postMessage", method="POST", secure=True)
        self.token = token
        self.channel = channel
        self.emoji = emoji

    def mapLogRecord(self, record):
        if self.formatter is None:  # Formatter가 설정되지 않은 경우
            text = record.msg
        else:
            text = self.formatter.format(record)

        emoji_dict = {
            "DEBUG": ":bug:",
            "INFO": ":pencil2:",
            "WARNING": ":warning:",
            "ERROR": ":no_entry:",  # include "exception"
            "CRITICAL": ":rotating_light:",
        }
        emoji = emoji_dict.get(record.levelname, "")

        return {
            "token": self.token,
            "channel": self.channel,
            "text": f"{emoji} {text}",
            "as_user": True,
        }

def _init_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s",
        handlers=[
            logging.StreamHandler(),
            SlackHandler(SLACK_TOKEN),
        ],
    )



logging.info("인포 로그 테스트.")

try:
    1 / 0
except:
    logging.exception("exception test")
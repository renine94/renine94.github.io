#!/bin/bash

## TODO: guild-announcement-release로 변경해야함 (참고 https://jojoldu.tistory.com/552)
SLACK_HOOKS_URL='https://hooks.slack.com/services/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'
GITHUB_PERSONAL_ACCESS_TOKEN=''

# if [ "${STATUS}" != "success" ]
# then
#   exit 1
# fi

## 최신 릴리즈 노트(배포내역)를 가져옴
OUTPUT=$(curl \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $GITHUB_PERSONAL_ACCESS_TOKEN" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/fitpetkorea/fitpetmall-backend/releases/latest |
  grep body |                                 # response에서 body value만 가져옴
  sed "s/\"body\": \"//" |                    # 불필요한 텍스트를 삭제
  awk -F'## What' '{ print $1 }' |            # What's Changed 이전에 내용만 가져옴
  sed "s/\"/'/g"  |                           # double quote를 single quote로 replace (https://stackoverflow.com/questions/51330529/getting-invalid-payload-when-trying-to-curl-slack/51333632#51333632)
  sed "s/ -/  ·/g"                            # list 문자열 보강 (https://api.slack.com/reference/surfaces/formatting#retrieving-messages)
)

## ECS에서 Container 교체 시간이 약 1s 정도 소요되어서 delay 추가
sleep 2

## Slack 채널(guild-announcement-release)에 배포알림
curl -X POST \
  -H 'Content-type: application/json' \
  --data '{
    "blocks": [
      {
        "type": "header",
        "text": {
          "type": "plain_text",
          "text": "✨ 핏펫몰 백엔드 상용서버 배포알림"
        }
      },
      {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "'"<!channel>\n${OUTPUT}"'"
          }
      },
    ]
  }' \
  $SLACK_HOOKS_URL
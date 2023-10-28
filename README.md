# rcac

当月の AWS コストを Slack に通知するアプリケーション ( 準備中 )

## Example AWS Deploy

- Deploy
```
sam build
sam deploy -g --parameter-overrides \
    ParameterKey=CHANNELNAME,ParameterValue="#<Channel Name>" \
    ParameterKey=HOOKURL,ParameterValue="https://hooks.slack.com/services/<Webhook URL for Slack>"
```

- Delete
```
sam delete
```
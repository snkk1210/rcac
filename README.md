# rcac

当月の AWS コストを Slack に通知するアプリケーションです。  

AWS 上に EventBridge + Lambda のコンポーネントを使ってデプロイできる他、 CLI での使用も可能です。

## Example AWS Deploy

- Deploy
```
sam build
sam deploy -g --parameter-overrides \
    ParameterKey=CHANNELNAME,ParameterValue="#<Channel Name>" \
    ParameterKey=HOOKURL,ParameterValue="https://hooks.slack.com/services/<Webhook URL for Slack>"
```

or

( Specify execution time )
```
sam build
sam deploy -g --parameter-overrides \
    ParameterKey=CHANNELNAME,ParameterValue="#<Channel Name>" \
    ParameterKey=HOOKURL,ParameterValue="https://hooks.slack.com/services/<Webhook URL for Slack>" \
    ParameterKey=CRON,ParameterValue="cron(<minute>\ <hour>\ *\ *\ ?\ *)"
```

- Delete
```
sam delete
```

## Command Line Usage

### 1. Notify to Slack
- Set environmental variables
```
export channelName="#<Channel Name>"
export hookURL="https://hooks.slack.com/services/<Webhook URL for Slack>"
```

- Execute
```
cd bin
python main.py -t 1
```

### 2. Notify to stdout

- Execute
```
cd bin
python main.py -t 2
```
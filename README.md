# rcac

## Example AWS Deploy

- Deploy
```
sam build
sam deploy -g --parameter-overrides \
    ParameterKey=CHANNELNAME,ParameterValue="" \
    ParameterKey=HOOKURL,ParameterValue=""
```

- Delete
```
sam delete
```
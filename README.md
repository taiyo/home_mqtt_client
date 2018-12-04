# home_mqtt_client

自宅で動作させるMQTTクライアントのプログラム。  
MQTTサーバとしては、[Beebotte](https://beebotte.com/)を利用する。

## 環境変数
Beebotteのトークンや家電を操作するURLを環境変数として```app.env```として設定する。

```
TOKEN=
TOPIC=
AIR=_URL=
TV_URL=
```

## 起動
```bash
docker-compose up -d
```

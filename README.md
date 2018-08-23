# Cerebro.Scholar.API.RelatedTag

## required

- python3
- requests
- serverless

## test

```bash
$ serverless invoke local --function main
```

## deploy
```bash
$ serverless config credentials --provider aws --key 액세스키ID --secret 비밀액세스키
$ pip3 install -r requirements.txt -t ./
$ sls deploy
```

## **CAUTION!!!**
do not push install packages in requirements.txt

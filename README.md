# cooking-GPT

## Samples
![fig1](./images/cooking-GPT.gif )

### result
![fig1](./images/result.png )
## Setup
初めにこのレポジトリをクローンしてください
```sh
git clone https://github.com/yabashikazuya/cooking-GPT.git
```

dockerのbuildを行います
```sh
cd cooking-GPT/docker
./build.sh
```

## 実行方法
1. dockerに入ります
```sh
cd ~/VisionTransformer/docker
./run.sh
```
2. 以下を実行することで学習を行うことができます
```sh
python3 main.py
```
あとはwebブラウザで`http://localhost:5000`にとぶだけです。
アップロードした画像はuploadsの中に入ります。

## テスト環境
・ubuntu22.04

## Collaborators
・[@higash1](https://github.com/higash1)

・[@mutokuda](https://github.com/mutokuda)
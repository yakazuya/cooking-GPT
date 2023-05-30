# cooking-GPT
## Slide
[google slide](https://docs.google.com/presentation/d/1QRioxU_DZO62ucU4HYKtcXWjA3XuZ01cO_aFyc2hgcA/edit?usp=sharing)


## Samples
![fig1](./images/cooking-GPT.gif )

### result
![fig1](./images/result.png )
## Setup
初めにこのレポジトリをクローンしてください
```sh
git clone https://github.com/yabashikazuya/cooking-GPT.git
```

shared_dir/modulesにあるapy_key.pyに自分のopenAIのapikeyを入力します

dockerのbuildを行います
```sh
cd cooking-GPT/docker
./build.sh
```

## 実行方法
1. dockerに入ります
```sh
cd ~/cooking-GPT/docker
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

## Contributor
・[@higash1](https://github.com/higash1)

・[@mutokuda](https://github.com/mutokuda)

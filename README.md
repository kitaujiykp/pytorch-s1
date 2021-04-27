## mecab install

1. Mecabのインストール

`sudo apt install mecab libmecab-dev mecab-ipadic-utf8`

2. mecab-python3のインストール
`pip3 install mecab-python3`


> error message: [ifs] no such file or directory: /usr/local/etc/mecabrc

```
# mecabのインストール先を確認する
$ sudo find / -iname mecabrc
⇛ /etc/mecabrc

# 確認したインストール先をbash_profileに書き込む
$  sudo vim  ~/.bash_profile
⇛ export MECABRC='/etc/mecabrc' を追記する

# 書き込んだ設定を反映する
$ source ~/.bash_profile
```

## sklearn install

`pip3 install -U scikit-learn`

## torchtext

`pip3 install torchtext`

> メモリ4G以上が望ましい

## pytorch

https://pytorch.org/get-started/locally/

> torchtextは下記ライブラリ依存するので、`pip3 install torchtext`を実行することでtorchもインストールされる  
> Installing collected packages: dataclasses, numpy, typing-extensions, torch, urllib3, idna, chardet, certifi, requests, tqdm, torchtext


### 参照url
https://qiita.com/kenta1984/items/5ba254afa8a524381c43
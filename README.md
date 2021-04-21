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

## torchtext

`pip3 install torchtext`


## pytorch

https://pytorch.org/get-started/locally/


### 参照url
https://qiita.com/kenta1984/items/5ba254afa8a524381c43
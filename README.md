# 【PySpark入門】第４弾 実戦！RDDを操作してプログラムを作ってみる

## ブログURL

https://blog.serverworks.co.jp/introducing-pyspark-4

## 概要

ブログで使用するコードおよびデータファイルをダウンロードできます。

## メインソースコード

### ソースコード

`./src/questionnaire_analysis.py`

### データ

コードが正しく動作するには、以下の三つのファイルが全部必要です。
`./data/questionnaire_data_1.txt`
`./data/questionnaire_data_2.txt`
`./data/questionnaire_data_3.txt`

## サンプルデータ作成スクリプト

ご自身でサンプルデータを作成し、いろいろなケースでデータ分析を行ってみたい方は、今回サンプルのCSVファイルを作成する際に使用したコードをアップロードしていますので、ご活用ください。

### ソースコード

`./etc/make_sample_data.py`

### 実行手順

#### python version

3.7

#### 前提

pipenvがインストールされていること(https://pipenv-ja.readthedocs.io/ja/translate-ja/install.html#installing-pipenv)

#### コマンド

```
$ pipenv shell
$ pipenv sync
$ python etc/make_sample_data.py
```

#### 実行結果

`src`ディレクトリ配下に`sample_file_n.txt`ファイルが生成されます。
最後の`n`を適切な数字に変えて使用してください。
# 【PySpark入門】第４弾 実戦！RDDを操作してプログラムを作ってみる

## ブログURL

https://blog.serverworks.co.jp/introducing-pyspark-4

## 概要

ブログで使用するコードおよびデータファイルをダウンロードできます。

## メインソースコード

### ソースコード

#### イベント満足度・イベント会場評価の評点が計９点を超えた来場客の名前・メールアドレス一覧

`./src/questionnaire_analysis_1.py`

#### 男性・女性のイベント満足度の平均点

`./src/questionnaire_analysis_2.py`

#### 年代（２０代・３０代・４０代・５０代・６０代）によるイベント満足度の平均点およびどの年代からの評価が最もよかったのか

`./src/questionnaire_analysis_3.py`

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
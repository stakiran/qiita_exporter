# qiita_exporter
Qiita v2 API を使って自身の投稿記事全てをエクスポートする Python スクリプト

# Requirement

- Windows7+
- Python2.7
- requests

# Installation

- `git clone https://github.com/stakiran/qiita_exporter`
- `cd qiita_exporter`
- `copy export.bat.sample export.bat`
- `export.bat` を開き、QIITA_ACCESS_TOKEN 環境変数にアクセストークンを設定する
  - アクセストークンは [Qiitaにログイン後、設定画面から発行できます](https://qiita.com/settings/applications)
  - READ しか使わないので権限は **read_qiita** で十分です
- プロキシが必要なら HTTPS_PROXY 環境変数もセットする
  - 例: `set HTTPS_PROXY=https://(IP):(PORT)`
- `export.bat` を実行する

# Sample

```terminal
$ cd qiita_exporter

$ export.bat
 Response=200, Detail={'Rate-Reset': '1500863004', 'X-XSS-Protection': '1; mode=block', 'X-Content-Type-Options': 'nosniff', 'Rate-Remaining': '989', 'transfer-encoding': 'chunked', 'Total-Count': '8', 'Vary': 'Origin', 'X-Request-Id': 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX', 'Rate-Limit': '1000', 'Server': 'nginx', 'Connection': 'keep-alive', 'X-Runtime': '0.431045', 'ETag': 'W/"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"', 'Link': '<https://qiita.com/api/v2/authenticated_user/items?page=1&per_page=100>; rel="first", <https://qiita.com/api/v2/authenticated_user/items?page=1&per_page=100>; rel="last"', 'Cache-Control': 'max-age=0, private, must-revalidate', 'Date': 'Mon, 24 Jul 2017 01:53:18 GMT', 'X-Frame-Options': 'SAMEORIGIN', 'Content-Type': 'application/json; charset=utf-8'}
8 entries.
[1/8] saving...
[2/8] saving...
[3/8] saving...
[4/8] saving...
[5/8] saving...
[6/8] saving...
[7/8] saving...
[8/8] saving...

$ dir /b *.md
GitHub でテキスト管理を行う GaaTS(GitHub as a Text Storage) について.md
GitHub で使われる慣習的なリポジトリについてまとめてみた.md
README.md
ソフトウェアエンジニアに100の質問.md
タスク管理メソッド todo.txt が面白そう.md
テキストを素早く挿入する手法の一つ Text Expansion についての雑多なまとめ.md
ベアプログラミングが無理ならサイレントベアプログラミングを検討しよう.md
半角英数字記号と全角英数字かなカナ記号の一覧まとめ.md
秀丸エディタの弱いところ、強いところ.md
```

# License

[MIT License](LICENSE)

# Author

[stakiran](https://github.com/stakiran)

# weeklu-period-discovery

## これは
１週間の曜日（月火水木金土日）で、ユーザの検索行動が異なると仮説を与えると、キーワードによって平日が多いか休日が多くなると言えます
 
過去数年のGoogle Display Networkのサーチキーワードを曜日ごとのimpressionの平均を求めることで、その仮説が成り立ちうるキーワードを探します

## 使い方
StormRulerなどのGDNなどのパフォーマンスが取得できるソフトで、Adwordsのログを取得していることが前提となります  

### データのシリアライズ
```console
$ python3 scanner.py --make1
```

### シリアライズしたデータを集計する
```cosnole
$ python3 scanner.py --make2
```

### 日付を曜日に変換して保存
```console
$ python3 scanner.py --make3
```

### 曜日ごとの平均値を計算
```console
$ python3 scanner.py --make4
```

### 計算結果の出力
```console
$ python3 scanner.py --make5
```

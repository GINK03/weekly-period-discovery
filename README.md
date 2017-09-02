# weekly-period-discovery

## what is this
１週間の曜日（月火水木金土日）で、ユーザの検索行動が異なると仮説を与えると、キーワードによって平日が多いか休日が多くなると言えます
 
過去数年のGoogle Display Networkのサーチキーワードを曜日ごとのimpressionの平均を求めることで、その仮説が成り立ちうるキーワードを探します

## how to use
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

## result
集計結果でキーワードごとに差があるが、大局的な傾向としては、健康志向やビジネスに関するものに関しては、月火水木が多い  
<p align="center">
  <img width="450px" src="https://user-images.githubusercontent.com/4949982/29996575-29b70654-903c-11e7-8c5d-58745ccbe643.png">
</p>
<div align="center"> 図1. 高血圧 </div>

<p align="center">
  <img width="450px" src="https://user-images.githubusercontent.com/4949982/29996588-669557ba-903c-11e7-8134-d0bf0e9407c3.png">
</p>
<div align="center"> 図2. 野菜ジュース </div>

<p align="center">
  <img width="450px" src="https://user-images.githubusercontent.com/4949982/29996596-93c6fc2a-903c-11e7-9d8c-1065b9d41a0d.png">
</p>
<div align="center"> 図3. 産婦人科 </div>

<p align="center">
  <img width="450px" src="https://user-images.githubusercontent.com/4949982/29996615-b8d93618-903c-11e7-956e-76d995cb79d3.png">
</p>
<div align="center"> 図4. 野村証券 </div>

これの対極として、デジタル製品に関しては土日が多い  
<p align="center">
  <img width="450px" src="https://user-images.githubusercontent.com/4949982/29996624-f61e835c-903c-11e7-916a-ae1ababbe23c.png">
</p>
<div align="center"> 図5. 女性 iphoneケース </div>

<p align="center">
  <img width="450px" src="https://user-images.githubusercontent.com/4949982/29996635-1e8c8640-903d-11e7-9d25-6bce8806a124.png">
</p>
<div align="center"> 図6. タブレット OS </div>

<p align="center">
  <img width="450px" src="https://user-images.githubusercontent.com/4949982/29996644-4796d9dc-903d-11e7-970d-ac318ad5d858.png">
</p>
<div align="center"> 図7. iphone7 </div>

<p align="center">
  <img width="450px" src="https://user-images.githubusercontent.com/4949982/29996651-66479d26-903d-11e7-8b84-c40512318e32.png">
</p>
<div align="center"> 図8. +スマートフォン </div>

特殊な動きをするキーワードの例
<p align="center">
  <img width="450px" src="https://user-images.githubusercontent.com/4949982/29996668-b9312ad4-903d-11e7-8550-0133f002ff3a.png">
</p>
<div align="center"> 図9. instagram </div>

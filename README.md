# Twitter getter bot Twitter ゲッターボット

# Operation オペレーション

- ツイート　数　（数はオプショナル　デフォルトで5つ）  
数の分の新しいツイートを返信する。最大20

- フォロワー  
フォロワーの数を出す
- フォロー
フォロー数を出す

- 最高いいね  
最近の最大いいねのツイート、いいね数を出す

- 最高リツート  
最近の最大ツイートのツイート、いいね数を出す

- @垢　数  
そのひとの最新のツイートを最大20まで出す。

- @垢　フォロワー  
そのアカウントのフォロワーの数を出す

- @垢　フォロー  
フォロー数を出すフォロー数を出す

### ツイート　数　（数はオプショナル　デフォルトで5つ）
できれば、ツイートごとにメッセージにして送る
push_messageを使ってやることにする？


#### 課題
これらのオペレーションをリッチメニューでできたら最高
tweepy でできることをもっと探して機能を追加できることに期待。
今現在自分のアカウントでしかツイートを拾えない。→　自分以外がボットを追加しても意味ない。。。
→　またはツイート、フォロワー、フォローの機能をやめるか
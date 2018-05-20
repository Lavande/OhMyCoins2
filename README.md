# ohmycoins
See how many coins you have and how much they value with data from many sources.
### 注意，这个repo是后端，需要配合[前端](https://github.com/seven777777/hackathon-onmycoins)使用

# Dorahacks 2018 上海 黑客松 梭哈老头队作品

如果你有很多钱包，在很多交易所有账户，那么很难一下子说清楚自己到底有哪些币，每样有多少，也不知道加起来值多少钱了。这个项目就是帮你做这件事，设置好自己的钱包地址以及交易所API，然后一键查询自己的虚拟货币资产状况。目前支持的数据来源有：
- Etherscan（直接提供地址查询）所有ETH和基于以太坊的代币
- 各交易所账户（币种和余额查询）
- - Poloniex 
- - Bittrex
- - Bitfinex
- - Bigone
- CoinmarketCap（查询价格）

## 简介
### 原理
根据提供的地址去etherscan查询余额，通过API查询交易所账户的余额，最后到Coinmarketcap查询所有币种当前CNY价格，最后前端生成图表，展示网页。

## TODO
- 添加更多数据来源，完善逻辑和容错处理
- （也许）写成Web服务或微信公众号服务
- 完善文档和readme

# WINDY IDIOM 大风成语输入法方案

## Introduction 介绍
想要更快速的输入成语？在抢成语接龙红包时拔得头筹？大风成语输入法方案可以帮你！
只需要输入首字拼音，即可为你推荐成语！

## Screenshot 截图
![](screenshots/1.png)
![](screenshots/2.png)

## How to use 使用方式
- 下载中州韵输入法在各平台的适配端(Android:trime(同文输入法), Windows:Weasel(小狼毫输入法))
- 下载output文件夹中的输入法方案
- 导入方案
- 开始享受!

## How to build
```
git clone https://github.com/yangrq/windy_idiom
cd windy_idiom
python convert_idiom.py
```

## Bug list 已知故障
- Android平台上，在QQ中发送成语接龙红包的输入框无法正常输入
- 在输入多个音节时，会不必要地联想以后几个音节开头的成语并将其添加至候选项尾部（不必要的智能组词）

## Donation 捐赠
欢迎捐赠！

<img src="http://yangrq.luobotou.org/wp-content/uploads/2019/08/wechat.png" alt="微信" width="120" height="120">
<img src="http://yangrq.luobotou.org/wp-content/uploads/2019/08/alipay.jpg" alt="支付宝" width="130" height="130">

## File description 文件描述

### idiom.json
源数据

### convert_idiom.py
去除不必要的信息并转换、输出拼音

### origin
源方案文件夹

### output
目标输出文件夹
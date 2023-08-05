# wechat_auto

微信群控系统

## Function list

1. 使用微信`文件助手`实现远程控制，在`文件助手`中输入`help`获取所有命令列表
2. 自动通过好友请求，打招呼信息保存在`wechat_auto.GREETING`变量中，为长度为3的一个数组

## New features

### 1

可以给制定群定时发送消息，消息内容在`/storage/joke`文件中读取，每条消息由'|'符号分割。
消息间隔时间在`wechat_auto.CHATROOM_SPAN`定义，默认为1小时，也就是3600秒。
群名称由`wechat_auto.CHATROOM_NAME_MESSAGE`定义，默认是"哈哈哈哈哈哈哈"
`wechat_auto.SWITCH_MESSAGE`默认为False，也就是关闭定时群消息功能

### 2

添加新功能，可以在所有群聊有新人加入的时候自动@新人打招呼，并且可是设置群名称，为LIST变量
过滤变量为`wechat_auto.CHATROOM_NAME_GREETING`
打招呼信息变量为`wechat_auto.CHATROOM_GREETING`

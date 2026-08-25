# 主要目的是让MikroTik RouterOS的防火墙直接绕过CN地址表，并且与proxy tools内规则一致

## 上游来数据库来自

https://github.com/MetaCubeX/meta-rules-dat

### 当前自动生成CN地址表

使用方法，将下面字段加入RouterOS的/system/script中，**如果设备性能弱，应适当延长delay**，默认等待5秒
```
/tool fetch url="https://raw.githubusercontent.com/gebilaozhaodezhaijidi/ros-import-cn/refs/heads/main/CN.rsc"
:delay 5s
:if ([:len [/file find name=CN.rsc]] > 0) do={
/ip firewall address-list remove [find list=CN] 
:delay 5s
/import file=CN.rsc
:delay 5s
/file remove [find name="CN.rsc"]
}
```
在system/scheduler/添加定时任务，该项目为每天早上7:00生成，建议设置成之后的时间

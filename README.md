# Tencent Cloud (QCloud) COS SDK
## 介绍

由于腾讯云官方至今（2018年3月16日）仍未提供 Python 3 下对象存储（下称“COS”）服务SDK，遍寻 GitHub 亦未发现功能完整的社区移植版本。故此，特花费一个下午完成了基于官方 Python 2 版本 SDK 的移植工作，希望能够帮助到同样被此问题折磨的朋友。

**重要提示**：*这不是COS的官方SDK！This is not an official version SDK of the COS!* 目前仅在 Python 3.5 下完成了 **Bucket 创建/删除**、**单文件上传/下载**、**分片上传**等 API 的测试，请自行评估并承担在生产环境使用此 SDK 的风险。

## 安装
使用 pip3 安装：
```shell
    pip3 install -U cos-python3-sdk-v5
```

手动安装：
```shell
    python3 setup.py install
```

## 使用
所有 API 调用方法与官方版本相同，详见[官方文档](https://cloud.tencent.com/document/product/436/12269)、[官方DEMO](https://github.com/tencentyun/cos-python-sdk-v5/blob/master/qcloud_cos/demo.py)

## 其他
欢迎各种测试报告和 PR，如有任何问题请发 Issue，谢谢！

## 给腾讯云的话
希望贵司能顺应技术潮流，尽快发布官方 Python 3 SDK，如本项目侵犯了贵司的合法权益，请联系本人删除。

# volo

This repo is to implement volo using MindSpore

# Finish

1、完成算子差异文档分析

2、model.py 完成

3、动态图模式下模型跑通训练

# TO DO

1、对静态图模式报错debug

2、静态图模式下跑通训练

# 更新日志

### 2022/10/12

修改完模型结构，拉取mindspore源码和fold的pr在gpu服务器上进行编译；

### 2022/10/14

测试模型结构；PYNATIVE模式下可以跑通；

### 2022/10/16

由于GPU服务器出问题，不能继续推进；尝试函数实现unfold和fold算子，用CPU跑模型；

### 2022/10/18

新的模型结构完成，在CPU上PYNATIVE模式下可以跑通；GRAPH模式依旧报错；准备继续推进PYNATIVE模式下的训练；

### 2022/10/20

修改yaml文件，动态图训练下跑通train.py；

### 2022/10/22

使用小数据集跑精度测试，50个epoch，能达到收敛，但精度较低；后续准备使用openi平台跑全数据集。
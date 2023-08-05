# Half.Sample

[![Build Status](https://travis-ci.com/KD-Group/Half.Sample.svg?branch=master)](https://travis-ci.com/KD-Group/Half.Sample.svg?branch=master)
[![Build status](https://ci.appveyor.com/api/projects/status/qry88i7n75txreu9/branch/master?svg=true)](https://ci.appveyor.com/project/SF-Zhou/half-sample/branch/master)

Sample, C++ Program in Half Application with Python Module

## Requirements

Python Requirements:

1. st
2. typing

Others:

1. C++11 environment
2. scons

You can also refer to the Travis-CI config file: `.travis.yml`, or Appveyor config file: `appveyor.yml`.

## pip安装 `pip install sample-kd`

ps: 由于`sample` 在 `pypi` 已经被人注册,所以只能加后缀. 安装后可以python安装目录下找到`sample.exe`

## 上传到pypi

1. 修改setup.py 里面的版本号
2. 给当前提交打tag: git tag -a "v0.0.1" -m "add tag v0.0.1"
3. push最新的commit: git push -m "balalala" (可以跳过,只push tag)
4. push最新的tag: git push --tag (提交tag会触发deploy操作) 


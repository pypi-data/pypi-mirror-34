# 项目：标准函数库
# 模块：Python相关实用命令
# 作者：黄涛
# License:GPL
# Email:huangtao.sh@icloud.com
# 创建：2015-08-09 07:50
# 修订：2016-03-19
# 修订：2016-5-12
# 修订：2016-9-23 新增pyupload功能，使用run_setup来进行安装调用

import sys
import os
from orange import Path, exec_shell
from orange.deploy import run_setup

libpath = str(Path('~/OneDrive/pylib'))


def _clear():
    for path in Path('.').glob('*.egg-info'):
        print('Path %s has beed deleted!' % (path))
        if path.is_dir():
            path.rmtree()


def pyupload():
    run_setup('sdist', '--dist-dir', libpath, 'upload')
    _clear()


def pysdist():
    run_setup('sdist', '--dist-dir', libpath)
    _clear()

# -*- coding: utf-8 -*-
# @Time : 2022/1/11 1:46
# @Author : WhaleFall
# @Site : 
# @File : config.py
# @Description : 项目的配置文件
import os
from pathlib import Path
import platform


class Config:
    BASE_DIR = Path(__file__).resolve().parent  # 项目绝对目录
    if platform.system() == "Windows":
        DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db', 'data.db')
    else:
        DATABASE_URI = 'sqlite:////' + os.path.join(BASE_DIR, 'db', 'data.db')

    def __init__(self):
        Path(Config.BASE_DIR, 'db').mkdir(exist_ok=True)

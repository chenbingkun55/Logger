                    Logger 日志记录器
                                          2015-01-20 ChenBK At chenbingkun55@163.com

说明：
    通过Log.py单入口记录日志到各种存储媒介中.
    1. 首先实现BigQuery媒介。

一、程序入口， 定义Logger 使用方法
    1. INFO     写入INFO日志。
    2. Warn     写入INFO日志。
    3. CUSTOM   自定义格式。



\_{*}+=
import os
import sys

sys.path.append('lib')
import bigquery as db
_db = None

初始化

写入日志

init()

_db.query()

@>


\_{初始化}+=
def init():
    _db = db.create_engine()
@>

\_{写入日志}+=
@>

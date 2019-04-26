#coding=gbk
"""
下面的代码使用Spark来统计100000000以内的素数数量，在6GB RAM、双核CPU的64位Win7+Spark单机平台上运行的时间为
760+秒
"""
from pyspark import SparkConf,SparkContext
from pyspark.sql import SQLContext
from random import random

conf = SparkConf().setAppName("isPrime")
sc = SparkContext(conf = conf)
sqlCtx = SQLContext(sc)
def isPrime(n):
    if n < 2:
        return False
    if n ==2:
        return True
    if not n & 1:
        return False
    for i in range(3, int(n ** 0.5) + 2, 2):
        if n % i == 0:
            return False
    return True

rdd = sc.parallelize(range(100000000))
result = rdd.filter(isPrime).count()
print('=' * 30)
print(result)
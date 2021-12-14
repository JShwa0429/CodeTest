""" 
높이 : V
낮에 : A 미터 오름
밤엔 : B 미터 미끄러짐
V에 다다를려면 며칠 걸리는 지 작성
"""
import math
A,B,V = map(int,input().split())
print(math.ceil((V-A) / (A-B)) + 1)


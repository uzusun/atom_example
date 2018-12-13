

#-*- coding:utf-8 -*-

population = [9860,3400,2455,2886,1517,1536,1142,197,12398,1506,1561,2089,1798,1757,2642,3285]
region_count = len(population)

sum_population = 0
for a in population:
    sum_population += a

avg_population = sum_population / region_count

print("인구 합계 : ", sum_population)
print("인구 평균 : ", avg_population)


#한글 깨질때 사용
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


region_population = {"서울":9860,"부산":3400,"대구":2455,"인천":2886,"광주":1517,"대전":1536,"울산":1142,"세종":197,"경기":12398,"강원":1506,"충북":1561,"충남":2089,"전북":1798,"전남":1757,"경북":2642,"경남":3285}

sum_population = 0
region_population["제주"] = 578
region_population["서울"] = 10200
region_population["인천"] = 3200
region_population["경기"] = 10300
for key in region_population.keys():
    print(key,region_population[key])
    sum_population += region_population[key]

avg_population = sum_population / len(region_population)

print("전국 인구 합계 : ", sum_population)
print("전국 인구 평균 : ", avg_population)


#한글 깨짐 보정
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

num_list = list()
for a in range(3):
    a =+ 1
    num = input("%d 번째 숫자를 입력하세요 : " % a)
    num_list.append(num)

print(num_list)

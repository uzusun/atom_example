#한글 깨짐 보정
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

drink_data = {"cola":1000, "milk":1500, "juice":2000, "water":900, "sprite":1000}

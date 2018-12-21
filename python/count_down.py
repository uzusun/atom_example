def count_down(count):
    if count == 0:
        print("End")
    else:
        print(count)
        count_down(count-1)

count_down(3)

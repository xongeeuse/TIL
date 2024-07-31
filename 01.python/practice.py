# # 5층*4가구 아파트에 택배기사 방문

# for floor in [1, 2, 3, 4, 5]:
#     for ho in [1, 2, 3, 4]:
#         print(floor, ho) 



# for i in range(6):
#     for n in range(4):
#         print(i, n)



# for hour in range(1, 13):
#     for min in range(1, 61):
#         print(hour, min)


# for floor in range(2):
#     print(f'{floor}층')
#     for ho in range(4):
#         print(f'{ho}호')


elements = [['A', 'B'], ['c', 'd']]

# A
# c
# d
# B
# c
# d
# 순으로 출력하려면?

# my sol
for elem in elements[0]:
    for item in elem:
        print(item)
        for elem in elements[1]:
            for item in elem:
                print(item)


# 00 10 11
# 01 10 11

# 강사님 풀이!
for i in range(0, 2):
    print(elements[0][i])
    for j in range(0, 2):
        print(elements[1][j])
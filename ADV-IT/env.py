data = 1200
count = 0
m_c = 0
if data <= 1000:
    m_c = 6
elif (data > 1000) and (data % 1000 != 0):
    count = (data // 1000) + 1
    m_c = count * 6
print(count, m_c)


print('K2'+1)
import itertools

order_times = []
for i in range(5):
    order_times.append(int(input()))

all_comb_order_times = list(set(list(itertools.permutations(order_times))))


ans = float('inf')
for comb_order_time in all_comb_order_times:
    order_time_total = 0
    for i in range(len(comb_order_time)):
        order_time_total += comb_order_time[i]
        if i != 4 and order_time_total % 10 != 0:
            add_num = 10 - (order_time_total % 10)
            order_time_total += add_num
        
    ans = min(ans, order_time_total)

print(ans)
# ETA: 8.67s [ 23%][=====> ] 233/1000 | elapsed time 2.33s
import datetime
import time


def ft_progress(list):
    start_t = datetime.datetime.now()
    list_len = len(list)
    for counter, n in enumerate(list, 1):
        current_t = datetime.datetime.now()
        elapsed_t = current_t - start_t
        q = counter / list_len
        unit = elapsed_t / counter
        eta = (list_len - counter) * unit
        nbr_of_equal = int(q * 10)
        nbr_of_space = 10 - nbr_of_equal
        bar = f"[{'=' * nbr_of_equal}>{' ' * nbr_of_space}]"
        print(f"ETA: {eta.seconds:2}.{int(eta.microseconds/10000):#02}s " +
              f"[{q:4.0%}]{bar} {counter}/{list_len} | elapsed time " +
              f"{elapsed_t.seconds}.{int(elapsed_t.microseconds/10000):#02}s",
              end='\r')
        yield n


listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.005)
print()
print(ret)

# listy = range(1000)
# ret = 0
# for elem in ft_progress(listy):
#     ret += (elem + 3) % 5
#     time.sleep(0.01)
# print()
# print(ret)

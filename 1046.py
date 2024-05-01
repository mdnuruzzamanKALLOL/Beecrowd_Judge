main_value = input()

start_time, end_time = main_value.split()

start_time = int(start_time)
end_time = int(end_time)

if start_time > end_time:
    duration = (24 - start_time) + end_time
    print("O JOGO DUROU {} HORA(S)".format(duration))
elif end_time > start_time:
    duration = end_time - start_time
    print("O JOGO DUROU {} HORA(S)".format(duration))
elif start_time == end_time:
    print("O JOGO DUROU 24 HORA(S)")
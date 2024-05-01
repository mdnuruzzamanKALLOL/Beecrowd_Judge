main_value = input()

initial_hour, initial_minute, final_hour, final_minute = main_value.split()

initial_hour = int(initial_hour)
initial_minute = int(initial_minute)
final_hour = int(final_hour)
final_minute = int(final_minute)

start_minutes = initial_hour * 60 + initial_minute
end_minutes = final_hour * 60 + final_minute

if initial_hour == final_hour and initial_minute == final_minute:
    hours = 24
    minutes = 0
else:
    if end_minutes <= start_minutes:
        end_minutes += 24 * 60

    duration_minutes = end_minutes - start_minutes

    hours = duration_minutes // 60
    minutes = duration_minutes % 60

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hours, minutes))
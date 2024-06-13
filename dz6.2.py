seconds_input = int(input("Введіть кількість секунд: "))
if seconds_input < 0 or seconds_input >= 8640000:
    print("Невірне значення. Введіть число більше або дорівнює 0 і менше ніж 8640000.")
else:
    days, remainder = divmod(seconds_input, 24 * 60 * 60)
    hours, remainder = divmod(remainder, 60 * 60)
    minutes, seconds = divmod(remainder, 60)
    if hours == 24:
        days += 1
        hours = 0
    if 10 <= days % 100 <= 20:
        days_word = 'днів'
    else:
        days_word = 'день' if days % 10 == 1 else 'дні' if 2 <= days % 10 <= 4 else 'днів'

    x = f"{days} {days_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

    print(x)

seconds_input = int(input("Введіть кількість секунд: "))

if seconds_input < 0 or seconds_input >= 8640000:
    print("Невірне значення. Введіть число більше або дорівнює 0 і менше ніж 8640000.")
else:
    days, remainder = divmod(seconds_input, 24 * 60 * 60)
    hours, remainder = divmod(remainder, 60 * 60)
    minutes, seconds = divmod(remainder, 60)

    x = f"{days} {'день' if days == 1 else 'дні' if 2 <= days <= 4 else 'днів'}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

    print(x)
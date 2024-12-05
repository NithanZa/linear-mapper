from sigfig import round

rounding_method = input("\nEnter the rounding method (sf or dp): ")
while rounding_method not in ("sf", "dp"):
    rounding_method = input("Invalid input. Enter the rounding method (sf or dp): ")

rounding_setting = int(input(f"\nRound to how many {rounding_method}?: "))
while rounding_setting < 0:
    rounding_setting = int(input("Invalid input. Enter a positive number: "))

start_x = float(input("\nEnter the starting x value (before map): "))
end_x = float(input("\nEnter the end x value (before map): "))
mapped_start_x = float(input("\nEnter the starting x value (after map): "))
mapped_end_x = float(input("\nEnter the end x value (after map): "))

start_y = float(input("\nEnter the starting y value (before map): "))
end_y = float(input("\nEnter the end y value (before map): "))
mapped_start_y = float(input("\nEnter the starting y value (after map): "))
mapped_end_y = float(input("\nEnter the end y value (after map): "))


def translate(x, y):
    interpolated_x = mapped_start_x + ((x - start_x) / (end_x - start_x)) * (mapped_end_x - mapped_start_x)
    interpolated_y = mapped_start_y + ((y - start_y) / (end_y - start_y)) * (mapped_end_y - mapped_start_y)
    return interpolated_x, interpolated_y


def custom_round(num, rounding_setting, rounding_method):
    return round(num, sigfigs=rounding_setting) if rounding_method == "sf" else round(num, decimals=rounding_setting)


while True:
    x = float(input("\nEnter the x value: "))
    y = float(input("\nEnter the y value: "))

    if x < start_x or x > end_x or y < start_y or y > end_y:
        print("\nOut of bounds.")
        continue

    translated_x, translated_y = translate(x, y)
    print(
        f"\nTranslated point: ({custom_round(translated_x, rounding_setting, rounding_method)}, {custom_round(translated_y, rounding_setting, rounding_method)})")

    repeat = "_"
    while repeat not in ("y", "n", ""):
        repeat = input("\nWould you like to enter another point? (Y/n): ").lower()

    exit() if repeat == "n" else None

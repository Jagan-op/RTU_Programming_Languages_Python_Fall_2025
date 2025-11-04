# file: lab_3_1_simple_datasets_minimal.py

# Data
temperatures = [18.2, 20.1, 19.4, 17.8, 21.0, 22.3, 20.7]
city_population = {
    "Riga": 605_802,
    "Vilnius": 592_389,
    "Tallinn": 454_188,
    "Kaunas": 312_120,
    "Liepaja": 68_945,
}

# Aggregates
average_temperature = sum(temperatures) / len(temperatures) if temperatures else 0.0  # why: avoid ZeroDivisionError
largest_city, largest_population = max(city_population.items(), key=lambda kv: kv[1])
smallest_city, smallest_population = min(city_population.items(), key=lambda kv: kv[1])
total_population = sum(city_population.values())

# Output
print("== Weekly Temperature Stats ==")
print(f"Average temperature: {average_temperature:.2f}")

print("\n== City Population Stats ==")
print(f"Largest city:  {largest_city} - {largest_population:,}")
print(f"Smallest city: {smallest_city} - {smallest_population:,}")
print(f"Total population: {total_population:,}")

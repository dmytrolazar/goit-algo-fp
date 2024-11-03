class Meal:
    def __init__(self, name, cost, calories):
        self.name = name
        self.cost = cost
        self.calories = calories
        self.ratio = calories / cost

def greedy_algorithm(items: list[Meal], budget: int) -> int:
    items.sort(key=lambda x: x.ratio, reverse=True)
    total_calories = 0
    chosen_items = []
    for item in items:
        if budget >= item.cost:
            budget -= item.cost
            total_calories += item.calories
            chosen_items.append(item.name)
    return "The optimal meal consists of " + ', '.join(chosen_items) + " and has " + str(total_calories) + " calories."

def dynamic_programming(budget, cost, calories, names, n):
    K  = [[0  for w in range(budget + 1)] for i in range(n + 1)] # таблиця оптимальних значень підзадач на кожному кроці для кількості калорій
    Km = [[[] for w in range(budget + 1)] for i in range(n + 1)] # таблиця оптимальних наборів страв на кожному кроці

    for i in range(n + 1):
        for w in range(budget + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif cost[i - 1] <= w:
                calories_if_meal_i = calories[i - 1] + K[i - 1][w - cost[i - 1]]
                K[i][w] = max(calories_if_meal_i, K[i - 1][w])
                if calories_if_meal_i >= K[i - 1][w]:
                    Km[i][w].extend(Km[i - 1][w - cost[i - 1]])
                    Km[i][w].append(names[i - 1])
                else:
                    Km[i][w].extend(Km[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
                Km[i][w].extend(Km[i - 1][w])
    return "The optimal meal consists of " + ', '.join(Km[n][budget]) + " and has " + str(K[n][budget]) + " calories."


meals = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

items = [Meal(meal, meals[meal]['cost'], meals[meal]['calories']) for meal in meals]
print("Greedy algorithm's perfect meal:", greedy_algorithm(items, budget))

calories = [meals[meal]['calories'] for meal in meals]
cost = [meals[meal]['cost'] for meal in meals]
names = [meal for meal in meals]
print("Dynamic algorithm's perfect meal:", dynamic_programming(budget, cost, calories, names, len(calories)))

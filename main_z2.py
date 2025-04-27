def read_recipes(file_name):
    cook_book = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break

            ingredient_count = int(file.readline().strip())
            ingredients = []

            for _ in range(ingredient_count):
                ingredient_line = file.readline().strip()
                if not ingredient_line:
                    continue

                ingredient_info = [part.strip() for part in ingredient_line.split('|')]
                ingredient = {
                    'ingredient_name': ingredient_info[0],
                    'quantity': int(ingredient_info[1]),
                    'measure': ingredient_info[2]
                }
                ingredients.append(ingredient)

            cook_book[dish_name] = ingredients
            file.readline()

    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count

                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}

    return shop_list


def print_shop_list(shop_list):
    print('{')
    for i, (name, details) in enumerate(shop_list.items()):
        print(f"  '{name}': {{'measure': '{details['measure']}', 'quantity': {details['quantity']}}}", end='')
        if i < len(shop_list) - 1:
            print(',')
        else:
            print()
    print('}')


def main():
    cook_book = read_recipes('recipes.txt')

    print("Доступные блюда:")
    for dish in cook_book.keys():
        print(f"- {dish}")

    while True:
        try:
            dishes = input("\nВведите названия блюд через запятую: ").split(',')
            dishes = [dish.strip() for dish in dishes]
            invalid_dishes = [dish for dish in dishes if dish not in cook_book]

            if invalid_dishes:
                print(f"Ошибка: следующие блюда не найдены: {', '.join(invalid_dishes)}")
                continue

            person_count = int(input("Введите количество персон: "))
            if person_count <= 0:
                print("Количество персон должно быть положительным числом")
                continue

            break
        except ValueError:
            print("Ошибка: введите корректное число")

    shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)

    print("\nСписок ингредиентов:")
    print_shop_list(shop_list)


if __name__ == '__main__':
    main()
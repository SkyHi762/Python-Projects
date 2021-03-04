import requests

Filter=input('Please state if you are vegan,vegetarian. If not, press any key to continue ')

if Filter=='vegan':
    exclu = input('State any additional unwanted ingredients')
    def recipe_search(ingredient):
        url = 'https://api.edamam.com/search?q={}&app_key=a0468863a0c0f670af48317340952ba3&app_id=37955c3a&health=vegan&excluded={}'.format(ingredient,exclu)
        result = requests.get(url)
        data = result.json()
        return data['hits']


    def run():
        ingredient = input('Enter an ingredient: ')
        recipes = recipe_search(ingredient)
        for recipe in recipes:
            print('Title: ' + recipe['recipe']['label']
                  + ' \nURL: ' + recipe['recipe']['url']
                  + ' \nIngredients:')
            i = (recipe['recipe']['ingredients'])
            for ing in i:
                print('  ' + (ing['text']))
            print('Calories: {}'.format(str(int(recipe['recipe']['calories']))))
            print()

    def choose_recipe():
        shop = input('what recipe have you chosen? ')
        chosen_recipe = '{}'.format(shop)
        url = 'https://api.edamam.com/search?q={}&app_key=a0468863a0c0f670af48317340952ba3&app_id=37955c3a' \
            .format(chosen_recipe)
        result = requests.get(url).json()
        data = result["hits"][0]['recipe']
        recipe_title = data['label']
        recipe_ingredient = data['ingredients']
        print(recipe_title)
        print('The ingredients have been saved in a file named,"SearchResults.csv"')
        save_to_file(recipe_ingredient)
        shopping_list()

    def shopping_list():
        needed_ingredients = (input('What ingredients do you need? ')).split(', ')
        in_fridge = (input('What ingredients do you have? ')).split(', ')
        fridge = [in_fridge]
        have = fridge

        for item in have:
            if item[-2:] == 'es':
                have.append(item[:-2])
            elif item[-1:] == 's':
                have.append(item[:-1])
            else:
                ()

        to_shop = []
        for item in needed_ingredients:
            if item in have:
                ()
            else:
                to_shop.append(item)

        print("You have {} in your fridge\nso you need to buy {}".format(have, to_shop))
        return shopping_list()

    # save the results into a file.
    def save_to_file(results):
        field_names = ['text', 'weight']
        with open("SearchResults.csv", "w+") as csv_file:
            search_result = csv.DictWriter(csv_file,fieldnames=field_names)
            search_result.writeheader()
            search_result.writerows(results)
            csv_file.flush()


    def guests():

        df = pandas.read_csv('SearchResults.csv',
                             header=0,
                             names=['Ingredients', 'Quantity (grams)'],
                             index_col='Ingredients')
        print(df)
        df.to_csv('SearchResults.csv')

        chosen_recipe = '{}'.format(shop)
        url = 'https://api.edamam.com/search?q={}&app_key=a0468863a0c0f670af48317340952ba3&app_id=37955c3a' \
            .format(chosen_recipe)
        result = requests.get(url).json()
        data = result["hits"][0]['recipe']

        recipe_ingredient = data['ingredients']
        weight = []
        for ing in recipe_ingredient:
            weight.append(float(ing['weight']))
        portions = float(data['yield'])

        guests = (float(input('How many guests are coming?')))
        if guests == 1.0:
            print('Great, this recipe makes 1 portion'.format(portions))
        elif guests > 1.0:
            print("This recipe makes {} portions. Let's calculate how much of each ingredient we need".format(
                portions))

        nec = []
        for i in weight:
            nec.append(i * guests)
        print(nec)

        df.insert(1, "Necessary Amount", nec, True)
        df.to_csv('SearchResults.csv')

    run()

    choose_recipe()

elif Filter=='vegetarian'=='veggie':
    exclu = input('State any additional unwanted ingredients')

    def recipe_search(ingredient):
        url = 'https://api.edamam.com/search?q={}&app_key=a0468863a0c0f670af48317340952ba3&app_id=37955c3a&health=vegan&excluded={}'.format(ingredient, exclu)
        result = requests.get(url)
        data = result.json()

        return data['hits']

    print(run)
    print(choose_recipe)
    print(save_to_file)
    print(guests)
else:

    exclu = input('State any unwanted ingredients')
    def recipe_search(ingredient):

        url='https://api.edamam.com/search?q={}&app_key=a0468863a0c0f670af48317340952ba3&app_id=37955c3a&excluded={}'.format(ingredient,exclu)
        result = requests.get(url)
        data = result.json()

        return data['hits']


    def run():
        ingredient = input('Enter an ingredient: ')
        recipes = recipe_search(ingredient)
        for recipe in recipes:
            print('Title: ' + recipe['recipe']['label']
                  + ' \nURL: ' + recipe['recipe']['url'] + '\nCalories: {}'.format(
                str(int(recipe['recipe']['calories'])))
                  + ' \nIngredients:')
            i = (recipe['recipe']['ingredients'])
            for ing in i:
                print('  ' + (ing['text']))
                print()


    def choose_recipe():
        shop = input('what recipe have you chosen? ')
        chosen_recipe = '{}'.format(shop)
        url = 'https://api.edamam.com/search?q={}&app_key=a0468863a0c0f670af48317340952ba3&app_id=37955c3a' \
            .format(chosen_recipe)
        result = requests.get(url).json()
        data = result["hits"][0]['recipe']
        recipe_title = data['label']
        recipe_ingredient = data['ingredients']
        print(recipe_title)
        print('The ingredients have been saved in a file named,"SearchResults.csv"')
        save_to_file(recipe_ingredient)
        shopping_list()


    def shopping_list():
        needed_ingredients = (input('What ingredients do you need? ')).split(', ')
        in_fridge = (input('What ingredients do you have? ')).split(', ')
        fridge = [in_fridge]
        have = fridge

        for item in have:
            if item[-2:] == 'es':
                have.append(item[:-2])
            elif item[-1:] == 's':
                have.append(item[:-1])
            else:
                ()

        to_shop = []
        for item in needed_ingredients:
            if item in have:
                ()
            else:
                to_shop.append(item)

        print("You have {} in your fridge\nso you need to buy {}".format(have, to_shop))


    # save the results into a file.
    def save_to_file(results):
        field_names = ['text', 'weight']
        with open("SearchResults.csv", "w+") as csv_file:
            search_result = csv.DictWriter(csv_file, fieldnames=field_names)
            search_result.writeheader()
            search_result.writerows(results)
            csv_file.flush()


    def guests():

        df = pandas.read_csv('SearchResults.csv',
                             header=0,
                             names=['Ingredients', 'Quantity (grams)'],
                             index_col='Ingredients')
        print(df)
        df.to_csv('SearchResults.csv')

        chosen_recipe = '{}'.format(shop)
        url = 'https://api.edamam.com/search?q={}&app_key=a0468863a0c0f670af48317340952ba3&app_id=37955c3a' \
            .format(chosen_recipe)
        result = requests.get(url).json()
        data = result["hits"][0]['recipe']

        recipe_ingredient = data['ingredients']
        weight = []
        for ing in recipe_ingredient:
            weight.append(float(ing['weight']))
        portions = float(data['yield'])

        guests = (float(input('How many guests are coming?')))
        if guests == 1.0:
            print('Great, this recipe makes 1 portion'.format(portions))
        elif guests > 1.0:
            print("This recipe makes {} portions. Let's calculate how much of each ingredient we need".format(
                portions))

        nec = []
        for i in weight:
            nec.append(i * guests)
        print(nec)

        df.insert(1, "Necessary Amount", nec, True)
        df.to_csv('SearchResults.csv')

    run()
    choose_recipe()
    run()




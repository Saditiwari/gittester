
recipes = { 
    "small": { 
        "ingredients": { 
            "bread": 2,  ## slice 
            "ham": 4, ## slice 
            "cheese": 4, ## ounces 
        }, 
        "cost": 1.75, 
    }, 
    "medium": { 
        "ingredients": { 
            "bread": 4,  ## slice 
            "ham": 6, ## slice 
            "cheese": 8, ## ounces 
        }, 
        "cost": 3.25, 
    }, 
    "large": { 
        "ingredients": { 
            "bread": 6,  ## slice 
            "ham": 8, ## slice 
            "cheese": 12, ## ounces 
        }, 
        "cost": 5.5, 
    } 
}
resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24  ## ounces
}

def check_resources(self, resources, recipes):
    for ingredient, amount in recipes[self]["ingredients"].items():
        if resources[ingredient] < amount:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

def process_coins():
    coins = {"large_dollar": 0, "half_dollar": 0, "quarter": 0, "nickel": 0}
    coins["large_dollar"] = int(input("how many large dollars?: "))
    coins["half_dollar"] = int(input("how many half dollars?: "))
    coins["quarter"] = int(input("how many quarters?: "))
    coins["nickel"] = int(input("how many nickels?: "))
    return coins

def make_sandwich(self, resources, recipes):
    for ingredient, amount in recipes[self]["ingredients"].items():
        resources[ingredient] -= amount
    print(f"{self} sandwich is ready. Bon appetit!")

def report(resources):
    print("Bread:", resources["bread"], "slice(s)")
    print("Ham:", resources["ham"], "slice(s)")
    print("Cheese:", resources["cheese"], "pound(s)")

while True:
    choice = input("What would you like? (small/ medium/ large/ off/ report): ")
    if choice == "off":
        break
    elif choice == "report":
        report(resources)
    elif choice in recipes:
        if check_resources(choice, resources, recipes):
            print("Please insert coins.")
            coins = process_coins()
            value = coins["large_dollar"] + coins["half_dollar"]*0.5 + coins["quarter"]*0.25 + coins["nickel"]*0.05
            if value >= recipes[choice]["cost"]:
                change = value - recipes[choice]["cost"]
                if change > 0:
                    print(f"Here is ${change:.2f} in change.")
                make_sandwich(choice, resources, recipes)
            else:
                print("Sorry, that's not enough money. Money refund")
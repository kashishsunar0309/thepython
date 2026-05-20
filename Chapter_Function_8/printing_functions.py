def print_models(unprinted_designs,complete_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing Model : {current_design}")
        complete_models.append(current_design)
def show_complete_models(complete_models):
    print("\n The following models have been printed: ")
    for model in complete_models:
        print(model)
        
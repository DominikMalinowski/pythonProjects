from printing_functions import print_models,show_completed_model 

#Rozpoczynamy od pewnych projektów, które mają być wydrukowane
unprinted_designs = ['etiu telefonu', 'robot pendant', 'dwunastościan']
completed_models = [] 
#Symulujemy wydruk poszczególnych projektów, dopóki pozosatał jakikolwiek projekt na 
#liscie. Kazdy wydrukowany model zostaje przeniesiony na liste completed_modules 

#while unprinted_designs:
#    current_design = unprinted_designs.pop()
#    print(f"Wydrukuj modelu: {current_design}")
#    completed_models.append(current_design)

#Wyświetlenie wszystkich wydrukowanych modeli 
#print("\nWydrukowane zostały nastepujace modele:")
#for completed_models in completed_models: 
#    print(completed_models) 


print_models(unprinted_designs, completed_models)
show_completed_model(completed_models)

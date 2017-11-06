def make_car(manufacturer,model_name,**args):
    car = {}
    car['muufacturer'] = manufacturer
    car['model_name'] = model_name
    for key,val in args.items():
        car[key] = val
    return car
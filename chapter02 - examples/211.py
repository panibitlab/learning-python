l = [{"city": "shiraz", "pop":1.57, "area": 240},
     {"city": "isfahan", "pop":1.96, "area": 551},
     {"city": "ahvaz", "pop":1.18, "area": 185},
     {"city": "tabriz", "pop":1.60, "area": 324},
     {"city": "mashhad", "pop":3.00, "area": 328}]

max_pop = 0
max_area = 0
min_area = 1e12

for d in l:
    if d["pop"] > max_pop:
        max_pop = d["pop"]
        max_pop_city = d["city"]
    if d["area"] > max_area:
        max_area = d["area"]
        max_area_city = d["city"]
    if d["area"] < min_area:
        min_area = d["area"]
        min_area_city = d["city"]

print(f'max poulation -> {max_pop_city} : {max_pop}')
print(f"max area ->  {max_area_city} : {max_area}")
print(f"min area -> {min_area_city} : {min_area}")
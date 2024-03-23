#5.	Используйте функцию zip() чтобы преобразовать код:

name_hero = [
    'Hulk',
    'Mr. Fantastic',
    'Invisible Woman',
    'Doctor Strange',
    'Doctor Octopus',
    'Spider-Man',
]

name_real = [
    'Bruce Banner',
    'Reed Richards',
    'Sue Storm',
    'Stephen Strange',
    'Otto Octavius',
    'Peter Parker',
]
f = (list(zip(name_hero, name_real)))
for name, hero in f:
    print(f"{name} - {hero}")


import config_reader as cr

configuration = cr.load()
print(configuration)
print(configuration[0])
print('Od poprzedniego napisu dzieli mnie pusta linia :(')
print(configuration[0].strip('\n'))
print('Od poprzedniego napisu nie dzieli mnie juz pusta linia')
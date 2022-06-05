import shelve

with shelve.open('shelve_test') as cars:
    cars['opel'] = 'Germany'
    cars['ford'] = 'USA'
    cars['mazda'] = 'Japan'
    cars['renault'] = 'France'
    # cars['ope'] = 'Germany'

    # print(cars['ford'])
    # print(cars['renault'])
    # print(cars.get('ope'))
    # print(cars['mazda'])
    #
    # # del cars['ope']
    #
    # cars['kia'] = 'South Korea'
    #
    # for key in cars:
    #     print(key + ': ' + cars[key])

    while True:
        key = input('Please enter car name: ')
        if key == 'quit':
            break
        if key in cars:
            country = cars[key]
            print(country)

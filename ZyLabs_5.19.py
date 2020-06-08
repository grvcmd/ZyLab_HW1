# output automotive services and their corresponding costs
print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')

services = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12, '-': 0}


# prompt user to choose two services
first_service = input('\n'+'Select first service:' + '\n')
second_service = input('Select second service:' + '\n')


# output an invoice for the selected services
print('\n' + "Davy's auto shop invoice" + '\n')
if first_service in services and first_service != '-':
    print('Service 1:', first_service + ',', '$' + str(services[first_service]))
elif first_service == '-':
    print('Service 1: No service')
if second_service in services and second_service != '-':
    print('Service 2:', second_service + ',', '$' + str(services[second_service]))
elif second_service == '-':
    print('Service 2: No service')


total = (services[first_service] + services[second_service])
print('\n' + 'Total:', '$' + str(total))


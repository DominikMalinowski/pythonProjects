
#providing number function
def provide_number():   

    num=float(input('Provide number:'))
    #checking if num is 0
    if num==0:
        raise Exception('it is not possible to divide by 0')
    # if not 0
    else:
        print('Division result is ' + str(10.0/num))

#while num is not proper number
while True:
    try:
        provide_number()
        break
    except Exception as err:
        print('An exception happened: ' + str(err))


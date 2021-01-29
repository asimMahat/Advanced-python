import time
 
def calprod():
    #calculating the product of first 1000 number
    product=1
    for i in range(1,10000):
        product=product * i

    return product

starttime=time.time()
prod=calprod()
endtime=time.time()

print("The lenght of digit is %s." % (len(str(prod))))
print("The actual value is %s" % prod)
print("It took %s to calculate." % (endtime-starttime))


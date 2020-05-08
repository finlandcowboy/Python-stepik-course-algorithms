items_count, capacity = map(int, input().split())
products = []

for i in range(1,items_count+1):
    x,y = map(int, input().split())   
    products.append([x,y])

products.sort(key = lambda i : i[0]/i[1], reverse = True)
print(products)

    

def klast(capacity,products):
    full_price = 0 
    
    for price,weight in products:
        if weight < capacity:
            full_price += price
            capacity -= weight
        else:
            full_price += price / weight * capacity
            break
        
    return float("{:.3f}".format(full_price))


print(klast(capacity,products))

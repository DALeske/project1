# https://www.101computing.net/the-egg-farmer-puzzle/

eggs = int(input("How many eggs did you pick up this morning?"))
c12 = eggs//12
c6 = int((eggs%12)/6) # divide the remainer of 12 by 6
eat = eggs-12*c12 - 6*c6
print("You will need", c12, "big cartons,",c6,"little cartons, and can eat",eat,"egg(s) this for breakfast")
#Task 2: Bank Interest If you have a savings account with a particular initial amount and a fixed yearly interest rate, 
# calculate the total amount in your account after a year. 
# So if you had $10,000 at a 7% interest write code that would tell us the amount at the end of the year. 
# For the example the expected outcome would be $10,700.
#geeks for geeks simple interest formula si = p * r * t
#p - principal t is time and r is rate

p = 10000
r = 7
t = 1

simple_interest = (p * r * t)/100

print(simple_interest)
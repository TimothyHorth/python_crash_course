# Lists are specified by using square brackets []
# Individual elements inside a list are separate by commas

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())

# Index positions start at 0, not 1

print(bicycles[3].title())

# To access the last item in a list, use -1 as the index

print(bicycles[-1].title())

message = f'My first bicycle was a {bicycles[0].title()}.'
print(message)

# Activity code is included below. Pg. 36.

friends = ['Cole', 'Michael', 'Connor', 'Stephen']
print(f'Hello, {friends[0].title()}!')
print(f'Hello, {friends[1].title()}!')
print(f'Hello, {friends[2].title()}!')
print(f'Hello, {friends[3].title()}!')

import sys

# parameters
num_grocery = 2		# how many stores to be counted as grocery_store
discount_grocery = 0.85	# credit card grocery cash back
share_rate = [0.5, 0.5]	# a matrix of share rates for each individual (can be more than 2)

# Welcome
print "Welcome to little expense share calculator!"
print '---'
print '[Config] num_grocery =', num_grocery, ', discount_grocery =', discount_grocery

# input sanitizing
if (len(sys.argv) < 2):
	print 'Input error: please enter cost from at least 1 store.'
	quit()
costs = [float(i) for i in sys.argv[1:]]
for cost in costs:
	if cost < 0:
		# negative cost allowed for refund/coupon
		print '[Warning] Entered a negative cost.'

# compute
total = 0.0
count = 0
for cost in costs:
	if count < num_grocery:
		cost *= discount_grocery
	total += cost
	print "Entry", count, ": cost =", "%.2f" % costs[count], ", discounted_cost =", "%.2f" % cost, ", Grocery" if (count < 2) else ", NOT Grocery"
	count += 1

# formatted output
print "total =", total
print "---"
shares = [i * total for i in share_rate]
shares_formatted = ['%.2f' % share for share in shares]
print "Shares: ", shares_formatted

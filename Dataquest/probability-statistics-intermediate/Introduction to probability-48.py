## 1. Probability basics ##

# Print the first two rows of the data.
print(flags[:2])

most_bars_country = flags["name"].iloc[flags["bars"].idxmax()]
highest_population_country = flags["name"].iloc[flags["population"].idxmax()]

## 2. Calculating probability ##

total_countries = flags.shape[0]

orange_probability = flags.orange.sum()/flags.shape[0]
stripe_probability = sum(flags.stripes.values > 1)/flags.shape[0]

## 3. Conjunctive probabilities ##

ten_heads = .5 ** 10
hundred_heads = .5 ** 100

## 4. Dependent probabilities ##

# Remember that whether a flag has red in it or not is in the `red` column.total_count = flags.shape[0]
total_count = flags.shape[0]
red_count = flags[flags["red"] == 1].shape[0]
one_red = (red_count / total_count) 
two_red = one_red * ((red_count - 1) / (total_count - 1))
three_red = two_red * ((red_count - 2) / (total_count - 2))

## 5. Disjunctive probability ##

start = 1
end = 18000

a = np.arange(18000) + 1       
hundred_prob =sum(np.where(a%100 ==0,1,0))/len(a)
seventy_prob = sum(np.where(a%70 ==0,1,0))/len(a)

## 6. Disjunctive dependent probabilities ##

stripes_or_bars = None
red_or_orange = None
red = flags[flags["red"] == 1].shape[0] / flags.shape[0]
orange = flags[flags["orange"] == 1].shape[0] / flags.shape[0]
red_and_orange = flags[(flags["red"] == 1) & (flags["orange"] == 1)].shape[0] / flags.shape[0]

red_or_orange = red + orange - red_and_orange

stripes = flags[flags["stripes"] > 0].shape[0] / flags.shape[0]
bars = flags[flags["bars"] > 0].shape[0] / flags.shape[0]
stripes_and_bars = flags[(flags["stripes"] > 0) & (flags["bars"] > 0)].shape[0] / flags.shape[0]

stripes_or_bars = stripes + bars - stripes_and_bars

## 7. Disjunctive probabilities with multiple conditions ##

heads_or = None

all_h = 0.5*0.5*0.5
heads_or = 1 - all_h

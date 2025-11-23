#
import pandas

mydataset = {"cars": ["BMW", "Volvo", "Ford"], "passings": [3, 7, 2]}
myvar = pandas.DataFrame(mydataset)
print(myvar)


#
import pandas as pd

mydataset = {"cars": ["BMW", "Volvo", "Ford"], "passings": [3, 7, 2]}
myvar = pd.DataFrame(mydataset)
print(myvar)


#
import pandas as pd

a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)


#
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

import numpy as np
import pandas as pd
np.random.seed(0)
# transactions
left = pd.DataFrame({'transaction_id': ['A', 'B', 'C', 'D'], 
                    'user_id': ['Peter', 'John', 'John', 'Anna'],
                    'value': np.random.randn(4),
                   })
# users
right = pd.DataFrame({'user_id': ['Paul', 'Mary', 'John', 'Anna'],
                     'favorite_color': ['blue', 'blue', 'red', 
                                        np.NaN],
                    })

left=left.merge(right,on='user_id',how='left')
print(left)
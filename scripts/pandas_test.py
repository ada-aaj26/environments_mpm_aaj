from envtest import pandas_test

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(6, 6), columns=list("ABCDEF"))

print(pandas_test(df))

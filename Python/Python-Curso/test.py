import pandas as pd
import numpy as np
def main():
    xx1 = np.random.normal(400,30,1000)
    xx2 = np.random.normal(500,30,1000)
    df = pd.DataFrame()
    df['amostra_1'] = xx1
    df['amostra_2'] = xx2
    df.to_csv('resultado.csv',index=False)


if __name__ == "__main__":
    main()

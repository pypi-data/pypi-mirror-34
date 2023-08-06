#사용조건 
#import pandas as pd
#import numpy as np
#from fancyimpute import KNN
import pandas as pd
import numpy as np
from fancyimpute import KNN

class KnnImpute7:
    def __init__(self, df):
        self.df_origin = df
        self.sample_base = pd.DataFrame({})
        self.target_base = pd.DataFrame({})
        self.target_column = []
        self.env_columns = []
        self.all_column = []
        self.num_na = pd.DataFrame({})
        self.sample_size = 0
        self.result_df = pd.DataFrame({})
        self.sample_origin= pd.DataFrame({})
    
    def test(self):
        self.num_na = self.df_origin[self.all_column].isna().sum(1).value_counts()
        self.num_na.index.name='Na_count'
        print('한 행 전체 데이터가 모두 NA라면 사용 불가, 현재 데이터에서 Na_count가 %d개 이상인 데이터 포인트가 있다면, 거리계산을 위해 컬럼을 늘려서 해결해보도록' % len(self.all_column))
        return self.num_na
    
    def make(self, all_column, sample_size):
        self.sample_size= sample_size
        if type(all_column) !=list:
            print("all_column should be list-like object")
            return 0
        self.all_column = all_column
       
        df_new = self.df_origin.loc[:, self.all_column]
        self.sample_origin = df_new.loc[df_new.isna().sum(1)==0,:]
        self.sample_base = self.sample_origin.sample(sample_size)
        self.target_base = df_new.loc[df_new.isna().sum(1)!=0, :]
        print("samplling되는 데이터포인트 %d개 \nna값을 계산해야할 타겟 데이터 포인트 %d개" % (len(self.sample_base), len(self.target_base)))
        
    
    def action(self, num, k = 3): #num : na값이 있는 행에서 한번에 처리할  행의 개수
        knn_action = KNN(k)
        total = np.floor(len(self.target_base)/num)
        rest_roop = len(self.target_base)%num
        flag = num
        for i in np.arange(0, total+1):
            if total==i and rest_roop == 0:
                break
            elif total == i:
                flag = rest_roop
        
            #temp_index  = self.target_base.index[int(num*i):int(num*(i+1))]
            #self.temp_index = temp_index
            print(i,'번째 루프')
            temp_samp_targ = pd.concat([self.target_base.iloc[int(num*i):int(num*i)+flag*1], self.sample_origin.sample(self.sample_size)])
            print(i,'번째 루프')
            temp_na_filled_df = pd.DataFrame(knn_action.complete(temp_samp_targ))
            temp_na_filled_df.columns = self.all_column
            print(i,'번째 루프')
            self.temp_na_filled_df = temp_na_filled_df
            self.result_df = pd.concat([self.result_df, temp_na_filled_df.iloc[0:flag]])
            print(i,'번째 루프')
        self.result_df.index = self.target_base.index  #na처리한 행들만의 index
    
    def finish(self):
        self.return_result = pd.concat([a.df_origin.loc[:, list(set(a.df_origin.columns) - set(a.all_column))], pd.concat([a.sample_origin, a.result_df]).sort_index()], axis=1)
        #pd.concat([a.df_origin.loc[:, list(set(a.df_origin.columns) - set(a.all_column))], a.result_df])
        #self.df_origin.loc[:, set(self.df_origin.columns) - set(self)]
        #pd.concat([self.result_df, self.sample_origin ]).sort_index()
        
    def show_result(self):
        return self.return_result
        
    def make2(self, target_columns, env_columns):
        if type(target_column) !=list or type(env_columns) != list:
            print("fit_column and env_columns should be list-like object")
            return 0
        self.target_column = target_column
        self.env_columns = env_columns
        self.all_column = self.target_column + self.env_columns
       
        df_new = self.df_origin.loc[:, self.all_column]
        self.sample_base = df_new.loc[df_new.isna().sum(1)==0,:].sample(100)
        self.target_base
        pass
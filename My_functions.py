def details(*args):
    '''
    Generate descriptive statistics.
    Analyzes both numeric and object type data of dataframe for each columns.
    Returns following data for each column of provided dataframe
    1. Counts	
    2. Missing	
    3. Missing percent	
    4. Unique	
    5. Dtype	
    6. Mode	
    7. Min	
    8. Max	
    9. Mean	
    10. Median	
    11. 25%	
    12. 50%	
    13. 75%	
    13. Std
    
    Modules require :
    ----------
    pandas
    IPython

    Parameters
    ----------
    *args : Dataframe

    Returns
    -------
    DataFrame
        Summary statistics of the Dataframe provided.

    '''
    from IPython.display import display
    import pandas as pd
    for i in range(0,len(args)):
        x = args[i]
        op = pd.DataFrame(columns=['Counts','Missing', 'Missing percent','Unique','Dtype','Mode','Min','Max','Mean','Median',
                                  '25%', '50%', '75%', 'Std'])
        
        for c in x.columns:
            if pd.api.types.is_numeric_dtype(x[c]):
                op.loc[c] = [x[c].count(), x[c].isna().sum(), (x[c].isna().sum()/len(x))*100, x[c].nunique(), x[c].dtype,
                              x[c].mode().values[0], x[c].min(),x[c].max(), x[c].mean(), x[c].median(), x[c].quantile(0.25),
                              x[c].quantile(0.50), x[c].quantile(0.75), x[c].std()]
            else:
                op.loc[c] = [x[c].count(), x[c].isna().sum(), (x[c].isna().sum()/len(x))*100, x[c].nunique(), x[c].dtype,
                              x[c].mode().values[0],'-','-','-','-','-','-','-','-']
        display(op)
        print('  ')








def cat(df, uni, tar=None):
        
    '''
    Plot seaborn countplot for all catergorical variable with count and percent
    
    Modules require :
    ----------
    pandas
    seaborn
    matplotlib

    Parameters
    ----------
    df : Dataframe
    uni : int
        Threashold value of unique values for column consider as categorical variable.
    tar : taget column use as hue in plot
    
    Returns
    -------
    Counplot
        Visualise analysis of categorical variable.

    '''
    
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    plt.rcParams['figure.figsize'] = (13,7)
    
    df1 = df.copy()
    
    for c in df.columns:
        if pd.api.types.is_numeric_dtype(df[c]):
            continue
        else:
            df = df.drop(c, axis=1)
    if tar:
        df = df.drop(tar, axis=1)
    
    for i in df.columns:
        total = int(len(df[i]))
        if df[i].nunique() <= uni:
            if tar:
                ax = sns.countplot(df[i], hue=df1[tar])
                plt.title(f'Data provided for {i} in counts\n', fontsize=18)
                
                txt2 = ''
                if '_label' in tar:
                    for l in range(0,(df1[tar].nunique())):
                        l1 = str(df1[tar].value_counts().index).split('[')[-1].split(']')[0]
                        l2 = str(df1[tar.split('_l')[0]].value_counts().index).split('[')[-1].split(']')[0]
                        txt2 +=l1.split(',')[l] +' : '+l2.split(',')[l] + '\n'

                plt.legend(bbox_to_anchor=(0, -0.05), loc=2, fontsize=14, ncol=df1[tar].nunique(), 
                           title=txt2, title_fontsize=14)
                
                txt = 'Values for ' + str(i) + ' in counts'+'\n\n'
                txt += str(df[i].value_counts()) + '\n\n'

                if '_label' in i :
                    c = i.split('_l')[:-1]
                    txt += str(df1[c].value_counts()) + '\n'

                ax.figure.text(0.92,0.88, txt, ha='left', va='top', fontsize=16, transform=plt.gcf().transFigure)

                for p in ax.patches:
                    txt = str(p.get_height())+'\n'
                    ax.set(xlabel=i, ylabel='Counts')
                    ax.text(p.get_x()+p.get_width()/2, p.get_height(), txt, fontsize=14, ha='center')
                plt.show()


                ax = sns.countplot(df[i], hue=df1[tar])
                plt.title(f'Data provided for {i} in percent\n', fontsize=18)

                txt2 = ''
                if '_label' in tar:
                    for l in range(0,(tn[tar].nunique())):
                        l1 = str(df1[tar].value_counts().index).split('[')[-1].split(']')[0]
                        l2 = str(df1[tar.split('_l')[0]].value_counts().index).split('[')[-1].split(']')[0]
                        txt2 +=l1.split(',')[l] +' : '+l2.split(',')[l] + '\n'

                plt.legend(bbox_to_anchor=(0, -0.1), loc=2, fontsize=14, ncol=df1[tar].nunique(), 
                           title=txt2, title_fontsize=14)
                
                txt = 'Values for ' + str(i) + ' in %'+'\n'
                txt += str(df[i].value_counts(normalize=True)*100) + '\n\n'

                if '_label' in i :
                    c = i.split('_l')[:-1]
                    txt += str(df1[c].value_counts(normalize=True)*100) + '\n'

                ax.figure.text(0.92,0.88, txt, ha='left', va='top', fontsize=16, transform=plt.gcf().transFigure)

                for p in ax.patches:
                    txt = str(round((p.get_height()/total)*100, 2)) + '\n'
                    ax.set(xlabel=i, ylabel='Counts')
                    ax.text(p.get_x()+p.get_width()/2, p.get_height(), txt, fontsize=14, ha='center')
                plt.show()
                
            else:
                
                ax = sns.countplot(df[i])
                plt.title(f'Data provided for {i} in counts\n', fontsize=18)

                txt = 'Values for ' + str(i) + ' in counts'+'\n\n'
                txt += str(df[i].value_counts()) + '\n\n'

                if '_label' in i :
                    c = i.split('_l')[:-1]
                    txt += str(df1[c].value_counts()) + '\n'

                ax.figure.text(0.92,0.88, txt, ha='left', va='top', fontsize=16, transform=plt.gcf().transFigure)

                for p in ax.patches:
                    txt = str(p.get_height())+'\n'
                    ax.set(xlabel=i, ylabel='Counts')
                    ax.text(p.get_x()+p.get_width()/2, p.get_height(), txt, fontsize=14, ha='center')
                plt.show()


                ax = sns.countplot(df[i])
                plt.title(f'Data provided for {i} in percent\n', fontsize=18)

                txt = 'Values for ' + str(i) + ' in %'+'\n'
                txt += str(df[i].value_counts(normalize=True)*100) + '\n\n'

                if '_label' in i :
                    c = i.split('_l')[:-1]
                    txt += str(df1[c].value_counts(normalize=True)*100) + '\n'

                ax.figure.text(0.92,0.88, txt, ha='left', va='top', fontsize=16, transform=plt.gcf().transFigure)

                for p in ax.patches:
                    txt = str(round((p.get_height()/total)*100, 2)) + '\n'
                    ax.set(xlabel=i, ylabel='Counts')
                    ax.text(p.get_x()+p.get_width()/2, p.get_height(), txt, fontsize=14, ha='center')
                plt.show()


    









def num(df, uni):
    
    '''
    Plot seaborn Distribution and Boxplot for all numerical variable
    
    Modules require :
    ----------
    pandas
    seaborn
    matplotlib
    scipy

    Parameters
    ----------
    df : Dataframe
    uni : int
        Threashold value of unique values for column consider as numerical variable.

    Returns
    -------
    Distribution and Boxplot
        Visualise analysis of numerical variable.

    '''
        
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    from scipy.stats import norm
    
    
    df1 = df.copy()
    
    for c in df.columns:
        if pd.api.types.is_numeric_dtype(df[c]):
            continue
        else:
            df = df.drop(c, axis=1)
    
    for i in df.columns:
        if df[i].nunique() > uni:
            plt.figure(figsize=(13,7))
            ax = sns.distplot(df[i], fit=norm)
            plt.title(f'\nDistribution for {i} column\n', fontsize=18)
            
            txt ='Standard Deviation :' + str(round(df[i].std(), 2)) + '\n\n'
            txt += 'Skewness : ' + str(round(df[i].skew(), 2)) + '\n\n'
            txt += 'Kurtosis : ' + str(round(df[i].kurt(), 2)) + '\n\n' 
            
            ax.figure.text(0.92,0.87, txt, ha='left', va='top', fontsize=16, transform=plt.gcf().transFigure)
            plt.show()

            plt.figure(figsize=(13,7))
            ax = sns.boxplot(df[i])
            plt.title(f'\nBoxplot for {i} column\n', fontsize=18)

            ot = []
            for x in df[i]:
                z = ((x-df[i].mean())/df[i].std())
                if np.abs(z) > 3:
                    ot.append(x)
            
            uw = (df[i].quantile(0.75)) + (1.5*(df[i].quantile(0.75)-df[i].quantile(0.25)))
            lw = (df[i].quantile(0.25)) - (1.5*(df[i].quantile(0.75)-df[i].quantile(0.25)))
            
            txt = 'mean : ' + str(round(df[i].mean(), 3)) +'\n\n'+ 'min : ' + str(df[i].min()) +'\n\n'
            txt+= 'max : ' + str(df[i].max()) +'\n\n'+ '25% : ' + str(df[i].quantile(0.25)) +'\n\n'
            txt+= '50% : ' + str(df[i].quantile(0.5)) +'\n\n'+ '75% : ' + str(df[i].quantile(0.75)) +'\n\n'
            txt+= 'Z outliers : '+str(len(ot))+'\n\n'+'upper whisker : '+str(round(uw,3))+'\n\n'+'lower whisker : '+str(round(lw,3))
            
            ax.figure.text(0.92,0.87, txt, ha='left', va='top', fontsize=16, transform=plt.gcf().transFigure)
            plt.show()

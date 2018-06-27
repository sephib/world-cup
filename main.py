from pathlib import Path
import pandas as pd

data_dir ='.'


def read_squad_to_df(l:list):
    print('process Squad')
    df_all = pd.DataFrame()
    for team in l:
        print(team)
        df = pd.read_fwf(team, skiprows=4,
                         names=['num_in_country', 'position', 'name', 'sepe', 'num_in_group', 'team'])
        df['country'] = team.parts[-1].split('-')[1].split('.')[0]
        df_all = pd.concat([df_all, df])
    df_all['year'] = l[0].parts[0].split('--')[0]
    return df_all


def main():
    df_all = pd.DataFrame()
    df = pd.DataFrame()
    l = []
    for i in Path(data_dir).rglob('*.txt'):
        l.append(i)
        if len(l) > 1:
            if l[-2].parent != l[-1].parent:
                j = l.pop()
                if 'squads' in l[0].parts:
                    # print(f'process: {l}')
                    df = read_squad_to_df(l)
                l = []
                l.append(j)
                if not df.empty:
                    df_all = pd.concat([df_all, df])
                    df = pd.DataFrame()
            else:
                pass
    print(f'len {df_all.shape}')
    print(f'{df_all.info()}')
    print(f'{df_all.head()}')
    df_all.to_csv('df_all.csv', index = False)



if __name__ == '__main__':
    main()

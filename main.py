from pathlib import Path
import pandas as pd

data_dir ='.'


def main():
    df_all = pd.DataFrame()
    df = pd.DataFrame()
    l = []
    for i in Path(data_dir).rglob('*.txt'):
        l.append(i)
        if len(l) > 1:
            if l[-2].parent != l[-1].parent:
                j = l.pop()
                print(f'process: {l}')
                if 'squads' in l[0].parts:
                    print('process Squad')
                    df = pd.read_fwf(l[0], skiprows=4,
                                     names=['num_in_country', 'position', 'name', 'sepe', 'num_in_group', 'team'])
                    df['country'] = l[0].parts[-1].split('-')[1].split('.')[0]
                print(f'--------------')
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
    df_all.to_csv('df_all.csv')



if __name__ == '__main__':
    main()

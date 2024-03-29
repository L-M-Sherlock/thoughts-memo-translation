from pathlib import Path

import pandas as pd
import os

if __name__ == '__main__':

    need_source = False

    trans_dir = Path('../utf8/')
    try:
        trans_dir.remove('.DS_Store')
    except:
        pass

    for path, _, files in os.walk(trans_dir):
        try:
            files.remove('.DS_Store')
        except:
            pass
        for file in files:
            print(file)
            try:
                text = pd.read_csv(os.path.join(path, file), header=None, index_col=0)
                text.columns = ['source', 'target']
                text.dropna(inplace=True)
            except:
                continue
            if 'link' in text.index or -1 in text.index:
                index = list(text.index)
                flag = 'link' if 'link' in text.index else -1
                index.remove(flag)
                text = text.reindex([index[0], flag] + index[1:])
            if file.find('.md') == -1:
                file = file.replace('.csv', '.md.csv')
            Path(f'./{path[7:]}').mkdir(parents=True, exist_ok=True)
            with open(f'./{path[7:]}/{file[:-4]}', 'w', encoding='utf-8') as f:
                if need_source:
                    for i in range(len(text['source'].values)):
                        f.write(text['source'].values[i] + '\n\n')
                        f.write(text['target'].values[i] + '\n\n')
                else:
                    f.writelines('\n\n'.join(text['target'].values))

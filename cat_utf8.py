from pathlib import Path
import pandas as pd
import os
import re

def clean_filename(filename):
    clean_name = re.sub(r'[^a-zA-Z0-9. ]', '', filename)
    return clean_name

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

        # Add an empty intro.md file to each directory
        intro_file = Path(f'./src/{path[7:]}/intro.md')
        intro_file.parent.mkdir(parents=True, exist_ok=True)
        intro_file.touch()

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
            Path(f'./src/{path[7:]}').mkdir(parents=True, exist_ok=True)
            with open(f'./src/{path[7:]}/{clean_filename(file[:-4])}', 'w', encoding='utf-8') as f:
                if need_source:
                    for src, tgt in zip(text['source'], text['target']):
                        f.write(src + '\n\n')
                        f.write(tgt + '\n\n')
                else:
                    f.writelines('\n\n'.join(text['target'].values))

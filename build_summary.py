import os

def get_markdown_files(directory):
    markdown_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md') and file != 'SUMMARY.md':
                markdown_files.append(os.path.join(root, file))
                print(f"Found markdown file: {file}")
    return markdown_files

def get_title(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('# '):
                return line.strip('# ').strip()
    return os.path.basename(file_path)

def create_summary(markdown_files):
    summary = "# Summary\n\n"
    current_dir = os.path.abspath('./src')
    dir_structure = {}

    # 构建目录结构
    for file in sorted(markdown_files):
        relative_path = os.path.relpath(file, current_dir)
        parts = relative_path.split(os.sep)
        current = dir_structure
        for part in parts[:-1]:
            if part not in current:
                current[part] = {}
            current = current[part]
        current[parts[-1]] = file

    # 递归生成摘要
    def write_summary(structure, indent=""):
        nonlocal summary
        for key, value in structure.items():
            if isinstance(value, dict):
                # 这是一个目录
                intro_path = os.path.relpath(value["intro.md"], current_dir).replace(" ", "%20")
                summary += f"{indent}* [{key}]({intro_path})\n"
                write_summary(value, indent + "  ")
            else:
                # 这是一个文件
                title = get_title(value)
                if title == 'intro.md':
                    continue
                encoded_path = os.path.relpath(value, current_dir).replace(" ", "%20")
                summary += f"{indent}* [{title}]({encoded_path})\n"

    write_summary(dir_structure)
    return summary

def main():
    current_directory = './src'
    markdown_files = get_markdown_files(current_directory)
    summary_content = create_summary(markdown_files)
    
    with open('./src/SUMMARY.md', 'w', encoding='utf-8') as f:
        f.write(summary_content)
    
    print("SUMMARY.md has been created successfully.")

if __name__ == "__main__":
    main()
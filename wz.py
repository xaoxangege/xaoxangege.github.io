import requests
from github import Github

# GitHub API Token
GITHUB_TOKEN = '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'
REPO_NAME = 'xaoxangege.github.io'
FILE_PATH = 'index.html'  # 上传的文件路径为根目录

# 生成 index.html 的 HTML 内容
def generate_html_content():
    # 这里根据账单数据生成 HTML 内容
    html_content = """
    <html>
    <head>
        <title>账单记录</title>
    </head>
    <body>
        <h1>账单记录</h1>
        <table>
            <tr><th>时间</th><th>金额</th><th>用户名</th></tr>
            <!-- 数据插入位置 -->
        </table>
    </body>
    </html>
    """
    return html_content

# 上传 HTML 到 GitHub
def upload_to_github():
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(REPO_NAME)

    try:
        # 获取文件内容
        file = repo.get_contents(FILE_PATH)
        current_content = file.decoded_content.decode('utf-8')
        
        # 如果内容变化则更新文件
        new_content = generate_html_content()
        if current_content != new_content:
            repo.update_file(FILE_PATH, "Updated index.html", new_content, file.sha)
            print("HTML 文件已上传到 GitHub")
        else:
            print("HTML 文件没有变化，不需要上传")
    except:
        # 如果文件不存在则创建
        new_content = generate_html_content()
        repo.create_file(FILE_PATH, "Created index.html", new_content)
        print("HTML 文件已上传到 GitHub")

# 执行上传操作
upload_to_github()

import gitlab
import requests
import config


gl = gitlab.Gitlab(config.gitlab_host, private_token=config.access_token)


def get_input(hint, default) -> str:
    val = input(hint + ' (' + default + '): ')
    if val == '':
        return default
    return val


def merge():
    project_name = get_input('请输入项目名称', config.project_name)
    try:
        project = gl.projects.get(project_name)
    except requests.exceptions.ConnectionError:
        print('连接代码仓库失败，请检查 config.py 配置是否正确.')
        exit(0)
    except gitlab.GitlabGetError:
        print('项目获取失败，请检查项目名称是否正确.')
        exit(0)
    except Exception as e:
        print(e)
        exit(0)

    # print(project.id)
    print('获取项目成功')

    current_branch = get_input('请输入来源分支', config.current_branch)
    target_branch = get_input('请输入目标分支', config.target_branch)
    title = input('请输入合并标题: ')

    print("正在合并：{0} 的 {1} 分支 到 {2} 分支...\r\n".format(project_name, current_branch, target_branch))

    try:
        # 合并请求
        mr = project.mergerequests.create({'source_branch': current_branch,
                                           'target_branch': target_branch,
                                           'title': title})
        # 接受合并请求
        mr.merge()
        print("合并结束...\r\n")
    except gitlab.GitlabOperationError:
        print("合并出错，请登陆代码仓库合并。 " + config.gitlab_host + "\r\n")


if __name__ == '__main__':
    print('开始执行 ' + config.gitlab_host + ' 上的分支合并..')
    merge()

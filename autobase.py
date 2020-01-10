import git

sylixosGitCfg = {
    'sylixos-base': {
            'gitUrl': 'git://sylixos.com/sylixos-base.git', 
            'filePath': '/home/pi/autobase/basefile'
    },
    'libsylixos': {
            'gitUrl': 'git://sylixos.com/libsylixos.git',
            'filePath': '/home/pi/autobase/basefile/libsylixos'
    }  
}

# 克隆仓库

def gitRepoClone(url, filePath):
    print('Now clone: ', url)
    repo = git.Repo.clone_from(url, filePath)
    # 查看repo状态
    print ('finish clone, status id :', repo.git.status())   # 返回通常的status几句信息
    #print (repo.is_dirty())    # 返回是否有改动（包括未add和未commit的）  

def main():
    for  repoName, info in sylixosGitCfg.items():
            gitRepoClone(info['gitUrl'], info['filePath'])

if __name__ == "__main__":
    main()

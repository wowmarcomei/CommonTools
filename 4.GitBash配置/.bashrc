export PS1='\[\e]0;laomei@mylaptop \w\a\]\nlaomei@mylaptop \[\e[33m\]\w\[\e[0m\]\n⎈ ➔  '
export LANG=en_US.UTF-8    #配置中文编码
export LC_ALL=en_US.UTF-8  #配置中文编码
alias l.='ls -d .* --color=auto' #修改其他快捷键，如ls -d
cd /d/Workstation # 默认进入到/d/workstation目录

# 设置 cd 命令默认回到自定义目录  /d/workstation
cd() {
    builtin cd "$@" || return
    if [ $# -eq 0 ]; then
        builtin cd /d/Workstation
    fi
}
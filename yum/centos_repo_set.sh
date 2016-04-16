#!/bin/sh

REPO_FILE=$1
GPG_KEY_FILE=RPM-GPG-KEY-CentOS-7

if [ x$1 == x ]; then
	REPO_FILE=CentOS-Base.repo
fi

rpm --import $GPG_KEY_FILE

if [ ! -f /etc/yum.repos.d/CentOS-Base.repo.bak ]; then
	mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak
fi

cp $REPO_FILE /etc/yum.repos.d/CentOS-Base.repo

yum clean all
yum makecache
echo '恭喜!yum源配置成功!'

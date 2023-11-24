# kill a process

exec{'pkill':
 command  => 'pkill killmenow',
 onlyif   => 'ps -ef | grep killmenow | grep -v grep',
 provider => 'shell',
}

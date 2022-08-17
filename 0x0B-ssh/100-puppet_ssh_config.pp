#Let’s practice using Puppet to make changes to our configuration file. Just as in the previous configuration file

exec { 'ssh_config':
    path    => '/usr/bin/',
    command => 'cat 2-ssh_config > /etc/ssh/ssh_config'
}
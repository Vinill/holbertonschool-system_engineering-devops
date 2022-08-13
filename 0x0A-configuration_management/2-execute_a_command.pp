#Using Puppet, create a manifest that kills a process named killmenow

exec { 'death to mfckr':
  command => '/usr/bin/pkill -f killmenow',
}
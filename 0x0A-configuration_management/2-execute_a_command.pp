# executes a command using pkill
exec {'kill a command':
  path    => ['/usr/bin'],
  command => 'pkill killmenow'
}

#this installs flask
exec {'Install_Flask':
  command => '/usr/bin/pip3 install Flask==1.0.2',
  path    => ['/usr/bin']
}

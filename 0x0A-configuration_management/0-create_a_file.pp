# Creates a file named 'school' in /tmp with specific ownership and permissions.

file { '/tmp/school':
  ensure  => file,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet',
}

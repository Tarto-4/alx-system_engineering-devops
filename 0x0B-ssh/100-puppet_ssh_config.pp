# Configures SSH client to use a private key and disable password authentication.
file_line { 'Turn off passwd auth':
  path    => '/etc/ssh/ssh_config',
  match   => '^PasswordAuthentication',
  line    => 'PasswordAuthentication no',
  ensure  => present,
  require => File['ssh_config'],
}

file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  match => '^IdentityFile',
  line  => 'IdentityFile ~/.ssh/school',
  ensure => present,
}

file { 'ssh_config':
  path   => '/etc/ssh/ssh_config',
  ensure => file,
}

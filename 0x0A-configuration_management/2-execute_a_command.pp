# Kills the process named 'killmenow'
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin:/bin',   
}

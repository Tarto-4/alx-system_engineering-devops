# This Puppet manifest configures Nginx to handle high concurrent connections by optimizing worker processes and connections.

package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => template('nginx/nginx.conf.erb'),
  require => Package['nginx'],
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  subscribe  => File['/etc/nginx/nginx.conf'],
  require    => File['/etc/nginx/nginx.conf'],
}

# Reload Nginx if the configuration file changes
exec { 'reload-nginx':
  command     => '/etc/init.d/nginx reload',
  refreshonly => true,
  subscribe   => File['/etc/nginx/nginx.conf'],
}

# Nginx configuration template file
file { '/etc/puppet/templates/nginx/nginx.conf.erb':
  ensure  => file,
  content => @("END"),
user  nginx;
worker_processes  auto;
pid        /var/run/nginx.pid;

events {
    worker_connections 1024;
    use epoll;
    multi_accept on;
}

http {
    sendfile        on;
    tcp_nopush      on;
    tcp_nodelay     on;
    keepalive_timeout  65;
    types_hash_max_size 2048;

    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    server {
        listen       80 default_server;
        listen       [::]:80 default_server;
        server_name  _;
        root         /usr/share/nginx/html;

        location / {
            try_files $uri $uri/ =404;
        }

        error_page 500 502 503 504 /50x.html;
        location = /50x.html {
            root /usr/share/nginx/html;
        }
    }
}
"END"
}


# Puppet manifest for setting up web static
  package { 'nginx':
    ensure => installed,
  }
  file { '/data':
    ensure  => 'directory',
  }

  file { '/data/web_static':
    ensure => 'directory',
  }

  file { '/data/web_static/releases':
    ensure => 'directory',
  }

  file { '/data/web_static/releases/test':
    ensure => 'directory',
  }

  file { '/data/web_static/shared':
    ensure => 'directory',
  }
  file { '/data/web_static/releases/test/':
    ensure  => directory,
    mode    => '0755',
    owner   => 'ubuntu',
    group   => 'ubuntu',
    recurse => true,
  }

  file { '/data/web_static/shared/':
    ensure => directory,
    mode   => '0755',
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  file { '/data/web_static/releases/test/index.html':
    ensure  => present,
    content => '<html>
                    <head>
                    </head>
                    <body>
                        Holberton School
                    </body>
                </html>',
    mode    => '0644',
    owner   => 'ubuntu',
    group   => 'ubuntu',
  }

  file { '/data/web_static/current':
    ensure => link,
    target => '/data/web_static/releases/test/',
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  $nginx_config = '/etc/nginx/sites-available/default'
  $search_text = 'location /'
  $line_number = inline_template("<%= @(file(\"${nginx_config}\").split(\"\\n\").index { |line| line.include?(\"${search_text}\") } + 1) %>")
  file_line { 'nginx_hbnb_static':
    path  => $nginx_config,
    line  => "location /hbnb_static {\n
              alias /data/web_static/current;\n
              try_files \$uri \$uri/ =404;\n
              }",
    match => "^\\s*location /",
    after => $line_number,
  }

  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File_line['nginx_hbnb_static'],
  }

#replaces typo string in wp settings file
exec { 'change to php':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-setti\
ngs.php",
  path    => '/bin'
}
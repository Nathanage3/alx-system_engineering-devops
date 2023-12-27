class killmenow {
  exec { 'kill_process':
    command => 'pkill -f killmenow',
    onlyif  => 'pgrep -f killmenow', # Only run if the process is currently running
  }
}

include killmenow

# install package

package{'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package{'Werkzeug':
  ensure   => '2.3.7',
  provider => 'pip3',
}

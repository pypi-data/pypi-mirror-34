0.2.4 2018-08-05
----------------

* Bugfix don't force the ALPN protocols
* Bugfix shutdown on reload
* Bugfix set the default log level if std(out/err) is used
* Bugfix HTTP/1.1 -> HTTP/2 Upgrade requests
* Bugfix correctly handle TERM and INT signals
* Bugix loop usage and creation for multiple workers

0.2.3 2018-07-08
----------------

* Bugfix setting ssl from config files
* Bugfix ensure modules aren't set as config values
* Bugfix use the wsgiref datetime formatter (accurate Date headers).
* Bugfix query_string value ASGI conformance

0.2.2 2018-06-27
----------------

* Bugfix ensure that hypercorn as a command line (entry point) works.

0.2.1 2018-06-26
----------------

* Bugfix ensure CLI defaults don't override configuration settings.

0.2.0 2018-06-24
----------------

* Bugfix correct ASGI extension names & definitions
* Bugfix don't log without a target to log to.
* Bugfix allow SSL values to be loaded from command line args.
* Bugfix avoid error when logging with IPv6 bind.
* Don't send b'', rather no-op for performance.
* Support IPv6 binding.
* Add the ability to load configuration from python or TOML files.
* Unblock on connection close (send becomes a no-op).
* Bugfix send the close message only once.
* Bugfix correct scope client and server values.
* Implement root_path scope via config variable.
* Stop creating event-loops, rather use the default/existing.

0.1.0 2018-06-02
----------------

* Released initial alpha version.

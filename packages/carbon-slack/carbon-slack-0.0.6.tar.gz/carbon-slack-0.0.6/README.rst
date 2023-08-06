Carbon-to-Slack Relay Library for Python
========================================

This library's main purpose is to relay metrics from a Slack channel to a Carbon daemon, for inclusion in a Graphite database. It also contains commands (and classes) used to send and receive metric messages to Carbon.

Configuration
-------------

You can configure this library in two ways:

`/etc/carbon-slack.yml` Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is what the "native" YAML configuration file looks like::

	token: xoxp-1234567890-yadda-yadda # Application token from Slack
	carbon-server: 127.0.0.1
	carbon-port: 2023
	channel: metrics

**NOTE:** You can get a sample of this from the command line using::

	$ carbon-slack-init

Any command provided in this library will expect to load the above configuration, by default using the ``/etc/carbon-slack.yml`` file (but you can also provide the configuration path using the ``--config | -c`` option).

Embedded in Your Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're using Carbon-Slack as a library, you can also load the necessary configuration elements from any ``dict`` using::

	import carbon_slack.config as conf
	config = conf.Config({
		conf.TOKEN: 'here is my Slack API token',
		conf.CHANNEL: 'metrics',
		conf.CARBON_SERVER: '127.0.0.1',
		conf.CARBON_PORT: 2023
	})

This is the same as::

	import carbon_slack.config as conf
	config = conf.Config({
		'token': 'here is my Slack API token',
		'channel': 'metrics',
		'carbon-server': 127.0.0.1,
		'carbon-port': 2023
	})

As you can see, you could initialize this directly from strings in a script, or by reading command line arguments, or from almost anywhere. You could even read in another YAML file that looked something like this::

	my-app-id: 10
	my-username: buildchimp
	relay:
		token: 'here is my Slack API token'
		channel: metrics
		carbon-server: 127.0.0.1
		carbon-port: 2023

Then, use something like the following to initialize your relay::

	import carbon_slack.config as conf
	from carbon_slack.relay import Relay
	import yaml

	with open('/path/to/app.yml') as f:
		data = yaml.safe_load(f)

	relay = Relay(conf.Config(data['relay']))

Sending Manually
----------------

Carbon-Slack provides a command-line client for sending metrics, which can be used like this::

	$ carbon-slack-send test.metric 1234

The command-line version of the sender relies on the standard configuration file (see above), and will use the current time when sending the metric. It can only send one metric at a time currently.

Carbon-Slack also provides a library-based approach, for sending metrics programmatically::

	from carbon_slack.slack import Sender

	sender = Sender(config)
	sender.send_metrics({'test.metric', 1234})

Relaying to Carbon
------------------

Relaying is what Carbon-Slack is designed to do. It uses Slack as a more-or-less public message bus for sending metrics, which means neither the Graphite DB server nor any of the clients need to be exposed to the internet directly by opening holes in your firewalls. Both the client and the relay initiate connections to Slack and interact on a channel using plaintext.

Metric messages in a Slack channel each contain one or more lines of the format::

	metric.name value timestamp-in-seconds

This means you can send a group of metrics in a single message to save on protocol overhead. When the Relay client sees messages in this format, it parses them and sends them on to the Carbon daemon associated with your Graphite DB instance, then deletes the messages from the Slack channel.

Why delete the messages? It helps prevent duplicate processing.

Here's an example of the Relay in action::

	from carbon_slack.relay import Relay

	relay = Relay(config)

	while True:
	    print "Relayed %d metrics" % relay.run()

Of course, the relay is designed to work from the command line as well::

	$ carbon-slack-relay

However, command-line usage will require you to use the normal configuration file format (either in the default location, or via the ``--config | -c`` command-line option).

kafkacli
========
Copyright (c) 2018-2018 Ryan Yuan

[https://github.com/ryanyuan/kafkacli](https://github.com/ryanyuan/kafkacli)

**kafkacli** is a Kafka utility tool that provides the following features:

* **Produce**: reading messages from stdin and producing them to the Kafka cluster with specific topic
* **Consume**: consuming messages from a topic to Kafka cluster and printing them to stdout
* **List**: Listing all existing the topics within the Kafka cluster


# Install

On Mac OS X, please refer to [https://github.com/ryanyuan/homebrew-tap](https://github.com/ryanyuan/homebrew-tap) for installation using [Homebrew](https://brew.sh/).

or

Using provided bash script to install:

````
sh install.sh
````

# Examples

Produce messages to topic1

    $ kafkacli -m produce -b 123.123.123.123:9092 -t topic1

Subscribe to topic1 and consume messages, with offset mode (earliest or latest. If offset mode is not specified, it uses latest by default.

    $ kafkacli -m consume -b 123.123.123.123:9092 -t topic1 -o earliest

List all the topics

    $ kafkacli -m list -b 123.123.123.123:9092


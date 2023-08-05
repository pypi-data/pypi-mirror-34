# Domain Events
A lightweight library with an implementation of Pub-Sub.

## Install

```
$ pipenv install domain-events
```

or

```
$ pip install domain-events
```

## Usage


In order to have the pub-sub working in your application, you'll need to write your own subscribers and to subscribe them to the publisher.

`domain-events` provides an interface for subscribers that needs to be implemented by your own subscribers in the first place. Two methods are mandatory: `handle(self, event)` and `_events_subscribed_to(self)`. Following is an example of how to do it.

```python

from domain_events import Subscriber


class ExampleSubscriber(Subscriber):

    def handle(self, event):
      #  Logic to handle the occurring event

    def _events_subscribed_to(self):
      """ Return the tuple of events it is subscribed to. """

      return (AnEvent, AnotherEvent)
```

Once the subscriber is implemented, you'll need to subscribe it to the event publisher.

```python

from domain_events import Publisher

Publisher().subscribe(ExampleSubscriber())
```

Now, in order to publish an event, just call the `publish` method on the `Publisher` with one of your domain events.

```python
from domain_events import Event, Publisher


class AnEvent(Event):
    pass

Publisher().publish(AnEvent())
```

The event will be passed on to the proper subscribers.

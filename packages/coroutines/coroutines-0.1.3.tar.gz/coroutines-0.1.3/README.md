# Coroutines
A set of generic coroutines for doing things with pipelines.

## Decorator
Instead of having to remember to "prime the pump" after creating a co-routine, just decorate it!

```python
@coroutine
def mycoroutine():
    while True:
        s=yield
        do_stuff(s)
```

## Producers
 - trivialProducer will send the same thing, forever!
 - cycleProducer will round-robin send items in an infinite loop.
 - fileProducer will open() a file and send it line by line.
 - finiteProducer will only send items for a limited count.

## Consumers
 - trivialConsumer will print whatever it is sent.
 - fileConsumer will write to a file everything it is sent.

## Filters
 - split will take a stream and send it to two downstream consumers
 - combine will receive from multiple upstream sources and will deterministically order its output.
 - matchre will match a regular expression against its incoming stream. Matches can be sent to one consumer and/or no-match
 can be sent to another


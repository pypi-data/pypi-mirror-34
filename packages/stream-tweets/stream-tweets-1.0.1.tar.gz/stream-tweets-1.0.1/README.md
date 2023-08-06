# Stream Tweets To Queue
## Purpose
Stream tweets from Twitter into a queue. Tweets can be placed onto
a queue (enqueue) and removed (dequeue) using two separate processes, threads, etc.

queue-tweets is built on top of tweepy's streaming module and as such, is coupled to it.

## Usage
```python
import queue

from queue_tweets import QueueStreamer


if __name__ == '__main__':
    streamer = QueueStreamer()
    
    # a queue must have a put() and get() method
    q = queue.Queue()
    streamer.queue = q
    
    # set the consumer keys and access tokens from twitter
    streamer.set_consumer_keys(consumer_key='put your key here',
                               consumer_secret='put your secret here')
    streamer.set_access_tokens(access_token='put your access_token here',
                               access_token_secret='put your secret here')

    # specify how long you want to stream tweets for
    streamer.collection_time = 15

    # start the streaming process, searching for tweets with 'donald trump' in this case.
    streamer.stream_to_queue(track='donald trump')

    # a value of 0 will be placed onto the queue, signifying that the collection process (exceeded > 15 seconds for this example)
    #  has terminated.
    val = None
    while val is not 0:
        val = q.get()
        print(val)
```

# rgpubsub

Simple helper utility to send Google Pubsub messages easily.

#### Simple usage example

    import rgpubsub
    from rgpubsub import Publisher
    
    publisher = Publisher.default_instance()
    
    topic_name = rgpubsub.topic('testtopic')
    
    message = {
        'foo': 'bar'
    }
    
    attributes = {
        'baz': 'bar'
    }
    
    publisher.publish(topic_name, message, attributes)
    
    print('Sent message')
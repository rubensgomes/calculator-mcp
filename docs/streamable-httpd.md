# Streamable HTTPD

The HTTP connections between the MCP client and server are streamable 
bidirectional connections.  The HTTP context-type used is "text/event-stream".
That is, the data is sent as UTF-8 encoded text in the TCP socker.  And the 
server sends events (Server-Sent Events) to the client over the same socker.


## Text vs Binary Connection

A number like 12345 takes 5 (five) bytes to be encoded in UTF-8 and send over
a text connection.  While in a binary connection, 12345 takes only 2 bytes to
be represented in a binary format.

A foreign character, like "é" takes 2 bytes to be encoded in UTF-8, but if 
using ISO-8859-1 it takes 1 byte.  So, the number of bytes used on binary
streams depends entirely on the encoding standard chosen by the sender and 
receiver for text characters.

## Bidirectional Connections

Although TCP sockets support an Input Stream and an Output Stream, the connection
is only bidirectional if the higher level protocol is also bidirectional.  Old
HTTP/1.1 connectsion were unidirectional; while HTTP/2 is bidirectional.

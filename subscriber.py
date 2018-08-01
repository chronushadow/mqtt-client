import paho.mqtt.client as mqtt

HOST = '127.0.0.1'
PORT = 1883

def on_connect(client, userdata, flags, response_code):
    client.subscribe(client.topic)

def on_message(client, userdata, message):
    print(message.topic + " " + str(message.payload.decode("utf-8"))) 

def main():
    client = mqtt.Client(protocol=mqtt.MQTTv311)

    client.topic = "topic/test"
    client.on_connect = on_connect
    client.on_message = on_message

    print("Started Subscribe")
    client.connect(HOST)

    client.loop_forever()

if __name__ == '__main__':
    main()

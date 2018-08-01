from time import sleep
import paho.mqtt.client as mqtt

HOST = '127.0.0.1'
PORT = 1883

def publish(client, topic='topic/default', message='default', number=1, wait=1):
    for i in range(number):
        client.publish(topic, message)
        print(topic + " " + message)
        sleep(wait)

def main():
    client = mqtt.Client(protocol=mqtt.MQTTv311)

    print("Started publish")
    client.connect(HOST)

    publish(client, "topic/test", "hogehoge", 50, 5)

    client.disconnect()
    print("Stopped publish")


if __name__ == '__main__':
    main()
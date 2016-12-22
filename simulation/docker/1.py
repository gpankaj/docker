from docker import Client
from io import BytesIO
import ast

class Server():
    def __init__(self):
        pass
    def get_server(self,engine="192.168.88.134", port = "2376", tls=False):
        uri = engine + ":" + port
        return Client(base_url=uri, tls=tls)


class DockerFile():
    def __init__(self):
        pass
    def get_docker_file(self, file_content):
        base_8_encoded_docker_file = BytesIO(file_content.encode('utf-8'))
        return base_8_encoded_docker_file


class Image(Server):
    client = Server().get_server()
    def __init__(self):
        pass
    def create_image(self,base_8_encoded_docker_file, tag):
        #check if image already exists.
        if(self.list_images()):
            pass
        else:
            return [line for line in self.client.build(fileobj = base_8_encoded_docker_file, rm = True, tag = tag )]
    def list_images(self):
        import json
        print self.client.images()[0]['Id'].split(':')[1]



if __name__=='__main__':
    raw_docker_file = '''FROM busybox:buildroot-2014.02'''
    encoded_docker_file = DockerFile().get_docker_file(raw_docker_file)
    output =  Image().create_image(encoded_docker_file,"pankajg3")

    print ast.literal_eval(output[-1])['stream']
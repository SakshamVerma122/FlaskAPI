from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
# Wrap our app under Api
api = Api(app)


# Just defining a random dictionary to use it in return
names = {"tim":{"age": 19,"gender":"male"},"Saksham":{"age" : 21,"gender":"male"}}



# Resource is inherited by Helloworld
# Basically we want to make a class i.e. a Resource and this Resource has few different methods that we can overwrite which will let us do things like handle a get request / handle a put request/handle a delete request
class Helloworld(Resource):

    # Example 2:
    # def get(self,name,test):
    #     return {"name":name,"test":test}
    
    def get(self,name):
        return names[name]

    def post(self):
        return {"data" : "Posted"}

# Example :1
# Adding Helloworld as a resource
# root of Helloworld
# api.add_resource(Helloworld,"/helloworld")

# Example :2
# Adding arguements 
# <string:name> means you will pass a string which get will receive as name
# And this is compulsory
# api.add_resource(Helloworld,"/helloworld/<string:name>/<int:test>")

# Example :3
api.add_resource(Helloworld,"/helloworld/<string:name>")

if __name__ == "__main__":
    # This is going to start our server and flask application
    # (debug=True) means it's in debug mode
    
    # Don't do debug = True in production enviroment only do it in testing enviromnet
    app.run(debug=True)
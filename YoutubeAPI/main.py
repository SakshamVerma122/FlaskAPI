from flask import Flask,request
from flask_restful import Api, Resource
# reqparse makes sur that when we send a request we pass the information that we need with that request

app = Flask(__name__)
# Wrap our app under Api
api = Api(app)

# Just defining a random dictionary to use it in return
videos = {}

# Resource is inherited by Helloworld
# Basically we want to make a class i.e. a Resource and this Resource has few different methods that we can overwrite which will let us do things like handle a get request / handle a put request/handle a delete request
class Video(Resource):

    def get(self,video_id):
        return videos[video_id]

    def put(self,video_id):
        # IMPORTANT THE print() GIVES OUTPUT IN THE CMD WHERE API IS EXECUTING # 

        # Gives info regarding the method in which we are in
        print(request.method)
        
        # To get the data we sent hidden in URL 
        # print(request.form)
        print(request.form)
        print(request.form["likes"])
        
        return {}
api.add_resource(Video,"/video/<int:video_id>")

if __name__ == "__main__":
    
    # This is going to start our server and flask application
    # (debug=True) means it's in debug mode
    # Don't do debug = True in production enviroment only do it in testing enviromnet
    app.run(debug=True)
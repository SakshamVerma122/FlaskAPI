#  Using reqparse(flask_restful) instead of request(flask)

from flask import Flask
from flask_restful import Api, Resource,reparse
# reqparse makes sure that when we send a request we pass the information that we need with that request

app = Flask(__name__)
# Wrap our app under Api
api = Api(app)

video_put_args = reparse.RequestParser()
# A new reparser object
# It automatically parse troug the request that's being sent and make sure that it fits the kind of guidelines that we are about to define here and has te correct information in it if it does it will actually allow us to grab that information very easily

# reparse.RequestParser().add_arguement("Strictlyrequiredarguement",type = datatype,help = "If not passed tis string will be passed")
video_put_args.add_arguement("name",type = str,help = "Name of the video")
video_put_args.add_arguement("views",type = int,help = "Views of the video")
video_put_args.add_arguement("likes",type = int,help = "Likes of the video")
videos = {}
# Just defining a random dictionary to use it in return

# Resource is inherited by Helloworld
# Basically we want to make a class i.e. a Resource and this Resource has few different methods that we can overwrite which will let us do things like handle a get request / handle a put request/handle a delete request
class Video(Resource):

    def get(self,video_id):
        return videos[video_id]

    def put(self,video_id):
       
        # This is going to get all the arguements defined above --> name,views,likes and if they weren't sent it'll automatically send back an error message
        args = video_put_args.parse_args()
        
        return {video_id:args }
api.add_resource(Video,"/video/<int:video_id>")

if __name__ == "__main__":
    
    # This is going to start our server and flask application
    # (debug=True) means it's in debug mode
    # Don't do debug = True in production enviroment only do it in testing enviromnet
    app.run(debug=True)
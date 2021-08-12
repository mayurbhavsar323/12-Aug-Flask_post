from flask import Flask
from flask_restful import Resource, Api
from flask import Flask
from flask_restful import Resource, Api, reqparse
import werkzeug
import requests

app = Flask(__name__)

api = Api(app)


from PIL import Image, ImageChops

from flask import send_file


from werkzeug.datastructures import FileStorage

class UploadImage(Resource):
    @app.route('/get_image')
    def get_image(self):
        if request.args.get('type') == '1':
            filename = 'ok.gif'
        else:
            filename = 'error.gif'
        return send_file(filename, mimetype='image/gif')


    def post(self,fname):
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=FileStorage , location='C:\\Users\\Mayur Bhavsar\\Pictures\\Saved Pictures\\nature.jpg')  #  werkzeug.datastructures.FileStorage
        args = parse.parse_args()

        print(type(args),"############mmm") #dataType #<class 'flask_restful.reqparse.Namespace'> ############mmm

        image_file = args['file']
        print(type(image_file),"############ppp") #dataType # <class 'NoneType'> ############ppp
        image_file.save("fname.jpg")

api.add_resource(UploadImage, '/uploadimage/<string:fname>')


if __name__ == "__main__":
    app.run(debug=True)

##########################################################################################################
    # rough work code
    # @app.route("/upload", methods=['POST'])
    # def upload():
    #     if request.method == 'POST':
    #         f = request.form.post('file')
    #         full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'resume1')
    #         f.save(full_filename)

        # return ("Uploaded Successfully")
########################################################################################################################    

# class UploadImage(Resource):
#     def post(self, fname):
#         file = request.files['file']
#         if file:
#             file.save()
#         else:
#             return {'False'}

#####################################################################################################


        
        






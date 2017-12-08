from flask import Flask, request, jsonify
from brpy import init_brpy
from io import BytesIO
from base64 import b64decode

app = Flask(__name__)

@app.route("/",methods=["GET"])
def homepage():
    return 'Flask API running.'

@app.route("/api/v1.0/estimation/age",methods=["POST"])
def age_estimation():
    ## Age estimation
    json_request = request.get_json()
    if 'query' in json_request.keys():
        # initialize
        br = init_brpy(br_loc="/usr/local/lib")
        br.br_initialize_default()
        br.br_set_property('algorithm','AgeEstimation')
        # get image
        image = BytesIO(b64decode(json_request.get('query'))).read()
        # write image to disk
        with open('/tmp/image.bytes','wb') as fl:
            fl.write(image)
        # enroll image
        br.br_enroll('/tmp/image.bytes','/tmp/matrix.csv')
        # get data
        lines = open('/tmp/matrix.csv','r').readlines()
        # result
        result = float(lines[1].split(',')[1])
        # finalize
        br.br_finalize()
        return jsonify({'mimetype':'application/json','status':200,'request':request.url,'response':[{'score':result}]})
    else:
        return jsonify({'error':{'message':'Request must contain a query'},'status':400,'request':request.url})

@app.route("/api/v1.0/estimation/gender",methods=["POST"])
def gender_estimation():
    ## Age estimation
    json_request = request.get_json()
    if 'query' in json_request.keys():
        # initialize
        br = init_brpy(br_loc="/usr/local/lib")
        br.br_initialize_default()
        br.br_set_property('algorithm','GenderEstimation')
        # get image
        image = BytesIO(b64decode(json_request.get('query'))).read()
        # write image to disk
        with open('/tmp/image.bytes','wb') as fl:
            fl.write(image)
        # enroll image
        br.br_enroll('/tmp/image.bytes','/tmp/matrix.csv')
        # get data
        lines = open('/tmp/matrix.csv','r').readlines()
        # result
        result = 0 if lines[1].split(',')[10]=='Male' else 1
        # finalize
        br.br_finalize()
        return jsonify({'mimetype':'application/json','status':200,'request':request.url,'response':[{'score':result}]})
    else:
        return jsonify({'error':{'message':'Request must contain a query'},'status':400,'request':request.url})

@app.route("/api/v1.0/verification",methods=["POST"])
def verification():
    ## 1:1 verification
    json_request = request.get_json()
    if all(image in json_request.keys() for image in ['query','target']):
        # initialize
        br = init_brpy(br_loc="/usr/local/lib")
        br.br_initialize_default()
        br.br_set_property('algorithm','FaceRecognition')
        # get images
        image1 = BytesIO(b64decode(json_request.get('query'))).read()
        image2 = BytesIO(b64decode(json_request.get('target'))).read()
        # image templates
        imagetmpl1 = br.br_load_img(image1, len(image1))
        imagetmpl2 = br.br_load_img(image2, len(image2))
        # enroll
        query = br.br_enroll_template(imagetmpl1)
        target = br.br_enroll_template(imagetmpl2)
        # score matrix
        scoresmat = br.br_compare_template_lists(target, query)
        # result
        result = float(br.br_get_matrix_output_at(scoresmat, 0, 0))
        # clean up templates
        br.br_free_template(imagetmpl1)
        br.br_free_template_list(target)
        br.br_free_template(imagetmpl2)
        br.br_free_template_list(query)
        # finalize
        br.br_finalize()
        return jsonify({'mimetype':'application/json','status':200,'request':request.url,'response':[{'score':result}]})
    else:
        return jsonify({'error':{'message':'Request must contain a query and target'},'status':400,'request':request.url})


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)

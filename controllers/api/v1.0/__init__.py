from flask import Flask, g, jsonify
from brpy import init_brpy
from flask import Flask
from io import BytesIO
from base64 import b64decode

app = Flask(__name__)

g.br = init_brpy(br_loc="/usr/local/lib")
g.br.br_initialize_default()

@app.route("/api/v1.0/recognition",methods=["POST"])
def recognition():
    g.br.br_set_property('algorithm','FaceRecognition')
    g.br.br_set_property('enrollAll','true')
    # images
    image1 = BytesIO(b64decode(reqeust.data.get('image1','')))
    image2 = BytesIO(b64decode(reqeust.data.get('image2','')))
    # image templates
    imagetmpl1 = g.br.br_load_img(image1, len(image1))
    imagetmpl12 = g.br.br_load_img(image2, len(image2))
    # enroll
    query = g.br.br_enroll_template(imagetmpl1)
    target = g.br.br_enroll_template(imagetmpl2)
    ## score matrix
    scoresmat = g.br.br_compare_template_lists(target, query)
    ## result
    result = g.br.br_get_matrix_output_at(scoresmat, 0, 0)
    # clean up - no memory leaks
    g.br.br_free_template(imagetmpl1)
    g.br.br_free_template_list(target)
    # clean up - no memory leaks
    g.br.br_free_template(imagetmpl2)
    g.br.br_free_template_list(query)
    g.br.br_finalize()
    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)

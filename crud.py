import json
from flask import Flask, redirect, render_template, request, jsonify, make_response, abort, url_for
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from flask_sqlalchemy import SQLAlchemy


with open("secret.json") as f:
    SECRET = json.load(f)

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:2029evgen@127.0.0.1:3306/webdatab5'
db = SQLAlchemy(app)



class CosmetologyBuild(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name_of_cosmetology = db.Column(db.String(30), unique=False)
    appoinment_for = db.Column(db.Integer, unique=False)
    produce_country = db.Column(db.String(30), unique=False)
    capacity_in_ml = db.Column(db.Integer, unique=False)
    price_in_uah = db.Column(db.Integer, unique=False)

    def __str__(self):
        return f"NameOfCosmetology:{self.name_of_cosmetology} AppoinmentFor:{self.appoinment_for} ProduceCountry:{self.produce_country} CapacityInMl:{self.capacity_in_ml} PriceInUAH:{self.price_in_uah}"


class CosmetologyBuildSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = CosmetologyBuild
        sql_session = db.session

    id = fields.Integer(dump_only=True)
    name_of_cosmetology = fields.String(required=True)
    appoinment_for = fields.Integer(required=True)
    produce_country = fields.String(required=True)
    capacity_in_ml = fields.Integer(required=True)
    price_in_uah = fields.Integer(required=True)


cosmetology_build_schema = CosmetologyBuildSchema()
cosmetology_builds_schema = CosmetologyBuildSchema(many=True)


@app.route("/home", methods=["GET"])
def get_all_cosmetology_builds():
    all_cosmetology_builds = CosmetologyBuild.query.all()
    cosmetology_builds = cosmetology_builds_schema.dump(all_cosmetology_builds)
    return render_template("index.html",cosmetology_builds=cosmetology_builds)



@app.route("/create", methods=["GET", "POST"])
def create_cosmetology_build():
    if request.method == "POST":
        try:
            cosmetology_build = CosmetologyBuild(
                name_of_cosmetology=request.form.get("name"),
                appoinment_for=request.form.get("appoinment"),
                produce_country=request.form.get("produce_country"),
                capacity_in_ml=request.form.get("capacity_in_ml"),
                price_in_uah=request.form.get("price_in_uah"))

            db.session.add(cosmetology_build)
            db.session.commit()
            return redirect(url_for('get_all_cosmetology_builds'))
        except Exception as e:
            print("Failed to add CosmetologyBuild")
            print(e)
    return render_template("create.html")


@app.route("/update/<id>", methods=["POST", "GET", "PUT"])
def update_cosmetology_build(id):
    cosmetology_builds = CosmetologyBuild.query.get(id)
    if request.method == "POST":
        if cosmetology_builds.name_of_cosmetology != request.form["name"]:
            cosmetology_builds.name_of_cosmetology = request.form["name"]
        if cosmetology_builds.appoinment_for != request.form["appoinment"]:
            cosmetology_builds.appoinment_for = request.form["appoinment"]
        if cosmetology_builds.produce_country != request.form["produce_country"]:
            cosmetology_builds.produce_country = request.form["produce_country"]
        if cosmetology_builds.capacity_in_ml != request.form["capacity_in_ml"]:
            cosmetology_builds.capacity_in_ml = request.form["capacity_in_ml"]
        if cosmetology_builds.price_in_uah != request.form["price_in_uah"]:
            cosmetology_builds.price_in_uah = request.form["price_in_uah"]
        db.session.add(cosmetology_builds)
        db.session.commit()
        return redirect(url_for('get_all_cosmetology_builds'))
    return render_template("edit.html", cosmetology_builds=cosmetology_builds)


@app.route("/delete/<id>")
def delete_cosmetology_build(id):
    cosmetology_builds = CosmetologyBuild.query.get(id)
    db.session.delete(cosmetology_builds)
    db.session.commit()
    return redirect(url_for('get_all_cosmetology_builds'))


if __name__ == "main":
    db.create_all()
    app.run(debug=True)

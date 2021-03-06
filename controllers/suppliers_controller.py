from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.supplier import Supplier
import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository

suppliers_blueprint = Blueprint("suppliers", __name__)

# INDEX
# GET '/products'
@suppliers_blueprint.route("/suppliers")
def products():
    suppliers = supplier_repository.select_all()
    return render_template("suppliers/index.html", all_suppliers = suppliers)


# NEW
# GET '/suppliers/new'
@suppliers_blueprint.route("/suppliers/new", methods=['GET'])
def new_supplier():
    products = product_repository.select_all()
    return render_template("suppliers/new.html", all_products = products)

# CREATE
# POST '/suppliers'
@suppliers_blueprint.route("/suppliers", methods =['POST'])
def create_supplier():
    supplier_name = request.form['supplier_name']
    supplier = Supplier(supplier_name)
    supplier_repository.save(supplier)
    return redirect('/suppliers')

# SHOW
# GET '/suppliers/<id>'
@suppliers_blueprint.route("/suppliers/<id>", methods=['GET'])
def show_supplier(id):
    supplier = supplier_repository.select(id)
    return render_template('suppliers/show.html', supplier = supplier)


# EDIT
# GET '/suppliers/<id>/edit'
@suppliers_blueprint.route("/suppliers/<id>/edit", methods=['GET'])
def edit_supplier(id):
    supplier = supplier_repository.select(id)
    products = product_repository.select_all()
    return render_template('suppliers/edit.html', supplier = supplier, all_products = products)

# UPDATE
# PUT/POST '/suppliers/<id>'
@suppliers_blueprint.route("/suppliers/<id>", methods=['POST'])
def update_supplier(id):
    supplier_name = request.form['supplier_name']
    supplier = Supplier(supplier_name)
    supplier_repository.update(supplier)
    return redirect('/suppliers')

# DELETE
# DELETE '/suppliers/<id>'
@suppliers_blueprint.route("/suppliers/<id>/delete", methods=['POST'])
def delete_supplier(id):
    supplier_repository.delete(id)
    return redirect('/suppliers')

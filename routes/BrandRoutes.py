from flask import Blueprint, jsonify, request
from repository.BrandRepository import get_all_brands, get_brand_by_id, create_brand, update_brand, delete_brand

brands_bp = Blueprint('brands', __name__)

@brands_bp.route('/api/v1/brands', methods=['GET'])
def get_all_brands_route():
  brands = get_all_brands() 
  brands_list = [{'id': brand.id, 'brand_name': brand.brand_name, 'owner_name': brand.owner_name, 'status': brand.status} for brand in brands]
  return jsonify({'brands': brands_list})

@brands_bp.route('/api/v1/brands/<int:brand_id>', methods=['GET'])
def get_brand_by_id_route(brand_id):
  brand = get_brand_by_id(brand_id)
  if brand:
    return jsonify({'brand': {'id': brand.id, 'brand_name': brand.brand_name, 'owner_name': brand.owner_name, 'status': brand.status}})
  else:
    return jsonify({'error': 'Brand not found'}), 404
  
@brands_bp.route('/api/v1/brands', methods=['POST'])
def create_brand_route():
  data = request.get_json()
  brand_name = data.get('brand_name')
  owner_name = data.get('owner_name')
  status = data.get('status')

  if not brand_name:
    return jsonify({'error': 'Brand name is required'}), 400

  if not owner_name:
    return jsonify({'error': 'Owner name is required'}), 400

  if not status:
    return jsonify({'error': 'Status is required'}), 400

  brand = create_brand(brand_name, owner_name, status)

  return jsonify({'message': 'Brand created succesfully', 'brand': {'id': brand.id, 'brand_name': brand.brand_name, 'owner_name': brand.owner_name, 'status': brand.status}})


@brands_bp.route('/api/v1/brands/<int:brand_id>', methods=['PUT'])
def update_brand_route(brand_id):
  data = request.get_json()
  brand_name = data.get('brand_name')
  owner_name = data.get('owner_name')
  status = data.get('status')

  if not brand_name:
    return jsonify({'error': 'Brand name is required'}), 400

  if not owner_name:
    return jsonify({'error': 'Owner name is required'}), 400

  if not status:
    return jsonify({'error': 'Status is required'}), 400
  
  exist_brand = get_brand_by_id(brand_id)
  if exist_brand:
    brand = update_brand(brand_id, brand_name, owner_name, status)
    return jsonify({'message': 'Brand updated succesfully', 'brand': {'id': brand.id, 'brand_name': brand.brand_name, 'owner_name': brand.owner_name, 'status': brand.status}})
  else:
    return jsonify({'error': 'Brand not found'}), 404

@brands_bp.route('/api/v1/brands/<int:brand_id>', methods=['DELETE'])
def delete_brand_route(brand_id):
  exist_brand = get_brand_by_id(brand_id)
  if exist_brand:
    delete_brand(brand_id)
    return jsonify({'message': 'Brand deleted succesfully'})
  else:
    return jsonify({'error': 'Brand not found'}), 404
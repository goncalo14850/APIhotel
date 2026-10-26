from flask_restful import Resource, reqparse
from models.hotel import HotelModel


class Hoteis(Resource):
    def get(self):
        return{"hoteis": [hotel.json() for hotel in HotelModel.query.all()]}}

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome", type=str, help="Nome obrigatório")
    argumentos.add_argument("estrelas", type=str, help="Estrelas obrigatório")
    argumentos.add_argument("diaria", type=str, help="Diaria obrigatório")
    argumentos.add_argument("cidade", type=str, help="Cidade obrigatório")

    def get(self, id_hotel):
        Hotel_encontrado = HotelModel.find_hotel(id_hotel)
        if Hotel_encontrado:
            return Hotel_encontrado.json(), 200
        return {"message": "Hotel not found."}, 404 # Not Found

    def post(self, id_hotel):
        dados = Hotel.argumentos.parse_args()
        Hotel_encontrado = HotelModel.find_hotel(id_hotel)
        if Hotel_encontrado:
                return{ "message": "Hotel with this id already exists" }
        novo_hotel = HotelModel(id_hotel, **dados)
        novo_hotel.save_hotel()
        return novo_hotel.json(), 200

    def put(self, id_hotel):
        dados = Hotel.argumentos.parse_args()
        Hotel_encontrado = HotelModel.find_hotel(id_hotel)
        if Hotel_encontrado:
            hotel_atualizado = HotelModel(id_hotel, **dados)
            hotel_atualizado.update_hotel(**dados)
            hotel_atualizado.save_hotel()
            return hotel_atualizado.json(), 200
            hotel.update(**dados)
            return hotel, 200
            
        novo_hotel = { "hotel_id": id_hotel, **dados }
        hoteis.append(novo_hotel)
        return novo_hotel, 201 # Created

    def delete(self, id_hotel):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel["hotel_id"] != id_hotel]
        return {"message": f"Hotel with {id_hotel} deleted"}

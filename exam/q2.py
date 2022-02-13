class Hall(object):
  def __init__(self,hall_id,hall_name, capacity,price_list,amenities_list):
    self.hall_id = hall_id
    self.hall_name = hall_name
    self.capacity = capacity
    self.price_list = price_list
    self.amenities_list = amenities_list

class HotelManagement(object):
  def init(self,halls_list,req_capacity,req_amenities_list):
    self.halls_list = halls_list
    self.req_capacity = req_capacity
    self.req_amenities_list = req_amenities_list

  def net_bill(self):
    for hall in self.halls_list:
      if(set(self.req_amenities_list).issubset(set(hall.amenities_list))):
        for price in hall.price_list:
          if self.req_capacity >= price[1] and self.req_capacity <= price[2]:
            net_price = price[0] * self.req_capacity 
            gst_price = (net_price * 113)/100
            return gst_price
    
    return 'Hall Not Found'

if __name__ == '__main__':
  num = int(input())
  halls_list = list()
  for i in range(num):
    hall_id = int(input())
    hall_name = str(input())
    capacity = int(input())

    # Price List tuple
    price_list = list()
    price_count = int(input())
    for j in range(price_count):
      price_per_plate = int(input())
      lower_limit = int(input())
      upper_limit = int(input())
      price_item_tupl = tuple(price_per_plate,lower_limit,upper_limit)
      price_list.append(price_item_tupl)

    #Amenities List
    amenities_list = list()
    amenities_count = int(input())
    for k in range(amenities_count):
      amenities_item = str(input())
      amenities_list.append(amenities_item)
    
    hall_obj = Hall(hall_id)
    halls_list.append(hall_obj)

  req_capacity = int(input())
  out_num = int(input())
  req_amenities_list = list()
  for i in range(out_num):
    req_amenities = str(input())
    req_amenities_list.append(req_amenities)

  output =  HotelManagement(req_capacity,req_amenities_list).net_bill()
  print(output)
  
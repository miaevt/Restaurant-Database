from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database_setup import Base, Restaurant, MenuItem
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
engine = create_engine('sqlite:///restaurantmenu.db', connect_args={'check_same_thread': False},
                       poolclass=StaticPool, echo=True)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Fake Restaurants
# restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

# restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {
#    'name': 'Blue Burgers', 'id': '2'}, {'name': 'Taco Hut', 'id': '3'}]
# restaurants = []

# Fake Menu Items
# items = []
# items = [{'name': 'Cheese Pizza', 'description': 'made with fresh cheese', 'price': '$5.99', 'course': 'Entree', 'id': '1'}, {'name': 'Chocolate Cake', 'description': 'made with Dutch Chocolate', 'price': '$3.99', 'course': 'Dessert', 'id': '2'}, {'name': 'Caesar Salad', 'description': 'with fresh organic vegetables',
#                                                                                                                                                                                                                                                        'price': '$5.99', 'course': 'Entree', 'id': '3'}, {'name': 'Iced Tea', 'description': 'with lemon', 'price': '$.99', 'course': 'Beverage', 'id': '4'}, {'name': 'Spinach Dip', 'description': 'creamy dip with fresh spinach', 'price': '$1.99', 'course': 'Appetizer', 'id': '5'}]
# item = {'name': 'Cheese Pizza', 'description': 'made with fresh cheese',
#        'price': '$5.99', 'course': 'Entree'}


@app.route('/', methods=['GET', 'POST'])
@app.route('/restaurants/', methods=['GET', 'POST'])
def showRestaurants():
    restaurants = session.query(Restaurant).all()
    return render_template('restaurants.html', restaurants=restaurants)
    # return "This page will show all of my restaurants"


@app.route('/restaurant/new/', methods=['GET', 'POST'])
def newRestaurant():
    if request.method == 'POST':
        new = Restaurant(name=request.form['name'])
        session.add(new)
        session.commit()
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('newrestaurant.html')
    # return "This page will be for making a new restaurant"


@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    restaurant = session.query(
        Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        restaurant.name = request.form['name']
        session.add(restaurant)
        session.commit()
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('editrestaurant.html', restaurant=restaurant)
    # return "This page will be for editing restaurant {}".format(restaurant_id)


@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    restaurant = session.query(
        Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        session.delete(restaurant)
        session.commit()
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('deleterestaurant.html', restaurant=restaurant)
    # return "This page will be for deleting restaurant {}".format(restaurant_id)


@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def showMenu(restaurant_id):
    return render_template('menu.html', restaurant=restaurant, items=items)
    # return "This page is the menu for restaurant {}".format(restaurant_id)


@app.route('/restaurant/<int:restaurant_id>/menu/new/')
def newMenuItem(restaurant_id):
    return render_template('newmenuitem.html')
    # return "This page is for making a new menu item for restaurant {}".format(
    #   restaurant_id)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return render_template('editmenuitem.html', item=item)
    # return "This page is for editing menu item {}".format(menu_id)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return render_template('deletemenuitem.html', item=item)
    # return "This page is for deleting menu item {}".format(menu_id)


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

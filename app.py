from flask import Flask,render_template,request,redirect,url_for,flash,session,jsonify,json
import mysql.connector
from otp import genotp
from itemid import itemidotp
from itemid import itemidotp
from cmail import sendmail
import os 
import logging
from collections import defaultdict
import razorpay
logging.basicConfig(level=logging.INFO)
from razorpay.errors import SignatureVerificationError

RAZORPAY_API_KEY='rzp_test_p1Y8tik4gQ37wZ'
RAZORPAY_API_SECRET='vjiqjfyj14fUsizxWatlpiRZ'
razorpay_client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET))
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='cloud'
)
app=Flask(__name__)
app.secret_key='esdfghj'
@app.route('/')
def base():
    return render_template('homepage.html')

# Signup Route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']

        if password != confirm_password:
            flash('Passwords do not match!', 'error')
            return redirect(url_for('signup'))

        try:
            cursor = mydb.cursor()
            query = "INSERT INTO user (name, email, password) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, email, password))
            mydb.commit()
            flash('Signup successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except mysql.connector.IntegrityError:
            flash('Email already registered!', 'error')
            return redirect(url_for('signup'))

    return render_template('signup.html')

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor = mydb.cursor(dictionary=True)
        query = "SELECT * FROM user WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))
        user = cursor.fetchone()
        print(user)  # Debugging: Check what user contains

        if user:
            session['user_id'] = user['id']  # Save the unique user ID in the session
            session['user_email'] = user['email']  # Optionally store email for reference
            session['user_name'] = user['name']  # Optionally store the user name for UI
            flash(f'Welcome back, {user["name"]}!', 'success')
            return redirect(request.args.get('next') or url_for('menu'))
        else:
            flash('Invalid email or password!', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')

#logout
@app.route('/logout')
def logout():
    if session.get('user'):
        session.pop('user')
        return redirect(url_for('base'))
    else:
        flash('already logged out!')
        return redirect(url_for('login'))


#adminsignup
@app.route('/adminsignup', methods=['GET', 'POST'])
def adminsignup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']

        if password != confirm_password:
            flash('Passwords do not match!', 'error')
            return redirect(url_for('adminsignup'))

        try:
            cursor = mydb.cursor()
            query = "INSERT INTO admin (name, email, password) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, email, password))
            mydb.commit()
            flash('Signup successful! Please log in.', 'success')
            return redirect(url_for('adminlogin'))
        except mysql.connector.IntegrityError:
            flash('Email already registered!', 'error')
            return redirect(url_for('adminsignup'))

    return render_template('adminsignup.html')

# AdminLogin Route
@app.route('/adminlogin', methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor = mydb.cursor(dictionary=True)
        query = "SELECT * FROM admin WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))
        admin = cursor.fetchone()

        if admin:
            session['admin_id'] = admin['id']
            session['admin_name'] = admin['name']
            flash(f'Welcome back, {admin["name"]}!', 'success')
            return redirect(url_for('base'))
        else:
            flash('Invalid email or password!', 'error')
            return redirect(url_for('adminlogin'))

    return render_template('adminlogin.html')

#adminlogout
@app.route('/adminlogout')
def adminlogout():
    if session.get('admin'):
        session.pop('admin')
        return redirect(url_for('base'))
    else:
        flash('already logged out!')
        return redirect(url_for('adminlogin'))

#adddish route
@app.route('/adddish', methods=['GET', 'POST'])
def adddish():
    if session.get('admin_id'):
        if request.method == 'POST':
            name = request.form['name']
            description = request.form['description']
            menu = request.form['menu'].capitalize()  
            price = request.form['price']
            image = request.files['image']

            valid_menu = ['Starters', 'Breads', 'Maincourse', 'Desserts']
            if menu not in valid_menu:
                flash('Invalid category. Please select a valid option.', 'error')
                return render_template('adddish.html')

            try:
                cursor = mydb.cursor()
                filename = f"{itemidotp()}.jpg"
                cursor.execute(
                    'INSERT INTO adddish (name, description, menu, price, image_path) VALUES (%s, %s, %s, %s, %s)',
                    (name, description, menu, price, filename)
                )
                mydb.commit()
                static_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
                image.save(os.path.join(static_path, filename))

                flash('Dish added successfully!', 'success')
            except Exception as e:
                flash(f"Error adding dish: {str(e)}", 'error')
                mydb.rollback() 
        return render_template('adddish.html')
    else:
        flash('Please log in as admin to add a dish.', 'error')
        return redirect(url_for('adminlogin'))

#menu
@app.route('/menu')
def menu():
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM adddish')
    dishes = cursor.fetchall()
    categorized_dishes = defaultdict(list) 
    for dish in dishes:
        category = dish[3]  
        categorized_dishes[category].append(dish)

    print(categorized_dishes) 
    return render_template('menu.html', categorized_dishes=categorized_dishes)


#updated dish
@app.route('/updatedish/<int:dish_id>', methods=['GET', 'POST'])
def updatedish(dish_id):
    if session.get('admin_id'):
        cursor = mydb.cursor(dictionary=True)
        cursor.execute('SELECT * FROM adddish WHERE id = %s', (dish_id,))
        dish = cursor.fetchone()  

        if not dish:
            flash('Dish not found!', 'error')
            return redirect(url_for('menu'))

        if request.method == 'POST':
            name = request.form['name']
            description = request.form['description']
            menu = request.form['menu'].capitalize()
            price = request.form['price']

            valid_menu = ['Starters', 'Breads', 'Maincourse', 'Desserts']
            if menu not in valid_menu:
                flash('Invalid category. Please select a valid option.', 'error')
                return render_template('updatedish.html', dish=dish)  

            cursor.execute('''UPDATE adddish SET name = %s, description = %s, menu = %s, price = %s
                WHERE id = %s''', (name, description, menu, price, dish_id))
            mydb.commit()

            flash('Dish updated successfully!', 'success')
            return redirect(url_for('menu'))

        return render_template('updatedish.html', dish=dish)
    else:
        flash('Please log in as admin to edit dishes.', 'error')
        return redirect(url_for('adminlogin'))
    
#deleteddish route
@app.route('/deletedish/<int:dish_id>', methods=['GET'])
def deletedish(dish_id):
    if session.get('admin_id'):
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM adddish WHERE id = %s', (dish_id,))
        dish = cursor.fetchone()

        if dish:
            cursor.execute('DELETE FROM adddish WHERE id = %s', (dish_id,))
            mydb.commit()

            flash('Dish deleted successfully!', 'success')
        else:
            flash('Dish not found!', 'error')

        return redirect(url_for('menu'))
    else:
        flash('Please log in as admin to delete dishes.', 'error')
        return redirect(url_for('adminlogin'))


@app.route('/add_to_cart/<int:dish_id>', methods=['POST'])
def add_to_cart(dish_id):
    quantity = int(request.form['quantity'])
    name = request.form['name']
    price = float(request.form['price'])
    image = request.form['image']
    print(quantity)
    print(price)
    print(image)
    user_id = session.get('user_id')
    if not user_id:
        flash("You must log in to add items to the cart.")
        return redirect(url_for('login'))

    if 'cart' not in session:
        session['cart'] = {}

    user_cart = session['cart'].get(str(user_id), {})  # Retrieve the user's cart
    if str(dish_id) not in user_cart:
        user_cart[str(dish_id)] = {'name': name, 'price': price, 'quantity': quantity, 'image': image}
        flash(f'{name} added to cart.')
    else:
        user_cart[str(dish_id)]['quantity'] += quantity
        flash(f'{name} quantity updated.')

    # Update the session
    session['cart'][str(user_id)] = user_cart
    session.modified = True
    return redirect(url_for('addedsuccess'))

@app.route('/addedsuccess')
def addedsuccess():
    return render_template('addedsuccess.html')


@app.route('/update_cart/<int:dish_id>', methods=['POST'])
def update_cart(dish_id):
    new_quantity = int(request.form['quantity'])
    if new_quantity <= 0:
        flash('Quantity must be greater than zero!', 'error')
        return redirect(url_for('viewcart'))

    user_id = session.get('user_id')
    if not user_id or 'cart' not in session or str(user_id) not in session['cart']:
        flash("No cart found!", 'error')
        return redirect(url_for('viewcart'))

    user_cart = session['cart'][str(user_id)]
    if str(dish_id) in user_cart:
        user_cart[str(dish_id)]['quantity'] = new_quantity
        session.modified = True
        flash('Cart updated successfully!', 'success')
    else:
        flash('Dish not found in the cart!', 'error')

    return redirect(url_for('viewcart'))



@app.route('/remove_from_cart/<int:dish_id>')
def remove_from_cart(dish_id):
    user_id = session.get('user_id')
    if not user_id or 'cart' not in session or str(user_id) not in session['cart']:
        flash("No cart found!", 'error')
        return redirect(url_for('viewcart'))

    user_cart = session['cart'][str(user_id)]
    if str(dish_id) in user_cart:
        del user_cart[str(dish_id)]
        session.modified = True
        flash('Item removed from cart.', 'success')
    else:
        flash('Dish not found in the cart!', 'error')

    return redirect(url_for('viewcart'))


@app.route('/viewcart')
def viewcart():
    user_id = session.get('user_id')
    if not user_id:
        flash("Please log in to view your cart.", "error")
        return redirect(url_for('login'))

    # Ensure the 'cart' key exists in the session
    if 'cart' not in session:
        session['cart'] = {}

    # Retrieve the user's cart
    user_cart = session['cart'].get(str(user_id), {})
    if not user_cart:
        flash("Your cart is empty!", "info")
        return render_template('view_cart.html', dishes=None)

    # Calculate the total price
    total_price = sum(item['quantity'] * item['price'] for item in user_cart.values())
    return render_template('view_cart.html', dishes=user_cart, total_price=total_price)


@app.route('/checkout', methods=['POST'])
def checkout():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    address = request.form.get('address')
    payment_method = request.form.get('payment_method')
    user_cart = session.get('cart', {}).get(str(user_id), {})  # Get the user's cart

    total_price = sum(item['quantity'] * item['price'] for item in user_cart.values())

    total_price_in_paise = max(int(total_price * 100), 100)

    if payment_method == 'Online':
        try:
            # Create Razorpay order
            order_data = {
                "amount": total_price_in_paise,
                "currency": "INR",
                "receipt": f"order_rcptid_{user_id}"
            }
            razorpay_order = razorpay_client.order.create(data=order_data)

            session['razorpay_order_id'] = razorpay_order['id']

            # Insert order summary into orders_summary table
            cursor = mydb.cursor()
            cursor.execute("""
                INSERT INTO orders_summary (customer_id, total_price, order_status, order_date, address, payment_method)
                VALUES (%s, %s, %s, NOW(), %s, %s)
            """, (user_id, total_price, 'Pending', address, payment_method))
            mydb.commit()
            order_id = cursor.lastrowid  # Get the newly inserted order_id (for future reference, if needed)

            # Insert order details into orders table (no order_summary_id)
            for dish_id, item in user_cart.items():
                item_total = item['quantity'] * item['price']
                cursor.execute("""
                    INSERT INTO orders (customer_id, dish_id, quantity, total_price, address, payment_method, order_status, order_date)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())
                """, (user_id, dish_id, item['quantity'], item_total, address, payment_method, 'Pending'))
            mydb.commit()

            if 'cart' in session:
                session['cart'].pop(str(user_id), None)


            flash("Your order has been placed successfully!", "success")
            return render_template(
                'razorpay_payment.html',
                razorpay_order=razorpay_order,
                total_price=total_price,
                address=address,
                payment_method=payment_method
            )
        except Exception as e:
            flash(f"Error creating Razorpay order: {str(e)}", "error")
            return redirect(url_for('viewcart'))

    elif payment_method == 'COD':
        try:
            # Insert order summary into orders_summary table
            cursor = mydb.cursor()
            cursor.execute("""
                INSERT INTO orders_summary (customer_id, total_price, order_status, order_date, address, payment_method)
                VALUES (%s, %s, %s, NOW(), %s, %s)
            """, (user_id, total_price, 'Pending', address, payment_method))
            mydb.commit()
            order_id = cursor.lastrowid  # Get the newly inserted order_id

            # Insert order details into orders table (no order_summary_id)
            for dish_id, item in user_cart.items():
                item_total = item['quantity'] * item['price']
                cursor.execute("""
                    INSERT INTO orders (customer_id, dish_id, quantity, total_price, address, payment_method, order_status, order_date)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())
                """, (user_id, dish_id, item['quantity'], item_total, address, payment_method, 'Pending'))
            mydb.commit()

            session.pop(str(user_id), None)  # Clear the user's cart after order

            flash("Your order has been placed successfully with Cash on Delivery!", "success")
            return redirect(url_for('orders'))
        except Exception as e:
            flash(f"Error placing order: {str(e)}", "error")
            return redirect(url_for('viewcart'))

    else:
        flash("Invalid payment method selected. Please try again.", "error")
        return redirect(url_for('viewcart'))


@app.route('/payment-success', methods=['POST'])
def payment_success():
    try:
        data = request.get_json()
        
        razorpay_order_id = data['razorpay_order_id']
        razorpay_signature = data['razorpay_signature']

        cursor = mydb.cursor()
        cursor.execute("""
            UPDATE orders
            SET order_status = 'Completed'
            WHERE razorpay_order_id = %s
        """, (razorpay_order_id,))
        
        mydb.commit()
        
        return jsonify({"status": "success", "redirect_url": url_for('orders')})
    except Exception as e:
        return jsonify({"status": "failed", "message": str(e)})



@app.route('/orders')
def orders():
    user_id = session.get('user_id')
    if not user_id:
        flash("Please log in to view your orders.")
        return redirect(url_for('login'))

    cursor = mydb.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT o.quantity, o.total_price, o.order_status, o.order_date, 
                   o.address, o.payment_method, d.name AS dish_name
            FROM orders o
            JOIN adddish d ON o.dish_id = d.id
            WHERE o.customer_id = %s
            ORDER BY o.order_date DESC
        """, (user_id,))
        orders = cursor.fetchall()
    finally:
        cursor.close()
    
    return render_template('orders.html', orders=orders)





@app.route('/payment-failure', methods=['GET'])
def payment_failure():
    return "Payment Failed. Please try again."

@app.route('/admin_dashboard')
def admin_dashboard():
    if session.get('admin_id'):
        cursor = mydb.cursor(dictionary=True)
        
        # Fetch orders with customer name and dish name
        cursor.execute('''
            SELECT 
                orders.id, 
                orders.quantity, 
                orders.total_price, 
                orders.order_status, 
                orders.order_date, 
                user.name AS customer_name, 
                adddish.name AS dish_name
            FROM orders
            JOIN user ON orders.customer_id = user.id
            JOIN adddish ON orders.dish_id = adddish.id
        ''')
        orders = cursor.fetchall()
        
        # Fetch dishes
        cursor.execute('SELECT * FROM adddish')
        dishes = cursor.fetchall()
        
        # Fetch customers
        cursor.execute('SELECT * FROM user')
        customers = cursor.fetchall()
        
        return render_template('admindashboard.html', orders=orders, dishes=dishes, customers=customers)
    else:
        flash('Please log in as admin to access the dashboard.', 'error')
        return redirect(url_for('adminlogin'))


@app.route('/delete_order/<int:order_id>', methods=['GET', 'POST'])
def delete_order(order_id):
    cursor = mydb.cursor()
    cursor.execute('DELETE FROM orders WHERE id = %s', (order_id,))
    mydb.commit()
    flash('Order deleted successfully!', 'success')
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/update_status/<int:order_id>', methods=['POST'])
def update_status(order_id):
    if session.get('admin_id'):
        new_status = request.form['status']  # Get the new status from the form
        cursor = mydb.cursor()
        cursor.execute('UPDATE orders SET order_status = %s WHERE id = %s', (new_status, order_id))
        mydb.commit()
        flash(f'Order status updated to {new_status}.', 'success')
        return redirect(url_for('orders'))  # Redirect back to the orders page
    else:
        flash('Please log in as admin to update order status.', 'error')
        return redirect(url_for('adminlogin'))

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if session.get('user_id'):  # Check if the user is logged in
        user_id = session['user_id']

        if request.method == 'POST':  # Handle profile updates
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            gender = request.form['gender']
            dob = request.form['dob']

            cursor = mydb.cursor()
            cursor.execute('UPDATE user SET name = %s, email = %s, password = %s, gender = %s, dob = %s WHERE id = %s',
                           (name, email, password, gender, dob, user_id))
            mydb.commit()
            flash('Profile updated successfully!', 'success')

        # Fetch user details
        cursor = mydb.cursor(dictionary=True)
        cursor.execute('SELECT * FROM user WHERE id = %s', (user_id,))
        user = cursor.fetchone()

        # Fetch user orders with dish details
        cursor.execute('''
            SELECT orders.id, orders.order_date, orders.total_price, adddish.name AS dish_name 
            FROM orders 
            INNER JOIN adddish ON orders.dish_id = adddish.id
            WHERE orders.customer_id = %s
            ''', (session['user_id'],))
        orders = cursor.fetchall()


        return render_template('profile.html', user=user, orders=orders)

    else:
        flash('Please log in to access your profile.', 'error')
        return redirect(url_for('login'))


@app.route('/feedback_form', methods=['GET', 'POST'])
def feedback_form():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        email = request.form['email']
        comment = request.form['comment']

        try:
            # Insert feedback into the database
            cursor = mydb.cursor()
            query = "INSERT INTO feedback (customer_name, email, comment) VALUES (%s, %s, %s)"
            cursor.execute(query, (customer_name, email, comment))
            mydb.commit()
            cursor.close()

            flash('Thank you for your feedback!', 'success')
            return redirect(url_for('base'))  # Redirect to homepage
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')

    return render_template('feedback_form.html')


if __name__ == '__main__':
    app.run(debug=True)
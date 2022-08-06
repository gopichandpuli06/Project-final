from enum import unique
from pickle import TRUE
from xml.dom import ValidationErr
from flask import Flask,redirect, render_template, flash, url_for,session,request,abort
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from email_validator import validate_email, EmailNotValidError
from sqlalchemy import false
import os
from ast import Delete
from sqlalchemy import delete
from flask_admin import Admin # used reference from https://youtu.be/0cySORIhkCg
from flask_admin.contrib.sqla import ModelView #used reference from https://youtu.be/0cySORIhkCg
from flask_admin.menu import MenuLink #used reference from https://flask-admin.readthedocs.io/en/latest/

app=Flask(__name__)
app.config['SECRET_KEY']='oursecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite') #setup database location
#
# Creating product details DB
#app.config['SQLALCHEMY_BINDS'] = {'productdetails': 'sqlite:///'+os.path.join(basedir,'productquantity.sqlite')}
#
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #dont want to modify every single modification so, it is false
db=SQLAlchemy(app)
admin = Admin(app)#changed

gid=False
ua=False
gemail=False
qnty=0
qnty1=0
qnty2=0
qnty3=0
qnty4=0
qnty5=0
qnty6=0
qnty1=0
qnty7=0
qnty8=0
qnty9=0
qnty10=0
qnty11=0
pname=False
pprice=False
pquant=False
line349=False

#change
class  Customers(db.Model):#changed
    __tablename__ = 'customerdbs'
    id=db.Column(db.Integer, primary_key=True)
    Firstname = db.Column(db.Text)
    lastname= db.Column(db.Text)
    Email=db.Column(db.Text)
    password=db.Column(db.Text)

    def __init__ (self,Firstname,lastname, Email, password):
        self.Firstname=Firstname
        self.lastname=lastname
        self.Email=Email
        self.password=password
    def __repr__ (self):
        return f"{self.id} : {self.Firstname} : {self.Email} : {self.password}"
#prodcut de creation
class Products(db.Model):#changed
    __tablename__ = 'productdbs'
    id=db.Column(db.Integer, primary_key=True)
    productname = db.Column(db.Text)
    productprice = db.Column(db.Integer)
    Availableunits= db.Column(db.Integer)

    def __init__ (self, productname, productprice,Availableunits):
        self.productname = productname
        self.productprice = productprice
        self.Availableunits=Availableunits
    def __repr__ (self):
        return f"{id} : {self.productname} : {self.productprice} {self.Availableunits}"

class Productorder(db.Model):#changed
    __tablename__ = 'allOrdersdbs'
    id=db.Column(db.Integer, primary_key=True)
    customer_id=db.Column(db.Integer)
    customer = db.Column(db.Text)
    productname = db.Column(db.Text)
    units= db.Column(db.Integer)
    Totalprice = db.Column(db.Integer)
    def __init__ (self, customer_id, customer,productname, units, Totalprice):
        self.customer_id=customer_id
        self.customer=customer
        self.productname = productname
        self.units = units
        self.Totalprice = Totalprice
    
    def __repr__ (self):
        return f"{self.customer_id} {self.customer} {self.productname} : {self.units} : {self.Totalprice}"

class SecureModelView(ModelView):#used reference from https://youtu.be/eQmLkqZA588
    def is_accessible(self):
       if "logged_in" in session:
            return True
       else:
            abort(403)

db.create_all()#changed
#changed
admin.add_view(SecureModelView(Customers,db.session))
admin.add_view(SecureModelView(Products,db.session))
admin.add_view(SecureModelView(Productorder,db.session))
admin.add_link(MenuLink(name='setquantity', category='', url="/setquantity"))
admin.add_link(MenuLink(name='Logout', category='', url="/logout"))
#changed

class MyForm(FlaskForm):
    username = StringField('User Name/ Email : ',validators=[DataRequired(), Length(min=5, max=80)])
    password = PasswordField('Password : ',validators=[DataRequired(), Length(min=8, max=80)])
    submit=SubmitField('Login')

class registerpage(FlaskForm):
    #username = StringField('User Name : ',validators=[DataRequired(), Length(min=8, max=80)])
    firstname = StringField('Firstname : ',validators=[DataRequired()])
    lastname = StringField('lastname : ',validators=[DataRequired()])
    email = StringField('Email : ',validators=[DataRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('Password : ',validators=[DataRequired(), Length(min=8, max=80)])
    cpassword = PasswordField('Confirm Password : ',validators=[DataRequired(), Length(min=8, max=80), EqualTo('password')])
    submit=SubmitField('Register')
#address add
class addresscheckout(FlaskForm):
    name=StringField('Firstname : ',validators=[DataRequired()])
    email = StringField('Email : ',validators=[DataRequired(), Email(message='Invalid email'), Length(max=50)])
    address= StringField('Address : ',validators=[DataRequired()])
    submit=SubmitField('Register')
#Add to cart add on 2nd Aug
class addtocart(FlaskForm):
    quantity=IntegerField('Quantity : ', validators=[DataRequired()])
    submit=SubmitField('Add to cart')
class Removepcart(FlaskForm):
    re_id=IntegerField('product name')
    submit=SubmitField('Remove all for cart')

class qnform(FlaskForm):
    promax13=IntegerField('promax13')
    s1=SubmitField('Update')
    pro13=IntegerField('pro13')
    s2=SubmitField('Update')
    Iphone13=IntegerField('Iphone13')
    s3=SubmitField('Update')
    s22Ultra=IntegerField('s22Ultra')
    s4=SubmitField('Update')
    s22plus=IntegerField('s22plus')
    s5=SubmitField('Update')
    s22=IntegerField('s22')
    s6=SubmitField('Update')
    A53=IntegerField('A53')
    s7=SubmitField('Update')
    A42=IntegerField('A42')
    s8=SubmitField('Update')
    A13=IntegerField('A13')
    s9=SubmitField('Update')
    Pixel6Pro=IntegerField('Pixel6Pro')
    s10=SubmitField('Update')
    Pixel6=IntegerField('Pixel6')
    s11=SubmitField('Update')

@app.route('/', methods=['GET','POST'])

@app.route('/index')

def index():
    return redirect(url_for('login'))
    #return render_template('homepage.html')

@app.route('/login', methods=['GET','POST'])

def login():
    form=MyForm()
    username=False
    password=False
    bool=False
    registeredpassword=False
    loon=False
    if form.validate_on_submit():
        username=form.username.data
        password=form.password.data
        print(username)
        print(password)
        global ua #changed
        if username =="admin" and password == "password":
            session['logged_in'] = True
            ua="admin"
            return render_template('homepage.html',name=ua)
        user_object = Customers.query.filter_by(Email=username).first()
        if user_object:
            print("hello the below one")
            print(user_object.password)
            print("Hello the above one")
            registeredpassword=user_object.password
            if password==registeredpassword:
                loon=False
            else:
                loon=True
                return render_template('login.html', form=form, loon=loon)
            
        else:
            bool=True
            return render_template('login.html', form=form, bool=bool)
        name=user_object.Firstname

        global gid, gemail
        gid=user_object.id
        
        gemail=user_object.Email
        ua=name

        print(name)
        print(gid)
        print(gemail)
        print('@@@@')
        print(ua)
        logged=True
        #return redirect(url_for('home'))

        return render_template('homepage.html', name=ua, logged=logged)
    return render_template('login.html',form=form)

@app.route('/signup', methods=['GET','POST'])
def signup():
    register=registerpage()
    #username=False
    firstname=False
    lastname=False
    email=False
    password=False
    bool=False
    allstudent=[]
    if register.validate_on_submit():
        #username=register.username.data
        firstname=register.firstname.data
        lastname=register.lastname.data
        email=register.email.data
        ua=firstname
        try:
            email = validate_email(email).email
        except EmailNotValidError as e:
            print(e)
        password=register.password.data
        #if the user submit the registeration form it will be stored in db by below steps
        #change
        user_object = Customers.query.filter_by(Email=email).first()
        # check if email exists or not
        if user_object:
            bool=True
            return render_template('SignUp.html',register=register,email=email, allstudent=allstudent, bool=bool)
        # password check
        size = len(password)
        t1=False
        t2=False
        t3=False
        pcheck=False
        print(size)
        for i in password:
            if i.isupper():
                t1=True
            elif i.islower():
                t2=True
            if i.isdigit():
                t3=True

        if t1==False or t2==False or t3==False:
            pcheck=True
            return render_template('SignUp.html',register=register,email=email, allstudent=allstudent, pcheck=pcheck)
#change
        new_studentdetails=Customers(firstname,lastname, email, password)
        db.session.commit()
        if register.submit.data:
            db.session.add_all([new_studentdetails])
            db.session.commit()
#change
            allstudent= Customers.query.all()
            print(allstudent)  


            #return redirect(url_for('thankyou'))
        registered=True

        #flash(f'Account created for {register.firstname.data}!', 'success')

        

        return redirect(url_for('thanks'))
        #return render_template('homepage.html',registered=registered, firstname=firstname)

    return render_template('SignUp.html',register=register,email=email, allstudent=allstudent)

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')


@app.route('/home')
def home():
    logged=True
    name=ua
    print(ua)
    return render_template('homepage.html', logged=logged, name=name)

@app.route('/logout')
def logout():
    session.clear()
    return render_template('loggout.html')

@app.route('/wishlist')
def wishlist():
    name=ua
    print(pname)
    return render_template('wishlist.html',name=name, pname=pname)

@app.route('/checkout', methods=['GET','POST'])
def checkout():
    name=ua
    prodlist=False
    val=0
    remove=Removepcart()
    #updateinf the check list
    product_qunt=Productorder.query.filter(Productorder.customer_id==gid)
    a=False
    print('please check price below')
    #print(product_qunt.productprice)
    #if a==False:
        #for l in product_qunt:      
            #if remove.submit.data:
                #print(valu)
                #proddel=Productorder.query.filter(Productorder.productname==l.productname).first()
                #print(proddel)
                #print('1')
                #db.session.delete(proddel)
                #db.session.commit()
        #prodlist=True
    if line349==False:
        for l in product_qunt:      
            val=val+l.Totalprice
            print(l.productname)
            print(l.Totalprice)
            prodlist=True
            if remove.submit.data:
                    #print(valu)
                proddel=Productorder.query.filter(Productorder.productname==l.productname).first()
                print('here')
                print(proddel.productname)
                print(proddel)
                print('1')
                db.session.delete(proddel)
                db.session.commit()
                val=val-l.Totalprice
                    #proddel=Product.query.get(l.productname)
                    #db.session.delete(proddel)
                    #db.session.commit()
        print(val)
        

    global checkoutvalue
    checkoutvalue=True
    return render_template('checkoutpage.html',name=ua, pname=pname, pprice=pprice, pquant=pquant, product_qunt=product_qunt, remove=remove,prodlist=prodlist,checkoutvalue=checkoutvalue, val=val)

@app.route('/orderlist', methods=['GET','POST'])
def orderlist():
    name = ua
    #added
    valu=request.args.get('type') #taken reference from https://stackoverflow.com/questions/50426137/flask-get-clicked-link-info-and-display-on-rendered-page
    print(valu)
    if valu=='True':
        global line349
        line349=True
        product_qunt=Productorder.query.filter(Productorder.customer_id==gid)
        #added/
        return render_template('orderedplaced.html', name=ua, checkoutvalue=checkoutvalue, product_qunt=product_qunt)
    return render_template('orderedplaced.html', name=ua)
#order placed page/

#address adding
@app.route('/Address', methods=['GET','POST'])
def Address():
    name=ua
    fname=False
    email=False
    Address=False
    form= addresscheckout()
    if form.validate_on_submit():
        fname=form.name.data
        email=form.email.data
        address=form.address.data
        val=True
        return render_template('Address.html',form=form, val=val, fname=fname, email=email, address=address, name=name)


    return render_template('Address.html',name=name, form=form)

@app.route('/setquantity',methods=['GET','POST'])
def set():
    form=qnform()
    if form.validate_on_submit():
        global qnty1,qnty2,qnty3,qnty4,qnty5,qnty6,qnty7,qnty8,qnty9,qnty10,qnty11
    elif 's1' in request.form:
        qnty1 = form.promax13.data
    elif 's2' in request.form:
        qnty2 = form.pro13.data
    elif 's3' in request.form:
        qnty3 = form.Iphone13.data
    elif 's4' in request.form:
        qnty4 = form.s22Ultra.data
    elif 's5' in request.form:
        qnty5= form.s22plus.data
    elif 's6' in request.form:
        qnty6= form.s22.data
    elif 's7' in request.form:
        qnty7= form.A53.data
    elif 's8' in request.form:
        qnty8 = form.A42.data
    elif 's9' in request.form:
        qnty9 = form.A13.data
    elif 's10' in request.form:
        qnty10 = form.Pixel6Pro.data
    elif 's11' in request.form:
        qnty11 = form.Pixel6.data
    print (qnty1,qnty2,qnty3,qnty4,qnty5,qnty6,qnty7,qnty8,qnty9,qnty10,qnty11)
    return render_template('setquantity.html',form=form)

###Apple###
@app.route('/promax13', methods=['GET','POST'])
def promax13():
    name=ua
    form=addtocart()
    prodname='Iphone 13 Pro Max'
    price=999
    qnty=qnty1
    global pname, pprice, pquant,tot
    if form.validate_on_submit():
        value=form.quantity.data
        pname=prodname
        pprice=price
        pquant=value
        global line349
        line349=False
        print("####")
        print(value)
        print(pprice)
        print(pquant)
        new_productdetails=Products(prodname, price,qnty)
        db.session.add_all([new_productdetails])
        db.session.commit()
        allstudent= Products.query.all()
        print(allstudent)
        print(qnty)
        qnty=qnty-value
        print(qnty)
        if qnty>=0:
            var = Products.query.filter_by(productname=prodname).first()
            var.Availableunits=qnty
            db.session.commit()
        tot=value*price
        print(tot)
        if tot>=0 and qnty>=0:
            new_orderdetails=Productorder(gid,name,prodname,value,tot)
            db.session.add_all([new_orderdetails])
            db.session.commit()
            allstudents= Productorder.query.all()
            print(allstudents)
        
        if qnty<=0:
            qnty=0
            out = True
            return render_template('checkoutpage.html',name=ua, pname=pname, pprice=pprice, pquant=pquant,out=out)
        print("added to cart")
        #return render_template('checkoutpage.html', name=name)
        return redirect('/checkout')

    return render_template('13promax.html',name=ua, form=form, price=price, prodname=prodname,pname=prodname)
#Iphone 13 Pro
@app.route('/pro13', methods=['GET','POST'])
def pro13():
    name=ua
    form=addtocart()
    prodname='Iphone 13 Pro'
    price=799
    qnty=qnty2
    global pname, pprice, pquant,tot
    if form.validate_on_submit():
        value=form.quantity.data
        pname=prodname
        pprice=price
        pquant=value
        global line349
        line349=False
        print("####")
        print(value)
        print(pprice)
        print(pquant)
        new_productdetails=Products(prodname, price,qnty)
        db.session.add_all([new_productdetails])
        db.session.commit()
        allstudent= Products.query.all()
        print(allstudent)
        qnty=qnty-value
        print(qnty)
        if qnty>=0:
            var = Products.query.filter_by(productname=prodname).first()
            var.Availableunits=qnty
            db.session.commit()
        tot=value*price
        print(tot)
        if tot>=0 and qnty>=0:
            new_orderdetails=Productorder(gid,name,prodname,value,tot)
            db.session.add_all([new_orderdetails])
            db.session.commit()
            allstudents= Productorder.query.all()
            print(allstudents)
        
        if qnty<=0:
            qnty=0
            out = True
            return render_template('checkoutpage.html',name=ua, pname=pname, pprice=pprice, pquant=pquant,out=out)
        print("added to cart")
        #return render_template('checkoutpage.html', name=name)
        return redirect('/checkout')
    return render_template('13pro.html',name=ua, form=form, price=price, prodname=prodname,pname=prodname)

#mofiication add to cart update
@app.route('/Iphone13', methods=['GET','POST'])
def Iphone13():
    name=ua
    form=addtocart()
    prodname='Iphone 13'
    price=699
    qnty=qnty3
    global pname, pprice, pquant,tot
    if form.validate_on_submit():
        value=form.quantity.data
        pname=prodname
        pprice=price
        pquant=value
        global line349
        line349=False
        print("####")
        print(value)
        print(pprice)
        print(pquant)
        new_productdetails=Products(prodname, price,qnty)
        db.session.add_all([new_productdetails])
        db.session.commit()
        allstudent= Products.query.all()
        print(allstudent)
        qnty=qnty-value
        print(qnty)
        if qnty>=0:
            var = Products.query.filter_by(productname=prodname).first()
            print(var.productname)
            var.Availableunits=qnty
            db.session.commit()
        tot=value*price
        print(tot)
        if tot>=0 and qnty>=0:
            new_orderdetails=Productorder(gid,name,prodname,value,tot)
            db.session.add_all([new_orderdetails])
            db.session.commit()
            allstudents= Productorder.query.all()
            print(allstudents)
        
        if qnty<=0:
            qnty=0
            out = True
            return render_template('checkoutpage.html',name=ua, pname=pname, pprice=pprice, pquant=pquant,out=out)
        print("added to cart")
        #return render_template('checkoutpage.html', name=name)
        return redirect('/checkout')
    return render_template('iphone13.html',name=ua, form=form, price=price, prodname=prodname,pname=prodname)

###Samsung###

@app.route('/s22Ultra', methods=['GET','POST'])
def s22Ultra():
    name=ua
    form=addtocart()
    prodname='Samsung S22 ultra'
    price=1099
    qnty=qnty4
    global pname, pprice, pquant,tot
    if form.validate_on_submit():
        value=form.quantity.data
        pname=prodname
        pprice=price
        pquant=value
        global line349
        line349=False
        print("####")
        print(value)
        print(pprice)
        print(pquant)
        new_productdetails=Products(prodname, price,qnty)
        db.session.add_all([new_productdetails])
        db.session.commit()
        allstudent= Products.query.all()
        print(allstudent)
        qnty=qnty-value
        print(qnty)
        if qnty>=0:
            var = Products.query.filter_by(productname=prodname).first()
            var.Availableunits=qnty
            db.session.commit()
        tot=value*price
        print(tot)
        if tot>=0 and qnty>=0:
            new_orderdetails=Productorder(gid,name,prodname,value,tot)
            db.session.add_all([new_orderdetails])
            db.session.commit()
            allstudents= Productorder.query.all()
            print(allstudents)
        
        if qnty<=0:
            qnty=0
            out = True
            return render_template('checkoutpage.html',name=ua, pname=pname, pprice=pprice, pquant=pquant,out=out)
        print("added to cart")
        #return render_template('checkoutpage.html', name=name)
        return redirect('/checkout')
    return render_template('s22ultra.html',name=ua, form=form, price=price, prodname=prodname,pname=prodname)

@app.route('/s22plus', methods=['GET','POST'])
def s22plus():
    name=ua
    form=addtocart()
    prodname='Samsung S22 Plus'
    price=999
    qnty=qnty5
    global pname, pprice, pquant,tot
    if form.validate_on_submit():
        value=form.quantity.data
        pname=prodname
        pprice=price
        pquant=value
        global line349
        line349=False
        print("####")
        print(value)
        print(pprice)
        print(pquant)
        new_productdetails=Products(prodname, price,qnty)
        db.session.add_all([new_productdetails])
        db.session.commit()
        allstudent= Products.query.all()
        print(allstudent)
        qnty=qnty-value
        print(qnty)
        if qnty>=0:
            var = Products.query.filter_by(productname=prodname).first()
            var.Availableunits=qnty
            db.session.commit()
        tot=value*price
        print(tot)
        if tot>=0 and qnty>=0:
            new_orderdetails=Productorder(gid,name,prodname,value,tot)
            db.session.add_all([new_orderdetails])
            db.session.commit()
            allstudents= Productorder.query.all()
            print(allstudents)
        
        if qnty<=0:
            qnty=0
            out = True
            return render_template('checkoutpage.html',name=ua, pname=pname, pprice=pprice, pquant=pquant,out=out)
        print("added to cart")
        #return render_template('checkoutpage.html', name=name)
        return redirect('/checkout')
    return render_template('s22plus.html',name=ua, form=form, price=price, prodname=prodname,pname=prodname)

@app.route('/s22', methods=['GET','POST'])
def s22():
    name=ua
    form=addtocart()
    prodname='Samsung S22'
    price=899
    qnty=qnty6
    global pname, pprice, pquant,tot
    if form.validate_on_submit():
        value=form.quantity.data
        pname=prodname
        pprice=price
        pquant=value
        global line349
        line349=False
        print("####")
        print(value)
        print(pprice)
        print(pquant)
        new_productdetails=Products(prodname, price,qnty)
        db.session.add_all([new_productdetails])
        db.session.commit()
        allstudent= Products.query.all()
        print(allstudent)
        qnty=qnty-value
        print(qnty)
        if qnty>=0:
            var = Products.query.filter_by(productname=prodname).first()
            var.Availableunits=qnty
            db.session.commit()
        tot=value*price
        print(tot)
        if tot>=0 and qnty>=0:
            new_orderdetails=Productorder(gid,name,prodname,value,tot)
            db.session.add_all([new_orderdetails])
            db.session.commit()
            allstudents= Productorder.query.all()
            print(allstudents)
        
        if qnty<=0:
            qnty=0
            out = True
            return render_template('checkoutpage.html',name=ua, pname=pname, pprice=pprice, pquant=pquant,out=out)
        print("added to cart")
        #return render_template('checkoutpage.html', name=name)
        return redirect('/checkout')
    return render_template('s22.html',name=ua, form=form, price=price, prodname=prodname,pname=prodname)

@app.route('/A53', methods=['GET','POST'])
def A53():
    name=ua
    form=addtocart()
    prodname='Samsung A53'
    price=599
    qnty=qnty7
    global pname, pprice, pquant,tot
    if form.validate_on_submit():
        value=form.quantity.data
        pname=prodname
        pprice=price
        pquant=value
        global line349
        line349=False
        print("####")
        print(value)
        print(pprice)
        print(pquant)
        new_productdetails=Products(prodname, price,qnty)
        db.session.add_all([new_productdetails])
        db.session.commit()
        allstudent= Products.query.all()
        print(allstudent)
        qnty=qnty-value
        print(qnty)
        if qnty>=0:
            var = Products.query.filter_by(productname=prodname).first()
            var.Availableunits=qnty
            db.session.commit()
        tot=value*price
        print(tot)
        if tot>=0 and qnty>=0:
            new_orderdetails=Productorder(gid,name,prodname,value,tot)
            db.session.add_all([new_orderdetails])
            db.session.commit()
            allstudents= Productorder.query.all()
            print(allstudents)
        
        if qnty<=0:
            qnty=0
            out = True
            return render_template('checkoutpage.html',name=ua, pname=pname, pprice=pprice, pquant=pquant,out=out)
        print("added to cart")
        #return render_template('checkoutpage.html', name=name)
        return redirect('/checkout')
    return render_template('A53.html',name=ua, form=form, price=price, prodname=prodname,pname=prodname)

@app.route('/A42', methods=['GET','POST'])
def A42():
    name=ua
    form=addtocart()
    prodname='Samsung A42'
    price=499
    qnty=qnty8
    global pname, pprice, pquant,tot
    if form.validate_on_submit():
        value=form.quantity.data
        pname=prodname
        pprice=price
        pquant=value
        global line349
        line349=False
        print("####")
        print(value)
        print(pprice)
        print(pquant)
        new_productdetails=Products(prodname, price,qnty)
        db.session.add_all([new_productdetails])
        db.session.commit()
        allstudent= Products.query.all()
        print(allstudent)
        qnty=qnty-value
        print(qnty)
        if qnty>=0:
            var = Products.query.filter_by(productname=prodname).first()
            var.Availableunits=qnty
            db.session.commit()
        tot=value*price
        print(tot)
        if tot>=0 and qnty>=0:
            new_orderdetails=Productorder(gid,name,prodname,value,tot)
            db.session.add_all([new_orderdetails])
            db.session.commit()
            allstudents= Productorder.query.all()
            print(allstudents)
        
        if qnty<=0:
            qnty=0
            out = True
            return render_template('checkoutpage.html',name=ua, pname=pname, pprice=pprice, pquant=pquant,out=out)
        print("added to cart")
        #return render_template('checkoutpage.html', name=name)
        return redirect('/checkout')
    return render_template('A42.html',name=ua, form=form, price=price, prodname=prodname,pname=prodname)

@app.route('/A13', methods=['GET','POST'])
def A13():
    name=ua
    form=addtocart()
    prodname='Samsung A13'
    price=399
    qnty=qnty9
    global pname, pprice, pquant,tot
    if form.validate_on_submit():
        value=form.quantity.data
        pname=prodname
        pprice=price
        pquant=value
        global line349
        line349=False
        print("####")
        print(value)
        print(pprice)
        print(pquant)
        new_productdetails=Products(prodname, price,qnty)
        db.session.add_all([new_productdetails])
        db.session.commit()
        allstudent= Products.query.all()
        print(allstudent)
        qnty=qnty-value
        print(qnty)
        if qnty>=0:
            var = Products.query.filter_by(productname=prodname).first()
            var.Availableunits=qnty
            db.session.commit()
        tot=value*price
        print(tot)
        if tot>=0 and qnty>=0:
            new_orderdetails=Productorder(gid,name,prodname,value,tot)
            db.session.add_all([new_orderdetails])
            db.session.commit()
            allstudents= Productorder.query.all()
            print(allstudents)
        
        if qnty<=0:
            qnty=0
            out = True
            return render_template('checkoutpage.html',name=ua, pname=pname, pprice=pprice, pquant=pquant,out=out)
        print("added to cart")
        #return render_template('checkoutpage.html', name=name)
        return redirect('/checkout')
    return render_template('A13.html',name=ua, form=form, price=price, prodname=prodname,pname=prodname)


@app.route('/Pixel6Pro', methods=['GET','POST'])
def Pixel6Pro():
    name=ua
    form=addtocart()
    prodname='Google Pixel 6 Pro'
    price=1099
    qnty=qnty10
    global pname, pprice, pquant,tot
    if form.validate_on_submit():
        value=form.quantity.data
        pname=prodname
        pprice=price
        pquant=value
        global line349
        line349=False
        print("####")
        print(value)
        print(pprice)
        print(pquant)
        new_productdetails=Products(prodname, price,qnty)
        db.session.add_all([new_productdetails])
        db.session.commit()
        allstudent= Products.query.all()
        print(allstudent)
        qnty=qnty-value
        print(qnty)
        if qnty>=0:
            var = Products.query.filter_by(productname=prodname).first()
            var.Availableunits=qnty
            db.session.commit()
        tot=value*price
        print(tot)
        if tot>=0 and qnty>=0:
            new_orderdetails=Productorder(gid,name,prodname,value,tot)
            db.session.add_all([new_orderdetails])
            db.session.commit()
            allstudents= Productorder.query.all()
            print(allstudents)
        
        if qnty<=0:
            qnty=0
            out = True
            return render_template('checkoutpage.html',name=ua, pname=pname, pprice=pprice, pquant=pquant,out=out)
        print("added to cart")
        #return render_template('checkoutpage.html', name=name)
        return redirect('/checkout')
    return render_template('pixel6Pro.html',name=ua, form=form, price=price, prodname=prodname,pname=prodname)

@app.route('/Pixel6', methods=['GET','POST'])
def Pixel6():
    name=ua
    form=addtocart()
    prodname='Google Pixel 6'
    price=999
    qnty=qnty11
    global pname, pprice, pquant,tot
    if form.validate_on_submit():
        value=form.quantity.data
        pname=prodname
        pprice=price
        pquant=value
        global line349
        line349=False
        print("####")
        print(value)
        print(pprice)
        print(pquant)
        new_productdetails=Products(prodname, price,qnty)
        db.session.add_all([new_productdetails])
        db.session.commit()
        allstudent= Products.query.all()
        print(allstudent)
        qnty=qnty-value
        print(qnty)
        if qnty>=0:
            var = Products.query.filter_by(productname=prodname).first()
            var.Availableunits=qnty
            db.session.commit()
        tot=value*price
        print(tot)
        if tot>=0 and qnty>=0:
            new_orderdetails=Productorder(gid,name,prodname,value,tot)
            db.session.add_all([new_orderdetails])
            db.session.commit()
            allstudents= Productorder.query.all()
            print(allstudents)
        
        if qnty<=0:
            qnty=0
            out = True
            return render_template('checkoutpage.html',name=ua, pname=pname, pprice=pprice, pquant=pquant,out=out)
        print("added to cart")
        #return render_template('checkoutpage.html', name=name)
        return redirect('/checkout')
    return render_template('pixel6.html',name=ua, form=form, price=price, prodname=prodname,pname=prodname)

if __name__=='__main__':
    app.run(debug=True)
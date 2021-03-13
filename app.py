from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
db = SQLAlchemy(app)

#code
class modelCode(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String)
class modelActiveCode(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String)

#cdi
class modelActive(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String)
class modelKeyboard(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String)

#lc103
class modelActive103(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String)
class modelKeyboard103(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String)

#lc104
class modelActive104(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String)
class modelKeyboard104(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String)

@app.route("/")
def home():
    return render_template("index.html")





@app.route("/CODE", methods=["POST", "GET"])
def code():
    if request.method == 'POST':
        
        #recupere le code
        db.session.query(modelCode).delete()
        db.session.commit()
        code = request.form.get('note')
        new_note = modelCode(data=code)
        db.session.add(new_note)
        db.session.commit()
        

        #activation
        db.session.query(modelActiveCode).delete()
        db.session.commit()
        etat_activation=request.form.get('activation')
        if etat_activation=='on':
            new_etat_clavier=modelActiveCode(data=etat_activation)
            db.session.add(new_etat_clavier)
            db.session.commit()
            return redirect(url_for('code'))
        else:
            etat_desactivation='off'
            new_etat_clavier=modelActiveCode(data=etat_desactivation)
            db.session.add(new_etat_clavier)
            db.session.commit()
            return redirect(url_for('code'))

    notes = modelCode.query.order_by(modelCode.id)
    activate=modelActiveCode.query.order_by(modelActiveCode.id)
    



    return render_template("code.html", code=notes, activate=activate)





@app.route("/CDI", methods=["POST", "GET"])
def cdi():

    
    
    if request.method == 'POST':
        

        #activation
        db.session.query(modelActive).delete()
        db.session.commit()
        etat_activation=request.form.get('activation')
        if etat_activation=='on':
            new_etat_clavier=modelActive(data=etat_activation)
            db.session.add(new_etat_clavier)
            db.session.commit()
        else:
            etat_desactivation='off'
            new_etat_clavier=modelActive(data=etat_desactivation)
            db.session.add(new_etat_clavier)
            db.session.commit()
            

        
            
        
        #disable clavier
        db.session.query(modelKeyboard).delete()
        db.session.commit()
        etat_clavier=request.form.get('disable')
        if etat_clavier=='on':
            etat_activation='off'
            new_etat_clavier=modelKeyboard(data=etat_activation)
            db.session.add(new_etat_clavier)
            db.session.commit()
            return redirect(url_for('cdi'))
        else:
            etat_desactivation='on'
            new_etat_clavier=modelKeyboard(data=etat_desactivation)
            db.session.add(new_etat_clavier)
            db.session.commit()
            return redirect(url_for('cdi'))



        
    
    claviersouris=modelKeyboard.query.order_by(modelKeyboard.id)
    
    
    notes = modelActive.query.order_by(modelActive.id)
    return render_template("CDI.html", notes=notes, claviersouris=claviersouris)



@app.route("/LC103", methods=["POST", "GET"])
def LC103():

    
    
    if request.method == 'POST':
        

        #activation
        db.session.query(modelActive103).delete()
        db.session.commit()
        etat_activation=request.form.get('activation103')
        if etat_activation=='on':
            new_etat_clavier=modelActive103(data=etat_activation)
            db.session.add(new_etat_clavier)
            db.session.commit()
        else:
            etat_desactivation='off'
            new_etat_clavier=modelActive103(data=etat_desactivation)
            db.session.add(new_etat_clavier)
            db.session.commit()
            

        
            
        
        #disable clavier
        db.session.query(modelKeyboard103).delete()
        db.session.commit()
        etat_clavier=request.form.get('disable103')
        if etat_clavier=='on':
            etat_activation='off'
            new_etat_clavier=modelKeyboard103(data=etat_activation)
            db.session.add(new_etat_clavier)
            db.session.commit()
            return redirect(url_for('LC103'))
        else:
            etat_desactivation='on'
            new_etat_clavier=modelKeyboard103(data=etat_desactivation)
            db.session.add(new_etat_clavier)
            db.session.commit()
            return redirect(url_for('LC103'))



        
    
    claviersouris=modelKeyboard103.query.order_by(modelKeyboard103.id)
    
    notes = modelActive103.query.order_by(modelActive103.id)
    return render_template("LC103.html", notes=notes, claviersouris=claviersouris)

@app.route("/LC104", methods=["POST", "GET"])
def LC104():

    
    
    if request.method == 'POST':
        

        #activation
        db.session.query(modelActive104).delete()
        db.session.commit()
        etat_activation=request.form.get('activation104')
        if etat_activation=='on':
            new_etat_clavier=modelActive104(data=etat_activation)
            db.session.add(new_etat_clavier)
            db.session.commit()
        else:
            etat_desactivation='off'
            new_etat_clavier=modelActive104(data=etat_desactivation)
            db.session.add(new_etat_clavier)
            db.session.commit()
            

        
            
        
        #disable clavier
        db.session.query(modelKeyboard104).delete()
        db.session.commit()
        etat_clavier=request.form.get('disable104')
        if etat_clavier=='on':
            etat_activation='off'
            new_etat_clavier=modelKeyboard104(data=etat_activation)
            db.session.add(new_etat_clavier)
            db.session.commit()
            return redirect(url_for('LC104'))
        else:
            etat_desactivation='on'
            new_etat_clavier=modelKeyboard104(data=etat_desactivation)
            db.session.add(new_etat_clavier)
            db.session.commit()
            return redirect(url_for('LC104'))



        
    
    claviersouris=modelKeyboard104.query.order_by(modelKeyboard104.id)
    
    notes = modelActive104.query.order_by(modelActive104.id)
    return render_template("LC104.html", notes=notes, claviersouris=claviersouris)




if __name__=="__main__":
    db.create_all()
    app.run( debug=True)

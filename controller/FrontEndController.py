from itsdangerous import URLSafeTimedSerializer

def FrontEndController(app, request, db, render_template, session, redirect):
    
    @app.route('/')
    def Hello():
        if not session.get('authenticated'):
            return render_template('index.html',user_name=None)
        return render_template('index.html',user_name=session['user_name'])
    
    @app.route('/login_page')
    def Login_page():
        if request.args['error']=='password':
            return render_template('login.html',error='password')
        elif request.args['error']=='user_exist':
            return render_template('login.html',error='user_exist')
        return render_template('login.html')

    @app.route('/register_page')
    def Register_page():
        if request.args['error']=='true':
            return render_template('register.html',error='error')
        return render_template('register.html')
     
        
    @app.route('/handwriting_page')
    def handwriting_page():
        if not session.get('authenticated'):
            return redirect('/')
        return render_template('handwriting.html')
    
    @app.route('/about_page')
    def about_page():
        if not session.get('authenticated'):
            return render_template('about.html',user_name=None)
        return render_template('about.html',user_name=session['user_name'])
    
    @app.route('/otphtml_page')
    def otphtml_page():
        if not session.get('authenticated'):
            return redirect('/')
        return render_template('otp.html')
    
    @app.route('/verify_otp', methods = ['POST'])
    def otp_page():
        if request.form['user_otp'] == request.form['actual_otp']:
            data='results/result.png'
            return render_template('OTP_result.html', data=data)
        return redirect('/otphtml_page')

    @app.route('/result_page')
    def result_page():
        data='results/result.png'
        return render_template('result.html', data=data)
    
    
    @app.route('/updatepassword_page')
    def updatePassword_page():
        confirm_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        token = request.args['token']
        email = confirm_serializer.loads(token, salt='email-confirmation-salt', max_age=3600)
        return render_template('update_password.html',email=email)

    @app.route('/verifyemailpassword_page')
    def verifyEmailPassword_page():
        return render_template('verifyemailpassword.html')

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html')
    
    @app.errorhandler(405)
    def page_not_found(e):
        return render_template('404.html')
    
    @app.errorhandler(500)
    def page_not_found(e):
        return render_template('404.html')

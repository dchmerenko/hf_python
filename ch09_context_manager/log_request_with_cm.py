from DBcm import UseDatabase

dbconfig = {'host': '127.0.0.1',
            'user': 'vsearch',
            'password': 'vsearchpasswd',
            'database': 'vsearchlogDB', }

with UseDatabase(dbconfig) as cursor:
    _SQL = """INSERT INTO log
                  (phrase, letters, ip, browser_string, results)
                  VALUES
                  (%s, %s, %s, %s, %s)"""
    cursor.execute(_SQL, (req.form['phrase'],
                          req.form['letters'],
                          req.remote_addr,
                          req.user_agent.browser,
                          res,))


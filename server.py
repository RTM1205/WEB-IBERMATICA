import subprocess
import os
from SimpleHTTPServer import SimpleHTTPRequestHandler
from BaseHTTPServer import HTTPServer
from urlparse import urlparse


class MyRequestHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        guardias_template = """
                        {0}
                        """
	welcome_template = """
                        {0}
                        """
	report_template = """
                        {0}
                        """
	reportDone_template = """
                        {0}
                        """
        if self.path == '/':
            try:
                with open("templates/welcome.html", 'r') as w:
                        welcome_html = w.read()
                        print(welcome_html)
			welcome_template = welcome_template.format(welcome_html)
                        self.send_response(200)
            except:
                self.send_response(400)
                welcome_html = "File not found"
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(welcome_template)
	elif self.path == '/guardias.html':
	    try:
		with open("templates/guardias.html", 'r') as g:
                        guardias_html = g.read()
                        print(guardias_html)
			guardias_template = guardias_template.format(guardias_html)
                        self.send_response(200)
	    except:
		self.send_response(400)
		guardias_html = "File not found"
	    self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(guardias_template)
	elif self.path == '/report.html':
            script_list = [f for f in os.listdir('.') if f.endswith('.sh')]
	    try:
		with open("templates/report.html", 'r') as r:
                        report_html = r.read()
			report_html = report_html.format('\n'.join(['<option value="{0}">{0}</option>'.format(s) for s in script_list]))
                        print(report_html)
                        self.send_response(200)
	    except:
		self.send_response(400)
		report_html = "File not found"
	    self.send_header('Content-type', 'text/html')
            self.end_headers()
            report_template = report_template.format(report_html)
            self.wfile.write(report_template)
	elif self.path.endswith('.sh'):
            script_name = self.path.split('=')[-1]
            email = self.headers.get('email', '')
            if not email=='':
                script_name = script_name + ' ' + email
                output = subprocess.check_output(['sh ' + script_name + ' ' + email],  universal_newlines=True)
	    print(script_name)
	    cmd = 'sh ' + script_name
            output = subprocess.check_output(["/bin/bash", "-c", cmd],  universal_newlines=True)
	    print(output)
            try:
                with open("templates/reportDone.html", "r") as rd:
                        reportDone_html = rd.read()
                        reportDone_html = reportDone_html.format(script_name, output)
                        self.send_response(200)
            except:
                self.send_response(400)
                reportDone_html = "File not found"
	    self.send_header('Content-type', 'text/html')
            self.end_headers()
            reportDone_template = reportDone_template.format(reportDone_html)
            self.wfile.write(reportDone_template)




if __name__ == '__main__':
    server = HTTPServer(('', 8000), MyRequestHandler)
    print('Server started on http://localhost:8000')
    server.serve_forever()

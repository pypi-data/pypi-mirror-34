#!/usr/bin/python3

import re
import urllib3
import json
from urllib.parse import urlencode
from screenlogger.screenlogger import Msg
from steemax import axverify
from steemax import axdb
from steemax import default
from steemax import sec


class Web:
    def __init__ (self):
        self.verify = axverify.AXverify()
        self.db = axdb.AXdb(default.dbuser, 
                            default.dbpass, 
                            default.dbname)
        self.msg = Msg(default.logfilename, 
                        default.logpath,
                        default.msgmode)


    def load_template(self, templatefile=""):
        ''' opens a template file and loads it
        into memory stored in a variable
        '''
        templatepath = default.webpath + "/" + templatefile
        with open(templatepath, 'r') as fh:
            try:
                template = fh.read()
            except Exception as e:
                self.msg.error_message(e)
                return None
            else:
                return template


    def make_page(self, template, **kwargs)
        ''' Fills in key / value pairs on a 
        given template
        '''
        regobj = re.compile(
            r"^(.+)(?:\n|\r\n?)((?:(?:\n|\r\n?).+)+)", 
            re.MULTILINE)
        newtemplate = regobj.sub('', template)
        for key, value in kwargs.items():
            newtemplate = re.sub(str(key), 
                                str(value), 
                                newtemplate)
        return newtemplate


    def login(self, token, dest="home"):
        ''' logs a user in using SteemConnect
        adds the user to the database if it's
        their first time.
        '''
        if self.verify_token(token):
            if self.db.get_user_token(self.verify.steem.username):
                self.db.update_token(self.verify.steem.username, 
                            self.verify.steem.accesstoken, 
                            self.verify.steem.refreshtoken)
            else:
                self.db.add_user(self.verify.steem.username, 
                            self.verify.steem.privatekey, 
                            self.verify.steem.refreshtoken, 
                            self.verify.steem.accesstoken)
            if dest == "info":
                return ("\r\n" 
                        + self.info_page(self.verify.steem.username))
            else:
                return ("\r\n" 
                        + self.make_page(self.load_template(
                        "templates/index.html"), 
                        ACCOUNT1=self.verify.steem.username,
                        REFRESHTOKEN=self.verify.steem.refreshtoken))
        else:
            return self.auth_url()


    def invite(self, token, account2, per, 
                    ratio, dur, response, ip):
        ''' Creates an invite
        '''
        if not self.verify_recaptcha(response, ip):
            return self.error_page("Invalid captcha.")
        if self.verify_token(sec.filter_token(token)):
            account2 = sec.filter_account(account2)
            if self.verify.steem.steem_instance().get_account(account2):
                memoid = self.db.add_invite(
                            self.verify.steem.username, 
                            account2,  
                            sec.filter_number(per), 
                            sec.filter_number(ratio), 
                            sec.filter_number(dur))
                if memoid:
                    return self.template("templates/memo.html", 
                                        MEMOMSG=memoid)
                else:
                    return self.error_page(self.db.errmsg)
            else:
                return self.error_page("Invalid account name.")
        else:
            return self.auth_url()


    def info_page(self, account):
        ''' Creates the page at steemax.info that displays
        all the exchanges a user is involved in and which
        provides the options to accept, barter or cancel a 
        particular exchange.
        '''
        axlist = self.db.get_axlist(account)
        boxtemplate = self.load_template("templates/infobox.html")
        infobox = ""
        for value in axlist:
            if value[7] == -1:
                memoid = str(value[6]) + ":start"
                buttoncode = None
            if value[7] == 0 or value[7] > 1:
                memoid = str(value[6]) + ":accept"
                buttoncode = '''
                <div class="button">Accept</div>
                <div class="button">Cancel</div>
                <div class="button">Barter</div>'''
            if value[7] == 1:
                memoid = str(value[6])
                buttoncode = '''
                <div class="button">Cancel</div>'''
            if value[7] != 4:
                box = self.make_page(boxtemplate,
                                AXID=value[0],
                                ACCOUNT1=value[1],
                                ACCOUNT2=value[2],
                                PERCENTAGE=value[3],
                                RATIO=value[4],
                                DURATION=value[5],
                                MEMOID=value[6],
                                MEMOSTR=memoid,
                                BTNCODE=buttoncode))
                infobox = infobox + box
        pagetemplate = self.load_template("templates/info.html")
        return self.make_page(pagetemplate, INFOBOX=infobox)


    def verify_token(self, token):
        ''' cleans and verifies a SteemConnect
        refresh token
        '''
        token = sec.filter_token(token)
        if (token is not None
                    and self.verify.steem.verify_key(
                    acctname="", tokenkey=token)):
            return True
        else:
            return False


    def auth_url(self):
        ''' Returns the SteemConnect authorization
        URL for SteemAX
        '''
        url = self.verify.steem.connect.auth_url()
        return ("Location: " + url + "\r\n")


    def error_page(self, msg):
        ''' Rutrns the HTML page with the
        given error message
        '''
        return ("\r\n" 
                + self.make_page(
                self.load_template("templates/error.html"), 
                ERRORMSG=msg))


    def verify_recaptcha(self, response, remoteip):
        ''' Verifies a Google recaptcha v2 token
        '''
        http = urllib3.PoolManager()
        encoded_args = urlencode({'secret': default.recaptcha_secret,
                            'response': response,
                            'remoteip': remoteip})
        url = default.recaptcha_url + "?" + encoded_args
        req = http.request('POST', url)
        if req.status == 200:
            self.json_resp = json.loads(req.data.decode('utf-8'))
        if self.json_resp['success']:
            return True
        else:
            return False


# EOF

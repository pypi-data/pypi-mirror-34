#!/usr/bin/python3

from steemax import axdb
from steemax import axverify
from steemax import default


def exchange():
    ''' This method actualizes the exchange between Steemians.
    ID          row[0]
    Inviter     row[1]
    Invitee     row[2]
    Percentage  row[3]
    Ratio       row[4]
    Duration    row[5]
    MemoID      row[6]
    Status      row[7]
    Timestamp   row[8]
    '''
    db = axdb.AXdb(default.dbuser, 
                        default.dbpass, 
                        default.dbname)
    verify = axverify.AXverify()
    axlist = db.get_axlist()
    for row in axlist:
        print("Comparing "+str(row[1])+" vs. "+str(row[2]))
        if verify.eligible_posts(row[1], row[2]):
            print ("Posts are eligible.")
            if verify.eligible_votes(row[1], 
                                row[2], 
                                row[3], 
                                row[4], 
                                0):
                print ("Votes are eligible")
                verify.steem.connect.steemconnect(
                                db.get_user_token(row[1]))
                verify.steem.connect.vote(
                                row[1], 
                                row[2], 
                                verify.post_two, 
                                row[3])
                verify.msg.message(row[1]+" has voted on "
                                +verify.post_two+" "+row[3]+"%")
                verify.steem.connect.steemconnect(
                                db.get_user_token(row[2]))
                verify.steem.connect.vote(
                                row[2], 
                                row[1], 
                                verify.post_one, 
                                verify.vote_cut)
                verify.msg.message(row[2]+" has voted on "
                                +verify.post_one+" "
                                +verify.vote_cut+"%")

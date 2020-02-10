#! python3

import imapclient
# import pyzmail

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)

conn.login('username@gmail.com', 'password')

conn.select_folder('INBOX', readonly=True)

UIDs = conn.search(['SINCE 20-Aug-2015']) #list

conn.fetch(UIDs, ['BODY[]', 'FLAGS'])
import MySQLdb
import wx
import wx.xrc
import smtplib
import random

class TabOne (wx.Panel):
    def __init__( self, parent ):
        wx.Panel.__init__(self, parent)
                
        gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
                
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"User", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        gSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        m_choice1Choices = []
        cur.execute("Select name from userinfo")    # 從資料庫抓出user
        for emp in cur.fetchall():
            m_choice1Choices.append(str(emp[0]))
        self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
        self.m_choice1.SetSelection( 0 )
        gSizer1.Add( self.m_choice1, 0, wx.ALL, 5 )
                
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Category", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        gSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
                
        m_choice2Choices = ["Book", "Album", "Movie", "Series"]
        self.m_choice2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
        self.m_choice2.SetSelection( 0 )
        gSizer1.Add( self.m_choice2, 0, wx.ALL, 5 )

        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        gSizer1.Add( self.m_staticText10, 0, wx.ALL, 5 )
                
        self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_textCtrl10, 0, wx.ALL, 5 )
                
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Author", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        gSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
                
        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
                
        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Year", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        gSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )
                
        self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_textCtrl4, 0, wx.ALL, 5 )
                
        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Comment", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        gSizer1.Add( self.m_staticText6, 0, wx.ALL, 5 )
                
        self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_textCtrl5, 0, wx.ALL, 5 )
                
        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Rate", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        gSizer1.Add( self.m_staticText7, 0, wx.ALL, 5 )

        m_choice3Choices = ["1", "2", "3", "4", "5"]
        self.m_choice3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
        self.m_choice3.SetSelection( 0 )
        gSizer1.Add( self.m_choice3, 0, wx.ALL, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"Insert", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_button3, 0, wx.ALL, 5 )
                
        self.SetSizer( gSizer1 )
        self.Layout()
                
        self.Centre( wx.BOTH )

        self.m_button3.Bind(wx.EVT_BUTTON, self.onInsert)

    def onInsert(self, event):
        User = self.m_choice1.GetStringSelection()
        Category = self.m_choice2.GetStringSelection()
        Name = self.m_textCtrl10.GetValue()
        Author = self.m_textCtrl2.GetValue()
        Year = self.m_textCtrl4.GetValue()
        Comment = self.m_textCtrl5.GetValue()
        Rate = self.m_choice3.GetStringSelection()

        cur.execute("Select * from {user}".format(user=User.lower()))
        for emp in cur.fetchall():
            print(emp)

        print("Insert")
        print("Insert into {user} Values('{category}', '{name}', '{author}', '{rate}', '{year}', '{comment}')".format(user=User.lower(), category=Category, author=Author, name=Name, year=Year, comment=Comment, rate=Rate))
        cur.execute("Insert into {user} Values('{category}', '{name}', '{author}', '{rate}', '{year}', '{comment}')".format(user=User.lower(), category=Category, author=Author, name=Name, year=Year, comment=Comment, rate=Rate))

        # send recommendation email
        if str(Rate) == "5":
            print("Notification:")
            cur.execute("select email from userinfo")
            rows = cur.fetchall()
            for email in rows:
                print(email[0])
                if email[0] != "":
                    smtp = smtplib.SMTP('smtp.gmail.com', 587)
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.login('hsinjutai@gmail.com','gjqoxlojsamgdybm')
                    from_addr = 'hsinjutai@gmail.com'
                    to_addr = email[0]
                    msg = "Subject: Recommendation\n\nHi,\n\nRecommend you {category} {name} by {author}.\nEnjoy your time with it!\n\n{user_name}".format(user_name=User, category=Category, author=Author, name=Name).encode('utf-8')
                    status = smtp.sendmail(from_addr, to_addr, msg)
                    if status == {}:
                        print("傳送成功")
                    else:
                        print("傳送失敗")
                    smtp.close()
        db.commit()
            
class TabTwo ( wx.Panel ):
	
    def __init__( self, parent ):
        wx.Panel.__init__(self, parent)

        # self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.texts = []
        self.count = 1

        bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
        gSizer3 = wx.GridSizer( 0, 3, 0, 0 )
		
        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Category", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )
        gSizer3.Add( self.m_staticText8, 0, wx.ALL, 5 )
                
        m_choice4Choices = ["Book", "Album", "Movie", "Series"]
        self.m_choice4 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice4Choices, 0 )
        self.m_choice4.SetSelection( 0 )
        gSizer3.Add( self.m_choice4, 0, wx.ALL, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer3.Add( self.m_button2, 0, wx.ALL, 5 )

        bSizer1.Add( gSizer3, 1, wx.EXPAND, 5 )

        gbSizer1 = wx.GridBagSizer( 0, 0 )
        gbSizer1.SetFlexibleDirection( wx.BOTH )
        gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
                
        self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Result", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText26.Wrap( -1 )
        self.m_staticText26.SetMinSize( wx.Size( 320,120 ) )
        gbSizer1.Add( self.m_staticText26, wx.GBPosition( 0, 0 ), wx.GBSpan( 2, 1 ), wx.ALL, 5 )

        self.m_button7 = wx.Button( self, wx.ID_ANY, u"↑", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button7.SetMinSize( wx.Size( 30,50 ) )
        gbSizer1.Add( self.m_button7, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button8 = wx.Button( self, wx.ID_ANY, u"↓", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button8.SetMinSize( wx.Size( 30,50 ) )
        gbSizer1.Add( self.m_button8, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        bSizer1.Add( gbSizer1, 1, wx.EXPAND, 5 )

        gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Numbers", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )
        gSizer4.Add( self.m_staticText12, 0, wx.ALL, 5 )

        self.m_choice5Choices = [] # 從result取出一共有幾筆資料
        self.m_choice5 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.m_choice5Choices, 0 )
        self.m_choice5.SetSelection( 0 )
        gSizer4.Add( self.m_choice5, 0, wx.ALL, 5 )
        
        bSizer1.Add( gSizer4, 1, wx.EXPAND, 5 )

        gSizer5 = wx.GridSizer( 0, 3, 0, 0 )

        m_choice6Choices = [ "name", "year", "rate"] # 從資料庫抓
        self.m_choice6 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice6Choices, 0 )
        self.m_choice6.SetSelection( 0 )
        gSizer5.Add( self.m_choice6, 0, wx.ALL, 5 )
                
        self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer5.Add( self.m_textCtrl6, 0, wx.ALL, 5 )
                
        self.m_button3 = wx.Button( self, wx.ID_ANY, u"Modify", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer5.Add( self.m_button3, 0, wx.ALL, 5 )
        
        bSizer1.Add( gSizer5, 1, wx.EXPAND, 5 )
                
        self.SetSizer( bSizer1 )
        self.Layout()
                
        self.Centre( wx.BOTH )

        self.m_button2.Bind(wx.EVT_BUTTON, self.onSearch)
        self.m_button7.Bind(wx.EVT_BUTTON, self.onUp)
        self.m_button8.Bind(wx.EVT_BUTTON, self.onDown)
        self.m_button3.Bind(wx.EVT_BUTTON, self.onModify)

    def onSearch(self, event):
        Category = self.m_choice4.GetStringSelection()
        print("Search")
        print("select * from alldata where category='{category}'".format(category=Category))
        cur.execute("select * from alldata where category='{category}'".format(category=Category))
        rows = cur.fetchall()

        self.count = 1
        self.m_choice5Choices = []
        self.m_choice5.SetItems(self.m_choice5Choices)
        for i in range(len(rows)):
            self.m_choice5Choices.append(str(i+1))
        self.m_choice5.SetItems(self.m_choice5Choices)

        self.texts = ["Results\n"]
        num = 0
        for row in rows:
            num += 1
            tmp = "{num:<5s}{user:<s} / {year:<s} / {name:<s} / {rate:<s}\n".format(num=str(num), user=str(row[0]), name=str(row[2]), year=str(row[3]), rate=str(row[4]))
            print(tmp)
            self.texts.append(tmp)
        temp = ""
        for i in range(len(self.texts)):
            if i < 6:
                temp += str(self.texts[i])
            else:
                break
        self.m_staticText26.SetLabel(temp)
        db.commit()

    def onUp(self, event):
        self.count -= 1
        print("up", self.count)
        print((self.count-1)*5+1, self.count*5)
        temp = "Results\n"
        for i in range(len(self.texts)):
            if i >= (self.count-1)*5+1 and i <= self.count*5:
                temp += str(self.texts[i])
            # else:
            #     self.count += 1
            #     break
        self.m_staticText26.SetLabel(temp)
        db.commit()

    def onDown(self, event):
        self.count += 1
        print("down", self.count)
        print((self.count-1)*5, self.count*5)
        temp = "Results\n"
        for i in range(len(self.texts)):
            if i > (self.count-1)*5 and i <= self.count*5:
                temp += str(self.texts[i])
            # else:
            #     self.count -= 1
            #     break
        self.m_staticText26.SetLabel(temp)
        db.commit()

    def onModify(self, event):
        Category = self.m_choice4.GetStringSelection()
        Num = self.m_choice5.GetStringSelection()
        ToModify = self.m_choice6.GetStringSelection()
        Input = self.m_textCtrl6.GetValue()
        print(Category, Num, ToModify, Input)

        print("select * from alldata where category='{category}'".format(category=Category))
        cur.execute("select * from alldata where category='{category}'".format(category=Category))
        rows = cur.fetchall()
        num = 0
        for row in rows:
            num += 1
            if str(num) == str(Num):
                user = row[0]
                name = row[2]

        print("Modify")
        cur.execute("update alldata set {toModify}='{input}' where (user_name='{user}') and (category='{category}') and (name='{name}')".format(toModify=ToModify, input=Input, user=user, category=Category, name=name))
        cur.execute("update {userDB} set {toModify}='{input}' where (category='{category}') and (name='{name}')".format(userDB=user.lower(), toModify=ToModify, input=Input, user=user, category=Category, name=name))
        db.commit()

class TabThree ( wx.Panel ):
	
    def __init__( self, parent ):
        wx.Panel.__init__(self, parent)

        gSizer5 = wx.GridSizer( 0, 2, 0, 0 )
		
        self.m_button4 = wx.Button( self, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer5.Add( self.m_button4, 0, wx.ALL, 5 )
                
        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        gSizer5.Add( self.m_staticText11, 0, wx.ALL, 5 )
                
        self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Books", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )
        gSizer5.Add( self.m_staticText12, 0, wx.ALL, 5 )
                
        self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )
        gSizer5.Add( self.m_staticText13, 0, wx.ALL, 5 )
                
        self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Album", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )
        gSizer5.Add( self.m_staticText14, 0, wx.ALL, 5 )
                
        self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText15.Wrap( -1 )
        gSizer5.Add( self.m_staticText15, 0, wx.ALL, 5 )
                
        self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Movie", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )
        gSizer5.Add( self.m_staticText16, 0, wx.ALL, 5 )
                
        self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )
        gSizer5.Add( self.m_staticText17, 0, wx.ALL, 5 )
                
        self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Series", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )
        gSizer5.Add( self.m_staticText18, 0, wx.ALL, 5 )
                
        self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )
        gSizer5.Add( self.m_staticText19, 0, wx.ALL, 5 )
                
                
        self.SetSizer( gSizer5 )
        self.Layout()
                
        self.Centre( wx.BOTH )

        self.m_button4.Bind(wx.EVT_BUTTON, self.onUpdate)

    def onUpdate(self, event):
        cur.execute("select * from alldata where category='{category}' and (rate=4 or rate=5)".format(category="Book"))
        rows = cur.fetchall()
        text = "Books\n"
        if len(rows) >= 3:
            tmp = random.sample(rows, k=3)
            for row in tmp:
                text += "{0:<8s}{1:{2}<10s}\n".format(str(row[3]), str(row[2]), chr(12288))
                print("{0:<8s}{1:{2}<10s}\n".format(str(row[3]), str(row[2]), chr(12288)))
        else:
            count = 0
            for row in rows:
                if count > 2:
                    break
                count += 1
                text += "{0:<8s}{1:{2}<10s}\n".format(str(row[3]), str(row[2]), chr(12288))
        self.m_staticText12.SetLabel(str(text))

        cur.execute("select * from alldata where category='{category}' and (rate=4 or rate=5)".format(category="Album"))
        rows = cur.fetchall()
        text = "Album\n"
        if len(rows) >= 3:
            tmp = random.sample(rows, k=3)
            for row in tmp:
                text += "{0:<8s}{1:{2}<10s}\n".format(str(row[3]), str(row[2]), chr(12288))
                print("{0:<8s}{1:{2}<10s}\n".format(str(row[3]), str(row[2]), chr(12288)))
        else:
            count = 0
            for row in rows:
                if count > 2:
                    break
                count += 1
                text += "{0:<8s}{1:{2}<10s}\n".format(str(row[3]), str(row[2]), chr(12288))
        self.m_staticText14.SetLabel(str(text))

        cur.execute("select * from alldata where category='{category}' and (rate=4 or rate=5)".format(category="Movie"))
        rows = cur.fetchall()
        text = "Movie\n"
        if len(rows) >= 3:
            tmp = random.sample(rows, k=3)
            for row in tmp:
                text += "{0:<8s}{1:{2}<10s}\n".format(str(row[3]), str(row[2]), chr(12288))
                print("{0:<8s}{1:{2}<10s}\n".format(str(row[3]), str(row[2]), chr(12288)))
        else:
            count = 0
            for row in rows:
                if count > 2:
                    break
                count += 1
                text += "{0:<8s}{1:{2}<10s}\n".format(str(row[3]), str(row[2]), chr(12288))
        self.m_staticText16.SetLabel(str(text))

        cur.execute("select * from alldata where category='{category}' and (rate=4 or rate=5)".format(category="Series"))
        rows = cur.fetchall()
        text = "Series\n"
        if len(rows) >= 3:
            tmp = random.sample(rows, k=3)
            for row in tmp:
                text += "{0:<8s}{1:{2}<10s}\n".format(str(row[3]), str(row[2]), chr(12288))
                print("{0:<8s}{1:{2}<10s}\n".format(str(row[3]), str(row[2]), chr(12288)))
        else:
            count = 0
            for row in rows:
                if count > 2:
                    break
                count += 1
                text += "{0:<8s}{1:{2}<10s}\n".format(str(row[3]), str(row[2]), chr(12288))
        
        self.m_staticText18.SetLabel(str(text))
        db.commit()


class LoginPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.LOGIN = False
		
        gSizer12 = wx.GridSizer( 0, 2, 0, 0 )
		
        self.m_radioBtn6 = wx.RadioButton( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer12.Add( self.m_radioBtn6, 0, wx.ALL, 5 )
        self.m_radioBtn6.Bind(wx.EVT_RADIOBUTTON, self.onRadioLogin)

        self.m_radioBtn7 = wx.RadioButton( self, wx.ID_ANY, u"Create User", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer12.Add( self.m_radioBtn7, 0, wx.ALL, 5 )
        self.m_radioBtn7.Bind(wx.EVT_RADIOBUTTON, self.onRadioCreate)

        self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"User name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText31.Wrap( -1 )
        gSizer12.Add( self.m_staticText31, 0, wx.ALL, 5 )

        self.m_textCtrl17 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl17.SetMinSize( wx.Size( 150,-1 ) )

        gSizer12.Add( self.m_textCtrl17, 0, wx.ALL, 5 )

        self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText32.Wrap( -1 )
        gSizer12.Add( self.m_staticText32, 0, wx.ALL, 5 )

        self.m_textCtrl18 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD)
        self.m_textCtrl18.SetMinSize( wx.Size( 150,-1 ) )

        gSizer12.Add( self.m_textCtrl18, 0, wx.ALL, 5 )

        self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Notification\n\ninput email if you\nwant to receive", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText33.Wrap( -1 )
        gSizer12.Add( self.m_staticText33, 0, wx.ALL, 5 )

        self.m_textCtrl19 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl19.SetMinSize( wx.Size( 150,-1 ) )

        gSizer12.Add( self.m_textCtrl19, 0, wx.ALL, 5 )

        self.m_button11 = wx.Button( self, wx.ID_ANY, u"Enter", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer12.Add( self.m_button11, 0, wx.ALL, 5 )
        self.m_button11.Bind(wx.EVT_BUTTON, self.onOpenResultFrame)

        self.SetSizer( gSizer12 )
        self.Layout()

        self.Centre( wx.BOTH )
        
    def onOpenResultFrame(self, event):
        print("login/create user")
        if self.m_radioBtn6.GetValue() == True and self.m_radioBtn7.GetValue() == False:
            Choice = "login"
        else:
            Choice = "add user"
        User = self.m_textCtrl17.GetValue()
        Password = self.m_textCtrl18.GetValue()
        Notification = self.m_textCtrl19.GetValue()

        if Choice == "add user":
            print("insert into userinfo values('{name}', '{email}', '{password}')".format(name=User, email=Notification, password=Password))
            text = "\n\nResult:\n"
            try:
                self.LOGIN = True
                cur.execute("insert into userinfo values('{name}', '{email}', '{password}')".format(name=User, email=Notification, password=Password))
                cur.execute("CREATE TABLE {user_name} (category VARCHAR(45), name VARCHAR(45), author_name VARCHAR(45), rate INT, year INT, comment VARCHAR(45))".format(user_name=User.lower()))
                cur.execute("CREATE TRIGGER `AFTER_INSERT_{user_name}` AFTER INSERT ON {user_name} FOR EACH ROW BEGIN INSERT INTO alldata(user_name, category, name, year, rate, comment) VALUE ('{user}', NEW.category, NEW.name, NEW.year, NEW.rate, NEW.comment); END".format(user_name=User.lower(), user=User))
                main.tab1.m_choice1.Append(User)
                text += "successful :)"
            except:
                self.LOGIN = False
                text += "failed :("

        else:
            cur.execute("select * from userinfo where name='{name}' and password='{password}'".format(name=User, password=Password))
            if cur.fetchall() == ():
                self.LOGIN = False
                text = "\n\nResult:\nfailed :("
            else:
                self.LOGIN = True
                text = "\n\nResult:\nsuccessful :)"
        
        loginResult.ppp.m_staticText34.SetLabel(str(text))
        db.commit()
        loginResult.Show()

    def onRadioLogin(self, event):
        self.m_staticText33.Show(False)
        self.m_textCtrl19.Show(False)

    def onRadioCreate(self, event):
        self.m_staticText33.Show(True)
        self.m_textCtrl19.Show(True)


class LoginResultPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer5 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Result", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText34.Wrap( -1 )
        self.m_staticText34.SetMinSize( wx.Size( -1,100 ) )

        bSizer5.Add( self.m_staticText34, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_button13 = wx.Button( self, wx.ID_ANY, u"OK!", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_button13, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
        self.m_button13.Bind(wx.EVT_BUTTON, self.onOpenMainFrame)

        self.SetSizer( bSizer5 )
        self.Layout()

        self.Centre( wx.BOTH )

    def onOpenMainFrame(self, event):
        login.Close()
        loginResult.Close()
        if login.pp.LOGIN == True:
            main.Show()

class MainFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title="Sharing for All", size=wx.Size(400, 480))
        # Creating the Tab holders: Panel and Notebook
        p = wx.Panel(self)
        nb = wx.Notebook(p)
        
        #Creating the Tab windows
        self.tab1 = TabOne(nb)
        self.tab2 = TabTwo(nb)
        self.tab3 = TabThree(nb)

        # add Tabs to Notebook and give a name to the Tabs
        nb.AddPage(self.tab1, "Insert")
        nb.AddPage(self.tab2, "Find + Modify")
        nb.AddPage(self.tab3, "Recommendation")
        # nb.AddPage(self.tab4, "Add User")

        # Set noteboook in a sizer to create the layout
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        p.SetSizer(sizer)

class LoginFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title="Login", size=wx.Size(400, 480))
        self.pp = LoginPanel(self)
        self.Show()

class LoginResultFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title="Login Result", size=wx.Size(300, 200))
        self.ppp = LoginResultPanel(self)

if __name__ == "__main__":
    app = wx.App()
    db = MySQLdb.connect(host="localhost", user="root", password="user", db="mid")
    print ("connected")
    cur = db.cursor()
    loginResult = LoginResultFrame()
    main = MainFrame()
    login = LoginFrame()
    app.MainLoop()
    db.commit()
    db.close()
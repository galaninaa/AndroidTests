import More_Options
import Settings

AppPath = '/Users/builder/Documents/builds/apk/Release/talkatoneandroid-5.6.4-rc2.apk'
#'C:\\PyCharmProj\\talkatoneAndroid-5.6.4-rc4.apk'

AccountData = {'email':'anton+auto3@talkme.im','number':'3656516221','name':''}

SignIn = {'id':'com.talkatone.android:id/sign_in_butt','xpath':'//android.widget.Button[@text="Sign in"]'}
SignUp = {'id':'com.talkatone.android:id/sign_up_butt','xpath':'//android.widget.Button[@text="Sign up"]'}

Calls = {'accessibility id':'Tab_0','xpath':'//android.widget.TextView[@content-desc="Tab_0"]','text':'Calls'}
Messages = {'accessibility id':'Tab_1','xpath':'//android.widget.TextView[@content-desc="Tab_1"]','text':'Messages'}
Contacts = {'accessibility id':'Tab_2','xpath':'//android.widget.TextView[@content-desc="Tab_2"]','text':'Contacts'}
Favorites = {'accessibility id':'Tab_3','xpath':'//android.widget.TextView[@content-desc="Tab_3"]','text':'Favorites'}

MainScreenHeader = {'id':'com.talkatone.android:id/toolbar_title'}

#My number: (XXX) XXX-XXXX is shown on Contacts and Favorites
MyNumber = {'id':'com.talkatone.android:id/topmost_header'}

MainTabsActionButton = {'id':'com.talkatone.android:id/mainTabsActionButton','xpath':'//android.widget.ImageButton[@resource-id="com.talkatone.android:id/mainTabsActionButton"]'}

#This is section bar Recent Calls and Recent Messages
SectionBar = {'id':'com.talkatone.android:id/section_name','xpath':'//android.widget.TextView[@resource-id="com.talkatone.android:id/section_name"]'}

MoreOptions = {'accessibility id':'More options','xpath':'//android.widget.ImageView[@content-desc="More options"]'}

NavigateUp = {'accessibility id':'Navigate up','xpath':'//android.widget.ImageButton[@content-desc="Navigate up"]'}




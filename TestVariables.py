import More_Options
import Settings
import  Voicemail
import ActiveCallScreen as acs

app_path = '/Users/builder/Documents/builds/apk/Release/talkatoneandroid-5.6.4-rc2.apk'
#  'C:\\PyCharmProj\\talkatoneAndroid-5.6.4-rc4.apk'

account_data = {'email': 'anton+auto3@talkme.im', 'number': '3656516221', 'name': ''}

sign_in = {'id': 'com.talkatone.android:id/sign_in_butt', 'xpath': '//android.widget.Button[@text="Sign in"]'}
sign_up = {'id': 'com.talkatone.android:id/sign_up_butt', 'xpath': '//android.widget.Button[@text="Sign up"]'}

calls = {'accessibility id': 'Tab_0', 'xpath': '//android.widget.TextView[@content-desc="Tab_0"]', 'text': 'Calls'}
messages = {'accessibility id': 'Tab_1', 'xpath': '//android.widget.TextView[@content-desc="Tab_1"]',
            'text': 'Messages'}
contacts = {'accessibility id': 'Tab_2', 'xpath': '//android.widget.TextView[@content-desc="Tab_2"]',
            'text': 'Contacts'}
favorites = {'accessibility id': 'Tab_3', 'xpath': '//android.widget.TextView[@content-desc="Tab_3"]',
             'text': 'Favorites'}

main_screen_header = {'id': 'com.talkatone.android:id/toolbar_title'}

# My number: (XXX) XXX-XXXX is shown on Contacts and Favorites
my_number = {'id': 'com.talkatone.android:id/topmost_header'}

main_tabs_action_button = {'id': 'com.talkatone.android:id/mainTabsActionButton',
                        'xpath': '//android.widget.ImageButton[@resource-id="com.talkatone.android:id/mainTabsActionButton"]'}

# This is section bar Recent Calls and Recent Messages
section_bar = {'id': 'com.talkatone.android:id/section_name',
              'xpath': '//android.widget.TextView[@resource-id="com.talkatone.android:id/section_name"]'}

more_options = {'accessibility id': 'More options', 'xpath': '//android.widget.ImageView[@content-desc="More options"]'}

navigate_up = {'accessibility id': 'Navigate up', 'xpath': '//android.widget.ImageButton[@content-desc="Navigate up"]'}

voicemail = {'accessibility id': 'Voicemail', 'xpath': '//android.widget.ImageButton[@content-desc="Voicemail"]'}

